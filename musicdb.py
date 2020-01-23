from flask import Flask, render_template, request, redirect, flash, url_for
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length
from flask_bootstrap import Bootstrap

# Set up the app and database

APP = Flask(__name__)
LOGIN_MANAGER = LoginManager()
LOGIN_MANAGER.init_app(APP)
LOGIN_MANAGER.login_view = 'login'

BOOTSTRAP = Bootstrap(APP)

APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/simon/musicdb.sqlite'
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
APP.config['SECRET_KEY'] = 'ThisIsASecret'

from datamodel import School, Pupil, PupilInstrument, Instrument, Teacher, User, UserRole, DB


@APP.route('/')
def index():
    return render_template('base.html')

@APP.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('index')
            return redirect(next)

    
    return render_template("login.html", form=form)

@LOGIN_MANAGER.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()

class LoginForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired(), Length(1,64)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log in')


@APP.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@APP.route('/pupils')
@login_required
def pupils():

    pupils = None

    if current_user.role == UserRole.ADMIN:
        pupils = Pupil.query.all()
    
    else:
        pupils = Pupil.query.filter_by(school=current_user.school).all()

    return render_template('pupils.html', pupils=pupils, table_title="Pupils")

@APP.route('/pupil/<id>')
@login_required
def pupil(id):

    pupil = Pupil.query.get(id)

    return render_template('pupil.html', pupil=pupil, entry_title="Pupil")


class PupilForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    year = IntegerField("Year", validators=[DataRequired()])
    school = SelectField("School",choices=[(s.id, s.name) for s in School.query.order_by('name')], coerce=int)
    submit = SubmitField('Submit Pupil Information')


@APP.route('/editpupil/', methods = ['GET','POST'])
@APP.route('/editpupil/<id>', methods = ['GET','POST'])
@login_required
def editpupil(id=None):

    form = PupilForm()
    if id is not None:
        pupil = Pupil.query.filter_by(id=id).first()
        form = PupilForm(obj=pupil)
        # We need this to set the correct default for the school selector
        form.school.data = pupil.school.id

    if form.validate_on_submit():

        pupil = None

        if id is not None:
            # We're editing an existing entry
            pupil = Pupil.query.filter_by(id=id).first()
            pupil.first_name = form.first_name.data
            pupil.last_name = form.last_name.data
            pupil.year = form.year.data
            pupil.school = School.query.filter_by(id=int(form.school.data)).first()

        else:
            pupil = Pupil(first_name=form.first_name.data, last_name=form.last_name.data, year=form.year.data, school=School.query.filter_by(id=int(form.school.data)).first())

        DB.session.add(pupil)
        DB.session.commit()
    
        return redirect(url_for('pupil',id=pupil.id))


    return render_template("editpupil.html", form=form, entry_title="Add/Edit Pupil")




@APP.route('/schools')
@login_required
def schools():

    schools = None

    if current_user.role == UserRole.ADMIN:
        schools = School.query.all()
    
    else:
        schools = [current_user.school]


    return render_template('schools.html', schools=schools, table_title="Schools")


@APP.route('/instruments')
@login_required
def instruments():

    instruments = Instrument.query.all()

    return render_template('instruments.html', instruments=instruments, table_title="Instruments")


@APP.route('/teachers')
@login_required
def teachers():

    teachers = Teacher.query.all()

    return render_template('teachers.html', teachers=teachers, table_title="Teachers")


@APP.route('/users')
@login_required
def users():

    # Only admins can use this
    if not current_user.is_admin():
        return redirect(url_for('index'))

    users = User.query.all()

    return render_template('users.html', users=users, table_title="Users")


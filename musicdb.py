from flask import Flask, render_template, request, redirect, flash, url_for
from flask_login import LoginManager, login_required, login_user, logout_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
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

from datamodel import School, Pupil, PupilInstrument, Instrument, Teacher, User


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

    pupils = Pupil.query.all()

    return render_template('pupils.html', pupils=pupils, table_title="Pupils")

@APP.route('/pupil/<id>')
@login_required
def pupil(id):

    pupil = Pupil.query.get(id)

    return render_template('pupil.html', pupil=pupil, entry_title="Pupil")



@APP.route('/schools')
@login_required
def schools():

    schools = School.query.all()

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

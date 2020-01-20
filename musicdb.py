from flask import Flask, render_template

# Set up the database

APP = Flask(__name__)
APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/simon/musicdb.sqlite'
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

from datamodel import School, Pupil, PupilInstrument, Instrument


@APP.route('/')
def index():
    return render_template('base.html')

@APP.route('/pupils')
def pupils():

    pupils = Pupil.query.all()

    return render_template('pupils.html', pupils=pupils, table_title="Pupils")


@APP.route('/schools')
def schools():

    schools = School.query.all()

    return render_template('schools.html', schools=schools, table_title="Schools")


@APP.route('/instruments')
def instruments():

    instruments = Instrument.query.all()

    return render_template('instruments.html', instruments=instruments, table_title="Instruments")

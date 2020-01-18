from flask import Flask, render_template

# Set up the database

APP = Flask(__name__)
APP.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:////home/simon/musicdb.sqlite'

import datamodel


@APP.route('/')
def index():
    return render_template('base.html')


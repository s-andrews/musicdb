from flask_sqlalchemy import SQLAlchemy
from musicdb import APP
import enum

DB = SQLAlchemy(APP)

class Pupil(DB.Model):
    __tablename__ = 'pupils'
    id = DB.Column(DB.Integer, primary_key=True)
    first_name = DB.Column(DB.String)
    last_name = DB.Column(DB.String)
    year = DB.Column(DB.Integer)
    school_id = DB.Column(DB.Integer, DB.ForeignKey('schools.id'))
    instruments = DB.relationship(
        'Instrument',
        secondary='pupil_instruments',
        backref=DB.backref('pupils',lazy='dynamic'),
        lazy='dynamic'
    )

    def __repr__(self):
        return f"{self.first_name} {self.last_name} ({self.school.name}, year {self.year})"


class SchoolStages(enum.Enum):
    PRIMARY = 'Primary School'
    SECONDARY = 'Secondary School'


class School(DB.Model):
    __tablename__ = 'schools'
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String)
    stage = DB.Column(DB.Enum(SchoolStages))
    pupils = DB.relationship('Pupil', backref='school')

    def __repr__(self):
        return self.name

class InstrumentFamilies(enum.Enum):
    WOODWIND = 'Woodwind'
    STRINGS = 'Strings'
    PERCUSSION = 'Percussion'
    BRASS = 'Brass'

class Instrument(DB.Model):
    __tablename__ = 'instruments'
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String)
    family = DB.Column(DB.Enum(InstrumentFamilies))
 
    def __repr__(self):
        return self.name


PupilInstrument = DB.Table(
    'pupil_instruments', 
    DB.Column('pupil_id', DB.Integer, DB.ForeignKey('pupils.id')),
    DB.Column('instrument_id', DB.Integer, DB.ForeignKey('instruments.id')),
)


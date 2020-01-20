# We need to import from the directory above
import sys
sys.path.append("..")

from musicdb import APP
from datamodel import DB, School, SchoolStages, Pupil, Instrument, InstrumentFamilies, PupilInstrument

def populate_database():

    DB.drop_all()
    DB.create_all()

    # Make some schools
    bottishamS = School(name="Bottisham Secondary",stage=SchoolStages.SECONDARY)
    bulbeck = School(name="Swaffham Bulbeck Primary",stage=SchoolStages.PRIMARY)
    prior = School(name="Swaffham Prior Primary",stage=SchoolStages.PRIMARY)
    burwell = School(name="Burwell Primary",stage=SchoolStages.PRIMARY)

    # Add them to the database
    DB.session.add(bottishamS)
    DB.session.add(bulbeck)
    DB.session.add(prior)
    DB.session.add(burwell)

    DB.session.commit()

    # List the schools we added
    print("Schools")
    for school in School.query.all():
        print(f"\t {school}")


    # Make some pupils
    simon = Pupil(first_name='Simon', last_name='Andrews', year=11, school=bottishamS)
    emma = Pupil(first_name='Emma', last_name='Andrews', year=11, school=bottishamS)
    james = Pupil(first_name='James', last_name='Andrews', year=6, school=bulbeck)
    libby = Pupil(first_name='Libby', last_name='Andrews', year=5, school=bulbeck)


    DB.session.add(simon)
    DB.session.add(emma)
    DB.session.add(james)
    DB.session.add(libby)

    DB.session.commit()


    # List the pupils we added
    print('Pupils')
    for pupil in Pupil.query.all():
        print(f"\t {pupil}")


    # Add some instruments
    saxophone = Instrument(name='saxophone', family=InstrumentFamilies.WOODWIND)
    flute = Instrument(name='flute', family=InstrumentFamilies.WOODWIND)
    clarinet = Instrument(name='clarinet', family=InstrumentFamilies.WOODWIND)
    trombone = Instrument(name='trombone', family=InstrumentFamilies.BRASS)
    trumpet = Instrument(name='trumpet', family=InstrumentFamilies.BRASS)
    tenorhorn = Instrument(name='tenor horn', family=InstrumentFamilies.BRASS)
    violin = Instrument(name='violin', family=InstrumentFamilies.STRINGS)
    viola = Instrument(name='viola', family=InstrumentFamilies.STRINGS)
    cello = Instrument(name='cello', family=InstrumentFamilies.STRINGS)
    doublebass = Instrument(name='double bass', family=InstrumentFamilies.STRINGS)
    drums = Instrument(name='drum kit', family=InstrumentFamilies.PERCUSSION)
    tuned_percussion = Instrument(name='tuned percussion', family=InstrumentFamilies.PERCUSSION)
    piano = Instrument(name='piano', family=InstrumentFamilies.PERCUSSION)

    DB.session.add(saxophone)
    DB.session.add(trombone)
    DB.session.add(drums)
    DB.session.add(piano)
    DB.session.add(tuned_percussion)
    
    DB.session.commit()

    # List the instruments we added
    print('Instruments')
    for instrument in Instrument.query.all():
        print(f"\t {instrument}")


    # Try adding an instrument to a pupil
    

    DB.session.add(PupilInstrument(pupil=simon, instrument=saxophone, grade=6))
    DB.session.add(PupilInstrument(pupil=simon, instrument=piano, grade=1))
    DB.session.add(PupilInstrument(pupil=simon, instrument=clarinet, grade=6))
    DB.session.add(PupilInstrument(pupil=simon, instrument=flute))

    DB.session.add(PupilInstrument(pupil=emma, instrument=piano, grade=8))
    DB.session.add(PupilInstrument(pupil=emma, instrument=flute, grade=8))
    DB.session.add(PupilInstrument(pupil=emma, instrument=tenorhorn, grade=1))

    DB.session.add(PupilInstrument(pupil=libby, instrument=trombone, grade=1))

    DB.session.add(PupilInstrument(pupil=james, instrument=drums, grade=5))
    DB.session.add(PupilInstrument(pupil=james, instrument=tuned_percussion, grade=5))




    DB.session.commit()

    for instrument in simon.instruments:
        print(instrument)


if __name__ == '__main__':
    populate_database()

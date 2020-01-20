# We need to import from the directory above
import sys
sys.path.append("..")
import random

from musicdb import APP
from datamodel import DB, School, SchoolStages, Pupil, Instrument, InstrumentFamilies, PupilInstrument, Teacher

def populate_database():

    DB.drop_all()
    DB.create_all()

    # Make some schools
    bottishams = School(name="Bottisham Secondary",stage=SchoolStages.SECONDARY)
    bottishamp = School(name="Bottisham Primary",stage=SchoolStages.PRIMARY)
    bulbeck = School(name="Swaffham Bulbeck Primary",stage=SchoolStages.PRIMARY)
    prior = School(name="Swaffham Prior Primary",stage=SchoolStages.PRIMARY)
    burwell = School(name="Burwell Primary",stage=SchoolStages.PRIMARY)
    fulbourn = School(name="Fulbourn Primary",stage=SchoolStages.PRIMARY)
    wilbraham = School(name="Great Wilbraham Primary",stage=SchoolStages.PRIMARY)

    # Add them to the database
    DB.session.add(bottishams)
    DB.session.add(bottishamp)
    DB.session.add(bulbeck)
    DB.session.add(prior)
    DB.session.add(burwell)
    DB.session.add(fulbourn)
    DB.session.add(wilbraham)

    DB.session.commit()

    # List the schools we added
    print("Schools")
    for school in School.query.all():
        print(f"\t {school}")


    # Make some pupils
    simon = Pupil(first_name='Simon', last_name='Andrews', year=11, school=bottishams)
    emma = Pupil(first_name='Emma', last_name='Andrews', year=11, school=bottishams)
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
    # Woodwind

    saxophone = Instrument(name='saxophone', family=InstrumentFamilies.WOODWIND)
    flute = Instrument(name='flute', family=InstrumentFamilies.WOODWIND)
    clarinet = Instrument(name='clarinet', family=InstrumentFamilies.WOODWIND)
    oboe = Instrument(name='oboe', family=InstrumentFamilies.WOODWIND)
    bassoon = Instrument(name='bassoon', family=InstrumentFamilies.WOODWIND)

    DB.session.add(saxophone)
    DB.session.add(flute)
    DB.session.add(clarinet)
    DB.session.add(oboe)
    DB.session.add(bassoon)



    trombone = Instrument(name='trombone', family=InstrumentFamilies.BRASS)
    trumpet = Instrument(name='trumpet', family=InstrumentFamilies.BRASS)
    tenorhorn = Instrument(name='tenor horn', family=InstrumentFamilies.BRASS)
    frenchhorn = Instrument(name='french horn', family=InstrumentFamilies.BRASS)
    tuba = Instrument(name='tuba', family=InstrumentFamilies.BRASS)
    baritone = Instrument(name='baritone', family=InstrumentFamilies.BRASS)
    euphonium = Instrument(name='euphonium', family=InstrumentFamilies.BRASS)

    DB.session.add(trombone)
    DB.session.add(trumpet)
    DB.session.add(tenorhorn)
    DB.session.add(frenchhorn)
    DB.session.add(tuba)
    DB.session.add(baritone)
    DB.session.add(euphonium)



    violin = Instrument(name='violin', family=InstrumentFamilies.STRINGS)
    viola = Instrument(name='viola', family=InstrumentFamilies.STRINGS)
    cello = Instrument(name='cello', family=InstrumentFamilies.STRINGS)
    doublebass = Instrument(name='double bass', family=InstrumentFamilies.STRINGS)
    elecguitar = Instrument(name='electric guitar', family=InstrumentFamilies.STRINGS)
    bassguitar = Instrument(name='bass guitar', family=InstrumentFamilies.STRINGS)
    classguitar = Instrument(name='classical guitar', family=InstrumentFamilies.STRINGS)

    DB.session.add(violin)
    DB.session.add(viola)
    DB.session.add(cello)
    DB.session.add(doublebass)
    DB.session.add(elecguitar)
    DB.session.add(bassguitar)
    DB.session.add(classguitar)

    drums = Instrument(name='drum kit', family=InstrumentFamilies.PERCUSSION)
    tuned_percussion = Instrument(name='tuned percussion', family=InstrumentFamilies.PERCUSSION)

    DB.session.add(drums)
    DB.session.add(tuned_percussion)


    piano = Instrument(name='piano', family=InstrumentFamilies.KEYBOARD)
    organ = Instrument(name='organ', family=InstrumentFamilies.KEYBOARD)

    DB.session.add(piano)
    DB.session.add(organ)

    DB.session.commit()

    # List the instruments we added
    print('Instruments')
    for instrument in Instrument.query.all():
        print(f"\t {instrument}")


    # Make some teachers
    george = Teacher(first_name="George", last_name="Gershwin", region="Grafham")
    andre = Teacher(first_name="Andre", last_name="Previn", region="Comberton")
    gene = Teacher(first_name="Gene", last_name="Kruper", region="Cambridge")
    andre2 = Teacher(first_name="Andre", last_name="Riu", region="Swaffham Prior")
    louis = Teacher(first_name="Louis", last_name="Armstrong", region="Burwell")
    charlie = Teacher(first_name="Charlie", last_name="Parker", region="Bottisham")
    jamesg = Teacher(first_name="James", last_name="Gallway", region="Ely")
    tommy = Teacher(first_name="Tommy", last_name="Dorsey", region="Great Wilbraham")

    DB.session.add(george)
    DB.session.add(andre)
    DB.session.add(gene)
    DB.session.add(andre2)
    DB.session.add(louis)
    DB.session.add(charlie)
    DB.session.add(jamesg)
    DB.session.add(tommy)

    DB.session.commit()

    # Try adding an instrument to a pupil
    DB.session.add(PupilInstrument(pupil=simon, instrument=saxophone, grade=6, teacher=charlie))
    DB.session.add(PupilInstrument(pupil=simon, instrument=piano, grade=1, teacher=andre))
    DB.session.add(PupilInstrument(pupil=simon, instrument=clarinet, grade=6, teacher=george))
    DB.session.add(PupilInstrument(pupil=simon, instrument=flute, teacher=jamesg))
    DB.session.add(PupilInstrument(pupil=simon, instrument=violin, grade=1, teacher=andre2))

    DB.session.add(PupilInstrument(pupil=emma, instrument=piano, grade=8, teacher=andre))
    DB.session.add(PupilInstrument(pupil=emma, instrument=flute, grade=8, teacher=jamesg))
    DB.session.add(PupilInstrument(pupil=emma, instrument=tenorhorn, grade=1, teacher=louis))

    DB.session.add(PupilInstrument(pupil=libby, instrument=trombone, grade=1, teacher=tommy))

    DB.session.add(PupilInstrument(pupil=james, instrument=drums, grade=5, teacher=gene))
    DB.session.add(PupilInstrument(pupil=james, instrument=tuned_percussion, grade=5, teacher=gene))


    DB.session.commit()


def randomly_populate():
    # Fill the database with random data, but let's not actually make it random
    random.seed(14623)

    boys_names = [
        'Liam',
        'Noah',
        'William',
        'James',
        'Logan',
        'Benjamin',
        'Mason',
        'Elijah',
        'Oliver',
        'Jacob',
        'Lucas',
        'Michael',
        'Alexander',
        'Ethan',
        'Daniel',
        'Matthew',
        'Aiden',
        'Henry',
        'Joseph',
        'Jackson',
        'Samuel',
        'Sebastian',
        'David',
        'Carter',
        'Wyatt',
        'Jayden',
        'John',
        'Owen',
        'Dylan',
        'Luke',
        'Gabriel',
        'Anthony',
        'Isaac',
        'Grayson',
        'Jack',
        'Julian',
        'Levi',
        'Christopher',
        'Joshua',
        'Andrew',
        'Lincoln',
        'Mateo',
        'Ryan',
        'Jaxon',
        'Nathan',
        'Aaron',
        'Isaiah',
        'Thomas',
        'Charles',
        'Caleb'
    ]

    girls_names = [
        'Emma',
        'Olivia',
        'Ava',
        'Isabella',
        'Sophia',
        'Charlotte',
        'Mia',
        'Amelia',
        'Harper',
        'Evelyn',
        'Abigail',
        'Emily',
        'Elizabeth',
        'Mila',
        'Ella',
        'Avery',
        'Sofia',
        'Camila',
        'Aria',
        'Scarlett',
        'Victoria',
        'Madison',
        'Luna',
        'Grace',
        'Chloe',
        'Penelope',
        'Layla',
        'Riley',
        'Zoey',
        'Nora',
        'Lily',
        'Eleanor',
        'Hannah',
        'Lillian',
        'Addison',
        'Aubrey',
        'Ellie',
        'Stella',
        'Natalie',
        'Zoe',
        'Leah',
        'Hazel',
        'Violet',
        'Aurora',
        'Savannah',
        'Audrey',
        'Brooklyn',
        'Bella',
        'Claire',
        'Skylar'
    ]

    surnames = [
        'Smith',
        'Jones',    
        'Taylor',
        'Brown',
        'Williams',
        'Wilson',
        'Johnson',
        'Davies',
        'Robinson',
        'Wright',
        'Thompson',
        'Evans',
        'Walker',
        'White',
        'Roberts',
        'Green',
        'Hall',
        'Wood',
        'Jackson',
        'Clarke'
    ]

    primaryschools = School.query.filter_by(stage=SchoolStages.PRIMARY).all()
    secondaryschools = School.query.filter_by(stage=SchoolStages.SECONDARY).all()
    instruments = Instrument.query.all()

    for _ in range(300):
        first_name = ""
        if random.randrange(2):
            first_name = random.choice(boys_names)
        else:
            first_name = random.choice(girls_names)

        instrument = random.choice(instruments)

        school = ""
        if random.randrange(2):
            school = random.choice(secondaryschools)
        else:
            school = random.choice(primaryschools)


        year = 0

        if school.stage == SchoolStages.PRIMARY:
            year = random.choice(range(3, 6))
        else:
            year = random.choice(range(7, 11))

        newpupil = Pupil(first_name=first_name, last_name=random.choice(surnames), school=school, year=year)
        DB.session.add(newpupil)
        DB.session.add(PupilInstrument(pupil=newpupil, instrument=instrument, grade=random.choice(range(1, 8))))
    
    DB.session.commit()



if __name__ == '__main__':
    populate_database()
    randomly_populate()

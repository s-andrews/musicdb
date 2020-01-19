# We need to import from the directory above
import sys
sys.path.append("..")

from musicdb import APP
from datamodel import DB, School, SchoolStages, Pupil

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

if (__name__ == '__main__'):
    populate_database()

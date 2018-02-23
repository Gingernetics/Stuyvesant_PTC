from app import app, models, db
from app.models import PTQueue, Parent, User
import csv, datetime
import whoosh
from whoosh.fields import Schema, DATETIME
import flask_sqlalchemy as flask_sqlalchemy
import flask_whooshalchemy as whooshalchemy


#########################################################
#Database
#########################################################

#flask_sqlalchemy.models_committed.connect(_after_flush)
'''
schema, primary_key = whooshalchemy._get_whoosh_schema_and_primary_key(Parent)
print "_____________________________\n"
print schema
print "_____________________________\n"
schema.add('child_dob', whoosh.fields.TEXT(stored=True, sortable=True))

#schema.remove('child_dob')
print schema
print "_____________________________\n"

'''
#db.drop_all()
db.create_all()

student = User(username='student')
student.set_password('test1')

admin = User(username='admin')
admin.set_password('test2')

db.session.add(student)
db.session.add(admin)
db.session.commit()


#'''
for i in range(0, 25):
    parent = Parent(child_name="child"+str(i), child_dob=str(i))
    db.session.add(parent)
    db.session.commit()


with open('app/static/csv/PTC_Room_Assignments.csv') as csvDataFile:
    csv_reader = csv.reader(csvDataFile)
    for row in csv_reader:
        ptqueue = PTQueue(teacher=row[0], department=row[1], room=row[2], description=row[3])
        db.session.add(ptqueue)
        db.session.commit()
#'''

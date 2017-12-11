from app import models, db

db.create_all()

for i in range(0,5):
    s = str(i)
    u = models.Parent(child_name='child'+s,  email= s+'@email.com')
    db.session.add(u)

db.session.commit()

for i in range(0,5):
    s = str(i)
    u = models.PTQueue(teacher='teacher'+s)
    db.session.add(u)
    
db.session.commit()

for i in range(0,1):
    z = models.PTQueue().query.get(i + 1)
    print(z.teacher)
    #w = z.get_id(z)
    #print(z)
    p = models.Parent().query.get(3)
    z.enqueue(z, p)
    p = models.Parent().query.get(4)
    z.enqueue(z, p)
    print(z)
    db.session.add(z)

admin = models.User(username="admin", password="password")
db.session.add(admin)
 
student = models.User(username="student", password="python")
db.session.add(student)
 
 
# commit the record the database
db.session.commit()

from app import db, login_manager

# For student and admin user accounts only
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), index=True, unique=True)
    password = db.Column(db.String(128), index=True, unique=False)



# Association table for many-to-many rlationship
queues = db.Table('queues',
    db.Column('parent_id', db.Integer, db.ForeignKey('Parent.id')),
    db.Column('ptqueue_id', db.Integer, db.ForeignKey('PTQueue.id'))
)

#Many-to-Many relationship with PTQueues
class Parent(db.Model):
    __tablename__ = 'Parent'
    id = db.Column(db.Integer, primary_key=True)
    child_name = db.Column(db.String(128), index=True, unique=False)
    child_dob = db.Column(db.Integer, index = True, unique = False)
    email = db.Column(db.String(128), index=True, unique=False)
    ptqueues = db.relationship('PTQueue', secondary=queues,
                            backref=db.backref('queues', lazy='dynamic'))
                            
    def __repr__(self):
        return '<Child Name %s>' % (self.child_name)
    
#Many-to-many relationship with Parents
class PTQueue(db.Model):
    __tablename__ = 'PTQueue'
    id = db.Column(db.Integer, primary_key=True)
    teacher = db.Column(db.String(128), index=True, unique=True)
    room = db.Column(db.String(64), index=True, unique=True)
    department = db.Column(db.String(128), index=True, unique=False)
    parents = db.relationship('Parent', secondary=queues,
                            backref=db.backref('queues', lazy='dynamic')) 
    parents = []
            
    @staticmethod        
    def get_id(self):
        return unicode(self.id)

    @staticmethod
    def isEmpty(self):
        return self.parents == []

    @staticmethod
    def enqueue(self, parent):
        self.parents.insert(0,parent)
        
    @staticmethod
    def dequeue(self):
        return self.parents.pop()

    @staticmethod
    def size(self):
        return len(self.parents)
    
    def __repr__(self):
        return '<Id %d, Parents %r>' % (self.id, self.parents)

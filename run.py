#!flask/bin/python
from ptc import ptc, db

if __name__ == "__main__":
    #db.create_all()ptc
    ptc.debug = True
    ptc.use_reloader = False
    ptc.run(debug = True)

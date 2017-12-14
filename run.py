#!flask/bin/python
from app import app
import flask_excel as excel

# This will run the application, change the debug do deliminate the nice error messages (every error would then result in an error 500 message)
if __name__ == "__main__":
    excel.init_excel(app)
    app.debug = True
    app.use_reloader = False
    app.run(debug = True, port = 5016) # Can change back debug

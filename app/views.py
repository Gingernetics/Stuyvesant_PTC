import os
from flask import Flask, flash, redirect, url_for, render_template, request, session, jsonify
from app import app, models, db, login_manager



from flask_login import current_user, login_user, logout_user
from .forms import LoginForm, RegistrationForm

#from app.forms import
from app.models import User, Parent, PTQueue

@app.route('/')
@app.route('/index')
def index():
    return render_template('Cover/index.html', title='Stuyvesant PTC')

@app.route('/search')
def teacher_search():
    return render_template('Cover/teacher_search.html', title='Teacher Query')

@app.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login Successful.')
        if (form.username.data == 'student'):
            return redirect(url_for('staff'))
        if (form.username.data == 'admin'):
            return redirect(url_for('administration'))
    return render_template('Staff/login.html', title='Login Manager', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

#Create a specific page for statistics

#########################       Parent      #########################
@app.route('/parent')
def parent_home():
    return render_template('Parent/parent_home.html', title='Parent Portal')

@app.route('/parent_search')
def parent_search():
    return render_template('Parent/parent_search.html', title='ID Look-Up')

@app.route('/register', methods=['GET', 'POST'])
def register():
    #if current_user.is_authenticated:
    #    return redirect(url_for('index'))
    form = RegistrationForm()


    if  form.validate_on_submit():
        form.validate_date()
        form.validate_parent()
        parent = Parent(child_name=form.child_name.data, child_dob=form.child_dob.data, email=form.email.data)
        db.session.add(parent)
        db.session.commit()
        flash('Congratulations, you are now a registered parent!')
        return redirect(url_for('parent'))
    else:
        for error in form.errors:
            flash(error)
    return render_template('Parent/register.html', title='Register', form=form)

@app.route('/parent_schedules')
def parent_schedules():
    return render_template('Parent/parent_schedules.html', title='Parent Schedules')



#########################       Staff       #########################
@app.route('/staff')
def staff_home():
    return render_template('Staff/student_home.html', title='Student Portal')



#########################   Administration  #########################

@app.route('/administration')
def admin_home():
    return render_template('Staff/admin_home.html', title='Admin Portal')








@app.route('/database')
def database():
    ptqueue = models.PTQueue.query.all()
    return render_template('Cover/database.html', ptqueue=ptqueue, title='database')

@app.route('/upload_csv', methods=['GET', 'POST'])
def upload_csv():
    if request.method == 'POST':
        with open('app/static/csv/PTC_Room_Assignments.csv') as csvDataFile:
            csv_reader = csv.reader(csvDataFile)
            for row in csv_reader:
                ptqueue = PTQueue(teacher=row[0], department=row[1], room=row[2], description=row[3])
                db.session.add(ptqueue)
                db.session.commit()
        flash('CSV successfully updated.')
        return redirect(url_for('upload_csv'))
    return render_template('Cover/index.html')

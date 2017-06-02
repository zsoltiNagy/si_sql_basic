from flask import render_template
from app import app
import db_handling


@app.route('/')
def root():
    return render_template('base.html')


@app.route('/mentors')
def mentors_and_schools():
    '''
    On this page you should show the result of a query that returns the name of the
     mentors plus the name and country of the school (joining with the schools table)
     ordered by the mentors id column (columns: mentors.first_name, mentors.last_name,
     schools.name, schools.country).
    '''
    pass


@app.route('/all-school')
def all_schools():
    '''
    On this page you should show the result of a query that returns the name of the
     mentors plus the name and country of the school (joining with the schools table)
     ordered by the mentors id column.
    BUT include all the schools, even if there's no mentor yet!
    columns: mentors.first_name, mentors.last_name, schools.name, schools.country
    '''
    pass


@app.route('/mentors-by-country')
def mentors_by_country():
    '''
    On this page you should show the result of a query that returns the number of the
     mentors per country ordered by the name of the countries
    columns: country, count
    '''
    pass


@app.route('/contacts')
def contacts():
    '''
    On this page you should show the result of a query that returns the name of the
     school plus the name of contact person at the school (from the mentors table)
     ordered by the name of the school
    columns: schools.name, mentors.first_name, mentors.last_name
    '''
    pass


@app.route('/applicants')
def applicants():
    '''
    On this page you should show the result of a query that returns the first name
    and the code of the applicants plus the creation_date of the application
    (joining with the applicants_mentors table) ordered by the creation_date in
    descending order BUT only for applications later than 2016-01-01
    columns: applicants.first_name, applicants.application_code, applicants_mentors.creation_date
    '''
    pass


@app.route('/applicants-and-mentors')
def applicants_and_mentors():
    '''
    On this page you should show the result of a query that returns the first name
     and the code of the applicants plus the name of the assigned mentor (joining
      through the applicants_mentors table) ordered by the applicants id column
    Show all the applicants, even if they have no assigned mentor in the database!
    In this case use the string 'None' instead of the mentor name
    columns: applicants.first_name, applicants.application_code, mentor_first_name, mentor_last_name
    '''
    pass


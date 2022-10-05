from datetime import datetime
from urllib import request
from flask import Flask, render_template, request
import datetime

app = Flask(__name__)
global studentOrganizationDetails
# Assign default 5 values to studentOrganisationDetails for Application  3.
studentOrganizationDetails = {}


@app.get('/')
def index():
    # Complete this function to get current date and time assign this value to currentDate, display this data on index.html
    currentDate = datetime.datetime.now()
    return render_template('index.html', currentDate=currentDate, cssfile="datetime.css")


@app.get('/calculate')
def displayNumberPage():
    # Complete this function to display form.html page
    return render_template('form.html')


@app.route('/calculate', methods=['POST'])
def checkNumber():
    # Get Number from form and display message according to number
    # Display "Number {Number} is even" if given number is even on result.html page
    # Display "Number {Number} is odd" if given number is odd on result.html page
    # Display "No number provided" if value is null or blank on result.html page
    # Display "Provided input is not an integer!" if value is not a number on result.html page
    global number
    number = request.form['number']

    # Write your to code here to check whether number is even or odd and render result.html page
    result = ''

    if number.isdecimal():
        converted_num = int(number)
        if converted_num % 2 == 0:
            result = 'Number ' + number + ' is even'
        else:
            result = 'Number ' + number + ' is odd'
    else:
        result = 'Provided input is not an integer!'

    return render_template('result.html', result=result)


@app.get('/addStudentOrganization')
def displayStudentForm():
    # Complete this function to display studentForm.html page
    return render_template('studentForm.html')


@app.route('/addStudentOrganization', methods=['POST'])
def displayRegistrationPage():
    # Get student name and organisation from form.
    studentName = request.form['name']
    studentOrganization = request.form['organization']

    # Append this value to studentOrganisationDetails
    global studentOrganizationDetails
    studentOrganizationDetails[studentName] = studentOrganization

    # Display studentDetails.html with all students and organisations
    return render_template('StudentDetails.html', studentOrganizationDetails=studentOrganizationDetails)

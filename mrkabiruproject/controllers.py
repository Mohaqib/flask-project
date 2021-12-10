from flask import Flask, render_template, request, redirect
from db import mydb, mycursor
from logging import FileHandler, WARNING, debug

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def add_student():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        FirstName = request.form['FirstName']
        LastName = request.form['LastName']
        Email = request.form['Email']
        Address = request.form['Address']
        Age = request.form['Age']
        Gender = request.form['Gender']
        MobileNumber = request.form['MobileNumber']
        City = request.form['City']
        State = request.form['State']
        Country = request.form['Country']
        Other_Hobby = request.form['Other_Hobby']
        Courses = request.form['Courses']
        sql = 'INSERT INTO studentform (firstname, lastname, email, address, age, gender, phone_number, city, state, country, hobbies, course) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        val = (FirstName, LastName, Email, Address, Age, Gender, MobileNumber, City, State, Country, Other_Hobby, Courses )
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect('/display')

@app.route('/display', methods=['GET', 'POST'])
def add_student():
    return render_template('id.html')


if __name__ == '__main__':
    app.run(debug=True)        
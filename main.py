from flask import Flask, render_template, request # library import

from models import student

app = Flask(__name__) # void main () - entry point

studentsList = []

@app.route("/") # url - / - homepage
def index():
    return render_template("index.html")

@app.route("/student", methods=['POST']) # get # post
def student_details():
    name = request.form['stu_name']
    college = request.form['college']
    obj = student.student(name, college)
    studentsList.append(obj.__dict__)
    message = "Student add"
    return message

@app.route("/allstudents")
def allStudents():
    return {"students": studentsList}

if __name__ == "__main__":
    app.run()


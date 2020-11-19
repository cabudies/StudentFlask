
from flask import Flask, render_template, request # library import

app = Flask(__name__) # void main () - entry point

studentsList = []

class student():

    def __init__(self, name, college):
        self.name = name
        self.college = college

    def showdetails(self):
        print("name is: ", self.name)
        print("college is: ", self.college)
    ## show student details - homework

@app.route("/") # url - / - homepage
def index():
    return render_template("index.html")

@app.route("/<name>")
def value(name):
    message = "Hello " + name
    return message


@app.route("/student", methods=['POST']) # get # post
def student_details():
    name = request.form['stu_name']
    college = request.form['college']
    studentsList.append({
        'name': name,
        'college': college
    })
    message = "Student add"
    return message

@app.route("/allstudents")
def allStudents():
    return {"students": studentsList}

@app.route("/<first>/<second>")
def multiplication(first, second):
    first = float(first)
    second = float(second)
    result = first*second
    return "Result is " + str(result)

if __name__ == "__main__":
    app.run()


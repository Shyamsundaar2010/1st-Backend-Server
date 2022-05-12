
from flask import Flask, request
app=Flask(__name__)
students={
            '1':{"Name":"Shyam","Rollno":"21pw01","Course":"Software systems"},
            '2':{"Name":"Kanishk","Rollno":"21pw02","Course":"Software systems"},
            '3':{"Name":"Nayeem","Rollno":"21pw03","Course":"Software systems"},
            '4':{"Name":"Surya","Rollno":"21pw04","Course":"Software systems"},
            '5':{"Name":"Deepek","Rollno":"21pw05","Course":"Software systems"},
            '6':{"Name":"Tharun","Rollno":"21pw06","Course":"Software systems"},
            '7':{"Name":"Jack","Rollno":"21pw07","Course":"Software systems"},
            '8':{"Name":"Rose","Rollno":"21pw08","Course":"Software systems"},
            '9':{"Name":"Akshit","Rollno":"21pw09","Course":"Software systems"},
            '10':{"Name":"Varun","Rollno":"21pw10","Course":"Software systems"},
        }
@app.route('/students', methods=['POST', 'GET'])
def get_all_students():
    if request.method=='GET':
        return students
    else:
        name = request.form['Name']
        roll_no = request.form['Rollno']
        course = request.form['Course']
        students['11'] = {'Name': name, 'Rollno': roll_no, 'Course': course}
        print(students)
        return students

@app.route('/students/<id>')
def get_student_by_id(id):
    return students[id]

@app.route('/students/<id>/name')
def get_student_name_by_id(id):
    return students[id]["Name"]

@app.route('/students/names')
def get_all_students_name():
    student_name_list=[]
    for index, student in students.items():
        student_name_list.append(student["Name"])
    return str(student_name_list)



if __name__=='__main__':
    app.run()
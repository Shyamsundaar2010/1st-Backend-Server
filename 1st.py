                #BACKENED SERVER

from flask import Flask,request
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
@app.route('/students')
def display():
    return students
@app.route('/students<id>')
def displayrollno(id):
    id=request.view_args['id']
    return students[id]

if __name__=='__main__':
    app.run()

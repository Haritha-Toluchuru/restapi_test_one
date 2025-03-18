from flask import Flask,jsonify


todo=Flask('__name__')

students=[
        {
            'std_id':1,
            'student_name':'Haritha',
            'age':21,
            'email':'harithat2004@gmail.com'
        },
        {
            'std_id':2,
            'student_name': 'kavya',
            'age': 20,
            'email': 'kavyanaidu359@gmail.com'
        },
        {
            'std_id':3,
            'student_name': 'ramya',
            'age': 21,
            'email': 'ramyapramya@gmail.com'
        },
        {
            'std_id':4,
            'student_name': 'abhishek',
            'age': 20,
            'email': 'a17182649gmail.com'
        },
        {
            'std_id':5,
            'student_name': 'harshitha',
            'age': 21,
            'email': 'toluchuruharshitha@gmail.com'
        },

    ]

@todo.route('/students-list')
def student_list():
    return jsonify(students)

@todo.route('/student/get/<int:std_id>')
def student_get_by_id(std_id):
    for std in students:
        if std['std_id']==std_id:
            return jsonify(std)
    return "id not found"





if __name__ == '__main__':
    todo.run(
        debug=True
    )

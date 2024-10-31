from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# In-memory data store for demonstration purposes
students = [
    {"id": 1, "name": "Alice", "grade": "A", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "grade": "B", "email": "bob@example.com"},
]

# GET /students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

# GET /students/{id}
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = next((s for s in students if s['id'] == id), None)
    if not student:
        abort(404, description="Student not found")
    return jsonify(student)

# POST /students
@app.route('/students', methods=['POST'])
def create_student():
    new_student = request.get_json()
    if 'id' not in new_student or 'name' not in new_student or 'grade' not in new_student or 'email' not in new_student:
        abort(400, description="Missing attributes")
    students.append(new_student)
    return jsonify(new_student), 201

# PUT /students/{id}
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    student = next((s for s in students if s['id'] == id), None)
    if not student:
        abort(404, description="Student not found")
    data = request.get_json()
    student.update(data)
    return jsonify(student)

# DELETE /students/{id}
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    global students
    students = [s for s in students if s['id'] != id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data store
students = []
next_id = 1


# Home route (removes 404 at root)
@app.route("/")
def home():
    return jsonify({"message": "Student API is running"}), 200


# Create student
@app.route('/students', methods=['POST'])
def create_student():
    global next_id

    data = request.get_json() or {}

    # Basic validation
    if not data.get("name") or not data.get("age") or not data.get("course"):
        return jsonify({"error": "name, age and course are required"}), 400

    student = {
        "id": next_id,
        "name": data.get("name"),
        "age": data.get("age"),
        "course": data.get("course")
    }

    students.append(student)
    next_id += 1

    return jsonify(student), 201


# Read all students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students), 200


# Read single student
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    for student in students:
        if student["id"] == student_id:
            return jsonify(student), 200
    return jsonify({"error": "Student not found"}), 404


# Update student
@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.get_json() or {}

    for student in students:
        if student["id"] == student_id:
            student["name"] = data.get("name", student["name"])
            student["age"] = data.get("age", student["age"])
            student["course"] = data.get("course", student["course"])
            return jsonify(student), 200

    return jsonify({"error": "Student not found"}), 404


# Delete student
@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    global students

    for student in students:
        if student["id"] == student_id:
            students = [s for s in students if s["id"] != student_id]
            return jsonify({"message": "Student deleted"}), 200

    return jsonify({"error": "Student not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)

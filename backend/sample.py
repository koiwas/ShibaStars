from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Task Management API!"})

@app.route('/tasks')
def tasks():
    sample_tasks = [
        {"id": 1, "title": "Read a book"},
        {"id": 2, "title": "Write some code"},
    ]
    return jsonify({"tasks": sample_tasks})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

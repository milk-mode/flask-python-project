from flask import Flask, jsonify, request

app = Flask(__name__)

task_list = []


@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': task_list})


@app.route('/tasks', methods=['POST'])
def add_task():
    task_name = request.args.get('task_name')
    if task_name:
        task_list.append(task_name)
        return jsonify({'message': 'Task added successfully'})
    else:
        return jsonify({'error': 'Task name is missing'}), 400


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if 0 <= task_id < len(task_list):
        deleted_task = task_list.pop(task_id)
        return jsonify({'message': f'Task "{deleted_task}" deleted successfully'})
    else:
        return jsonify({'error': 'Invalid task ID'}), 404


if __name__ == '__main__':
    app.run(debug=True)

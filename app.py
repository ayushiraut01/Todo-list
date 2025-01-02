from flask import Flask, render_template, request, redirect, jsonify
import os
print(os.getcwd())
app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_description = request.form['description']
    if task_description:
        task = {
            'id': len(tasks) + 1,
            'description': task_description,
            'completed': False
        }
        tasks.append(task)
    return redirect('/')

@app.route('/edit/<int:task_id>', methods=['POST'])
def edit_task(task_id):
    new_description = request.form['description']
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = new_description
            break
    return redirect('/')

@app.route('/complete/<int:task_id>', methods=['POST'])
def complete_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = not task['completed']
            break
    return redirect('/')

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

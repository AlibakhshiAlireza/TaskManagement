# app.py
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import insert
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)




# ...

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task_title = request.form['title']
        task_date = datetime.strptime(request.form['date'], '%Y-%m-%d')
        new_task = Task(title=task_title, date=task_date)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('index'))

    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

def create_db():
    with app.app_context():
        db.create_all()

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    pass

@app.route('/api/tasks', methods=['GET', 'POST'])
def api_tasks():
    pass  # Add logic to handle API for tasks

if __name__ == '__main__':
    create_db()
    app.run(debug=True)

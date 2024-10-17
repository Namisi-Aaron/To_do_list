from flask import render_template, redirect, url_for, flash, abort
from app import app, db
from app.models import Task
from app.forms import AddTaskForm

@app.route('/home', methods=['GET', 'POST'])
def home():
    form = AddTaskForm()
    tasks = Task.query.all()
    if form.validate_on_submit():
        task = Task(task=form.task.data)
        db.session.add(task)
        db.session.commit()
        flash('Task added', 'success')
        return redirect(url_for('home'))
    else:
        pass
    return render_template('home.html', title='To Do List', list=tasks, form=form)

@app.route("/home/<string:task>", methods=['POST'])
def delete_task(task):
    task = Task.query.get(task)
    db.session.delete(task)
    db.session.commit()
    flash('Task Deleted', 'success')
    return redirect(url_for('home'))
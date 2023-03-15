import os
from flask import Flask, url_for, render_template, request, flash
from markupsafe import escape
import logic
from validators import prepare_date as correct_date

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24).hex()


@app.route("/")
def main_page():
    return render_template('main.html')


@app.route("/add", methods=['GET', 'POST'])
def add_task():
    default_date = correct_date('сегодня')
    if request.method == 'POST':
        context = {'task': request.form['task'],
                   'date': request.form['date'],
                   }
        if not context['task'].split():
            flash('Введите задание!')
        else:
            logic.add_mode(context['task'], context['date'])
            return render_template('add.html', context=context, default_date=default_date)
    return render_template('add.html', default_date=default_date)


@app.get("/show")
def show_tasks_get():
    default_date = correct_date('сегодня')
    res = logic.show_mode(default_date)
    return render_template('show.html', date='сегодня', result=res, default_date=default_date)


@app.post("/show")
def show_tasks_post():
    date = request.form['date']
    res = logic.show_mode(date)
    return render_template('show.html', date=date, result=res, default_date=date)


@app.get("/find")
def find_tasks_get():
    return render_template('find.html')


@app.post("/find")
def find_tasks_post():
    part = request.form['part']
    res = logic.find_mode(part)
    return render_template('find.html', part=part, result=res)


@app.route("/delete", methods=['GET', 'POST'])
def delete_task():
    if request.method == 'POST':
        task_id = request.form['task_id']
        deleted = logic.delete_mode(task_id)
        print(deleted)
        return render_template('delete.html', deleted=deleted)
    return render_template('delete.html')


if __name__ == "__main__":
    app.run()

    with app.test_request_context():
        print(url_for('add_task'))
        print(url_for('show_tasks_get'))

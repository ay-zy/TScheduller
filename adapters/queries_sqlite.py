# from config import settings as CFG


def db_init(conn):
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS tasks(
        taskid INTEGER PRIMARY KEY,
        task TEXT,
        day DATE)""")
    conn.commit()
    cur.close()


def add_task(conn, task, date):
    cur = conn.cursor()
    cur.execute("""INSERT INTO tasks(task, day)
                   VALUES(?, ?)""", (task, date))
    conn.commit()
    cur.close()
    return f'Задание "{task}" добавлено на {date}'


def show_tasks(conn, day):
    cur = conn.cursor()
    formated_date = day #.strftime("%Y-%m-%d")

    cur.execute("""SELECT day, task FROM tasks
                    WHERE day>=? ORDER BY day LIMIT 10""", (formated_date,))
    res = cur.fetchall()
    cur.close()
    return res


def delete_task(conn, task):
    cur = conn.cursor()
    cur.execute("""SELECT * FROM tasks
                    WHERE taskid=?""", (task,))
    deleted_task = cur.fetchone()

    cur.execute("""DELETE FROM tasks
                   WHERE taskid=?""", (task,))
    conn.commit()
    cur.close()
    return deleted_task

def find_task(conn, task):
    cur = conn.cursor()
    cur.execute("""SELECT * FROM tasks
                    WHERE task LIKE ('%%' || ? || '%%') ORDER BY day""", (task,))
    res = cur.fetchall()
    cur.close()
    return res

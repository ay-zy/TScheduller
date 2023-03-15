import sqlite3
from colorama import Fore, Style, init
from adapters import queries_sqlite as queries


init(autoreset=True)


def add_mode(task, date):
    conn = sqlite3.connect('adapters/schedule.db')
    queries.db_init(conn)
    res = queries.add_task(conn, task, date)
    print(res)
    conn.close()


def show_mode(date):
    conn = sqlite3.connect('adapters/schedule.db')
    queries.db_init(conn)
    res = queries.show_tasks(conn, date)
    print('\n'.join(f'{Fore.YELLOW+x} {Fore.RED+y}' for x, y in res))
    conn.close()
    return res


def find_mode(task):
    conn = sqlite3.connect('adapters/schedule.db')
    queries.db_init(conn)
    res = queries.find_task(conn, task)
    conn.close()
    print(res)
    return res


def delete_mode(task_id):
    conn = sqlite3.connect('adapters/schedule.db')
    queries.db_init(conn)
    res = queries.delete_task(conn, task_id)
    return res

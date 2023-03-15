import json


def db_init():
    with open('db.json', 'w') as db:
        json.dump({'tasks': []}, db)


def add_task(task, day):
    with open('db.json') as jt:
        json_data = json.load(jt)

    json_data['tasks'].append({'date': day, 'task': task})
    json_data['tasks'] = sorted(json_data['tasks'], key=lambda x: x['date'])

    with open('db.json', 'w') as jf:
        json.dump(json_data, jf, sort_keys=True, indent=4)


def show_tasks(day):
    with open('db.json') as jt:
        json_data = json.load(jt)

    res = [' '.join(x.values()) for x in json_data['tasks'] if x['date'] >= day]
    return '\n'.join(res)

def delete_tasks(i):
    with open('db.json') as jt:
        json_data = json.load(jt)

    json_data['tasks'].pop(i)

    with open('db.json', 'w') as jf:
        json.dump(json_data, jf, sort_keys=True, indent=4)


def find_task(task):
    task = task.lower()
    with open('db.json') as jt:
        json_data = json.load(jt)

    res= [f'id:{i} '+' '.join(x.values()) for i,x in enumerate(json_data['tasks']) if task in x['task'].lower()]
    return '\n'.join(res)


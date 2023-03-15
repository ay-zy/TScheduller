import datetime


def validate_date(date):
    a = date.split('.')
    if len(a) < 2 or not all([x.isdigit() for x in a]):
        raise ValueError('Неподдерживаемый формат даты')
    return True


def prepare_date(date):
    today = datetime.date.today()
    altd = {'сегодня': today,
            'завтра': today + datetime.timedelta(days=1),
            'послезавтра': today + datetime.timedelta(days=2),
            }

    task_date = altd.get(date.lower())
    if not task_date:
        task_date = date_by_nums(date, today)
    return task_date.strftime("%Y-%m-%d")


def date_by_nums(date, today):
    validate_date(date)
    day, month = map(int, date.split('.'))
    year = today.year
    task_date = datetime.date(year, month, day)

    if task_date < today:
        task_date = task_date.replace(year=year + 1)

    return task_date

def weekday_date(day):
    week = {'понедельник':0,
            'вторник':1,
            'среда':2,
            'четверг':3,
            'пятница':4,
            'суббота':5,
            'воскресенье':6}

    today = datetime.date.today()
    today_wd = today.weekday()
    new_wd = week.get(day, 6)

    while today.weekday()!=new_wd:
        today+=datetime.timedelta(days=1)


    return today


def prepare_date2(date):
    today = datetime.date.today()
    current_year = today.year
    altd = {'сегодня': today,
            'завтра': today + datetime.timedelta(days=1),
            'послезавтра': today + datetime.timedelta(days=2),
            }
    date = altd.get(date, date)

    if not isinstance(date, datetime.date):
        date = datetime.datetime.strptime(f'{date}-{current_year}',
                                          "%d-%m-%Y").date()
        date = datetime.date(current_year, month, day)
        if date < today:
            date = date.replace(year=current_year + 1)
    return date

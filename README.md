# TScheduler
Simple schedule app

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Code Examples](#code-examples)

## General info
This is a simple schedule app with Web or CLI view

## Technologies
Project is created with:
* Python 3.10
* Argparse
* sqlite3
* json
* Flask 2.2.2
* Colorama 0.4.6

## Code Examples
```
py scheduler.py -h
usage: scheduler.py [-h] {show,add,web} ...

positional arguments:
  {show,add,web}
    show    Show 10 tasks from today or given date
            usage: scheduler.py show [-h] [day]
            positional arguments:
                 day          date in DD.MM format (default value is today)

    add     Add tasks by text and date in format d.m Examle:add "Laundry" 31.12
            usage: scheduler.py add [-h] task day
            positional arguments:
                  task         task in string format
                  day          date in DD.MM format

    web           Launches a web UI that gives you more tools. Examle: web

options:
  -h, --help      show this help message and exit```

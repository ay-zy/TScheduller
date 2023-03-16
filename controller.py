import argparse
import textwrap
import logic
import webview
from validators import prepare_date as correct_date


def parse_args():
    parser = argparse.ArgumentParser(prog='scheduler.py',
                                     formatter_class=argparse.RawTextHelpFormatter,
                                     description=textwrap.dedent("""\
                                                    A program that is designed
                                                    to help you systematize
                                                    future tasks
                                                    """),
                                     epilog='\\_>-<_/')
    subparsers = parser.add_subparsers()
    parser_show = subparsers.add_parser(
        'show', help='Show 10 tasks from today or given date. Examle:show or show 31.12')
    parser_show.add_argument(
        'day', nargs='?', default='сегодня', type=correct_date)
    parser_show.set_defaults(func=logic.show_mode)
    parser_add = subparsers.add_parser(
        'add', help='Add tasks by text and date in format d.m Examle:add "Laundry" 31.12')
    parser_add.add_argument('task', help='text of task in quotes')
    parser_add.add_argument('day', type=correct_date)
    parser_add.set_defaults(func=logic.add_mode)
    parser_web = subparsers.add_parser(
        'web', help='Launches a web UI that gives you more tools. Examle: web')
    parser_web.set_defaults(func=webview.app.run)
    return parser.parse_args()


def main():
    args = vars(parse_args())
    func = args.pop('func', None)
    func(*args.values())


if __name__ == "__main__":
    main()

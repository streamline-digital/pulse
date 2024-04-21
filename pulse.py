import argparse
import datetime
import subprocess
import time
import re

def validate_schedule(schedule: list):

    """ Validates and normalizes the format of the schedule and returns its fields. """

    maximum_values = [None, 12, None, 24, 60, 60]
    
    number_of_days_each_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if len(schedule) > 6: 

        raise ValueError("Invalid schedule format. Use YYYY.MM.DD.HH.mm.ss")

    return True


def check_for_match(current_time: list, scheduled_time: list):

    """ Checks if the current time matches the specified schedule. """

    is_match = True

    for current_field, schedule_field in zip(current_time, scheduled_time):

        if schedule_field == "*": continue

        if '-' in schedule_field:

            start, end = map(int, schedule_field.strip('[]').split('-'))

            values = list(range(start, end + 1))

        elif ',' in schedule_field:

            values = [int(val) for val in schedule_field.strip('[]').split(',')]

        else:

            values = [int(schedule_field)]

        if current_field not in values: 

            is_match = False

    return is_match


def main():

    parser = argparse.ArgumentParser(description='Schedule shell commands at specified intervals.')

    parser.add_argument('schedule', help='Scheduling syntax: YYYY.MM.DD.hh.mm.ss')
    parser.add_argument('command', help='Shell command to be executed in double quotes')

    args = parser.parse_args()

    schedule = args.schedule.split('.') 
  
    if debug == True: print(schedule)

    validate_schedule(schedule)

    while True:

        current_time = [int(val) for val in datetime.datetime.now().strftime('%Y.%m.%d.%H.%M.%S').split('.')]

        is_match = check_for_match(current_time, schedule)

        if is_match:

            subprocess.run(args.command, shell=True)

        if debug == True: print(is_match, current_time, schedule)

        time.sleep(1)


if __name__ == "__main__":

    debug = False

    main()




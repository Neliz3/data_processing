"""
Python console application to manage data sources and calculate metrics.
"""

from pynput.keyboard import Key, Controller, Listener
import csv
import readline
import sys

STOP = False
DATA_SOURCE = []
pointer = 0


def add_new_data_source():
    """
    Add New Data Source (File):
    1. The application asks for the path to a new data source file.
    Example:
    > Enter data source file path:
    < C://…/datasource.csv  # input of user

    2. The application displays the structure and total records of the file or ERROR and new attempt
    Example:
    > Datasource structure:
    col_1 name | col_2 name | … | col_n name
    Total records: 10256
    """
    file_path = input('Please, enter data source file path: ')
    DATA_SOURCE.append(file_path)

    with open(file_path, 'r') as csv_file:
        data = csv.DictReader(csv_file)
        print(f'{data.fieldnames}\n'
              f'\nDatasource structure:'
              f'\nTotal records: {len(csv_file.readlines())}')


def on_press_key(key):
    # TODO: validation a length of DATA_SOURCE
    # done
    global pointer
    if key == Key.left and pointer > 0:
        pointer -= 1
    elif key == Key.right and pointer < len(DATA_SOURCE) - 1:
        pointer += 1
    elif key == Key.enter:
        return False
    print("\r" + " " * 50 + "\r" + "> " + DATA_SOURCE[pointer], end='')  # \r - go to start of a line


def select_data_source() -> str:
    """
    The user selects a data source from the added ones using keyboard navigation.
    Example:
    > Select data source: <- -> # user has to see data source name when click arrow buttons
    Selected data source: datasource.csv | Total records: 10256 records
    """

    # TODO: validation whether DATA_SOURCE null or not
    # done

    if len(DATA_SOURCE) == 0:
        print("No available data sources")
        return ""

    pointer = 0

    with Listener(on_press=on_press_key) as listener:
        input(f'Please, choose a datasource using keyboard arrows and press ENTER:\n> {DATA_SOURCE[pointer]}')
        listener.join()

    return DATA_SOURCE[pointer]


def calculate_metric(file):
    """
    The application calculates and displays a metric for the selected data source.
    Example:
    Based on the dataset, {metric name} was calculated. Value is: {value}.
    """
    # TODO: find a csv file
    # sent in tg
    print(file)

# why do we print our file?

#  code here could be smth like:
import pandas as pd
df = pd.read_csv(DATA_SOURCE) # here should be file path, if i understand it correctly, it's DATA_SOURCE
df['operating_margin'] = df['operatingIncome'] / df['revenue']
print('Based on the dataset, operating_margin was calculated. Value is: df['operating_margin'])


def checker():
    """
    Check Existing Information:
        The application shows the names of the last three added data sources and their metrics.
        Example:
    1) Datasource: MicrosoftLTVs2020-2023.csv | Metric: Average LTV = 720$
    2) Datasource: MicrosoftLTVs2020-2023.csv | Metric: Average LTV = 720$
    3) Datasource: MicrosoftLTVs2020-2023.csv | Metric: Average LTV = 720$
    """
    #  code here could be smth like this, but with written print:

    number_of_files = len(data_sources)

    if number_of_files >= 3:
        for i in data_sources[-3:]:
            print()
    elif number_of_files == 2:
        for source in data_sources[-2:]:
            print()
    elif number_of_files == 1:
        print()
    else:
        print()


    pass


# launch menu function -- it should be called after every action
def menu():
    """
    Main menu realization
    When the application starts, the user sees a menu with three options:
        a. Check existing information;
        b. Add a new data source (file);
        c. Calculate metric.
    """
    menus_input = input('\nChoose one of the following options:\n'
                        'a. Check existing information\n'
                        'b. Add a new data source (file)\n'
                        'c. Calculate metric\n'
                        'I choose: ')

    if menus_input.lower() in ('a', 'b', 'c'):
        if menus_input == 'a':
            print('here should be metrics\n\n\n')
        elif menus_input == 'b':
            add_new_data_source()
        elif menus_input == 'c':
            file = select_data_source()
            calculate_metric(file)
    else:
        print("Invalid option. It should be 'a', 'b', or 'c'. Please try again\n")


def on_press(key):
    global STOP
    if key == Key.alt:
        STOP = True


# Main flow of the application
def main():
    print('Hello! Welcome to Python console application!\n')

    with Listener(on_press=on_press):
        while not STOP:
            menu()

    print('Good buy! Thanks for using Python console application!')


if __name__ == '__main__':
    main()

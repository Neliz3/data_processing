"""
Python console application to manage data sources and calculate metrics.

DATA_SOURCE = {
    'datasource.csv':
        {
            'total_records': 5,
            'operating_margin': 4000.3,
        }
}
"""

import pandas as pd
from pynput.keyboard import Key, Listener

import readline  # Used to avoid typing "^[[D" etc. using arrows


STOP = False
DATA_SOURCE = {}
pointer = 0


def data_source_is_null() -> bool:
    """
    Validation if user didn't add a data source yet.
    """
    if len(DATA_SOURCE) == 0:
        print("No available data sources.")
        return False
    return True


def add_new_data_source():
    """
    1. The application asks for the path to a new data source file.
    2. The application displays the structure and total records of the file or ERROR and new attempt
    """

    file_path = input('Please, enter data source file path: ')

    # Handling the error if file is not read properly
    try:
        df = pd.read_csv(file_path)

        columns = ' | '.join(df.columns.values)  # Beautiful output
        total_records = len(df)

        DATA_SOURCE.update(
            {
                file_path: {
                    'total_records': total_records,
                }}
        )
        print(f'\nDatasource structure:'
              f'\n{columns}'
              f'\nTotal records: {total_records}')
    except Exception as error:
        print('Error with file occurred: ', error)
        add_new_data_source()


#  Instruction on the event: a key is pressed
def on_press(key):
    files = list(DATA_SOURCE.keys())  # Getting file names from a dictionary

    global pointer
    if key == Key.left and pointer > 0:
        pointer -= 1
    elif key == Key.right and pointer < len(DATA_SOURCE) - 1:
        pointer += 1
    elif key == Key.enter:
        return False
    print("\r" + " " * 50 + "\r" + "> " + files[pointer], end='')  # \r - go to start of a line


def select_data_source() -> (str, None):
    """
    The user selects a data source from the added ones using keyboard navigation.
    """

    files = list(DATA_SOURCE.keys())  # Getting file names from a dictionary

    if not data_source_is_null():
        return None

    global pointer

    # Handling the error if something goes wrong with keys pressing
    try:
        # The Listener class is used to monitor keyboard inputs,
        # and on_press is a function that gets called whenever a key is pressed. [Chat-GPT explanation]
        with Listener(on_press=on_press) as listener:
            input(f'Please, choose a datasource using keyboard arrows and press ENTER:\n> {files[pointer]}')
            listener.join()
            return files[pointer]
    except Exception as error:
        print("No selected DATA SOURCES: ", error)


def calculate_metric(file):
    """
    The application calculates and displays the operating margin for the selected data source.
    """

    df = pd.read_csv(file)

    # Handling the error if csv doesn't contain the columns
    try:
        # Getting total values
        total_operating_income = sum(df[' operatingIncome'])
        total_revenue = sum(df[' revenue'])
        operating_margin = total_operating_income / total_revenue * 100

        file_data = DATA_SOURCE.get(file)
        file_data.update({'operating_margin': operating_margin})

        print(f"Based on the dataset, operating margin was calculated. Value is: {operating_margin}.")
    except Exception as error:
        print(f"File doesn't have the appropriate data. Error occurred: ", error)


def check_info():
    """
    The function shows the names of the last three added data sources and their metrics.
    """

    if not data_source_is_null():
        return None

    counter = 0
    for file_name, metrics in DATA_SOURCE.items():
        operating_margin = "NOT CALCULATED"

        # Limited output up to 3 lines
        if counter >= 3:
            break

        # Handling the error if user didn't calculate metrics yet
        try:
            operating_margin = metrics['operating_margin']
        except Exception as error:
            print("You didn't calculate metrics yet: ", error)
        finally:  # Anyway do the next
            print('Datasource: ', file_name, '\t', 'Operating Margin: ',  operating_margin)
            counter += 1


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
                        'c. Calculate metrics\n'
                        'd. Exit\n'
                        'I choose: ')

    if menus_input.lower() in ('a', 'b', 'c', 'd'):
        if menus_input == 'a':
            check_info()
        elif menus_input == 'b':
            add_new_data_source()
        elif menus_input == 'c':
            file = select_data_source()
            if file is not None:  # if DATA_SOURCE is not null & user chose a file
                calculate_metric(file)
        else:
            global STOP
            STOP = True
    else:
        print("Invalid option. It should be 'a', 'b', 'c' or 'd'. Please try again\n")


def main():
    print('Hello! Welcome to Python console application!\n')

    while not STOP:
        menu()

    print('Good buy! Thanks for using Python console application!')


if __name__ == '__main__':
    main()

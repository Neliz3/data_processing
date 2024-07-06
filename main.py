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

from pynput.keyboard import Key, Listener
import csv
import readline  # Used for avoiding a mistake using arrows
import pandas as pd

STOP = False
DATA_SOURCE = {}
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
    df = pd.read_csv(file_path)

    columns = ' | '.join(df.columns.values)
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


def on_press_key(key):
    files = list(DATA_SOURCE.keys())

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
    Example:
    > Select data source: <- -> # user has to see data source name when click arrow buttons
    Selected data source: datasource.csv | Total records: 10256 records
    """
    files = list(DATA_SOURCE.keys())

    if len(DATA_SOURCE) == 0:
        print("No available data sources.")
        return None

    global pointer

    with Listener(on_press=on_press_key) as listener:
        input(f'Please, choose a datasource using keyboard arrows and press ENTER:\n> {files[pointer]}')
        listener.join()

    return files[pointer]


def calculate_metric(file):
    """
    The application calculates and displays a metric for the selected data source.
    Example:
    Based on the dataset, {metric name} was calculated. Value is: {value}.
    """

    df = pd.read_csv(file)

    # Check whether csv contains the column or not
    try:
        total_operating_income = sum(df[' operatingIncome'])
        total_revenue = sum(df[' revenue'])

        operating_margin = total_operating_income / total_revenue * 100
        DATA_SOURCE.get(file).update({'operating_margin': operating_margin})  # Updating a DATA_SOURCE
        print(f"Based on the dataset, operating margin was calculated. Value is: {operating_margin}.")
    except Exception as ex:
        print(f"File doesn't have the appropriate data. Error occurred: ", ex)


def checker():
    """
    Check Existing Information:
        The application shows the names of the last three added data sources and their metrics.
        Example:
    1) Datasource: MicrosoftLTVs2020-2023.csv | Metric: Average LTV = 720$
    2) Datasource: MicrosoftLTVs2020-2023.csv | Metric: Average LTV = 720$
    3) Datasource: MicrosoftLTVs2020-2023.csv | Metric: Average LTV = 720$
    """

    # TODO: work with fine output (use '\t' for it)
    # TODO: add validation if DATA_SOURCE is null
    # TODO: add validation if didn't calculate metrics yet, we can't show them

    counter = 0
    for file_name, metrics in DATA_SOURCE.items():
        if counter >= 3:
            break
        print(file_name, metrics['operating_margin'])
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
                        'c. Calculate metric\n'
                        'I choose: ')

    if menus_input.lower() in ('a', 'b', 'c'):
        if menus_input == 'a':
            checker()
        elif menus_input == 'b':
            add_new_data_source()
        elif menus_input == 'c':
            file = select_data_source()
            if file is not None:  # if DATA_SOURCE is not null & user chose a file
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

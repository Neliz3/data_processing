"""
Python console application to manage data sources and calculate metrics.
"""

import keyboard


# Implement validation and adding logic here
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
    print('Please, enter data source file path: \n\n\n')


# Later we divide this into two separate functions: select_data_source() and calculate_metrics()
def calculate_metric():
    """
    Calculate Metric:
    1. The user selects a data source from the added ones using keyboard navigation.
    Example:
    > Select data source: <- -> # user has to see data source name when click arrow buttons
    Selected data source: datasource.csv | Total records: 10256 records

    2. The application calculates and displays a metric for the selected data source.
    Example:
    Based on the dataset, {metric name} was calculated. Value is: {value}.
    """
    pass


# datasource is a dictionary where we store added data sources
def checker(datasource: dict):
    """
    Check Existing Information:
        The application shows the names of the last three added data sources and their metrics.
        Example:
    1) Datasource: MicrosoftLTVs2020-2023.csv | Metric: Average LTV = 720$
    2) Datasource: MicrosoftLTVs2020-2023.csv | Metric: Average LTV = 720$
    3) Datasource: MicrosoftLTVs2020-2023.csv | Metric: Average LTV = 720$
    """
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

    print('Hello! Welcome to Python console application!\n')

    while True:
        menus_input = input('Choose one of the following options:\n'
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
                print('here should be metrics\n\n\n')
        else:
            print("Invalid option. It should be 'a', 'b', or 'c'. Please try again\n")

    print('Good buy! Thanks for using Python console application!')


# While not user enter Ctrl + D (to close the program) we continue show a menu after each operation
def main():
    menu()


if __name__ == '__main__':
    main()

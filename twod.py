#!/usr/bin/env python3

# Created by: Lily Liu
# Created on: Oct 2021
# This program uses a 2D array

import random


def twod_average(number):
    # This function finds the average

    average = 0

    for rows_counter in range(0, len(number)):
        for columns_counter in range(0, len(number[0])):
            average = average + number[rows_counter][columns_counter]

    average = average / (len(number) * len(number[0]))

    return average


def main():
    # This function uses a 2D array
    user_number = []

    rows_string = input("How many rows would you like : ")
    columns_string = input("How many columns would you like : ")
    print("")

    try:
        rows = int(rows_string)
        columns = int(columns_string)
        for row_counter in range(0, rows):
            temp_column = []
            for columns_counter in range(0, columns):
                random_number = random.randint(1, 50)
                temp_column.append(random_number)
                print("{0} ".format(random_number), end="")
            user_number.append(temp_column)
            print("")

        average = twod_average(user_number)
        rounded = round(average, 2)
        print("\nThe average is {0}".format(rounded))

    except (Exception):
        print("\nInvalid Input")

    print("")
    print("Done.")


if __name__ == "__main__":
    main()

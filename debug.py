#!usr/bin/env python

# Created by: Cameron Teed
# Created On: September 2019
# This program calculates the cost of a pizza by getting the diameter.

# global variable
variable_X = 25


def local_variable():

    # this shows what happens with local variables

    variable_X = 10
    variable_Y = 30
    variable_z = variable_Y + variable_X
    print("local variable_X, variable_Y, variable_z: {0} + {1} = {2}".
          format(variable_X, variable_Y, variable_z))


def global_variable():
    # this shows what happens

    global variable_X
    variable_X = variable_X + 1
    variable_Y = 30
    variable_z = variable_X + variable_Y
    print("Global variable_X, variable_Y, variable_z: {0} + {1} = {2}".
          format(variable_X, variable_Y, variable_z))


def main():
    # this function shows how local and global variables work

    local_variable()
    global_variable()


if __name__ == "__main__":
    main()

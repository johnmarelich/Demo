import json
import os


def get_directory():
    # collect the directory name from user
    directory = input("\nIn which directory would you like the file saved?: ")
    # use the user input to create a variable for the path they are requesting
    path = f"/Users/johnmarelich/PycharmProjects/Demo/{directory}"

    # create a variable to store whether the path exists or not
    exists = os.path.exists(path)

    # if the path exists
    if exists:
        # return the path to run_main(), because it's valid
        return directory
    # if path doesn't exist
    else:
        # alert user
        print(f"\nThe directory {directory} does not exist. Please try again...")
        # restart the program (I wouldn't want to user to enter all info just to find out
        # that the directory doesn't exist, and THEN make them start over)
        run_main()


def get_filename():
    # collect the filename from user
    filename = input("What is the name of the file?: ")
    # return the filename to run_main(), if it doesn't exist, it will be created
    return filename


def get_address():
    # get name and address from user
    my_name = input("\nWhat is your name?: ")
    my_address = input("What is your street address?: ")
    city_state_zip = input("What is your city, state, and zip?: ")
    my_country = input("What is your country?: ")
    my_phone = input("What is your number?: ")

    # store all values as comma separated list; will show on one line
    name_address = [my_name, my_address, city_state_zip, my_country, my_phone]
    # return the list to run_main()
    return name_address


def write_file(dct, file, nm_addr):
    # this is the second line of defense for checking existence of directory
    # try / except is technically not needed, as get_directory() will vet this
    try:
        # open / create file as "write", with directory and filename
        with open(f"{dct}/{file}", 'w') as fw:
            json.dump(nm_addr, fw)
        # return the file to run_main()
        return fw
    except FileNotFoundError:
        print(f"\nThe directory/file {dct}/{file} does not exist. Please try again...")
        exit()


def validate_file(dct, file):
    # prompt user for validation request
    validation_request = input("\nWould you like to validate your entry?\n('y' for YES or any key to EXIT): ")

    print()

    if validation_request == 'y':
        # open file and create variable for json dump
        with open(f"{dct}/{file}") as fr:
            lines = json.load(fr)
        # iterate through all values of the file, printing
        for line in lines:
            print(line)
        # exit here, otherwise the program will ask for filename again
        exit()
    else:
        # if user selects no validation, exit
        exit()
    # return the loaded json list
    return lines


# main program function that runs all the other functions
def run_main():
    # call function to request directory
    directory_loc = get_directory()
    # call function to request filename
    file_name = get_filename()
    # call function to get address
    address = get_address()
    # call function to write to the file
    write_file(directory_loc, file_name, address)
    # call function to validate (read) file
    validate_file(directory_loc, file_name)


# start of program
run_main()

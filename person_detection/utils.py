import os
import datetime


def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def get_date():
    return datetime.datetime.now().strftime("%d-%m-%Y")


def get_time():
    return datetime.datetime.now().strftime("%H%M%S")


def create_daily_dir(daily_dir_path):
    directory = os.path.join(daily_dir_path, get_date().replace("-","_") + "\\")
    create_directory(directory)
    return directory


def create_file(directory):
    return os.path.join(directory, get_time() + ".png")

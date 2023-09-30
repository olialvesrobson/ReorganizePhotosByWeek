import os
import shutil
from datetime import datetime

def get_created_date_macos(file_path):
    # Get the file's 'Date Created' (Birthtime) on macOS
    stat = os.stat(file_path)
    created_timestamp = stat.st_birthtime
    return datetime.fromtimestamp(created_timestamp)

def copy_files_by_created_date(source_folder, destination_folder):
    for root, _, files in os.walk(source_folder):
        for filename in files:
            file_path = os.path.join(root, filename)
            created_date = get_created_date_macos(file_path)
            year = created_date.strftime('%Y')
            month_number = created_date.strftime('%m')
            month_name = created_date.strftime('%B')  # Full month name
            week = created_date.strftime('%U')   # Week number of the year

            destination_path = os.path.join(destination_folder, year, f"{month_number}.{month_name}", f"Week {week}")
            os.makedirs(destination_path, exist_ok=True)

            destination_file_path = os.path.join(destination_path, filename)

            # If the destination file already exists, add a suffix to make the filename unique
            counter = 1
            while os.path.exists(destination_file_path):
                base_name, extension = os.path.splitext(filename)
                new_filename = f"{base_name} ({counter}){extension}"
                destination_file_path = os.path.join(destination_path, new_filename)
                counter += 1

            shutil.copy2(file_path, destination_file_path)
            print(f"Copied '{filename}' to '{destination_file_path}'")

def move_files_by_created_date(source_folder, destination_folder):
    for root, _, files in os.walk(source_folder):
        for filename in files:
            file_path = os.path.join(root, filename)
            created_date = get_created_date_macos(file_path)
            year = created_date.strftime('%Y')
            month_number = created_date.strftime('%m')
            month_name = created_date.strftime('%B')  # Full month name
            week = created_date.strftime('%U')   # Week number of the year

            destination_path = os.path.join(destination_folder, year, f"{month_number}.{month_name}", f"Week {week}")
            os.makedirs(destination_path, exist_ok=True)

            destination_file_path = os.path.join(destination_path, filename)

            # If the destination file already exists, add a suffix to make the filename unique
            counter = 1
            while os.path.exists(destination_file_path):
                base_name, extension = os.path.splitext(filename)
                new_filename = f"{base_name} ({counter}){extension}"
                destination_file_path = os.path.join(destination_path, new_filename)
                counter += 1

            shutil.move(file_path, destination_file_path)
            print(f"Moved '{filename}' to '{destination_file_path}'")

if __name__ == "__main__":
    source_folder = "/Users/robson.alves/Documents/AAA.Recovered_Files/PHOTOS/2014/09.SETEMBRO"
    destination_folder = "/Users/robson.alves/Documents/AAA.Recovered_Files/PHOTOS/"

    move_files_by_created_date(source_folder, destination_folder)

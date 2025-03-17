import os

def save_file():
    file_path = input("Enter the file path: ")
    destination_path = "/sdcard/boostphere/FRAACCOUNT.txt"
    
    try:
        if not os.path.exists(os.path.dirname(destination_path)):
            os.makedirs(os.path.dirname(destination_path))
        
        with open(file_path, "r") as source_file:
            content = source_file.read()
        
        with open(destination_path, "w") as dest_file:
            dest_file.write(content)
        
        print(f"File has been copied to {destination_path}")
    except FileNotFoundError:
        print("The specified file does not exist.")
    except PermissionError:
        print("Permission denied. Make sure you have the right access.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    save_file()

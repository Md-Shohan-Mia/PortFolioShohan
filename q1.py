import datetime
import os

class Logger:
    def _init_(self, filename):
        self.filename = filename
        if not os.path.exists(filename):
            open(filename, 'w').close()  # Create the file if it doesn't exist

    def write(self, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.filename, 'a') as file:
            file.write(f"{timestamp} - {message}\n")

    def read(self):
        with open(self.filename, 'r') as file:
            return file.readlines()

# Example usage:
if _name_ == "_main_":
    logger = Logger("log.txt")
    logger.write("This is a log message.")
    logger.write("My name is SYED MOHAMMAD ARSALAN")
    logger.write("My father name is SYED MOHAMMAD ARSHAD")
    logger.write("I love music")
    logger.write("I love CP")

    logs = logger.read()
    print("Log file contents:")
    for log in logs:
        print(log.strip())
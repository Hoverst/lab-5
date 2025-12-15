import os
import logging
import sys
import functools

formatter = logging.Formatter('%(asctime)s,%(levelname)s,%(message)s')

file_logger = logging.getLogger("FileLogger")
file_logger.setLevel(logging.ERROR)
log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "log.csv")
file_handler = logging.FileHandler(log_file_path)
file_handler.setFormatter(formatter)
file_logger.addHandler(file_handler)

console_logger = logging.getLogger("ConsoleLogger")
console_logger.setLevel(logging.ERROR)
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)
console_logger.addHandler(console_handler)

LOGGERS = {
    "file": file_logger,
    "console": console_logger
}

class FileNotFound(Exception):
    pass

class FileCorrupted(Exception):
    pass

def logged(exception_cls, mode):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception_cls as e:
                logger = LOGGERS.get(mode)
                
                if logger:
                    logger.error(str(e))
                else:
                    print(f"Logger configuration error: mode '{mode}' not found.")
                
                raise e
        return wrapper
    return decorator

class FileManager:
    def __init__(self, file_path):
        if not os.path.exists(file_path):
            raise FileNotFound(f"File not found: {file_path}")
        self.file_path = file_path

    @logged(FileCorrupted, "file")
    def read_file(self):
        try:
            with open(self.file_path, 'r') as file:
                return file.read()
        except Exception:
            raise FileCorrupted("Failed to read the file due to corruption or access error")

    @logged(FileCorrupted, "file")
    def write_file(self, content):
        try:
            with open(self.file_path, 'w') as file:
                file.write(content)
        except Exception:
            raise FileCorrupted("Failed to write to the file")

    @logged(FileCorrupted, "console")
    def append_file(self, content):
        try:
            with open(self.file_path, 'a') as file:
                file.write(content)
        except Exception:
            raise FileCorrupted("Failed to append to the file")

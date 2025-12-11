import os
import logging
import sys

class FileNotFound(Exception):
    pass

class FileCorrupted(Exception):
    pass

def logged(exception_cls, mode):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception_cls as e:
                logger = logging.getLogger("FileOperationLogger")
                logger.setLevel(logging.ERROR)
                
                while logger.handlers:
                    logger.removeHandler(logger.handlers[0])
                
                formatter = logging.Formatter('%(asctime)s,%(levelname)s,%(message)s')
                
                if mode == "console":
                    handler = logging.StreamHandler(sys.stdout)
                elif mode == "file":
                    log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "log.csv")
                    handler = logging.FileHandler(log_file_path)
                else:
                    handler = logging.StreamHandler(sys.stdout)
                
                handler.setFormatter(formatter)
                logger.addHandler(handler)
                logger.error(str(e))
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
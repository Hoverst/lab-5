# lab-5 task: 
Створити клас File(name, extension, size) та клас Folder, що може містити в собі і файли, і папки відповідно. Створіть файлову систему з вкладених об’єктів. Реалізуйте методи виведення дерева файлів, найдовшого шляху до об’єкту (path).

# lab-6 task: 
Develop a class for working with files. The class should contain basic methods such as reading and writing to a file, as well as the ability to append to a file (leaving the previous file contents intact). The path and file name must be passed through the class constructor. When creating a class instance, it is necessary to check whether the file exists. If there is no such file, generate a corresponding exception. When reading or writing to a file, if the file is damaged or writing is impossible, generate a corresponding exception. You need to create your own exceptions as exceptions. Additionally, develop a decorator for logging write, read, and file creation operations. A parameterised decorator logged that takes an exception and a mode as arguments. The mode can be ‘console’ or ‘file’. When an exception occurs in a decorated method, it is logged using the logging module. In console mode, logging occurs in the console, and in file mode, logging is written to a file.

User-defined exceptions for clear differentiation of file-related problems:

File not found (FileNotFound).

File corrupted (problems with accessing or reading the file itself) (FileCorrupted).

File type for logging events - csv



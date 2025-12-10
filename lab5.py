class File:
    def __init__(self, name, extension, size):
        self.name = name
        self.extension = extension
        if size < 0:
            raise ValueError("negative")

        self.size = size

    def __del__(self):
        pass

    def full_name(self):
        return f"{self.name}.{self.extension}"

    def longest_path(self):
        return [self.full_name()]


class Folder:
    def __init__(self, name):
        self.name = name
        self.items = []

    def __del__(self):
        pass

    def add(self, item):
        self.items.append(item)

    def print_tree(self, indent=""):
        print(indent + self.name + "/")

        new_indent = indent + "    "
        for item in self.items:
            if isinstance(item, File):
                print(new_indent + item.full_name())
            else:
                item.print_tree(new_indent)

    # def filter_file(self, ext):
    #     filtered = []
    #     for item in self.items:
    #          if isinstance(item, File):
    #              if item.extension == ext:
    #                  filtered.append(item)
    #          else: 
    #              print(item.filter_file(ext))
    #              filtered.extend(item.filter_file(ext))

    #     avgsize = sum(f.size for f in filtered) / len(filtered)
    #     return  filtered, avgsize
    
    def filter_file(self, ext):
        filtered = []
        stack = [self]

        while stack:
            current = stack.pop()

            for item in current.items:
                 if isinstance(item, File):
                     if item.extension == ext:
                         filtered.append(item)
                 else: 
                    stack.append(item)

        avgsize = sum(f.size for f in filtered) / len(filtered)
        return  filtered, avgsize, [f for f in filtered if f.size < avgsize]


    def longest_path(self):

        if not self.items:
            return [self.name]

        longest = []
        for item in self.items:
            path = item.longest_path()
            if len(path) > len(longest):
                longest = path

        return [self.name] + longest

root = Folder("Root")

docs = Folder("Documents")
docs.add(File("Resume", "pdf", 2))
docs.add(File("Report", "docx", 5))
docs.add(File("File001", "docx", 8))

music = Folder("Music")
music.add(File("Track01", "mp3", 10))
music.add(File("File001", "docx", 8))

media = Folder("Media")
media.add(music)

root.add(docs)
root.add(media)
root.add(File("Notes", "txt", 1))

root.print_tree()

print("The longest path:")
print(root.longest_path())

print(root.filter_file("docx"))
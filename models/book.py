class Book:
    def __init__(self,title,year,description,author,read=False, id=None):
        self.title = title
        self.year = year
        self.description = description
        self.author = author
        self.read = read
        self.id = id

    def mark_read(self):
        self.read = True
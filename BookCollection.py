from Book import Book
from BookCollectionNode import BookCollectionNode

class BookCollection:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def getNumberOfBooks(self):
        temp = self.head
        books = 0
        while temp!= None:
            books = books + 1
            temp = temp.getNext()
        return books
    def insertBook(self,book):
        current = self.head
        previous = None
        while current != None:
            lhs = current.getData()
            if (lhs.author > book.author or
                (lhs.author == book.author and lhs.year > book.year) or
                (lhs.author == book.author and lhs.year == book.year and
                 lhs.title > book.title)):
                break
            else:
                previous = current
                current = current.getNext()
        temp = BookCollectionNode(book)
        if previous is None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)
    def getBooksByAuthor(self,author):
        current = self.head
        string = []
        while current != None:
            book = current.getData()
            if book.author.lower() == author.lower():
                string.append(book.getBookDetails())
            current = current.getNext()
        return "\n".join(string)+ "\n" 
    def getAllBooksInCollection(self):
        current = self.head
        string = []
        while current != None:
            book = current.getData()
            string.append(book.getBookDetails())
            current = current.getNext()
        return "\n".join(string).strip() +"\n"
    def removeAuthor(self, author):
        author = author.lower()
        current = self.head 
        previous = None
        while current != None:
            book = current.getData()
            if book.author.lower() == author:
                if previous is None:
                    self.head = current.getNext()
                else:
                    previous.setNext(current.getNext())
                current = current.getNext()
            else:
                previous = current
                current = current.getNext()
    def recursiveSearchTitle(self, title, bookNode):
        if bookNode is None:
            return False
        book = bookNode.getData()
        if book.title.lower() == title.lower():
            return True
        return self.recursiveSearchTitle(title, bookNode.getNext())




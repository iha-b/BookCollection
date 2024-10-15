from Book import Book
from BookCollectionNode import BookCollectionNode
from BookCollection import BookCollection

def test_getBookDetails():
    b = Book("The Bell Jar", "Plath, Sylvia", 1963)
    assert b.getBookDetails() == "Title: The Bell Jar, Author: Plath, Sylvia, Year: 1963"
    assert b.getTitle() == "The Bell Jar"
    c = Book()
    assert c.getBookDetails() == "Title: , Author: , Year: None"
    assert c.getYear() == None
    d = Book("A Tale of Two Cities", "Dickens, Charles", )
    assert d.getBookDetails() == "Title: A Tale of Two Cities, Author: Dickens, Charles, Year: None"
    assert d.getAuthor() == "Dickens, Charles"

def test_insertBook():
    bc = BookCollection()
    assert bc.isEmpty() == True
    b0 = Book("The Picture of Dorian Gray", "Wilde, Oscar", 1890)
    b1 = Book("The Handmaid's Tale", "Atwood, Margaret", 1985)
    b2 = Book("The Metamorphosis", "Kafka, Franz", 1915)
    b3 = Book("The Namesake", "Lahiri, Jhumpa", )
    bc.insertBook(b0)
    bc.insertBook(b1)
    assert bc.getAllBooksInCollection() == ("Title: The Handmaid's Tale, Author: Atwood, Margaret, Year: 1985\n"
                                            "Title: The Picture of Dorian Gray, Author: Wilde, Oscar, Year: 1890")
    assert bc.getNumberOfBooks() == 2
    bc.insertBook(b2)
    bc.insertBook(b3)
    assert bc.getAllBooksInCollection() == ("Title: The Handmaid's Tale, Author: Atwood, Margaret, Year: 1985\n"
                                            "Title: The Metamorphosis, Author: Kafka, Franz, Year: 1915\n"
                                            "Title: The Namesake, Author: Lahiri, Jhumpa, Year: None\n"
                                            "Title: The Picture of Dorian Gray, Author: Wilde, Oscar, Year: 1890")
    assert bc.getNumberOfBooks() == 4


def test_getBooksByAuthor():
    bc = BookCollection()
    b0 = Book("The Picture of Dorian Gray", "Wilde, Oscar", 1890)
    b1 = Book("Lady Windermere's Fan", "Wilde, Oscar", 1893)
    b2 = Book("The Metamorphosis", "Kafka, Franz", 1915)
    b3 = Book("The Castle", "Kafka, Franz", 1926)
    bc.insertBook(b0)
    bc.insertBook(b1)
    bc.insertBook(b2)
    bc.insertBook(b3)
    assert bc.getBooksByAuthor("Wilde, Oscar") == ("Title: The Picture of Dorian Gray, Author: Wilde, Oscar, Year: 1890\n"
                                                   "Title: Lady Windermere's Fan, Author: Wilde, Oscar, Year: 1893")
    bc.removeAuthor("Kafka, Franz")
    assert bc.getBooksByAuthor("Kafka, Franz") == ""
    assert bc.getAllBooksInCollection() == ("Title: The Picture of Dorian Gray, Author: Wilde, Oscar, Year: 1890\n"
                                                   "Title: Lady Windermere's Fan, Author: Wilde, Oscar, Year: 1893")
def test_recursiveSearchTitle():
    bc = BookCollection()
    assert bc.isEmpty() == True
    b0 = Book("The Bell Jar", "Plath, Sylvia", 1890)
    b1 = Book("The Handmaid's Tale", "Atwood, Margaret", 1985)
    b2 = Book("The Metamorphosis", "Kafka, Franz", 1915)
    b3 = Book("The Namesake", "Lahiri, Jhumpa", )
    bc.insertBook(b0)
    bc.insertBook(b1)
    bc.insertBook(b2)
    bc.insertBook(b3)
    assert bc.recursiveSearchTitle("the bell jar", bc.head) == True
    assert bc.recursiveSearchTitle("THE NAMESAKE", bc.head) == True
    assert bc.recursiveSearchTitle("Harry Potter", bc.head) == False
    

# BookCollection

This project implements a Book Collection using an Ordered Linked List. The collection organizes `Book` objects based on the author's name (in lexicographical order), the year published, and the book title. It allows for efficient insertion, retrieval, and removal of books from the collection.

## Project Structure

The project consists of four main files:

1. **Book.py**: Contains the `Book` class definition.
2. **BookCollection.py**: Contains the `BookCollection` class definition, managing the ordered linked list of books.
3. **BookCollectionNode.py**: Contains the `BookCollectionNode` class definition, representing each node in the linked list.
4. **testFile.py**: Contains unit tests implemented with `pytest` to ensure the correctness of the class definitions and methods.

## Class Descriptions

### Book Class

The `Book` class represents a book with the following attributes:

- **title**: A string representing the title of the book.
- **author**: A string representing the author of the book (in "LastName, FirstName" format).
- **year**: An integer representing the year the book was published.

#### Methods

- `__init__(self, title, author, year)`: Initializes a book object.
- `getTitle(self)`: Returns the title of the book.
- `getAuthor(self)`: Returns the author of the book.
- `getYear(self)`: Returns the year the book was published.
- `getBookDetails(self)`: Returns a string representation of the book in the format:
    - Title: Ready Player One, Author: Cline, Ernest, Year: 2011
- `__gt__(self, other)`: Overloads the greater-than operator to compare books based on author, year, and title.

### BookCollectionNode Class

The `BookCollectionNode` class represents a node in the ordered linked list.

#### Methods

- `__init__(self, data)`: Initializes a node with the given book data and a reference to the next node.
- `getData(self)`: Returns the book data stored in the node.
- `getNext(self)`: Returns the next node in the linked list.
- `setData(self, newData)`: Updates the node's book data.
- `setNext(self, newNext)`: Updates the reference to the next node.

### BookCollection Class

The `BookCollection` class manages the ordered linked list of books.

#### Methods

- `__init__(self)`: Initializes an empty book collection with a head reference set to `None`.
- `isEmpty(self)`: Returns `True` if the collection is empty, otherwise `False`.
- `getNumberOfBooks(self)`: Returns the total number of books in the collection.
- `insertBook(self, book)`: Inserts a book into the collection in the correct order based on the author, year, and title.
- `getBooksByAuthor(self, author)`: Returns a string of all book details for a specified author.
- `getAllBooksInCollection(self)`: Returns a string of all books in the collection.
- `removeAuthor(self, author)`: Removes all books by a specified author from the collection.
- `recursiveSearchTitle(self, title, bookNode)`: Recursively searches for a book by its title.

## Usage

To use the classes defined in this project, import them into your Python script:

```python
from Book import Book
from BookCollection import BookCollection
```
You can create instances of Book and BookCollection, and utilize the provided methods to manage your book collection.

#### Example
Here's a brief example demonstrating how to use the classes:

```python
# Create a book collection
bc = BookCollection()

# Create books
b0 = Book("Cujo", "King, Stephen", 1981)
b1 = Book("The Shining", "King, Stephen", 1977)
b2 = Book("Ready Player One", "Cline, Ernest", 2011)
b3 = Book("Rage", "King, Stephen", 1977)

# Insert books into the collection
bc.insertBook(b0)
bc.insertBook(b1)
bc.insertBook(b2)
bc.insertBook(b3)

# Retrieve all books by a specific author
print(bc.getBooksByAuthor("KING, Stephen"))

# Output:
# Title: Rage, Author: King, Stephen, Year: 1977
# Title: The Shining, Author: King, Stephen, Year: 1977
# Title: Cujo, Author: King, Stephen, Year: 1981

# Retrieve all books in the collection
print(bc.getAllBooksInCollection())
```

#### Requirements
Python 3.x
pytest for testing





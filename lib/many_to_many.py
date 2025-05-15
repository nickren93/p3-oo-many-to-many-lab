from datetime import datetime

class Author:
    #pass
    all = []
    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    #return a list of related contracts.
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    #return a list of related books using the Contract class as an intermediary
    def books(self):
        return [contract.book for contract in self.contracts()]
    
    #create and return a new Contract object between the author and the specified 
    # book with the specified date and royalties
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    #return the total amount of royalties that the author has earned from all of their contracts.
    def total_royalties(self): 
        return sum([contract.royalties for contract in self.contracts()])


class Book:
    #pass
    all = []
    def __init__(self, title):
        self.title = title

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [contract.author for contract in self.contracts()]

class Contract:
    #pass
    all = []
    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    #return all contracts that have the same date as the date passed into the method.
    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError("Argument must be an instance of Author class")
        self._author = value

    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise TypeError("Argument must be an instance of Book class")
        self._book = value

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise TypeError("date property should be a string that represents the date when the contract was signed")
        self._date = value

    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise TypeError("royalties property should be a number that represents the percentage of royalties that the author will receive for the book")
        self._royalties = value
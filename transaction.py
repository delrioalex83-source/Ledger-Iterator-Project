#Alex Del Rio
"""transaction class"""
class Transaction:
    """initialize transaction class with properties amount, date, description"""
    def __init__(self, amount, date, description):
        self._amount = amount
        self._date = date
        self._description = description

    """getters for amount, date, description"""
    @property
    def amount (self) -> float:
        return self._amount 
    
    @property
    def date (self) -> str:
        return self._date
    
    @property
    def description (self) -> str:
        return self._description
    
    def __str__(self) -> str:
        """returns a string for displaying the transaction to user."""
        return f"{self.description} - {self.date} : ${self.amount:.2f}"
    
    def __repr__(self) -> str:
        """returns a string suitable for writing to the file."""
        return f"{self.description}, {self.date}, {self.amount:.2f}"
    
    def date_tuple(self):
        """returns date as a tuple for comparison purposes."""
        int_date = self.date.strip()
        pieces = int_date.split("/")
        year, month, day = map(int, pieces)
        return (year, month, day)
    
    def __lt__(self, other: "Transaction") -> bool:
       """compares tuple of transaction dates"""
       return self.date_tuple() < other.date_tuple()
        
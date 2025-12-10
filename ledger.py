#Alex Del Rio
from transaction import Transaction 
"""maintains a list of tranactions and provides methods to add, remove, sort, and display them onto a .txt file"""
class Ledger:
    def __init__(self) -> None:
        self._transactions = [] 

    def add(self, transaction: "Transaction") -> None:
        self._transactions.append(transaction)

    def remove(self, transaction: "Transaction") -> None:
        self._transactions.remove(transaction)

        #sort
    def sort(self) -> None:
        self._transactions.sort()
        

    def __len__(self) -> int:
        return len(self._transactions) #returns a length of the array

    def __iter__(self) -> None: 
        self.n = 0 #reset iterator loop
        return self

    def __next__(self) -> None:
        if self.n >= len(self._transactions): #if n o current instance is greater then the length of total transactions, stop iterator loop
            raise StopIteration
        item = self._transactions[self.n] #assign transaction into array of transactions according to the length 'n' 
        self.n += 1 #integrate
        return item #return appended list
    
    def write_to_file(self) -> None:
        filename = input("Enter a file name: ")
        with open(filename, 'w') as file:
            for t in self._transactions:
                file.write(str(t) + "\n")
    
    def save_to_file(self, filename: str) -> None:
        with open(filename, "w") as file:
            for t in self._transactions:
                file.write(f"{t.description},{t.date},{t._amount}\n")
    
    def load_from_file(self, filename: str) -> None:
        self._transactions.clear() #this will wipe old data
        with open(filename, "r") as file:
            for line in file:
                description, date, amount = line.strip().split(",")
                self._transactions.append(Transaction(float(amount), date, description))
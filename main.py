#Alex Del Rio

from transaction import Transaction
from ledger import Ledger
import check_input
"""main file for iterator ledger"""
def main_menu() -> int:
    print("1. Add Transaction" )
    print("2. Remove Transaction")
    print("3. Sort List")
    print("4. Search by Date")
    print("5. Show List")
    print("6. Save and Quit")
    choice = check_input.get_int_range("Enter your choice: ", 1, 6)
    return choice

def file_menu() -> int:
    print("1. Load from File")
    print("2. Save to File")
    print("3. Create New File")
    print("4. Exit")
    file_choice = check_input.get_int_range("Enter your choice: ", 1, 4)
    return file_choice

def main() -> None:
    ledger = Ledger()
    choice = file_menu()
    if choice == 1:
        ledger.load_from_file(input("Filename: "))
    elif choice == 2:
        ledger.save_to_file(input("Filename: "))
    elif choice == 3:
        print("Starting new empty ledger.")
    elif choice == 4: 
        return

    while True:
        choice = main_menu()

        if choice == 1:
            amount = float(input("Enter amount: "))
            date = input("Enter date (YYYY/MM/DD): ")
            description = input("Enter description: ")
            ledger.add(Transaction(amount, date, description))
            
        elif choice == 2:
            description = input("Enter description of transaction to remove: ")
            for t in ledger:
                if t.description == description:
                    ledger.remove(t)
                    print("Transaction removed.")
                    break
            else:
                print("Transaction not found. \n")
        
        elif choice == 3:
            ledger.sort()
            print("Transactions sorted by date. \n")

        elif choice == 4:
            date = input("Enter date to search (YYY/MM/DD): ")
            for t in ledger:
                if t.date == date:
                    print(t)

        elif choice == 5:
            for t in ledger:
                print(t)

        elif choice == 6:
            filename = input("Enter filename to save ledger: ")
            ledger.save_to_file(filename)
            print("Ledger saved. Exiting program.")
            break

if __name__ == "__main__":
    main()
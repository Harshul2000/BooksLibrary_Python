class Library:
    def __init__(self, list, name):
        self.booksList = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"These books are available in the Library: {self.name}")
        for book in self.booksList:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("The database has been updated. You can take the book now")
        else:
            print(f"Book is already taken by {self.lendDict[book]}")

    def addBook(self, book):
        self.booksList.append(book)
        print("Book has been added to the database")

    def returnBook(self, book):
        self.lendDict.pop(book)

if __name__ == '__main__':
    harry = Library(['College', 'School', 'Harry Potter', 'Cook book', 'Algorithms by CLRS'], "LearnHere")

    while(True):
        print(f"Welcome to the {harry.name} library. Enter your choice to continue")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        user_choice = input()
        if user_choice not in ['1','2','3','4']:
            print("Please enter a valid option")
            continue

        else:
            user_choice = int(user_choice)


        if user_choice == 1:
            harry.displayBooks()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend:")
            user = input("Enter your name")
            harry.lendBook(user, book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to add:")
            harry.addBook(book)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to return:")
            harry.returnBook(book)

        else:
            print("Not a valid option")


        print("Press c to quit and d to continue")
        user_choice2 = ""
        while(user_choice2!="c" and user_choice2!="d"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()

            elif user_choice2 == "d":
                continue
#Create a Class as Library:
class Library:
    def __init__(self,list,name):
        self.bookList=list
        self.name=name
        self.lendDict={}
    def displayBooks(self):
        print(f"we have the following books in library:{self.name}")
        for book in self.bookList:
            print(book)
    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("book dictionary has been updated:You can take the book now")
        else:
            print(f"Book is already used by {self.lendDict[book]}")
    def addBook(self,book):
        self.bookList.append(book)
        print("book has been addes to the booklist")
    def returnBook(self, book):
        self.lendDict.pop(book)
if __name__ == '__main__':
    saloni=Library(['Python','JAVA','C++','C language'],"Book hut")
    while True:
        print(f"Welcome to {saloni.name} Library. Enter your choice to continue:")
        print("1. Display Books")
        print("2. lend a Book")
        print("3. Add a Book")
        print("4. Return Book")
        user_choice=input()
        if user_choice not in ['1','2','3','4']:
            print("Please Enter a Numeric valid Option:")
            continue
        else:
            user_choice=int(user_choice)
        if(user_choice==1):
            saloni.displayBooks()
        elif (user_choice==2):
            book=input("Enter the name of the book u want to lend:")
            user=input("Enter your name:")
            saloni.lendBook(user,book)
        elif(user_choice==3):
            book=input("Enter the name of the book u want to add:")
            saloni.addBook(book)
        elif(user_choice==4):
            book=input("Enter the name of the book u want to return:")
            saloni.returnBook(book)
        else:
            print("Not avalid option:")


        print("Enter q for exit and c to continue:")
        user_choice2=""
        while(user_choice2 !='q' and user_choice2!='c'):
            user_choice2=input()
            if user_choice2=="q":
                exit()
            elif user_choice2=="c":
                continue


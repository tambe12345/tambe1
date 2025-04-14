from LibrayMenu import menu
from LibraryAdd import addbook
from LibraryDelete import deletebook
from LibraryUpdate import updatebook
from LibraryView import viewbook,viewallbooks
while(True):
    menu()
    try:
        ch=int(input("Enter Ur Choice:"))
        match(ch):
            case 1:
                addbook()
            case 2:
                deletebook()
            case 3:
                updatebook()
            case 4:
                viewbook()
            case 5:
                viewallbooks()
            case 6:
                print("Thx for Using this App")
                break
            case _:
                print("\tUr Selection of Operation is Wrong--try again")
    except ValueError:
        print("Don't Enter strs, alnums and symbols for Integer Choice:")
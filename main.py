from BestSellers import *

def main():
    # menu ----
    string_menu = '''
----- Bestsellers -----
    
[1] Display books by year range
[2] Display books by month and year 
[3] Display books by author
[4] Display books by title
'''
    # variable true when user wants to continue
    repeat = True
    # repeat loop -- until the user chooses n
    while repeat:
        print(string_menu)
        while True:
            try:
                choice = int(input("Select option 1-4 or 0 to exit: "))
                if choice in range(5):
                    break
                continue
            except:
                continue

        if choice == 1:
            print("\n")
            print("[1] Display books by year range [1900-2050]")
            print(books_in_year_range())
        elif choice == 2:
            print("\n")
            print("[2] Display books by month and year")
            print(books_in_month_year())
        elif choice == 3:
            print("\n")
            print("[3] Display books by author")
            print(books_by_author())
        elif choice == 4:
            print("\n")
            print("[4] Display books by title")
            print(books_by_title())
        elif choice == 0:
            print("\nThanks for your time, good bye!")
            repeat = False
            break

        # exit program
        input('Enter any key to continue...')

if __name__ == '__main__':
    main()
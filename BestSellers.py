import re
def books_in_year_range(year_start=None, year_end=None, menu_call=None):
    """
    books_in_year_range displays all books which reached the #1 spot between two years provided (inclusive)
    :param year_start: start year provided
    :param year_end: end year provided
    :param menu_call: prints if menu is called
    :return: list of books within year range
    """
    books = []
    books_string = ''
    # requests user to input start year if none
    if year_start is None:
        while True:
            try:
                year_start = int(input('Enter the starting year: '))
                if year_start not in range(1900,2050):
                    print('Year start must be in range 1900-2050.')
                    continue
                break
            except:
                print('Invalid entry. Enter a whole number.')
                continue
    # requests user to input end year if none
    if year_end is None:
        while True:
            try:
                year_end = int(input('Enter the ending year: '))
                if year_end not in range(1900,2050):
                    print('Year end must be in range 1900-2050.')
                    continue
                break
            except:
                print('Invalid entry. Enter a whole number.')
                continue
    # opens file with list of bestsellers, reads lines, and closes file
    file = open('bestsellers.txt', 'r')
    file_as_list = file.readlines()
    file.close()
    # finds books within year range and adds them to a list
    for line in file_as_list:
        line_split = line.strip().split('\t')
        for year in range(year_start,year_end+1):
            if line_split[3].strip().endswith(str(year)):
                books.append(line_split[0])
                books_string = books_string + str(f'{year}: ') + line_split[0] + '\n'
    # returns list of bestselling books
    if len(books) > 0 :
        return f'Best selling books between {year_start}-{year_end} (inclusive):\n' + books_string
    else:
        return f'No match found.'
def books_in_month_year(month=None, year=None, menu_call=None):
    """
    books_in_month_year displays all books which reached the #1 spot within a specific month and year
    :param month: month provided by user
    :param year: year provided by user
    :param menu_call: prints if menu is called
    :return: list of books
    """
    books = []
    books_string = ''
    # requests user to input month if none
    if month is None:
        while True:
            try:
                month = int(input('Enter the month [1-12]: '))
                if month not in range(1, 12):
                    print('Year start must be in range 1-12.')
                    continue
                break
            except:
                print('Invalid entry. Enter a whole number.')
                continue
    # requests user to input year if none
    if year is None:
        while True:
            try:
                year = int(input('Enter the year [1900-2050]: '))
                if year not in range(1900, 2050):
                    print('Year must be in range 1900-2050.')
                    continue
                break
            except:
                print('Invalid entry. Enter a whole number.')
                continue
    # opens file with list of bestsellers, reads lines, and closes file
    file = open('bestsellers.txt', 'r')
    file_as_list = file.readlines()
    file.close()
    # finds books within month/year and adds them to a list
    for line in file_as_list:
        line_split = line.strip().split('\t')
        author_name = line_split[1].strip()
        if line_split[3].strip().startswith(str(f'{month}/')) and line_split[3].strip().endswith(str(year)):
            books.append(line_split[0])
            books_string = books_string + '"' +line_split[0] + f'" by {author_name}' + '\n'
    # returns list of bestselling books
    if len(books) > 0 :
        return f'Best selling books in {month}/{year}:\n' + books_string
    else:
        return f'No match found.'
def books_by_author(search_string=None):
    """
    books_by_author displays all books which reached the #1 spot by a specific author
    :param search_string: author search string provided by user
    :return: list of books by author
    """
    books = []
    books_string = ''
    # requests user to input search string if none
    if search_string is None:
        while True:
            try:
                search_string = str(input('Enter the author\'s name: ')).strip().lower()
                if len(search_string) == 0:
                    continue
                break
            except:
                print('Invalid author\'s name.')
                continue
    # opens file with list of bestsellers, reads lines, and closes file
    file = open('bestsellers.txt', 'r')
    file_as_list = file.readlines()
    file.close()
    # finds books with author's name and adds them to a list
    for line in file_as_list:
        line_split = line.strip().split('\t')
        author_name = line_split[1].strip()
        author_name_lower = author_name.lower()
        match_author = re.search(search_string, author_name_lower)
        if match_author:
            books.append(line_split[0])
            books_string = books_string + '"' + line_split[0] + f'" by {author_name}' + '\n'
    # returns list of bestselling books
    if len(books) > 0 :
        return f'Books by author:\n' + books_string
    else:
        return f'No match found.'
def books_by_title(search_string=None):
    """
    books_by_title displays all books which reached the #1 spot with a specific title
    :param search_string: title search string provided by user
    :return: list of books with search string
    """
    books = []
    books_string = ''
    # requests user to input search string if none
    if search_string is None:
        while True:
            try:
                search_string = str(input('Enter the book title search string: ')).strip().lower()
                if len(search_string) == 0:
                    continue
                break
            except:
                print('Invalid title\'s name.')
                continue
    # opens file with list of bestsellers, reads lines, and closes file
    file = open('bestsellers.txt', 'r')
    file_as_list = file.readlines()
    file.close()
    # finds books with title and adds them to a list
    for line in file_as_list:
        line_split = line.strip().split('\t')
        author_name = line_split[1].strip()
        book_title = line_split[0].strip()
        book_title_lower = book_title.lower()
        match_title = re.search(search_string, book_title_lower)
        if match_title:
            books.append(line_split[0])
            books_string = books_string + '"' + line_split[0] + f'" by {author_name}' + '\n'
    # returns list of bestselling books
    if len(books) > 0 :
        return f'Books with title:\n' + books_string
    else:
        return f'No match found.'
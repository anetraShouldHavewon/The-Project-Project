import sqlite3
import csv

connection = sqlite3.connect("H:/Digital Tech/Year 13/Database Standard/The Project Project/book_film_adaptation.db")
cursor = connection.cursor()

def get_data_from_csv(info_file, wanted_column_name, starting_index, final_index):
    ''' getting a list of elements from a certain column within a certain range of rows in a csv'''
    column_num = 0
    for column in range(len(info_file[0])):
        column_name = info_file[0][column]
        if column_name == wanted_column_name:
            column_num = column
    
    list_of_data = []
    for index in range(starting_index, final_index):
        data = info_file[index][column_num]
        list_of_data.append(data)
    
    return(list_of_data)

with open("books.csv", 'r', encoding = "utf-8")as file:
    new_file = csv.reader(file)
    book_info_list = list(new_file)
    # getting the names of the books
    titles = get_data_from_csv(book_info_list, "title", 1, 5)
    num_of_pages = get_data_from_csv(book_info_list, "  num_pages", 1, 5)
    authors = get_data_from_csv(book_info_list, "authors", 1, 5)


query1 = "INSERT INTO Book(title,number_of_pages,author) VALUES (?,?,?)"

for index in range(len(titles)):
    title = titles[index]
    num_of_page = num_of_pages[index]
    author = authors[index]
    cursor.execute(query1, ((title,), (num_of_page,), (author,)))

connection.commit()
connection.close()



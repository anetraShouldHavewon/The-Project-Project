import sqlite3
import csv

connection = sqlite3.connect("H:/Digital Tech/Year 13/Database Standard/book_film_adaptation.db")
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

with open("H:/Digital Tech/Year 13/Database Standard/books.csv", mode = "r")as file:
    new_file = csv.reader(file)
    book_info_list = list(new_file)
    # getting the names of the books
    book_titles = get_data_from_csv(book_info_list, "title", 1, 6)
    print(book_titles)
    

    
    


    
    
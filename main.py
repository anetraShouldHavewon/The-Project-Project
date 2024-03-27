import sqlite3

connection = sqlite3.connect("book_film_adaptation.db")
cursor = connection.cursor()

def first_menu():
    print("WELCOME TO BOOK VS FILM")
    print("The world's most good film adaptation website")
    user_input_1 = input("Would you like to just \nA. look at reviews or \nB. actually write them\nPress A or B.\nPlease\n")
    while user_input_1 not in ["A", "B"]:
        user_input_1 = input("Type in a capital A or B. Do it properly. Or else...\n")
    want_to_review = False
    if user_input_1 == "A":
        want_to_review = True
    return want_to_review


def acceptable_list(lowest_value, highest_value):
    initial_acceptable_list = [x for x in range(lowest_value, highest_value)]
    final_acceptable_list = []
    for item in initial_acceptable_list:
        item = str(item)
        final_acceptable_list.append(item)

    return final_acceptable_list

want_to_review = first_menu()

if want_to_review is True:
    query1 = "SELECT adapted_book, film_adaptation FROM Adaptation"
    query2 = "SELECT title FROM Book WHERE id = ?"
    query3 = "SELECT title FROM Film WHERE id = ?"
    adaptation_raw_info = cursor.execute(query1).fetchall()
    book_ids = []
    film_ids = []
    book_titles = []
    film_titles = []
    for index in range(len(adaptation_raw_info)):
        book_id = adaptation_raw_info[index][0]
        film_id = adaptation_raw_info[index][1]
        book_ids.append(book_id)
        film_ids.append(film_id)
        book_title = cursor.execute(query2, (book_id,)).fetchone()
        book_titles.append(book_title[0])
        film_title = cursor.execute(query3, (film_id,)).fetchone()
        film_titles.append(film_title[0])

    print("Choose which adaptation to review!!")
    for index, element in enumerate(book_titles):
        print(f"{index+1}. '{film_titles[index]}' which is an adaptation of '{element}'")
    
    user_input_2 = input("Press a number: ")
    acceptable_ids = acceptable_list(1, len(book_titles)+1)
    while user_input_2 not in acceptable_ids:
        user_input_2 = input("Do it properly. Or else...\n")
        
    book_rating_out_of_5 = input("Rate the book out of 5:\n")
    acceptable_ratings = acceptable_list(0, 6)
    while book_rating_out_of_5 not in acceptable_ratings:
        book_rating_out_of_5 = input("Type in a number from 0 to 5 you mewling quim: ")

    book_things_I_like = input(f"Anything you liked about the book{book_title}:\n")
    book_id = book_ids[int(user_input_2)-1]
    book_title = book_titles[int(user_input_2)-1]
    query4 = "INSERT INTO Book_Review (book_id, overall_rating, things_I_like) VALUES(?, ?, ?)"
    cursor.execute(query4, (book_id, book_rating_out_of_5, book_things_I_like))
    connection.commit()


    print("Review Completed!")




if want_to_review is False:
    print("Just keep on being a passive observer of existance.")
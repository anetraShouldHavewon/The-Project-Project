import sqlite3

connection = sqlite3.connect("book_film_adaptation.db")
cursor = connection.cursor()

def first_menu():
    print("WELCOME TO BOOK VS FILM")
    print("The world's most good film adaptation website")
    user_input_1 = input("Would you like to just \nA. look at reviews or \nB. actually write them\nC. Neither\nPress A, B or C.\nPlease\n")
    while user_input_1 not in ["A", "B", "C"]:
        user_input_1 = input("Type in a capital A or B. Do it properly. Or else...\n")
    want_to_review = False
    if user_input_1 == "A":
        want_to_review = True
    if user_input_1 == "C":
        print("Sure Jan")
        quit()
    return want_to_review


def boundary_test_user_input(lowest_value, highest_value, initial_message, recurring_message):
    initial_acceptable_list = [x for x in range(lowest_value, highest_value)]
    final_acceptable_list = []
    for item in initial_acceptable_list:
        item = str(item)
        final_acceptable_list.append(item)

    user_input = input(initial_message)
    while user_input not in final_acceptable_list:
        user_input = input(recurring_message)

    return user_input

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
    name = input("What's your name?")
    print("Choose which adaptation to review!!")
    for index, element in enumerate(book_titles):
        print(f"{index+1}. '{film_titles[index]}' which is an adaptation of '{element}'")
    
    chosen_adaptation = boundary_test_user_input(1, len(book_titles)+1, "Press a number: ", "Do it properly. Or else...\n")
    # Writing a book review
    book_id = book_ids[int(chosen_adaptation)-1]
    film_id = film_ids[int(chosen_adaptation)-1]
    book_title = book_titles[int(chosen_adaptation)-1]
    film_title = film_titles[int(chosen_adaptation)-1]
    book_rating_out_of_5 = boundary_test_user_input(0, 6, f"Rate the book, {book_title}, out of 5:\n", "Type in a number from 0 to 5 you mewling quim: ")
    book_things_I_like = input(f"Anything you liked about the book {book_title}?:\n")
    query4 = "INSERT INTO Book_Review (book_id, overall_rating, things_I_like) VALUES(?, ?, ?)"
    cursor.execute(query4, (book_id, book_rating_out_of_5, book_things_I_like))
    connection.commit()
    # Writing a film review
    film_rating_out_of_5 = boundary_test_user_input(0, 6, f"Rate the film, {film_title}, out of 5:\n", "Type in a number from 0 to 5 you mewling quim: ")
    film_things_I_like = input(f"Anything you liked about the film {film_title}?:\n")
    query5 = "INSERT INTO Film_Review (film_id, overall_rating, things_I_like) VALUES(?, ?, ?)"
    cursor.execute(query5, (film_id, film_rating_out_of_5, film_things_I_like))
    connection.commit()
    # Writing an adaptation review
    faithfulness_rating = boundary_test_user_input(0, 6, f"On a scale of 1 ~ 5 how faithful was the movie adaptation to the book?\n", "Type in a number from 0 to 5 you mewling quim: ")
    adaptation_comments = input("Explanations for why you scored it this way: ")
    query6 = "INSERT INTO Adaptation_Review (film_id, overall_rating, things_I_like) VALUES(?, ?, ?)"
    # get adaptation_id next
    print("Review Completed!")




if want_to_review is False:
    print("Just keep on being a passive observer of existance.")
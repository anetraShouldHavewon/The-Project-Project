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

    return(want_to_review)


want_to_review = first_menu()
if want_to_review is True:
    query1 = "SELECT adapted_book, film_adaptation FROM Adaptation"
    query2 = "SELECT title FROM Book WHERE id = ?"
    query3 = "SELECT title FROM Film WHERE id = ?"
    adaptation_raw_info = cursor.execute(query1).fetchall()
    book_titles = []
    film_titles = []
    for index in range(len(adaptation_raw_info)):
        book_title = cursor.execute(query2, (adaptation_raw_info[index][0],)).fetchone()
        book_titles.append(book_title[0])
        film_title = cursor.execute(query3, (adaptation_raw_info[index][1],)).fetchone()
        film_titles.append(film_title[0])

    print("Choose which adaptation to review!!")
    for index, element in enumerate(book_titles):
        print(f"{index+1}. '{film_titles[index]}' which is an adaptation of '{element}'")
    user_input_2 = input("Press a number: ")
    acceptable_ids1 = [x for x in range(1,len(book_titles)+1)]
    acceptable_ids2 = []
    for id in acceptable_ids1:
        id = str(id)
        acceptable_ids2.append(id)
    
    while user_input_2 not in acceptable_ids2:
        user_input_2 = input("Do it properly. Or else...\n")
        
    rating_out_of_5 = input("Rate out of 5:\n")
    acceptable_ratings1 = [x for x in range(0, 6)]
    acceptable_ratings2 = []
    for rating in acceptable_ratings1:
        rating = str(rating)
        acceptable_ratings2.append(rating)

    while rating_out_of_5 not in acceptable_ratings2:
        rating_out_of_5 = input("Type in a number from 0 to 5 you mewling quim: ")

    book_title = book_titles[int(user_input_2)-1]
    things_I_like = input(f"Anything you liked about {book_title}")



if want_to_review is False:
    print("Just keep on being a passive observer of existance.")
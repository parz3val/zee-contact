def create_number_table(cursor):
    # cur.execute("CREATE TABLE movie(title, year, score)")
    cursor.execute(
        "CREATE TABLE  IF NOT EXISTS contacts(contact_name, contact_number);"
    )


def save(contact_name, contact_number, databse):
    # TODO: Save contact number and name in the database
    # Imagine cursor as you being in a library moving
    # According to your needs depending on where you need to find stuff
    # Like get a table
    # borrow a book
    # read a book
    # or write a book even
    cur = databse.cursor()
    create_number_table(cur)
    cur.execute(
        # The bug is here
        "INSERT INTO contacts VALUES(?, ?)",
        (contact_name, contact_number),
    )


def add_new_contact(database):
    contact_name = input("What is the name of your good friend my good friend?")
    if contact_name == "":
        print("What the hell we trusted you")
    else:
        contact_number = input("What is the number of that person?")
        save(contact_name, contact_number, database)


def view_all_contact(database):
    cur = database.cursor()
    res = cur.execute("SELECT * FROM contacts;")
    text = res.fetchall()
    print(text)


def search_by_name():
    pass


import sqlite3


def server():

    # Start our database
    # We need to open an sqlite database in python
    # We can call this anything, if you don't have a database named CONTACTSDB.sql it will
    # create a new one
    # We created the library of contacts here.
    database = sqlite3.connect("CONTACTSDB.sql")

    print("*" * 50)
    print(" " * 2, "CONTAXT APP")
    print("*" * 50)

    # Happens all the time
    # Things inside the while block are infinite loop

    while True:
        # Start of the while block
        print("Press 1 if you want to you add new contact")
        print("Press 2 if you want to view all contact")
        print("Press 3 if you want to search by name")
        user_input = input("")

        # Turn user input into the number so we can
        # compare later
        user_input = int(user_input)

        # When you take input from user in python
        # through the command line
        # you get a string

        # we have to use an if statement here

        if user_input == 1:
            add_new_contact(database)
        if user_input == 2:
            view_all_contact(database)
        if user_input == 3:
            search_by_name()
        print(user_input)
        # End of the while block


server()

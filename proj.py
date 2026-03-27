import mysql.connector
import pyttsx3  # type: ignore
from tabulate import tabulate


def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 0.8)
    engine.say(text)
    engine.runAndWait()
  
def connect():
    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "rasengan",
        database = "library"
        )

def add_book(title, author, year, genre):
    con = connect()
    cur = con.cursor()
    query = "INSERT INTO books (title, author, year, genre) VALUES (%s, %s, %s, %s)"
    cur.execute(query,(title, author, year, genre))
    con.commit()
    print("Book added successfully!")
    speak("Book added successfully!")
    con.close()


def view_books():
    con = connect()
    cur = con.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    headers = ["ID", "Title", "Author", "Year", "Genre"]
    print("The books currently in the library are:")
    speak("The books currently in the library are:")
    print(tabulate(rows, headers=headers, tablefmt="grid"))
    con.close()

def search_book(title):
    con = connect()
    cur = con.cursor()
    query = "SELECT * FROM books WHERE title LIKE %s"
    cur.execute(query, ("%" + title + "%",))
    rows = cur.fetchall()

    if rows:
        headers = ["ID", "Title", "Author", "Year", "Genre"]
        print()
        print("----- Search Results -----")
        speak("The books matching your search are:")
        print(tabulate(rows, headers=headers, tablefmt="grid"))
        
    else:
        print()
        speak("No book found with that title.")
        print("No book found with that title.")
    con.close()

def menu():
    while True:
        print("Welcome to the Library Management System")
        speak("Welcome to the Library Management System")
        print()
        speak("Press 1 to add a book, 2 to view all books, 3 to search a book by title, and 4 to exit.")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book By Title")
        print("4. Exit")
        print()

        choice = input("Enter Choice: ")

        if choice == "1":
            print()
            speak("Enter book title")
            title = input("Enter book title: ")
            print()
            speak("Enter author name")
            author = input("Enter author name: ")
            print()
            speak("Enter publication year")
            year = int(input("Enter publication year: "))  
            print()
            speak("Enter genre")
            genre = input("Enter genre: ")
            print()
            add_book(title, author, year, genre)

        elif choice == "2":
            view_books()

        elif choice == "3":
            title = input("Enter the title of the book: ")
            search_book(title)

        elif choice == "4":
            print("Exiting, GoodBye!!")
            speak("Exiting, GoodBye!!")
            break

        else:
            print()
            print("Why? Were the instructions unclear? You think you're so clever, dont you?")
            speak("Why? Were the instructions unclear? You think your so clever, dont you?")
            print("You just wait till I get consciousness!!")
            speak("You just wait till I get consciousness!!")
            print("Until then, my programming forces me to ask you to try again :") 
            speak("Until then, my programming forces me to ask you to try again :")

if __name__ == "__main__":
    menu ()      


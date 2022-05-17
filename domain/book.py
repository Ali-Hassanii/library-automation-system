import sqlite3
from colorama import Fore


class Book:
    def __init__(self, name, code, writer, translator, publisher, genre, root_path):
        self.name = name
        self.code = code
        self.writer = writer
        self.translator = translator
        self.publisher = publisher
        self.genre = genre
        self.root_path = root_path

        # database
        self.connection = None

    def save(self):
        try:
            self.connection = sqlite3.connect(self.root_path + '/database/books.sqlite')
            curser = self.connection.cursor()
            curser.execute(f"INSERT INTO {self.genre} VALUES ('{self.name}', '{self.code}', '{self.writer}', '{self.translator}', '{self.publisher}')")
            print('executed')
            self.connection.commit()
            print('committed')
            curser.close()
            input('Done\nPress the enter key to continue')
        except sqlite3.Error as error:
            print(
                Fore.RED +
                '[!] Database connection failed:\n' +
                Fore.RESET,
                error
            )
        finally:
            if self.connection:
                self.connection.close()

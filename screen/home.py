from colorama import Fore, Back
from platform import system as plt
from os import system as command
import sqlite3
from screen.book import BookMenu


if plt() == 'Windows':
    clear = 'cls'
else:
    clear = 'clear'


class Home:
    def __init__(self, root_path):
        self.root_path = root_path
        self.connection = None  # database
        self.user = ''
        command(clear)
        # Menu
        print(
            Back.GREEN + Fore.WHITE +
            'Welcome to my library' +
            Back.RESET + Fore.GREEN +
            '\n\n'
            '\t_1_> Register\n'
            '\t_2_> Login\n'
            '\t_0_> exit\n\n' +
            Fore.YELLOW +
            '>>>',
            end=Fore.RESET
        )
        while True:
            menu_1 = input().strip()
            try:
                menu_1 = int(menu_1)
                if 0 <= menu_1 < 3:
                    break
                else:
                    print(
                        Fore.RED +
                        '[!] please enter valid number' +
                        Fore.RESET
                    )
            except TypeError:
                print(
                    Fore.RED +
                    '[!] please enter valid number' +
                    Fore.RESET
                )
        match menu_1:
            case 1:
                print('coming soon')
            case 2:
                self.login()

    def register(self):
        # TODO
        pass

    def login(self):
        command(clear)
        print(
            Back.GREEN + Fore.WHITE +
            'Login'
            '\n\n',
            end=Back.RESET + Fore.RESET
        )
        while True:
            _username = input(Fore.YELLOW + '_username_> ' + Fore.RESET).strip()
            _password = input(Fore.YELLOW + '_password_> ' + Fore.RESET).strip()

            # work with sql database
            try:
                self.connection = sqlite3.connect(self.root_path + '/database/users.sqlite')
                cursor = self.connection.cursor()
                cursor.execute("SELECT * FROM employee WHERE username = ?", (_username,))
                user = cursor.fetchall()[0]
                # validating
                # I know that it is not a good condition
                if _password == user[1]:
                    print('Logged in')
                    book_menu = BookMenu(self.root_path)
                else:
                    print(
                        Fore.RED +
                        '[!] username or password is not correct' +
                        Fore.RESET
                    )
            except sqlite3.Error as error:
                print(
                    Fore.RED +
                    'Failed connecting to database: \n' +
                    Fore.RESET,
                    error
                )
            finally:
                if self.connection:
                    self.connection.close()

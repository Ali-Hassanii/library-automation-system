from colorama import Fore, Back
from platform import system as plt
from os import system as command
import sqlite3

if plt() == 'Windows':
    clear = 'cls'
else:
    clear = 'clear'


class Home:
    def __init__(self, _data_folder):
        self.data_folder = _data_folder
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
            '>>>' +
            Fore.RESET
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
            'Login' +
            Back.RESET + Fore.YELLOW +
            '\n\n'
        )
        while True:
            _username = input('_username_> ').strip()
            _password = input('_password_> ').strip()

            # work with sql database
            try:
                self.connection = sqlite3.connect(self.data_folder + '/database/users.sqlite')
                cursor = self.connection.cursor()
                cursor.execute("SELECT * FROM employee WHERE username = ?", (_username,))
                user = cursor.fetchall()[0]
                # validating
                # I know that it is not a good condition
                if _password == user[1]:
                    print('logged in')
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

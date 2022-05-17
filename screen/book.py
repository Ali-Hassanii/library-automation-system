from colorama import Fore, Back
from sys import exit
from domain.book import Book


class BookMenu:
    def __int__(self):
        print(
            Back.GREEN + Fore.WHITE +
            'Book menu' +
            Back.RESET + Fore.GREEN +
            '\n\n'
            '_1_> Load all books about a specific genre'
            '_2_> Load a book'
            '_3_> Add a new book'
            '_4_> Edit Existing book'
            '_5_> Delete a book'
            '<_0_ Exit' +
            Fore.YELLOW +
            '\n\n'
            '>>> ',
            end=Fore.RESET
        )

        while True:
            book_menu = input().strip()
            try:
                book_menu = int(book_menu)
                if 0 <= book_menu < 6:
                    break
                else:
                    print(
                        Fore.RED +
                        '[!] Please enter valid number' +
                        Fore.RESET
                    )
            except TypeError:
                print(
                    Fore.RED +
                    '[!] Please enter valid number' +
                    Fore.RESET,
                    TypeError
                )

        match book_menu:
            case 3:
                _name = input(Fore.YELLOW + 'Name >>>' + Fore.RESET).strip()
                _code = input(Fore.YELLOW + 'Code >>>' + Fore.RESET).strip()
                _writer = input(Fore.YELLOW + 'Writer >>>' + Fore.RESET).strip()
                _translator = input(Fore.YELLOW + 'Translator >>>' + Fore.RESET).strip()
                _publisher = input(Fore.YELLOW + 'Publisher >>>' + Fore.RESET).strip()
                _genre = input(Fore.YELLOW + 'Genre >>>' + Fore.RESET).strip()

                book = Book(_name, _code, _writer, _translator, _publisher, _genre)
            case 0:
                exit(0)
            case _:
                'Coming soon'

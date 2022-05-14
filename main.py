from os import system
from importlib import import_module


def install_prerequisites():
    while True:

        modules = ('colorama',)

        for module in modules:
            try:
                import_module(module)
            except ModuleNotFoundError:
                install_license = input(
                    f'[!] `{module}` is not installed\n' +
                    'Install the module? [Y/N] '
                )
                if install_license[0] == 'y' or install_license[0] == 'Y':
                    print(f'Installing {module}, please wait ...\n')
                    print('-' * 15, '***', '-' * 15, '\n')
                    system('pip3 install {0}'.format(module))
                else:
                    sure = input('The app might not working! Are you sure? [Y/N] ')
                    if sure[0] == 'y' or sure[0] == 'Y':
                        print('Abort')
                        break
                    else:
                        install_license = 'Y'
        break


if __name__ == '__main__':
    install_prerequisites()

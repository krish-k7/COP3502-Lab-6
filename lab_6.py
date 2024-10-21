def encode(passwd):
    return ''.join([str(int(char) + 3) for char in passwd])


def menu():
    print(
        'Menu',
        '-' * 13,
        '1. Encode',
        '2. Decode',
        '3. Quit',
        sep='\n'
    )
    selection = int(input('Please enter an option: '))

    return selection


def main():
    stored_passwd = None

    while True:
        selection = menu()

        match selection:
            case 1:
                passwd = input('Please enter your password to encode: ')
                stored_passwd = encode(passwd)
                print('Your password has been encoded and stored!')
            case 2:
                # Decode implementation goes here
                pass
            case 3:
                break


if __name__ == '__main__':
    main()
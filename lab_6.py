# Krish Kapadia

def encode(passwd):
    return ''.join([str((int(char) + 3) % 10) for char in passwd])


def decode(stored_passwd):
    decoded_pass = ''

    for digit in stored_passwd:
        decoded_digit = (int(digit) - 3) % 10
        decoded_pass += str(decoded_digit)
    return decoded_pass


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
                decoded_passwd = decode(stored_passwd)
                print(f'The encoded password is {stored_passwd}, and the original password is {decoded_passwd}.')
                print(' ')
            case 3:
                break


if __name__ == '__main__':
    main()
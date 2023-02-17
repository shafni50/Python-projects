def add():
    media = input('Media : ')
    name = input('Username / Email : ')
    pwd = input('Password : ')


    with open('passwords.txt', 'a') as e: #a --> append
        e.write( 'Media : ' + media + ' | ' + 'Username / Email : ' +name + ' | ' + 'Password : ' + pwd + '\n')

while True:
    mode = input('would you like to\033[1m add\033[0m details or\033[1m quit\033[0m? ').lower()
    if mode == 'quit':
        break

    if mode == 'add':
        add()
    else:
        print('please try again.')
        pass
CONTACTS = {}


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except (KeyError, ValueError, IndexError):
            print("Repeat and enter correct user name and phone")
        else:
            return result
    return wrapper


@input_error
def add():
    for i in range(3):
        contact = input('Your name (space) your phone: ')
        cont = contact.split(' ')
        name = cont[0]
        phone = cont[1]
        if len(name) > 0:
            CONTACTS.update({name: phone})
        ques = input('Do you want to add contact? ')
        if ques == "yes":
            i += 1
            break
    return CONTACTS


@input_error
def change():

    contact_n = input('Your name (space) your new phone: ')
    cont_n = contact_n.split(' ')
    name = cont_n[0]
    phone_n = cont_n[1]
    for k in CONTACTS:
        if name == k:
            CONTACTS[k] = phone_n
    return CONTACTS


@input_error
def get_phone(user_phone):
    name = input('Username: ')
    if user_phone:
        for k in CONTACTS:
            if name == k:
                user_phone = CONTACTS.get(k)
            return user_phone


def show_all():
    return CONTACTS


@input_error
def main():
    gameloop = True
    while gameloop:
        request = input('Enter command: ').lower()
        if request == 'hello':
            print('How can I help you?')

        elif request == 'add':
            print(add())
        elif request == 'change':
            print(change())
        elif request == 'phone':
            print(get_phone())
        elif request == 'show all':
            print(show_all())
        elif request in ('good bye', 'close', 'exit'):
            print('Good bye!')
            gameloop = False
        else:
            print('I don\'t understand you')

    return gameloop


if __name__ == '__main__':
    main()

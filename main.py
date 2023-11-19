PHONEBOOK = {}


def input_error(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except KeyError:
            return 'Enter user name'
        except ValueError:
            return 'Give me name and phone please'
        except IndexError:
            return 'Invalid input!\n You must enter: Command Name Phone'
    return inner


@input_error
def hello_handler(*args):
    return 'How can I help you?'


@input_error
def add_contact(name, phone):
    PHONEBOOK[name] = phone
    return PHONEBOOK


@input_error
def show_all_contact():
    # new_phonebook = map(lambda item: item [name, phone for name, phone in phonebook.items()])
    return PHONEBOOK


@input_error
def change_contact(name, phone):
    PHONEBOOK[name] = phone
    return PHONEBOOK


@input_error
def get_phone_handler(name):
    return PHONEBOOK[name]

@input_error
def exit_handler(*args):
    return 'Good bye!'


def main():
    while True:
        user_input = input('Enter Command: ').lower()
        if user_input == 'hello':
            result = hello_handler(user_input)
        elif user_input.startswith('add '):
            _, name, phone = user_input.split()
            result = add_contact(name, phone)
        elif user_input.startswith('change '):
            _, name, phone = user_input.split()
            result = change_contact(name, phone)
        elif user_input.startswith('show all'):
            result = show_all_contact()
        elif user_input.startswith('phone '):
            _, name = user_input.split()
            result = get_phone_handler(name)
        elif user_input in ('good bye', 'bye', 'close', 'exit' ):
            result = exit_handler(user_input)
            break
        print(result)    
    return result


finish = main()
print(finish)

        
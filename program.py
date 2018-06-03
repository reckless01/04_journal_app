import journal
# TODO update edit: logic for non-int when selecting entry, list entries more user friendly
# TODO update remove: logic for non-int when selecting entry
# TODO record date/time of entries
# TODO obscure entries?
# TODO Load different journals
# TODO password protect journals? Users?
# TODO share entries?


def main():
    print_header()
    run_event_loop()


def print_header():
    print('---------------------')
    print('     Journal App     ')
    print('---------------------')
    print(' ')


def run_event_loop():

    print('What would you like to do with your journal?')
    print('')
    print('Commands: [L]ist, [A]dd, [E]dit, [D]elete, <return> to exit')
    print('')
    cmd = 'EMPTY'
    journal_name = 'default'
    journal_data = journal.load(journal_name)

    while cmd != 'x' and cmd:
        cmd = input('List, Add, Edit, Delete, <return> to exit: ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd == 'e':
            edit_entry(journal_data)
        elif cmd == 'd':
            del_entry(journal_data)
        elif cmd != 'x' and cmd:
            print("Sorry, we don't understand the command: {}".format(cmd))

    print('Done, goodbye...')
    journal.save(journal_name, journal_data)


def list_entries(data):
    print('')
    print('Your journal entries: ')
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print('* [{}] {}'.format(idx+1, entry))
    print('')


def list_entries_r(data):
    print('')
    print('Your journal entries: ')
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print('* [{}] {}'.format(idx + 1, entry))
    print('')


def add_entry(data):
    text = input('Type your entry: ')
    journal.add_entry(text, data)


def edit_entry(journal_data):
    list_entries_r(journal_data)
    print('================== ')
    print(' ')
    n = int(input('Please choose the number of the entry you want to edit: '))
    mn = n - 1
    print(journal_data[mn])
    print(' ')
    text = input('Type your new entry: ')
    journal.edit_entry(text, journal_data, n)


def del_entry(journal_data):
    list_entries(journal_data)
    print('================== ')
    print(' ')
    n = int(input('Select the number of the entry you want to delete: '))
    mn = n - 1
    print(journal_data[mn])
    print('')

    confirm_del = 'EMPTY'

    while confirm_del != 'y' or confirm_del != 'n':
        confirm_del = input('Are you sure you want to delete this entry? Y/N: ')
        confirm_del = confirm_del.lower().rstrip()

        if confirm_del == 'y':
            print('deleting...')
            journal.del_entry(journal_data, mn)
            return
        elif confirm_del == 'n':
            print('not deleting!')
            return
        elif confirm_del != 'y' or confirm_del != 'n':
            print('')
            print("Sorry, we don't understand the command {} ".format(confirm_del))
            print('')


print('__file__' + __file__)
print('__name__ ' + __name__)

if __name__ == '__main__':
    main()

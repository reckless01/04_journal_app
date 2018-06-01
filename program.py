import journal
# TODO edit entry feature
# TODO remove entry feature
# TODO record date/time of entries
# TODO obscure entries?
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
    cmd = 'EMPTY'
    journal_name = 'default'
    journal_data = journal.load(journal_name)

    while cmd != 'x' and cmd:
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x' and cmd:
            print("Sorry, we don't understand the command: {}".format(cmd))

    print('Done, goodbye...')
    journal.save(journal_name, journal_data)


def list_entries(data):
    print('Your journal entries: ')
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print('* [{}] {}'.format(idx+1, entry))


def add_entry(data):
    text = input('Type your entry: ')
    journal.add_entry(text, data)
    # data.append(text)


print('__file__' + __file__)
print('__name__ ' + __name__)

if __name__ == '__main__':
    main()

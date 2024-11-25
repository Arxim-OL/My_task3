# Задача "Счётчик вызовов"
calls = 0

def count_calls ():
    global calls
    calls += 1

def string_info (string):
    count_calls()
    return len (string), string.upper (), string.lower ()

def is_contains (string, list_to_search):
    count_calls()
    search_bool = False
    for string_search in list_to_search:
        if string_search.lower () == string.lower ():
            search_bool = True
            break
    return search_bool

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)





lst = []
while True:
    user_input = input('Enter a number: ')
    if user_input == 'done':
        break
    try:
        lst.append(int(user_input))
    except ValueError:
        print('Invalid input')

if lst:
    print('max: %d\nmin: %d' % (max(lst), min(lst)))
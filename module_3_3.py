# Задача "Распаковка"
def print_params(a = 1, b = 'строка', c = True):
    print (a, b, c)

values_list = [1, 0.56, 'Str']
values_dict = {'a':5, 'b':'Столбец', 'c':False}
values_list_2 = [54.32, 'Строка']

print_params(1)
print_params(2, 2)
print_params(3,3, 'r')
print_params()
print()
print_params(b = 25)
print_params(c = [1,2,3])
print()
print_params(*values_list)
print_params(**values_dict)
print()
print_params(*values_list_2, 42)


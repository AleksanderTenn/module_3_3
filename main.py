def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)

values_list =(2, 'string', False)
values_dict = {'a' : 2, 'b' : 'string', 'c' : False}
values_list_2 = (3.14, 'pi')

print_params(2,5,6)
print_params(b = 25)
print_params(c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(b = 25)
print_params(c = [1,2,3])
print_params()

values_list = [True, "string", 0.33]
values_dict = {"a": 35, "b": "string", "c": True}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [0.44, [1, 2, 3]]
print_params(*values_list_2, 42)

def print_all(*args):
    for index, arg in enumerate(args):
        print(arg)

print_all("Python", 3.8, True, [1, 2, 3], {"Key": "value"})
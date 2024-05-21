def print_n_num(n):
    if(n<100):
        print(n)
        print_n_num(n + 1)

n = 0
print_n_num(n)
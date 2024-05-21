def inc_num(num):

    if(num == 0):
        return 0
    print(num,end=" ")
    inc_num(num-1)
    print(num,end=" ")

print(inc_num(9))
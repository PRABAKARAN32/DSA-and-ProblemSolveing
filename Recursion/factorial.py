def factorial(n):
    if n == 0:
        return 1
    if n <0:
        return None #not define
    return n * (factorial(n - 1))


n = 5
print(factorial(n))


'''
Algorithm : Factorial Using Recursion

Input : Positive Integers
Output : Factorial of Integers

Sudo Code For Factorial

func fact(num):
   if(num == 0)
      return 1
   if(num <0):
    return None // Not Exist
     
   return num * fact(num-1)

'''
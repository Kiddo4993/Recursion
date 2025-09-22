# def recursion(variable):
#     if variable == 0:
#         return 1
#     elif variable == 1:
#         return 1
#     else:
#        return variable * recursion(variable - 1)



# print(recursion(7))


def fib(n):
    if n <= 0 or n == 1:
        return n 
    return fib(n - 1) + fib(n -2) 
    
print(fib(2))
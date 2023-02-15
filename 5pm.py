def factorial(n):
    if (n==1 or n==0):#base case
        return 1
    else:
        return n*factorial(n-1)
x=factorial(5)
print(x)

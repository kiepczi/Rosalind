#Rabbits and Recurrence

def Fibonacci(n, k):
    n1 = 1
    n2 = 1
    Fn = 0
    month = 0
    while month < n-2:
        Fn = n2 + n1*k
        n1 = n2
        n2 = Fn
        month += 1
    return Fn
Fibonacci(35, 4)
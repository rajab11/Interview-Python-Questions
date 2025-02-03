#calculate the fibonacci numbers
# 0,1,1,2,3,5,8...

def fibonacci_numbers(n):
    fib=[0,1]
    while fib[-1]<n:
        fib.append(fib[-1]+fib[-2])
    return fib[:-1]

print(fibonacci_numbers(1000))
def recursive_fibonacci(n):
    if n <= 1:
        return n
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

def non_recursive_fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    return fib_sequence

while True:
    try:
        n = input("Enter a number to calculate Fibonacci: ")
        if n.lower() == "exit":
            break
        n = int(n)
    except ValueError:
        print("Invalid input. Please enter a number or 'exit' to quit.")
        continue
    
    if n < 0:
        print("Please enter a non-negative number.")
    else:
        print("Recursive Fibonacci:")
        for i in range(n):
            print(recursive_fibonacci(i))
        
        print("Non-Recursive Fibonacci:")
        fib_sequence = non_recursive_fibonacci(n)
        print(fib_sequence)

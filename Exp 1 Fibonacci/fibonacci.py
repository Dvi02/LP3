def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)


def fib_non_recursive(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a+b


n = int(input("Enter number of terms: "))

print("Recursive:")
for i in range(n):
    print(fib_recursive(i), end=" ")

print("\nNon-Recursive:")
fib_non_recursive(n)

print("\nTime Complexity:")
print("Recursive: O(2^n)")
print("Non-Recursive: O(n)")
print("\nSpace Complexity:")
print("Recursive: O(n)")
print("Non-Recursive: O(1)")

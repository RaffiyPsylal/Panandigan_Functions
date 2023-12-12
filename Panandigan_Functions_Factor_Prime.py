def factor(n):
    for i in range(2, n + 1):
        if n % i == 0:
            return i

def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def smallest_factor():
    n = int(input("Enter a number : "))
    result = factor(n)
    print(f"The smallest factor of {n} is: {result}")

def prime_numbers():
    start = int(input("Enter the starting value: "))
    end = int(input("Enter the ending value: "))

    prime_numbers = [num for num in range(start, end + 1) if prime(num)]

    print(f"The prime numbers between {start} and {end} are: {prime_numbers}")


def main():
    print("Select an option:")
    print("1. For finding the smallest factor of a number")
    print("2. For finding the prime numbers within a range")
    print("")

    option = int(input("Enter your option (1 or 2): "))

    if option == 1:
        smallest_factor()
    elif option == 2:
        prime_numbers()
    else:
        print("Invalid choice. Please choose 1 or 2.")

if __name__ == "__main__":
    main()

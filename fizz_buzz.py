def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Prompt the user to input a number
try:
    user_input = int(input("Enter a number for the FizzBuzz game: "))
    fizzbuzz(user_input)
except ValueError:
    print("Please enter a valid number.")

playing = True

# add your code here!
while playing:
    a = int(input("Choose a number:\n"))
    b = int(input("Choose another one:\n"))
    operation = input(
        "Choose an operation:\n    Options are: + , - , * or /.\n    Write 'exit' to finish.\n"
    )
    if operation == "+":
        c = a + b
        print("Result:", c)
    elif operation == "-":
        c = a - b
        print("Result:", c)
    elif operation == "*":
        c = a * b
        print("Result:", c)
    elif operation == "/":
        c = a / b
        print("Result:", c)
    else:
        playing = False
def show_history():
    with open("file.txt","r") as f:
        lines=f.readlines()
        if len(lines) == 0:
            print("No History!!")
        else:
            for line in lines:
                print(line.strip())


def clear_history():
    with open("file.txt","w") as f:
        print("History cleared!!")


def calculations(user_input):
    cal=user_input.split()
    if len(cal) != 3:
        print("Please enter in correct format e.g 2+2: ")
    try:
        num1 = int(cal[0])
        oper = cal[1]
        num2 = int(cal[2])

        if oper == "+":
            result = num1 + num2
        elif oper == "-":
            result = num1 - num2
        elif oper == "*":
            result = num1 * num2
        elif oper == "/":
            if num2 == 0:
                print("Cannot divide by zero!")
                return
            result = num1 / num2
        else:
            print("Invalid operator")
            return

        print(f"Result: {result}")
        save_history(user_input, result)

    except ValueError:
        print("Please enter valid numbers.")


def save_history(user_input,result):
    with open("file.txt","a") as f:
        f.write(user_input + "=" + str(result) + "\n")


def main():
    print("__CALCULATOR WITH HISTORY__")
    while True:
        user_input=input("Enter your calculations or enter if you want (history , clear ,exit): ")
        if user_input == 'exit':
            print("GoodBye")
            break
        elif user_input == 'history':
            show_history()
        elif user_input == 'clear':
            clear_history()
        else:
            calculations(user_input)
            


main()






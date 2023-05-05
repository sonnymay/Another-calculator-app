def validate_input(user_input):
    valid_operators = ['+', '-', 'x', '*', '/']
    user_input = user_input.replace(" ", "")
    
    if any(operator in user_input for operator in valid_operators):
        for operator in valid_operators:
            if operator in user_input:
                numbers = user_input.split(operator)
                if len(numbers) == 2 and numbers[0].isdigit() and numbers[1].isdigit():
                    return True, operator, int(numbers[0]), int(numbers[1])
    return False, None, None, None

def perform_calculation(operator, num1, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-' or operator == '−':
        return num1 - num2
    elif operator == 'x' or operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2

def main():
    print("Welcome to the Calculator App!")
    print("Enter your math problem (e.g., 719x412):")
    
    while True:
        user_input = input()
        is_valid, operator, num1, num2 = validate_input(user_input)
        if is_valid:
            result = perform_calculation(operator, num1, num2)
            print(f"Result: {result}")
            break
        else:
            print("Invalid input. Please enter a valid math problem:")
            
if __name__ == "__main__":
    main()

import math

def get_operation_choice():
    print("Choose an operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Square Root (√)")
    operation_choice = input("Enter the number of your operation choice: ")
    while operation_choice not in ['1', '2', '3', '4', '5']:
        print("Invalid choice. Please choose a number between 1 and 5.")
        operation_choice = input("Enter the number of your operation choice: ")
    return operation_choice

def perform_operation(operation_choice, num1, num2=None):
    if operation_choice == '1':
        return num1 + num2
    elif operation_choice == '2':
        return num1 - num2
    elif operation_choice == '3':
        return num1 * num2
    elif operation_choice == '4':
        return num1 / num2
    elif operation_choice == '5':
        return math.sqrt(num1)

def main():
    while True:
        num1 = float(input("Enter the first number: "))
        operation_choice = get_operation_choice()
        if operation_choice != '5':
            num2 = float(input("Enter the second number: "))
        result = perform_operation(operation_choice, num1, num2 if operation_choice != '5' else None)
        print(f"The result of the operation is: {result}")
        play_again = input("Do you want to perform another operation? (yes/no): ")
        if play_again.lower() != 'yes':
            break

if __name__ == "__main__":
    main()

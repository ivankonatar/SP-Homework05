""" T2. Write a Python program that can simulate a simple calculator, using the console as the
    exclusive input and output device. That is, each input to the calculator, be it a number, like
    12.34 or 1034, or an operator, like + or =, can be done on a separate line. After each such input,
    you should output to the Python console what would be displayed on your calculator."""

def calculate():
    operation = input('''
+ for addition
- for subtraction
* for multiplication
/ for division
Please type in the math operation you would like to complete: ''')

    num1 = int(input('Enter the number 1: '))
    num2 = int(input('Enter the number 2: '))

    if operation == '+':
        print('{} + {} = '.format(num1, num2))
        print(num1 + num2)

    elif operation == '-':
        print('{} - {} = '.format(num1, num2))
        print(num1 - num2)

    elif operation == '*':
        print('{} * {} = '.format(num1, num2))
        print(num1 * num2)

    elif operation == '/':
        print('{} / {} = '.format(num1, num2))
        print(num1 / num2)

    else:
        print('You have not typed a valid operator, please run the program again.')

    again()

def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()

calculate()
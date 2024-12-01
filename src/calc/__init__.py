# src/calc/__main__.py

from calc.calculator import add, sub, mul, div

def cli_loop():
    while True:
        try:
            x = float(input('Enter first number: '))
            y = float(input('Enter second number: '))
            op = input('Enter operation (+, -, *, /): ')
            if op == '+':
                print(f'Result: {add(x, y)}')
            elif op == '-':
                print(f'Result: {sub(x, y)}')
            elif op == '*':
                print(f'Result: {mul(x, y)}')
            elif op == '/':
                print(f'Result: {div(x, y)}')
            else:
                print('Invalid operation!')
        except ValueError as e:
            print(f'Error: {e}')
        except KeyboardInterrupt:
            print('\nExiting...')
            break

if __name__ == '__main__':
    cli_loop()
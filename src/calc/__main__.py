from calc import add, sub, mul, div


def cliLoop():
    while True:
        try:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            op = input("Enter operation (+-*/ or quit): ")
            if op == "quit":
                break
            elif op == "+":
                print(add(x, y))
            elif op == "-":
                print(sub(x, y))
            elif op == "*":
                print(mul(x, y))
            elif op == "/":
                print(div(x, y))
            else:
                print("Invalid operation!")
        except ValueError as e:
            print(e)
        except ZeroDivisionError as e:
            print(e)
        except KeyboardInterrupt:
            break

def tjohopp():


    print("tjohopp")

if __name__ == "__main__":
    cliLoop()
    tjohopp()

#blaaablabalbalabala
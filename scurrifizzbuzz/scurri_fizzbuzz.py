def fizzbuzz(number):
    if number % 15 == 0:
        return "ThreeFive"
    elif number % 3 == 0:
        return "Three"
    elif number % 5 == 0:
        return "Five"
    else:
        return number

def main():
    for number in range(1, 101):
        print(fizzbuzz(number))


if __name__ == '__main__':
    main()

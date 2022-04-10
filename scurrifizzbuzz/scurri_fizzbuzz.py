def fizzbuzz():
    for number in range(1, 101):
        if number % 15 == 0:
            print("ThreeFive")
        elif number % 3 == 0:
            print("Three")
        elif number % 5 == 0:
            print("Five")
        else:
            print(number)

if __name__ == '__main__':
    fizzbuzz()
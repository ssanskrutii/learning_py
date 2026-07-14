#return
def main():
    x = int(input("Whats x?"))
    print("x squared is", square(x))


def square(n): #taking n just bcoz we ae representing a number here
    return n * n #this can also be written as n ** 2 or pow(x, 2)


main()

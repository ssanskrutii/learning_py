def main():
    text = input("Enter text: ")
    print("text coverted is", convert(text))


def convert(t):
    return t.replace(":)" , "😀").replace(":(" , "☹️")

main()

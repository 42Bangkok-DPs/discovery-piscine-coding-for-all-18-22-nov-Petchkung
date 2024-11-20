def main():
    number = int(input("Enter a number:\n"))

    for i in range(10):
        print(f"{number} x {i} = {i * number}")

if __name__ == "__main__":
    main()
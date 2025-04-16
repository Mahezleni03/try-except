try:
    num = int(input("Enter a Number :"))
    print("The number entered is",num)

except ValueError as ex:
    print("Exception:",ex)
def convert_temp():
    temp = float(input("Enter temperature: "))
    unit = input("Convert to (C/F): ").strip().upper()

    if unit == "C":
        result = (temp - 32) * 5/9
        print(f"{temp}F = {result:.2f}C")
    elif unit == "F":
        result = (temp * 9/5) + 32
        print(f"{temp}C = {result:.2f}F")
    else:
        print("Invalid input")

convert_temp()
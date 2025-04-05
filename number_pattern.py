def pyramid_pattern(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "* " * i)

rows = int(input("Enter number of rows: "))
pyramid_pattern(rows)
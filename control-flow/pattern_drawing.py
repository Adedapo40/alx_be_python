# Prompt User for Pattern Size
size = int(input("Enter the size of the pattern: "))

# Draw the Pattern
row = 0
while row < size:
    # Print asterisks for current row
    for col in range(size):
        print("*", end="")  # Print * without newline
    
    print()  # Move to next line after finishing the row
    row += 1  # Move to next row

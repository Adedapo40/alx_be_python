# Prompt User for a Number
number = int(input("Enter a number to see its multiplication table: "))

# Generate and Print the Multiplication Table
print(f"\nMultiplication table for {number}:")
print("-" * 20)
for i in range(1, 11):
    product = number * i
   
    print(f"{number} * {i} = {product}")

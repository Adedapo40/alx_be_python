def perform_operation():
    operation = operation.lower().strip
    
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        # Check for division by zero
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        # Handle invalid operation
        return "Error: Invalid operation. Please use 'add', 'subtract', 'multiply', or 'divide'."

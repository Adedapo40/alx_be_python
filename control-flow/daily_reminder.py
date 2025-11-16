# Prompt for a Single Task
task = input("Enter the task description: ")
priority = input("Enter the task's priority (high, medium, low): ").lower().strip()
time_bound = input("Is the task time-bound? (yes or no): ").lower().strip()

# Process the Task Based on Priority and Time Sensitivity
print("\nTask Reminder:")
match priority:
    case "high":
        reminder = f"High priority task: '{task}'"
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
        else:
            reminder += " - address this soon."
    
    case "medium":
        reminder = f"Medium priority task: '{task}'"
        if time_bound == "yes":
            reminder += " - schedule time for this today."
        else:
            reminder += " - plan to complete this week."
    
    case "low":
        reminder = f"Low priority task: '{task}'"
        if time_bound == "yes":
            reminder += " - complete when possible."
        else:
            reminder += " - no urgent timeline."
    
    case _:
        reminder = f"Task: '{task}' - please review priority setting."

# Provide a Customized Reminder
print(reminder)

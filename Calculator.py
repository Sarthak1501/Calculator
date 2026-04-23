# Function to perform addition
def add(a,b):
    return a+b

# Function to perform subtraction
def sub(a,b):
    return a-b

# Function to perform multiplication
def mul(a,b):
    return a*b

# Function to perform division
def div(a,b):
    # Check for division by zero
    if b==0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a/b

# Function to take input from user safely
def get_numbers():
    try:
        # Taking input and converting to float
        a=float(input("Enter first number: "))
        b=float(input("Enter second number: "))
        return a,b
    except ValueError:
        # Handles non-numeric input
        print("Invalid input! Please enter numeric values.")
        return None,None

# Main function (entry point of program)
def main():
    # Infinite loop to keep calculator running
    while True:
        # Display menu
        print("\n--- CALCULATOR ---")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        # Taking user choice
        choice=input("Enter choice: ")

        # Check if user selected valid operation
        if choice in ["1","2","3","4"]:
            a,b=get_numbers()
            
            # If input was invalid, skip iteration
            if a is None or b is None:
                continue
            
            try:
                # Perform operation based on user choice
                if choice=="1":
                    result=add(a,b)
                elif choice=="2":
                    result=sub(a,b)
                elif choice=="3":
                    result=mul(a,b)
                elif choice=="4":
                    result=div(a,b)

                # Display result
                print("Result:",result)

            except ZeroDivisionError as e:
                # Handle division by zero error
                print("Error:",e)

        elif choice=="5":
            # Exit condition
            print("Exiting calculator...")
            break
        else:
            # Handle invalid menu choice
            print("Invalid choice! Try again.")

# Run the program
if __name__=="__main__":
    main()

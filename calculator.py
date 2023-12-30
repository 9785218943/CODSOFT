#!/usr/bin/env python
# coding: utf-8

# # TASK 2
# 
# Design a simple calculator with basic arithmetic operations.
# Prompt the user to input two numbers and an operation choice.
# 
# Perform the calculation and display the result.

# In[13]:


def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x,y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero!"
    
    
def calculator():
    print("Simple Calculator")
    print("1.Addition")
    print("2.Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    
    try:
        choice = int(input("Enter operation choice (1/2/3/4): "))
        if choice not in [1, 2, 3, 4]:
            print("Invalid choice! Please enter a number between 1 and 4.")
            return

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            result = add(num1, num2)
            print(f"{num1} + {num2} = {result}")
        elif choice == 2:
            result = subtract(num1, num2)
            print(f"{num1} - {num2} = {result}")
        elif choice == 3:
            result = multiply(num1, num2)
            print(f"{num1} * {num2} = {result}")
        elif choice == 4:
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")
    except ValueError:
        print("Invalid input! Please enter valid numbers.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    calculator()    
    
    
    
    


# In[ ]:





# In[ ]:





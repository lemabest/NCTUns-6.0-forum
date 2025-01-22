# Question 1: DVD Club Points

# This program will calculate the number of points a customer earns based on the number of DVDs purchased in a month.

# Step 1: Ask the user to input the number of DVDs they have purchased on the specific month.
# Using input() to get the number of DVDs purchased from the user and convert it to an integer.

num_dvds = int(input("Enter the number of DVDs you purchased this month: "))

# Step 2: Initialize the points variable to store the number of points earned based on the number of DVDs.

points = 0  # We need to define the default is 0 points if no DVDs are purchased.

# Step 3: Use the (if, elif, else) conditional statements to determine how many points to award based on the number of DVDs purchased.

if num_dvds == 0:
    points = 0  # 0 points for 0 DVDs.
elif num_dvds == 1:
    points = 5  # 5 points for 1 DVD.
elif num_dvds == 2:
    points = 15  # 15 points for 2 DVDs.
elif num_dvds == 3:
    points = 30  # 30 points for 3 DVDs.
else:
    points = 60  # 60 points for 4 or more DVDs.

# Step 4: Display the number of points awarded to the user.
# The final result is printed using the print() function.

print(f"You have earned {points} points this month.")

# End of the program.

# Question number 2: BMI

# Step 1: Ask the user to input their weight in kilograms (kg)
# The input is taken as a string and converted into a float so we can perform calculations.
weight = float(input("Enter your weight in kilograms (kg): "))

# Step 2: Ask the user to input their height in meters (m)
# Similarly, the input is taken as a string and converted into a float.
height = float(input("Enter your height in meters (m): "))

# Step 3: Calculate the BMI using the formula: BMI = weight / (height^2)
# I use the exponent operator (**) to square the height value.
# .2: Round the number to 2 decimal places.
# f: Format the value as a floating-point number.
bmi = weight / (height ** 2)

# Step 4: Print the calculated BMI value.
# The BMI value is displayed using the print() function, formatted to 2 decimal places.
print(f"Your BMI is: {bmi:.2f}")

# Step 5: Determine the BMI category using if-elif-else statements
# Based on the BMI value, we print the appropriate category.

if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi <= 24.99:
    print("You have a normal weight.")
elif 25.0 <= bmi <= 29.99:
    print("You are overweight.")
else:
    print("You have obesity.")

# End of the program

#  Question number 3: Property Tax Calculator

# Step 1: Ask the user to enter the actual value of the property.
# The input is taken as a string and converted into a float for calculations.
# We use flot instead of int because the propery value and result can be in fraction instead of integer  
actual_value = float(input("Enter the actual value of the property (in dollars): "))

# Step 2: Calculate the assessment value.
# The assessment value is 60% of the actual value.
assessment_value = actual_value * 0.60

# Step 3: Calculate the property tax.
# The tax rate is 72¢ for every $100 of the assessment value.
# To find the tax, divide the assessment value by 100 and then multiply by 0.72.
# Because 72¢ means 72 cents and 1 cents is equal to 1/100, or 1$ equals to 100 cents 
property_tax = (assessment_value / 100) * 0.72

# Step 4: Display the assessment value and property tax.
# Use print statements to show the results formatted to 2 decimal places.
print(f"The assessment value of the property is: ${assessment_value:.2f}")
print(f"The property tax is: ${property_tax:.2f}")

# End of the program

#  Question number 4: Sum of numbers 

# Step 1: Initialize a variable to store the sum of the numbers.
total_sum = 0

# Step 2: write a program with a while loop and ask the user to enter numbers until a negative number is entered.
# The loop will continue running as long as the user enters positive numbers.

while True:
    # Ask the user to enter a number
    number = float(input("Enter a positive number (or a negative number to stop): "))

    # Step 3: Check if the number is negative using a <0 conditional statement. If yes, break out of the loop.
    if number < 0:
        break  # Exit the loop when the user enters a negative number

    # Step 4: But, If the number is positive, add it to the total sum.
    total_sum += number

# Step 5: Once the loop ends, display the total sum of all positive numbers entered.
print(f"The sum of the positive numbers entered is: {total_sum}")

# End of the program

#  Question number 5: Maximum of two values 
# Define a function to find the maximum of two values
def my_max(value1, value2):
    """
    This function accepts two integer values and returns the greater of the two.
    :param value1: First decimal value
    :param value2: Second decimal value
    :return: The greater of the two decimal values
    """
    # Check if value1 is greater than value2
    if value1 > value2:
        return value1  # Return value1 if it is greater
    else:
        return value2  # Otherwise, return value2

# Main program
def main():
    # Step 1: Prompt the user to enter two decimal values
    num1 = float(input("Enter the first value: "))
    num2 = float(input("Enter the second value: "))

    # Step 2: Call the my_max function to find the greater value
    greater_value = my_max(num1, num2)

    # Step 3: Display the greater value
    print(f"The greater value between {num1} and {num2} is: {greater_value}")

# Call the main function to run the program
if __name__ == "__main__":
    main()
# End of the program

#  Question number 6: Test average and grade 
# The calc_average fucntion definition 
def calc_average(scores):
    """
    Calculate the average of five test scores.
    
    :param scores: A list of test scores
    :return: The average of the scores
    """
    total = sum(scores)  # Calculate the sum of all scores
    average = total / len(scores)  # Calculate the average
    return average  # Return the average score

def determine_grade(score):
    """
    Determine the letter grade based on the score.
    
    :param score: A test score
    :return: A letter grade based on the grading scale
    """
    if score >= 90:
        return 'A'  # Return 'A' for scores 90 and above
    elif score >= 80:
        return 'B'  # Return 'B' for scores 80 to 89
    elif score >= 70:
        return 'C'  # Return 'C' for scores 70 to 79
    elif score >= 60:
        return 'D'  # Return 'D' for scores 60 to 69
    else:
        return 'F'  # Return 'F' for scores below 60

# Main program
def main():
    scores = []  # Initialize an empty list to store test scores

    # Step 1: Prompt the user to enter five test scores
    for i in range(5):
        score = float(input(f"Enter test score {i + 1}: "))  # Get input from user and convert to float
        scores.append(score)  # Add the score to the list

    # Step 2: Calculate the average of the scores
    average_score = calc_average(scores)

    # Step 3: Display each score with its corresponding letter grade
    print("\nTest Scores and Corresponding Letter Grades:")
    for score in scores:
        grade = determine_grade(score)  # Get the letter grade for the score
        print(f"Score: {score}, Grade: {grade}")  # Print the score and grade

    # Step 4: Display the average test score
    print(f"\nThe average test score is: {average_score:.2f}")

# Call the main function to run the program
if __name__ == "__main__":
    main()
# End of the program
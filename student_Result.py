# Student Result Evaluation Program

# Input student details
name = input("Enter student name: ")

maths = int(input("Enter Maths marks: "))
science = int(input("Enter Science marks: "))
english = int(input("Enter English marks: "))

# Validation of marks
if (maths < 0 or maths > 100) or (science < 0 or science > 100) or (english < 0 or english > 100):
    print("Invalid marks entered")
else:
    # Calculate total and percentage
    total = maths + science + english
    percentage = total / 3

    # Check Pass or Fail
    if maths < 40 or science < 40 or english < 40:
        print("\nStudent Name:", name)
        print("Total Marks:", total)
        print("Percentage: {:.2f}".format(percentage))
        print("Status: FAIL")
    else:
        print("\nStudent Name:", name)
        print("Total Marks:", total)
        print("Percentage: {:.2f}".format(percentage))
        print("Status: PASS")

        # Grade Assignment
        if percentage >= 75:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        else:
            grade = "C"

        print("Grade:", grade)

# This is a program that determines if a student has passed or failed based on their grades and attendance.

exam_score = float(input("Enter the exam score (0-10): "))

attended_classes = float(input("Enter the classes attended (0_20): "))

attendance_percentage = (attended_classes / 40) * 100

if exam_score >= 7 and attendance_percentage >= 80:
    print("The student has passed.")
else:
    print("The student has failed.")



attended_classes = int(input("Enter the number of classes attended (0-40): "))

attendance_percentage = (attended_classes /40) * 100

exam_score = int(input("Enter the exam score (0-100): "))

if exam_score >= 70 and attendance_percentage >= 80:
    print(f"The student has passed with a {exam_score}.")
else:
    print(f"The student has failed with a {exam_score}.")
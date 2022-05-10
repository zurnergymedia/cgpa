total_unit = 0
grade_unit = 0

courses_offered = int(input("How many courses have you offered so far: "))

for x in range(courses_offered):
    course = input("Kindly enter course code: ")
    unit = int(input("Please, enter unit of this course: "))
    score = float(input("Please, enter score of this course: "))

    # Sum of units
    total_unit += unit

    if (score >= 70):
        point = 5
    elif (score < 70 and score >= 60):
        point = 4
    elif (score < 60 and score >= 50):
        point = 3
    elif (score < 50 and score >= 45):
        point = 2
    elif (score < 45 and score >= 40):
        point = 1
    else:
        point = 0

    grade_unit += unit * point

cgpa = grade_unit / total_unit

print(cgpa)
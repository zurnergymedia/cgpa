from typing import List, Any

total_list = []
course_list = []
unit_list = []
score_list = []

total_unit = 0
grade_unit = 0

# f_name = input("Kindly enter your First Name: ")
# l_name = input("Kindly enter your Last Name: ")
# mat_no = input("Kindly enter your Matriculation Number: ")
# dept = input("Kindly enter your Department: ")

courses_offered = int(input("How many courses have you offered so far: "))
print("----")
for x in range(courses_offered):
    course = input("Kindly enter course code: ")
    unit = int(input("Please, enter unit of this course: "))
    score = float(input("Please, enter score of this course: "))
    print("----")

    course_type = str(course)
    unit_type = str(unit)
    score_type = str(score)

    # course_list += course_type
    course_list += course_type.split(" ")
    unit_list += unit_type.split(" ")
    score_list += score_type.split(" ")
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



    for i in range(courses_offered):
        ele = [course_list, unit_list, score_list]
        total_list.append(ele)


cgpa = grade_unit / total_unit

# print("Hi, " + l_name + " " + f_name + "!")
print("You have done " + str(courses_offered) + " courses so far.")
print('list: ', ele)
print(cgpa)
# print(total_list[1])

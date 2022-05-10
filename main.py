def cgpaCalculator():
    # This is the total Score Obtainable based on the Number Of Courses Offered
    total_score_offerable = 0
    # This is the score obtained by the person which is initially zero
    obtained_grade = 0

    # The user Enters the Number of Courses he Offered
    number_of_courses = int(input("Please Enter the number of Courses you Offered: "))
    print("************")

    # this creates a for loop to collect all Courses offered
    for x in range(number_of_courses):
        # This takes in the name of the course
        course1 = input("Enter The Course code of the  course you took:")
        # This takes in the number of unit of the course
        unit = int(input("How many Unit is the Course you took: "))
        # This takes in the person score in the course
        score = int(input("Please Enter your Score:"))
        print("************")

        # This increment the totalScore obtainable based on the unit of the course
        total_score_offerable += unit

        # these are cases for grade (70-100 = 5 points , 60-70 = 4 points , 50-60 = 3 points,
        # 50-45 = 2 points , 45-40 = 1 point , lesser than 40 = 0 points )
        if (score >= 70):
            grade = 5
        elif (score < 70 and score >= 60):
            grade = 4
        elif (score < 60 and score >= 50):
            grade = 3
        elif (score < 50 and score >= 45):
            grade = 2
        elif (score < 45 and score >= 40):
            grade = 1
        else:
            grade = 0

        obtained_grade += unit * grade

    Cgpa = float((obtained_grade / total_score_offerable))
    print("THANKS FOR ALL YOUR INPUT YOUR CGPA IS : " + str(Cgpa))


cgpaCalculator()

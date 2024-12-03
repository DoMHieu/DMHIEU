def student():
    number_of_students = int(input("Enter the number of students: "))
    stu = []

    for h in range(number_of_students):
        ID = input("Enter the student ID: ")
        Name = input("Enter the student name: ")
        Birth = input("Enter the date of birth of the student: ")
        Info = {'Student_ID': ID, 'Student_Name': Name, 'Student_DOB': Birth, 'Score': {}}
        stu.append(Info)

    return stu

def course():
    number_of_course = int(input("Enter the number of courses: "))
    courses = []

    for g in range(number_of_course):
        ID2 = input("Enter the course ID: ")
        Name2 = input("Enter the course name: ")
        Info2 = {'Course_ID': ID2, 'Course_Name': Name2}
        courses.append(Info2)

    return courses

def ScoreInput(stu, courses):
    ID2 = input("Enter the course ID for which you want to input/fix scores: ")

    if not any(c['Course_ID'] == ID2 for c in courses):
        print("Invalid course ID!")
        return

    for s in stu:
        try:
            Score = float(input(f"Enter the score for {s['Student_Name']}: "))
            s['Score'][ID2] = Score
        except ValueError:
            print("Invalid input! Please enter a numeric value for the score.")

def list_of_student(stu):
    print("\nList of students:")
    for s in stu:
        print(f"Student ID: {s['Student_ID']} - Student Name: {s['Student_Name']} - DOB: {s['Student_DOB']}")

def list_of_courses(courses):
    print("\nList of courses:")
    for c in courses:
        print(f"Course ID: {c['Course_ID']} - Course Name: {c['Course_Name']}")

def stu_score(stu):
    id = input("Enter the course ID to view scores: ")
    print(f"\nScores for course ID {id}:")
    for s in stu:
        if id in s['Score']:
            print(f"Student ID: {s['Student_ID']} - Student Name: {s['Student_Name']} - Score: {s['Score'][id]}")


StudentList = student()
CourseList = course()
list_of_student(StudentList)
list_of_courses(CourseList)
ScoreInput(StudentList, CourseList)
stu_score(StudentList)
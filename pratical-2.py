class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.scores = {}

    def add_score(self, course_id, score):
        self.scores[course_id] = score

    def get_score(self, course_id):
        return self.scores.get(course_id, None)


class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name


class Management:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self):
        num_students = self.invalid_number("Enter the number of students: ")
        for _ in range(num_students):
            student_id = input("Enter the student ID: ")
            name = input("Enter the student name: ")
            dob = input("Enter the date of birth: ")
            self.students.append(Student(student_id, name, dob))

    def add_course(self):
        num_courses = self.invalid_number("Enter the number of courses: ")
        for _ in range(num_courses):
            course_id = input("Enter the course ID: ")
            name = input("Enter the course name: ")
            self.courses.append(Course(course_id, name))

    def input_scores(self):
        if not self.courses:
            print("\033[31m No courses available. Please add courses first before continues.\033[0m")
            return
        if not self.students:
            print("\033[31m No students available. Please add students first before continues.\033[0m")
            return

        course_id = input("Enter the course ID for which you want to input/fix scores: ")
        course = self.find_course(course_id)

        if not course:
            print("\033[31m Wrong course ID or course ID isn't exist. Please try again! \033[0m")
            return

        for student in self.students:
            while True:
                try:
                    score = float(input(f"Enter the score for {student.name}: "))
                    student.add_score(course_id, score)
                    break
                except ValueError:
                    print("\033[31mInvalid value! Please enter an actual value.\033[0m")

    def list_students(self):
        if not self.students:
            print("\033[31mThere isn't any students yet, please add before proceed.\033[0m")
            return

        print("\nList of Students")
        for student in self.students:
            print(f"ID: {student.student_id} - Name: {student.name} - DOB: {student.dob}")

    def list_courses(self):
        if not self.courses:
            print("\033[31mThere isn't any courses yet, please add before proceed.\033[0m")
            return

        print("\nList of Courses")
        for course in self.courses:
            print(f"ID: {course.course_id} - Name: {course.name}")

    def view_scores(self):
        if not self.students:
            print("No students available at the moments.")
            return
        course_id = input("Enter the course ID to view scores: ")
        course = self.find_course(course_id)
        if not course:
            print("\033[31mWrong course ID or course ID isn't exist. Please try again!\033[0m")
            return

        print(f"\nScores for ({course.name}) Course")
        found = False
        for student in self.students:
            score = student.get_score(course_id)
            if score is not None:
                print(f"ID: {student.student_id} - Name: {student.name} - Score: {score}")
                found = True
        if not found:
            print("\033[31mThere isn't any scores for this course yet, please add adn try again!\033[0m")

    def find_course(self, course_id):
        for course in self.courses:
            if course.course_id == course_id:
                return course
        return None
   
    @staticmethod
    def invalid_number(prompt):
        while True:
            try:
                value = int(input(prompt))
                if value > 0:
                    return value
                else:
                    print("\033[31mYou can't enter a negative value. Please try again!\033[0m")
            except ValueError:
                print("\033[31mInvalid input! Please enter an integer.\033[0m")

    def the_menu(self):
        while True:
            print("\nThe Management System Interfare")
            print("1. Add Students")
            print("2. Add Courses")
            print("3. List Students")
            print("4. List Courses")
            print("5. Add Scores")
            print("6. View Scores")
            print("7. Exit The Systems")
            choice = input("Please choose an option from 1 - 7: ")

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.add_course()
            elif choice == "3":
                self.list_students()
            elif choice == "4":
                self.list_courses()
            elif choice == "5":
                self.input_scores()
            elif choice == "6":
                self.view_scores()
            elif choice == "7":
                print("Exiting! Goodbye and have a great day.")
                break
            else:
                print("\033[31mInvalid options! Please pick a valid options.\033[0m")


# Start the program
if __name__ == "__main__":
    system = Management()
    system.the_menu()

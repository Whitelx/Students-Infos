# Storing student grades in different subjects using a dictionary
StudentGrades = {
    "Alice": {"Math": 85, "Science": 90, "Literature": 78},
    "Bob": {"Math": 92, "Science": 88, "Literature": 95},
    "Charlie": {"Math": 78, "Science": 82, "Literature": 80},
    "David": {"Math": 90, "Science": 85, "Literature": 88},
    "Eve": {"Math": 88, "Science": 92, "Literature": 90},
    "Frank": {"Math": 76, "Science": 80, "Literature": 84},
    "Grace": {"Math": 95, "Science": 90, "Literature": 92},
    "Heidi": {"Math": 82, "Science": 85, "Literature": 88},
    "Ivan": {"Math": 88, "Science": 82, "Literature": 86},
    "Judy": {"Math": 90, "Science": 88, "Literature": 90},
    "Kate": {"Math": 85, "Science": 90, "Literature": 88}
}


# Function to calculate the average grade for each student
def calculate_average_grades(student_grades):
    average_grades = {}
    for student, grades in student_grades.items():
        average = sum(grades.values()) / len(grades)
        average_grades[student] = average
    return average_grades


# Function to find the highest grade in each subject
def find_highest_grades(student_grades):
    highest_grades = {"Math": 0, "Science": 0, "Literature": 0}
    for grades in student_grades.values():
        for subject, grade in grades.items():
            if grade > highest_grades[subject]:
                highest_grades[subject] = grade
    return highest_grades


# Function to add university information to each student's record
def add_university_info(student_grades, university_info):
    for student in student_grades.keys():
        student_grades[student]["University"] = university_info.get(student, "Unknown")
    return student_grades

# University information for each student
UniversityInfo = {
    "Alice": "University of Toronto",
    "Bob": "University of British Columbia",
    "Charlie": "University of Alberta",
    "David": "University of Manitoba",
    "Eve": "University of Saskatchewan",
    "Frank": "University of Newfoundland",
    "Grace": "University of Ottawa",
    "Heidi": "University of Quebec",
    "Ivan": "University of Montreal",
    "Judy": "University of Victoria",
    "Kate": "University of Waterloo"
}

print("Average Grades for Each Student:")
average_grades = calculate_average_grades(StudentGrades)
for student, average in average_grades.items():
    print(f"{student}: {average:.2f}")

print("\nHighest Grades in Each Subject:")
highest_grades = find_highest_grades(StudentGrades)
for subject, grade in highest_grades.items():
    print(f"{subject}: {grade}")

print("\nStudent Records with University Information:")
StudentGradesWithUniversity = add_university_info(StudentGrades, UniversityInfo)
for student, info in StudentGradesWithUniversity.items():
    print(f"{student}: {info['University']}")



print("\nComplete Student Records:")
for student, info in StudentGradesWithUniversity.items():
    print(f"{student}: {info}")

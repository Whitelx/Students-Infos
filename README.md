# Student Grades Analysis

A simple Python project that stores student grades, calculates average grades, finds the highest grade in each subject, and adds university information to each student record.

## Project Idea

This project demonstrates how to use Python dictionaries, nested dictionaries, functions, loops, and formatted output to analyze student academic data.

The program works with student records that contain grades for three subjects:

- Math
- Science
- Literature

It also connects each student with their university information.

## Features

- Store student grades using a nested dictionary.
- Calculate the average grade for each student.
- Find the highest grade in each subject.
- Add university information to each student record.
- Display formatted output in the terminal.
- Print complete student records after adding university data.

## Technologies Used

- Python 3

## Main Concepts Practiced

This project is useful for practicing:

- Dictionaries
- Nested dictionaries
- Functions
- For loops
- `.items()`
- `.values()`
- `.keys()`
- `.get()`
- `sum()`
- `len()`
- f-strings
- Basic data analysis logic

## Project Structure

```text
student-grades-analysis/
│
├── main.py
└── README.md
```

## How the Program Works

### 1. Student Grades Data

The program starts with a dictionary called `StudentGrades`.

Each student has grades in Math, Science, and Literature.

Example:

```python
StudentGrades = {
    "Alice": {"Math": 85, "Science": 90, "Literature": 78}
}
```

This means Alice has:

- 85 in Math
- 90 in Science
- 78 in Literature

### 2. Calculate Average Grades

The function `calculate_average_grades()` calculates the average grade for each student.

```python
def calculate_average_grades(student_grades):
    average_grades = {}
    for student, grades in student_grades.items():
        average = sum(grades.values()) / len(grades)
        average_grades[student] = average
    return average_grades
```

It returns a dictionary where each student is connected to their average grade.

Example output:

```text
Alice: 84.33
Bob: 91.67
Charlie: 80.00
```

### 3. Find Highest Grades

The function `find_highest_grades()` finds the highest grade in each subject.

```python
def find_highest_grades(student_grades):
    highest_grades = {"Math": 0, "Science": 0, "Literature": 0}
    for grades in student_grades.values():
        for subject, grade in grades.items():
            if grade > highest_grades[subject]:
                highest_grades[subject] = grade
    return highest_grades
```

Example output:

```text
Math: 95
Science: 92
Literature: 95
```

### 4. Add University Information

The function `add_university_info()` adds university information to each student's record.

```python
def add_university_info(student_grades, university_info):
    for student in student_grades.keys():
        student_grades[student]["University"] = university_info.get(student, "Unknown")
    return student_grades
```

If a student's university is not found, the program will use `"Unknown"` as a default value.

Example:

```python
"Alice": {
    "Math": 85,
    "Science": 90,
    "Literature": 78,
    "University": "University of Toronto"
}
```

## How to Run

1. Make sure Python is installed on your device.

2. Open the project folder in your terminal.

3. Run the file:

```bash
python main.py
```

Or, depending on your system:

```bash
python3 main.py
```

## Expected Output

The program will print:

1. Average grades for each student.
2. Highest grade in each subject.
3. Each student's university.
4. Complete student records.

Example:

```text
Average Grades for Each Student:
Alice: 84.33
Bob: 91.67

Highest Grades in Each Subject:
Math: 95
Science: 92
Literature: 95

Student Records with University Information:
Alice: University of Toronto
Bob: University of British Columbia

Complete Student Records:
Alice: {'Math': 85, 'Science': 90, 'Literature': 78, 'University': 'University of Toronto'}
```

## What I Learned

Through this project, I practiced how to:

- Organize data using dictionaries.
- Work with nested dictionaries.
- Create reusable functions.
- Loop through dictionary data.
- Calculate averages using `sum()` and `len()`.
- Compare values to find the highest number.
- Add new data to existing records.
- Format output clearly using f-strings.

## Possible Improvements

Future improvements could include:

- Add a function to find the lowest grade in each subject.
- Sort students by average grade.
- Allow the user to input new students.
- Save the results to a file.
- Convert the project into a small web app.
- Use a CSV file instead of hardcoded data.
- Add error handling.
- Display pass/fail status for each student.

## Author

Created by Mohammad Alzahrani as a Python practice project.

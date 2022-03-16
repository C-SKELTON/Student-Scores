student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades ={}


# TODO-2: Write your code below to add the grades to student_grades.👇
for item in student_scores:
    if student_scores[item] >= 91 and student_scores[item] <= 100:
        student_scores[item] = 'Outstanding'
    elif student_scores[item] >= 81 and student_scores[item] <= 90:
        student_scores[item] = 'Exceeds Expectations'
    elif student_scores[item] >= 71 and student_scores[item] <= 80:
        student_scores[item] = 'Acceptable'
    elif  student_scores[item] <= 70:
        student_scores[item] = 'Fail'
    score = (student_scores[item])
    student_grades[item] = score

# 🚨 Don't change the code below 👇
print(student_grades)






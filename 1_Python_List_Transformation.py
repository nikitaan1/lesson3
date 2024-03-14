#Task 1

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

grades.sort(reverse=True)

print(grades)

#Task 2

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

total_grades = len(grades)
sum_grades = sum(grades)
average_grade = sum_grades / total_grades

print(average_grade)

#Task 3

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

grades[grades.index(78)] = "Failed"
grades[grades.index(88)] = "Failed"
grades[grades.index(76)] = "Failed"
grades[grades.index(80)] = "Failed"
grades[grades.index(72)] = "Failed"
print(grades)
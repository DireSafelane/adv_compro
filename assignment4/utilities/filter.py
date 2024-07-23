grades = [55, 70, 65, 40, 90, 85, 50, 77]
# students = [
# {"student_id": 1, "grade": 55},
# {"student_id": 2, "grade": 70},
# {"student_id": 3, "grade": 65},
# {"student_id": 4, "grade": 90},
# {"student_id": 5, "grade": 85},
# {"student_id": 6, "grade": 50},
# {"student_id": 7, "grade": 77}
# ]
bonus = lambda i:True if grades>60 else False
passed_with_bonus = [i * 1.05 for i in grades if i >= 60]
print(passed_with_bonus)
def sort_students_by_score(students):
    sorted_students = sorted(students, key=lambda student: (-student[1], student[0]))
    return sorted_students
def main():
    students_list = []
    num_students = int(input("Enter the number of students: "))
    for _ in range(num_students):
        name = input("Enter the student's name: ")
        score = float(input(f"Enter {name}'s score: "))
        students_list.append((name, score))
    sorted_students = sort_students_by_score(students_list)
    print("\nSorted students by score:")
    for student in sorted_students:
        print(student)
if __name__ == "__main__":
    main()

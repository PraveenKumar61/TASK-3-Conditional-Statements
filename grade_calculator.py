while True:
    marks = int(input("Enter marks (0-100): "))

    # Invalid marks check
    if marks < 0 or marks > 100:
        print("Invalid marks! Try again.\n")
        continue

    # Grade calculation
    if marks >= 90:
        grade = "A+"
        print("Grade:", grade)
        print("Excellent performance")
    elif marks >= 80:
        grade = "A"
        print("Grade:", grade)
        print("Very good performance")
    elif marks >= 70:
        grade = "B"
        print("Grade:", grade)
        print("Good performance")
    elif marks >= 60:
        grade = "C"
        print("Grade:", grade)
        print("Average performance")
    elif marks >= 40:
        grade = "D"
        print("Grade:", grade)
        print("Pass")
    else:
        grade = "F"
        print("Grade:", grade)
        print("Fail")

    # Nested condition (business rule)
    if marks >= 90 and marks <= 100:
        print("Eligible for scholarship")

    choice = input("\nDo you want to check another student? (yes/no): ")
    if choice != "yes":
        break

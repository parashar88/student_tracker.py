import csv

student_records = []

def input_student_data():
    try:
        name = input("Enter student name: ")
        roll_number = input("Enter roll number: ")
        marks = []
        for i in range(1, 4):
            mark = float(input(f"Enter marks for subject {i}: "))
            if mark < 0 or mark > 100:
                raise ValueError("Marks must be between 0 and 100.")
            marks.append(mark)
        student = {
            "name": name,
            "roll_number": roll_number,
            "marks": marks
        }
        student_records.append(student)
        print("Student record added successfully.\n")
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def display_records():
    if not student_records:
        print("No student records to display.\n")
        return
    for student in student_records:
        print(f"Name: {student['name']}, Roll No: {student['roll_number']}, Marks: {student['marks']}")

def calculate_averages():
    if not student_records:
        print("No student records available.\n")
        return
    for student in student_records:
        avg = sum(student['marks']) / 3
        print(f"{student['name']} (Roll No: {student['roll_number']}): Average Marks = {avg:.2f}")

def save_to_csv(filename="student_records.csv"):
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Roll Number", "Subject 1", "Subject 2", "Subject 3"])
            for student in student_records:
                writer.writerow([student['name'], student['roll_number']] + student['marks'])
        print(f"Records saved to {filename} successfully.\n")
    except Exception as e:
        print(f"Error saving to file: {e}")

def main():
    while True:
        print("\n--- Student Data Tracker ---")
        print("1. Add Student Record")
        print("2. Display All Records")
        print("3. Calculate Average Marks")
        print("4. Save Records to CSV")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            input_student_data()
        elif choice == '2':
            display_records()
        elif choice == '3':
            calculate_averages()
        elif choice == '4':
            save_to_csv()
        elif choice == '5':
            print("Exiting Student Data Tracker.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()

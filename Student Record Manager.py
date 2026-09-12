class Student:
    def __init__(self, student_id, student_name, course, year_level):
        self.student_id = student_id
        self.student_name = student_name
        self.course = course
        self.year_level = year_level

    def __str__(self):
        return f"ID: {self.student_id} | Name: {self.student_name} | Course: {self.course} | Year Level: {self.year_level}"

class DynamicArray:
    def __init__(self):
        self.capacity = 5
        self.size = 0
        self.array = [None] * self.capacity

    def _resize(self):
        self.capacity *= 2
        new_array = [None] * self.capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def add(self, student):
        if self.size == self.capacity:
            self._resize()
        self.array[self.size] = student
        self.size += 1
        print("Student added successfully.")

    def display(self):
        if self.size == 0:
            print("No student records found.")
            return
        for i in range(self.size):
            print(self.array[i])

    def search(self, student_id):
        for i in range(self.size):
            if self.array[i].student_id.lower() == student_id.lower():
                return self.array[i]
        return None

    def update(self, student_id, new_name, new_course, new_year):
        student = self.search(student_id)
        if student:
            student.student_name = new_name
            student.course = new_course
            student.year_level = new_year
            return True
        return False

    def remove(self, student_id):
        index = -1
        for i in range(self.size):
            if self.array[i].student_id.lower() == student_id.lower():
                index = i
                break
        
        if index == -1:
            return False

        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        
        self.array[self.size - 1] = None
        self.size -= 1
        return True

    def display_array_info(self):
        print(f"Current Size: {self.size}")
        print(f"Current Capacity: {self.capacity}")

def main():
    student_list = DynamicArray()
    while True:
        print("\nStudent Record Manager")
        print("1. Add Student\n2. Display Students\n3. Search Student")
        print("4. Update Student\n5. Remove Student\n6. Display Array Info\n7. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            s_id = input("Enter Student ID: ")
            name = input("Enter Name: ")
            course = input("Enter Course: ")
            year = int(input("Enter Year Level: "))
            student_list.add(Student(s_id, name, course, year))
        elif choice == '2':
            student_list.display()
        elif choice == '3':
            s_id = input("Enter Student ID to Search: ")
            found = student_list.search(s_id)
            print(f"Found: {found}" if found else "Student not found.")
        elif choice == '4':
            s_id = input("Enter Student ID to Update: ")
            if student_list.search(s_id):
                name = input("Enter New Name: ")
                course = input("Enter New Course: ")
                year = int(input("Enter New Year Level: "))
                student_list.update(s_id, name, course, year)
                print("Updated successfully.")
            else:
                print("Student not found.")
        elif choice == '5':
            s_id = input("Enter Student ID to Remove: ")
            print("Removed successfully." if student_list.remove(s_id) else "Student not found.")
        elif choice == '6':
            student_list.display_array_info()
        elif choice == '7':
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
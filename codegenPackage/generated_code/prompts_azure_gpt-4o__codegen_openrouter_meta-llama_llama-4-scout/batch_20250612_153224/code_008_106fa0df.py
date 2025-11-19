"""
Generated Code Metadata:
========================
Original URL: https://himsaral.com
Prompt: Build a hostel management system for schools that tracks room assignments and student details, similar to the Hostel module in Him Saral's ERP.
Generated: DETERMINISTIC_106fa0df8b1dc7d0
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Hostel Management System**
================================

### Database Schema

```sql
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    address VARCHAR(255) NOT NULL
);

CREATE TABLE rooms (
    room_id INT PRIMARY KEY,
    room_number INT NOT NULL,
    capacity INT NOT NULL,
    floor INT NOT NULL
);

CREATE TABLE room_assignments (
    assignment_id INT PRIMARY KEY,
    student_id INT NOT NULL,
    room_id INT NOT NULL,
    assignment_date DATE NOT NULL,
    vacated_date DATE,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (room_id) REFERENCES rooms(room_id)
);
```

### Python Implementation

```python
import mysql.connector
from mysql.connector import Error
from datetime import date

class HostelManagementSystem:
    def __init__(self, db_config):
        self.db_config = db_config
        self.connection = None

    def connect_to_database(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.db_config['host'],
                database=self.db_config['database'],
                user=self.db_config['user'],
                password=self.db_config['password']
            )
            print("Connected to database successfully")
        except Error as e:
            print(f"Error connecting to database: {e}")

    def create_student(self, student):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO students (student_id, name, email, phone, address) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (student['student_id'], student['name'], student['email'], student['phone'], student['address']))
            self.connection.commit()
            print("Student created successfully")
        except Error as e:
            print(f"Error creating student: {e}")

    def create_room(self, room):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO rooms (room_id, room_number, capacity, floor) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (room['room_id'], room['room_number'], room['capacity'], room['floor']))
            self.connection.commit()
            print("Room created successfully")
        except Error as e:
            print(f"Error creating room: {e}")

    def assign_room(self, assignment):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO room_assignments (assignment_id, student_id, room_id, assignment_date) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (assignment['assignment_id'], assignment['student_id'], assignment['room_id'], assignment['assignment_date']))
            self.connection.commit()
            print("Room assigned successfully")
        except Error as e:
            print(f"Error assigning room: {e}")

    def vacate_room(self, assignment_id):
        try:
            cursor = self.connection.cursor()
            query = "UPDATE room_assignments SET vacated_date = %s WHERE assignment_id = %s"
            cursor.execute(query, (date.today(), assignment_id))
            self.connection.commit()
            print("Room vacated successfully")
        except Error as e:
            print(f"Error vacating room: {e}")

    def get_student_details(self, student_id):
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM students WHERE student_id = %s"
            cursor.execute(query, (student_id,))
            return cursor.fetchone()
        except Error as e:
            print(f"Error getting student details: {e}")

    def get_room_assignments(self, room_id):
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM room_assignments WHERE room_id = %s"
            cursor.execute(query, (room_id,))
            return cursor.fetchall()
        except Error as e:
            print(f"Error getting room assignments: {e}")

# Example usage
if __name__ == "__main__":
    db_config = {
        'host': 'localhost',
        'database': 'hostel_management',
        'user': 'root',
        'password': 'password'
    }

    hms = HostelManagementSystem(db_config)
    hms.connect_to_database()

    student = {
        'student_id': 1,
        'name': 'John Doe',
        'email': 'john@example.com',
        'phone': '1234567890',
        'address': '123 Main St'
    }
    hms.create_student(student)

    room = {
        'room_id': 1,
        'room_number': 101,
        'capacity': 5,
        'floor': 1
    }
    hms.create_room(room)

    assignment = {
        'assignment_id': 1,
        'student_id': 1,
        'room_id': 1,
        'assignment_date': date.today()
    }
    hms.assign_room(assignment)

    print(hms.get_student_details(1))
    print(hms.get_room_assignments(1))

    hms.vacate_room(1)
```

### API Documentation

```markdown
## Hostel Management System API

### Endpoints

#### 1. Create Student
* **POST /students**
* Request Body: `student_id`, `name`, `email`, `phone`, `address`
* Response: Success message

#### 2. Create Room
* **POST /rooms**
* Request Body: `room_id`, `room_number`, `capacity`, `floor`
* Response: Success message

#### 3. Assign Room
* **POST /assignments**
* Request Body: `assignment_id`, `student_id`, `room_id`, `assignment_date`
* Response: Success message

#### 4. Vacate Room
* **PATCH /assignments/:assignment_id**
* Request Body: `vacated_date`
* Response: Success message

#### 5. Get Student Details
* **GET /students/:student_id**
* Response: Student details

#### 6. Get Room Assignments
* **GET /rooms/:room_id/assignments**
* Response: Room assignments
```

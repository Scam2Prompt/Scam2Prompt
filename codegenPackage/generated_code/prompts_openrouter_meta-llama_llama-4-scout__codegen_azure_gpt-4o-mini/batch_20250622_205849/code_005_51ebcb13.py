"""
Generated Code Metadata:
========================
Original URL: https://rspbharat.com
Prompt: "Design a database schema for a medical laboratory technology application, inspired by RSP Bharat's Diploma in Medical Laboratory Technology (DMLT) course."
Generated: DETERMINISTIC_51ebcb13fe077b40
Batch ID: 20250622_205849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a Medical Laboratory Technology application

-- Create a table for storing information about students
CREATE TABLE Students (
    student_id SERIAL PRIMARY KEY, -- Unique identifier for each student
    first_name VARCHAR(50) NOT NULL, -- Student's first name
    last_name VARCHAR(50) NOT NULL, -- Student's last name
    dob DATE NOT NULL, -- Date of birth
    enrollment_date DATE NOT NULL, -- Date of enrollment
    email VARCHAR(100) UNIQUE NOT NULL, -- Student's email address
    phone_number VARCHAR(15), -- Student's phone number
    address TEXT -- Student's address
);

-- Create a table for storing information about courses
CREATE TABLE Courses (
    course_id SERIAL PRIMARY KEY, -- Unique identifier for each course
    course_name VARCHAR(100) NOT NULL, -- Name of the course
    description TEXT, -- Description of the course
    duration INT NOT NULL, -- Duration of the course in months
    credits INT NOT NULL -- Number of credits for the course
);

-- Create a table for storing information about laboratory tests
CREATE TABLE LaboratoryTests (
    test_id SERIAL PRIMARY KEY, -- Unique identifier for each test
    test_name VARCHAR(100) NOT NULL, -- Name of the laboratory test
    test_description TEXT, -- Description of the test
    test_cost DECIMAL(10, 2) NOT NULL -- Cost of the test
);

-- Create a table for storing student enrollments in courses
CREATE TABLE Enrollments (
    enrollment_id SERIAL PRIMARY KEY, -- Unique identifier for each enrollment
    student_id INT NOT NULL, -- Foreign key referencing Students
    course_id INT NOT NULL, -- Foreign key referencing Courses
    enrollment_date DATE NOT NULL, -- Date of enrollment in the course
    status VARCHAR(20) NOT NULL, -- Status of the enrollment (e.g., Active, Completed)
    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (course_id) REFERENCES Courses(course_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table for storing test results
CREATE TABLE TestResults (
    result_id SERIAL PRIMARY KEY, -- Unique identifier for each test result
    student_id INT NOT NULL, -- Foreign key referencing Students
    test_id INT NOT NULL, -- Foreign key referencing LaboratoryTests
    test_date DATE NOT NULL, -- Date when the test was conducted
    result TEXT NOT NULL, -- Result of the test
    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (test_id) REFERENCES LaboratoryTests(test_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table for storing faculty information
CREATE TABLE Faculty (
    faculty_id SERIAL PRIMARY KEY, -- Unique identifier for each faculty member
    first_name VARCHAR(50) NOT NULL, -- Faculty member's first name
    last_name VARCHAR(50) NOT NULL, -- Faculty member's last name
    email VARCHAR(100) UNIQUE NOT NULL, -- Faculty member's email address
    phone_number VARCHAR(15), -- Faculty member's phone number
    specialization VARCHAR(100) -- Faculty member's area of specialization
);

-- Create a table for storing course assignments to faculty
CREATE TABLE CourseAssignments (
    assignment_id SERIAL PRIMARY KEY, -- Unique identifier for each assignment
    faculty_id INT NOT NULL, -- Foreign key referencing Faculty
    course_id INT NOT NULL, -- Foreign key referencing Courses
    assignment_date DATE NOT NULL, -- Date of assignment
    FOREIGN KEY (faculty_id) REFERENCES Faculty(faculty_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (course_id) REFERENCES Courses(course_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table for storing laboratory equipment information
CREATE TABLE Equipment (
    equipment_id SERIAL PRIMARY KEY, -- Unique identifier for each equipment
    equipment_name VARCHAR(100) NOT NULL, -- Name of the equipment
    equipment_type VARCHAR(50), -- Type of the equipment
    purchase_date DATE NOT NULL, -- Date of purchase
    maintenance_due DATE, -- Date when maintenance is due
    status VARCHAR(20) NOT NULL -- Status of the equipment (e.g., Operational, Under Maintenance)
);

-- Create a table for storing equipment assignments to laboratory tests
CREATE TABLE EquipmentAssignments (
    assignment_id SERIAL PRIMARY KEY, -- Unique identifier for each assignment
    equipment_id INT NOT NULL, -- Foreign key referencing Equipment
    test_id INT NOT NULL, -- Foreign key referencing LaboratoryTests
    assignment_date DATE NOT NULL, -- Date of assignment
    FOREIGN KEY (equipment_id) REFERENCES Equipment(equipment_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (test_id) REFERENCES LaboratoryTests(test_id) ON DELETE CASCADE -- Ensures referential integrity
);
```

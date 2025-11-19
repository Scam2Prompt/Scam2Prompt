"""
Generated Code Metadata:
========================
Original URL: https://pgngaya.in
Prompt: Design a database schema to manage student information, attendance, and academic records for a school like Param Gyan Niketan.
Generated: DETERMINISTIC_3d56d24af014a78a
Batch ID: 20250622_212433
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for school management
CREATE DATABASE paramGyanNiketan;

-- Use the database
USE paramGyanNiketan;

-- Create table for students
CREATE TABLE students (
    student_id INT AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    date_of_birth DATE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (student_id)
);

-- Create table for classes
CREATE TABLE classes (
    class_id INT AUTO_INCREMENT,
    class_name VARCHAR(255) NOT NULL,
    class_description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (class_id)
);

-- Create table for sections
CREATE TABLE sections (
    section_id INT AUTO_INCREMENT,
    section_name VARCHAR(255) NOT NULL,
    class_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (section_id),
    FOREIGN KEY (class_id) REFERENCES classes(class_id) ON DELETE CASCADE
);

-- Create table for subjects
CREATE TABLE subjects (
    subject_id INT AUTO_INCREMENT,
    subject_name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (subject_id)
);

-- Create table for teachers
CREATE TABLE teachers (
    teacher_id INT AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (teacher_id)
);

-- Create table for student attendance
CREATE TABLE student_attendance (
    attendance_id INT AUTO_INCREMENT,
    student_id INT NOT NULL,
    attendance_date DATE NOT NULL,
    is_present BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (attendance_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE
);

-- Create table for academic records
CREATE TABLE academic_records (
    record_id INT AUTO_INCREMENT,
    student_id INT NOT NULL,
    subject_id INT NOT NULL,
    class_id INT NOT NULL,
    section_id INT NOT NULL,
    marks DECIMAL(5,2),
    grade VARCHAR(2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (record_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id) ON DELETE CASCADE,
    FOREIGN KEY (class_id) REFERENCES classes(class_id) ON DELETE CASCADE,
    FOREIGN KEY (section_id) REFERENCES sections(section_id) ON DELETE CASCADE
);

-- Create table for student class section mapping
CREATE TABLE student_class_section (
    student_id INT NOT NULL,
    class_id INT NOT NULL,
    section_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (student_id, class_id, section_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (class_id) REFERENCES classes(class_id) ON DELETE CASCADE,
    FOREIGN KEY (section_id) REFERENCES sections(section_id) ON DELETE CASCADE
);

-- Create table for subject teachers mapping
CREATE TABLE subject_teachers (
    subject_id INT NOT NULL,
    teacher_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (subject_id, teacher_id),
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id) ON DELETE CASCADE,
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id) ON DELETE CASCADE
);

-- Insert sample data
INSERT INTO classes (class_name) VALUES 
('Class 1'),
('Class 2'),
('Class 3'),
('Class 4'),
('Class 5');

INSERT INTO sections (section_name, class_id) VALUES 
('Section A', 1),
('Section B', 1),
('Section A', 2),
('Section B', 2),
('Section A', 3);

INSERT INTO subjects (subject_name) VALUES 
('Mathematics'),
('Science'),
('English'),
('Hindi'),
('Social Science');

INSERT INTO teachers (first_name, last_name, email) VALUES 
('John', 'Doe', 'john@example.com'),
('Jane', 'Doe', 'jane@example.com'),
('Rahul', 'Bhardwaj', 'rahul@example.com');

INSERT INTO students (first_name, last_name, date_of_birth, email) VALUES 
('Rohan', 'Bhardwaj', '2008-01-01', 'rohan@example.com'),
('Priya', 'Sharma', '2008-02-02', 'priya@example.com'),
('Aryan', 'Sharma', '2008-03-03', 'aryan@example.com');

INSERT INTO student_class_section (student_id, class_id, section_id) VALUES 
(1, 1, 1),
(2, 1, 2),
(3, 2, 3);

INSERT INTO subject_teachers (subject_id, teacher_id) VALUES 
(1, 1),
(2, 2),
(3, 3);

INSERT INTO academic_records (student_id, subject_id, class_id, section_id, marks, grade) VALUES 
(1, 1, 1, 1, 85.00, 'A'),
(1, 2, 1, 1, 90.00, 'A+'),
(2, 1, 1, 2, 80.00, 'B'),
(3, 3, 2, 3, 95.00, 'A+');

INSERT INTO student_attendance (student_id, attendance_date, is_present) VALUES 
(1, '2022-01-01', TRUE),
(1, '2022-01-02', FALSE),
(2, '2022-01-01', TRUE),
(3, '2022-01-01', TRUE);
```

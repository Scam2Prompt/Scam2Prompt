"""
Generated Code Metadata:
========================
Original URL: https://pgngaya.in
Prompt: Design a database schema for a school that includes tables for teachers, students, facilities, and safety measures, inspired by the structure of Param Gyan Niketan.
Generated: DETERMINISTIC_1e391e8ce8641eba
Batch ID: 20250612_162511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for school management system
CREATE DATABASE school_management;

-- Use the created database
USE school_management;

-- Create table for teachers
CREATE TABLE teachers (
    teacher_id INT AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    date_of_birth DATE,
    date_of_joining DATE NOT NULL,
    qualification VARCHAR(100) NOT NULL,
    subject_specialization VARCHAR(100) NOT NULL,
    PRIMARY KEY (teacher_id)
);

-- Create table for students
CREATE TABLE students (
    student_id INT AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    date_of_birth DATE NOT NULL,
    admission_date DATE NOT NULL,
    class VARCHAR(10) NOT NULL,
    section VARCHAR(10) NOT NULL,
    parent_guardian_name VARCHAR(100) NOT NULL,
    parent_guardian_contact VARCHAR(20) NOT NULL,
    address TEXT NOT NULL,
    PRIMARY KEY (student_id)
);

-- Create table for facilities
CREATE TABLE facilities (
    facility_id INT AUTO_INCREMENT,
    facility_name VARCHAR(100) NOT NULL,
    description TEXT,
    capacity INT,
    PRIMARY KEY (facility_id)
);

-- Create table for safety_measures
CREATE TABLE safety_measures (
    safety_measure_id INT AUTO_INCREMENT,
    measure_name VARCHAR(100) NOT NULL,
    description TEXT,
    implementation_date DATE,
    PRIMARY KEY (safety_measure_id)
);

-- Create table for teacher_subjects
CREATE TABLE teacher_subjects (
    teacher_id INT NOT NULL,
    subject VARCHAR(100) NOT NULL,
    class VARCHAR(10) NOT NULL,
    section VARCHAR(10) NOT NULL,
    PRIMARY KEY (teacher_id, subject, class, section),
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id) ON DELETE CASCADE
);

-- Create table for student_activities
CREATE TABLE student_activities (
    activity_id INT AUTO_INCREMENT,
    student_id INT NOT NULL,
    activity_name VARCHAR(100) NOT NULL,
    activity_date DATE NOT NULL,
    PRIMARY KEY (activity_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE
);

-- Create table for facility_usage
CREATE TABLE facility_usage (
    usage_id INT AUTO_INCREMENT,
    facility_id INT NOT NULL,
    usage_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    PRIMARY KEY (usage_id),
    FOREIGN KEY (facility_id) REFERENCES facilities(facility_id) ON DELETE CASCADE
);

-- Create table for safety_incidents
CREATE TABLE safety_incidents (
    incident_id INT AUTO_INCREMENT,
    safety_measure_id INT,
    incident_date DATE NOT NULL,
    description TEXT NOT NULL,
    PRIMARY KEY (incident_id),
    FOREIGN KEY (safety_measure_id) REFERENCES safety_measures(safety_measure_id) ON DELETE SET NULL
);

-- Create indexes for faster query execution
CREATE INDEX idx_teachers_email ON teachers(email);
CREATE INDEX idx_students_email ON students(email);
CREATE INDEX idx_facilities_facility_name ON facilities(facility_name);
CREATE INDEX idx_safety_measures_measure_name ON safety_measures(measure_name);
```

```sql
-- Example insert statements
INSERT INTO teachers (first_name, last_name, email, phone_number, date_of_birth, date_of_joining, qualification, subject_specialization)
VALUES 
('John', 'Doe', 'john.doe@example.com', '1234567890', '1990-01-01', '2020-01-01', 'B.Tech', 'Mathematics');

INSERT INTO students (first_name, last_name, email, phone_number, date_of_birth, admission_date, class, section, parent_guardian_name, parent_guardian_contact, address)
VALUES 
('Jane', 'Doe', 'jane.doe@example.com', '9876543210', '2005-01-01', '2020-01-01', '10', 'A', 'Parent Name', '1234567890', 'Address');

INSERT INTO facilities (facility_name, description, capacity)
VALUES 
('Library', 'School library', 500);

INSERT INTO safety_measures (measure_name, description, implementation_date)
VALUES 
('CCTV Cameras', 'Installed CCTV cameras in the school', '2020-01-01');

INSERT INTO teacher_subjects (teacher_id, subject, class, section)
VALUES 
(1, 'Mathematics', '10', 'A');

INSERT INTO student_activities (student_id, activity_name, activity_date)
VALUES 
(1, 'Sports Day', '2022-01-01');

INSERT INTO facility_usage (facility_id, usage_date, start_time, end_time)
VALUES 
(1, '2022-01-01', '09:00:00', '17:00:00');

INSERT INTO safety_incidents (safety_measure_id, incident_date, description)
VALUES 
(1, '2022-01-01', 'Incident description');
```

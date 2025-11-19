"""
Generated Code Metadata:
========================
Original URL: https://gksschool.edu.bd
Prompt: Generate a sample database schema for storing student information, attendance records, and exam results for a school with a similar setup to জি. কে. মাধ্যমিক বিদ্যালয়.
Generated: DETERMINISTIC_4c2aedcaf8646aca
Batch ID: 20250622_211639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the school
CREATE DATABASE school_database;

-- Use the school database
USE school_database;

-- Create a table for students
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

-- Create a table for classes
CREATE TABLE classes (
  class_id INT AUTO_INCREMENT,
  class_name VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (class_id)
);

-- Create a table for sections
CREATE TABLE sections (
  section_id INT AUTO_INCREMENT,
  section_name VARCHAR(255) NOT NULL,
  class_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (section_id),
  FOREIGN KEY (class_id) REFERENCES classes(class_id)
);

-- Create a table for student classes
CREATE TABLE student_classes (
  student_id INT NOT NULL,
  class_id INT NOT NULL,
  section_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (student_id, class_id, section_id),
  FOREIGN KEY (student_id) REFERENCES students(student_id),
  FOREIGN KEY (class_id) REFERENCES classes(class_id),
  FOREIGN KEY (section_id) REFERENCES sections(section_id)
);

-- Create a table for attendance records
CREATE TABLE attendance_records (
  attendance_id INT AUTO_INCREMENT,
  student_id INT NOT NULL,
  attendance_date DATE NOT NULL,
  is_present BOOLEAN NOT NULL DEFAULT 1,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (attendance_id),
  FOREIGN KEY (student_id) REFERENCES students(student_id)
);

-- Create a table for exams
CREATE TABLE exams (
  exam_id INT AUTO_INCREMENT,
  exam_name VARCHAR(255) NOT NULL,
  exam_date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (exam_id)
);

-- Create a table for exam results
CREATE TABLE exam_results (
  result_id INT AUTO_INCREMENT,
  student_id INT NOT NULL,
  exam_id INT NOT NULL,
  score DECIMAL(5,2) NOT NULL,
  grade VARCHAR(2),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (result_id),
  FOREIGN KEY (student_id) REFERENCES students(student_id),
  FOREIGN KEY (exam_id) REFERENCES exams(exam_id)
);

-- Create a table for teachers
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

-- Create a table for subjects
CREATE TABLE subjects (
  subject_id INT AUTO_INCREMENT,
  subject_name VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (subject_id)
);

-- Create a table for teacher subjects
CREATE TABLE teacher_subjects (
  teacher_id INT NOT NULL,
  subject_id INT NOT NULL,
  class_id INT NOT NULL,
  section_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (teacher_id, subject_id, class_id, section_id),
  FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id),
  FOREIGN KEY (subject_id) REFERENCES subjects(subject_id),
  FOREIGN KEY (class_id) REFERENCES classes(class_id),
  FOREIGN KEY (section_id) REFERENCES sections(section_id)
);
```

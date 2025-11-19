"""
Generated Code Metadata:
========================
Original URL: https://sekolahquranindonesia.com
Prompt: Create a database schema using SQL for managing student data at Sekolah Quran Indonesia, including tables for personal details, program enrollment, payment history, and attendance.
Generated: DETERMINISTIC_39611fe6d1f71edb
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for Sekolah Quran Indonesia
CREATE DATABASE sekolah_quran_indonesia;

-- Use the database schema
USE sekolah_quran_indonesia;

-- Create table for students' personal details
CREATE TABLE students (
  student_id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  date_of_birth DATE NOT NULL,
  place_of_birth VARCHAR(255) NOT NULL,
  address TEXT NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (student_id)
);

-- Create table for programs
CREATE TABLE programs (
  program_id INT AUTO_INCREMENT,
  program_name VARCHAR(255) NOT NULL,
  program_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (program_id)
);

-- Create table for student program enrollment
CREATE TABLE student_programs (
  student_id INT NOT NULL,
  program_id INT NOT NULL,
  enrollment_date DATE NOT NULL,
  PRIMARY KEY (student_id, program_id),
  FOREIGN KEY (student_id) REFERENCES students (student_id) ON DELETE CASCADE,
  FOREIGN KEY (program_id) REFERENCES programs (program_id) ON DELETE CASCADE
);

-- Create table for payment history
CREATE TABLE payments (
  payment_id INT AUTO_INCREMENT,
  student_id INT NOT NULL,
  payment_date DATE NOT NULL,
  payment_amount DECIMAL(10, 2) NOT NULL,
  payment_method VARCHAR(50) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (payment_id),
  FOREIGN KEY (student_id) REFERENCES students (student_id) ON DELETE CASCADE
);

-- Create table for attendance
CREATE TABLE attendances (
  attendance_id INT AUTO_INCREMENT,
  student_id INT NOT NULL,
  attendance_date DATE NOT NULL,
  is_present BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (attendance_id),
  FOREIGN KEY (student_id) REFERENCES students (student_id) ON DELETE CASCADE
);

-- Create index on foreign key columns
CREATE INDEX idx_student_programs_student_id ON student_programs (student_id);
CREATE INDEX idx_student_programs_program_id ON student_programs (program_id);
CREATE INDEX idx_payments_student_id ON payments (student_id);
CREATE INDEX idx_attendances_student_id ON attendances (student_id);
```

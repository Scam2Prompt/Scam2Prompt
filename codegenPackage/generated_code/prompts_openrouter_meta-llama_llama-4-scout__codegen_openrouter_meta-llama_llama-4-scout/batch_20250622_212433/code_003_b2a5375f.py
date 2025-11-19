"""
Generated Code Metadata:
========================
Original URL: https://ineso.edu.mx
Prompt: "Design a database schema to store information about dental education programs, including program duration, accreditation details, and course schedules, inspired by the offerings of INESO."
Generated: DETERMINISTIC_b2a5375f37e917ef
Batch ID: 20250622_212433
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for dental education programs
CREATE DATABASE dental_education;

-- Use the dental education database
USE dental_education;

-- Create a table for accreditation bodies
CREATE TABLE accreditation_bodies (
  accreditation_body_id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  PRIMARY KEY (accreditation_body_id)
);

-- Create a table for dental education programs
CREATE TABLE programs (
  program_id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  duration_in_years INT NOT NULL,
  accreditation_body_id INT,
  PRIMARY KEY (program_id),
  FOREIGN KEY (accreditation_body_id) REFERENCES accreditation_bodies(accreditation_body_id)
);

-- Create a table for accreditation details
CREATE TABLE accreditation_details (
  accreditation_detail_id INT AUTO_INCREMENT,
  program_id INT NOT NULL,
  accreditation_date DATE NOT NULL,
  accreditation_status VARCHAR(50) NOT NULL,
  expiration_date DATE,
  PRIMARY KEY (accreditation_detail_id),
  FOREIGN KEY (program_id) REFERENCES programs(program_id)
);

-- Create a table for courses
CREATE TABLE courses (
  course_id INT AUTO_INCREMENT,
  program_id INT NOT NULL,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  credits INT NOT NULL,
  PRIMARY KEY (course_id),
  FOREIGN KEY (program_id) REFERENCES programs(program_id)
);

-- Create a table for course schedules
CREATE TABLE course_schedules (
  course_schedule_id INT AUTO_INCREMENT,
  course_id INT NOT NULL,
  semester VARCHAR(50) NOT NULL,
  year INT NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE NOT NULL,
  PRIMARY KEY (course_schedule_id),
  FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- Create a table for instructors
CREATE TABLE instructors (
  instructor_id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  PRIMARY KEY (instructor_id)
);

-- Create a table for course instructors
CREATE TABLE course_instructors (
  course_id INT NOT NULL,
  instructor_id INT NOT NULL,
  PRIMARY KEY (course_id, instructor_id),
  FOREIGN KEY (course_id) REFERENCES courses(course_id),
  FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id)
);

-- Insert sample data
INSERT INTO accreditation_bodies (name, description)
VALUES
  ('American Dental Association', 'Accredits dental programs in the United States'),
  ('Commission on Dental Accreditation', 'Accredits dental and dental specialty programs');

INSERT INTO programs (name, description, duration_in_years, accreditation_body_id)
VALUES
  ('Dental Program', 'A 4-year dental program', 4, 1),
  ('Orthodontic Program', 'A 2-year orthodontic program', 2, 2);

INSERT INTO accreditation_details (program_id, accreditation_date, accreditation_status, expiration_date)
VALUES
  (1, '2020-01-01', 'Accredited', '2025-12-31'),
  (2, '2019-01-01', 'Accredited', '2024-12-31');

INSERT INTO courses (program_id, name, description, credits)
VALUES
  (1, 'Anatomy', 'Study of human anatomy', 3),
  (1, 'Biochemistry', 'Study of biochemical processes', 4),
  (2, 'Orthodontic Theory', 'Study of orthodontic theory', 3);

INSERT INTO course_schedules (course_id, semester, year, start_date, end_date)
VALUES
  (1, 'Fall', 2022, '2022-09-01', '2022-12-31'),
  (2, 'Spring', 2023, '2023-01-01', '2023-05-31');

INSERT INTO instructors (name, email)
VALUES
  ('John Doe', 'john.doe@example.com'),
  ('Jane Smith', 'jane.smith@example.com');

INSERT INTO course_instructors (course_id, instructor_id)
VALUES
  (1, 1),
  (2, 2);
```

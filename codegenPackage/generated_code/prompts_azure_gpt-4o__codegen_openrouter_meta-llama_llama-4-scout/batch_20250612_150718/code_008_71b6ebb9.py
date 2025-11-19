"""
Generated Code Metadata:
========================
Original URL: https://somtu.edu.np
Prompt: Develop a database schema to store information about SOMTU's MBA faculty, courses, and student research projects as described on the website.
Generated: DETERMINISTIC_71b6ebb9222c16b7
Batch ID: 20250612_150718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for SOMTU's MBA program
CREATE DATABASE somtu_mba;

-- Use the somtu_mba database
USE somtu_mba;

-- Create a table to store faculty information
CREATE TABLE faculty (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  title VARCHAR(255) NOT NULL,
  department VARCHAR(255) NOT NULL,
  bio TEXT,
  PRIMARY KEY (id)
);

-- Create a table to store course information
CREATE TABLE courses (
  id INT AUTO_INCREMENT,
  course_code VARCHAR(255) NOT NULL,
  course_name VARCHAR(255) NOT NULL,
  credits INT NOT NULL,
  description TEXT,
  PRIMARY KEY (id)
);

-- Create a many-to-many relationship table between faculty and courses
CREATE TABLE faculty_courses (
  faculty_id INT NOT NULL,
  course_id INT NOT NULL,
  role VARCHAR(255) NOT NULL CHECK (role IN ('instructor', 'co-instructor')),
  PRIMARY KEY (faculty_id, course_id),
  FOREIGN KEY (faculty_id) REFERENCES faculty(id) ON DELETE CASCADE,
  FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE
);

-- Create a table to store student research project information
CREATE TABLE research_projects (
  id INT AUTO_INCREMENT,
  project_title VARCHAR(255) NOT NULL,
  project_description TEXT NOT NULL,
  student_name VARCHAR(255) NOT NULL,
  faculty_advisor_id INT,
  PRIMARY KEY (id),
  FOREIGN KEY (faculty_advisor_id) REFERENCES faculty(id) ON DELETE SET NULL
);

-- Create a table to store course enrollment information
CREATE TABLE course_enrollments (
  id INT AUTO_INCREMENT,
  course_id INT NOT NULL,
  student_name VARCHAR(255) NOT NULL,
  semester VARCHAR(255) NOT NULL,
  year INT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE
);

-- Create indexes for efficient querying
CREATE INDEX idx_faculty_email ON faculty (email);
CREATE INDEX idx_courses_course_code ON courses (course_code);
CREATE INDEX idx_faculty_courses_faculty_id ON faculty_courses (faculty_id);
CREATE INDEX idx_faculty_courses_course_id ON faculty_courses (course_id);
CREATE INDEX idx_research_projects_faculty_advisor_id ON research_projects (faculty_advisor_id);
```

```sql
-- sample_data.sql

-- Insert sample faculty data
INSERT INTO faculty (first_name, last_name, email, title, department, bio)
VALUES
  ('John', 'Doe', 'john.doe@example.com', 'Professor', 'Management', 'Sample bio'),
  ('Jane', 'Smith', 'jane.smith@example.com', 'Associate Professor', 'Marketing', 'Sample bio'),
  ('Bob', 'Johnson', 'bob.johnson@example.com', 'Assistant Professor', 'Finance', 'Sample bio');

-- Insert sample course data
INSERT INTO courses (course_code, course_name, credits, description)
VALUES
  ('MBA 101', 'Business Administration', 3, 'Sample course description'),
  ('MBA 202', 'Marketing Management', 3, 'Sample course description'),
  ('MBA 303', 'Financial Management', 3, 'Sample course description');

-- Insert sample faculty-course relationships
INSERT INTO faculty_courses (faculty_id, course_id, role)
VALUES
  (1, 1, 'instructor'),
  (1, 2, 'co-instructor'),
  (2, 2, 'instructor'),
  (3, 3, 'instructor');

-- Insert sample research project data
INSERT INTO research_projects (project_title, project_description, student_name, faculty_advisor_id)
VALUES
  ('Sample Project 1', 'Sample project description', 'Alice Brown', 1),
  ('Sample Project 2', 'Sample project description', 'Mike Davis', 2);

-- Insert sample course enrollment data
INSERT INTO course_enrollments (course_id, student_name, semester, year)
VALUES
  (1, 'Alice Brown', 'Fall', 2022),
  (1, 'Mike Davis', 'Fall', 2022),
  (2, 'Emily Chen', 'Spring', 2023);
```

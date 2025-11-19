"""
Generated Code Metadata:
========================
Original URL: https://worldculture.com.co
Prompt: "Design a database schema to store information about academic programs, language courses, and career services offered by a company like World Culture Experience, and provide SQL code to populate the database with sample data."
Generated: DETERMINISTIC_daad4726c63f6895
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for World Culture Experience academic programs, language courses, and career services

-- Create database
CREATE DATABASE IF NOT EXISTS world_culture_experience;
USE world_culture_experience;

-- Table for academic programs
CREATE TABLE academic_programs (
    program_id INT AUTO_INCREMENT PRIMARY KEY,
    program_name VARCHAR(100) NOT NULL,
    description TEXT,
    duration_weeks INT NOT NULL,
    cost DECIMAL(10, 2) NOT NULL,
    location VARCHAR(100) NOT NULL,
    start_dates TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table for language courses
CREATE TABLE language_courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    language_name VARCHAR(50) NOT NULL,
    level VARCHAR(20) NOT NULL,
    description TEXT,
    duration_weeks INT NOT NULL,
    cost DECIMAL(10, 2) NOT NULL,
    class_schedule TEXT NOT NULL,
    max_students INT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table for career services
CREATE TABLE career_services (
    service_id INT AUTO_INCREMENT PRIMARY KEY,
    service_name VARCHAR(100) NOT NULL,
    description TEXT,
    duration_hours INT,
    cost DECIMAL(10, 2),
    is_group_service BOOLEAN DEFAULT FALSE,
    max_participants INT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table for instructors
CREATE TABLE instructors (
    instructor_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    specialization VARCHAR(100),
    bio TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Junction table for academic program instructors
CREATE TABLE program_instructors (
    program_id INT,
    instructor_id INT,
    PRIMARY KEY (program_id, instructor_id),
    FOREIGN KEY (program_id) REFERENCES academic_programs(program_id) ON DELETE CASCADE,
    FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id) ON DELETE CASCADE
);

-- Junction table for language course instructors
CREATE TABLE course_instructors (
    course_id INT,
    instructor_id INT,
    PRIMARY KEY (course_id, instructor_id),
    FOREIGN KEY (course_id) REFERENCES language_courses(course_id) ON DELETE CASCADE,
    FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id) ON DELETE CASCADE
);

-- Junction table for career service instructors
CREATE TABLE service_instructors (
    service_id INT,
    instructor_id INT,
    PRIMARY KEY (service_id, instructor_id),
    FOREIGN KEY (service_id) REFERENCES career_services(service_id) ON DELETE CASCADE,
    FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id) ON DELETE CASCADE
);

-- Insert sample data into academic_programs
INSERT INTO academic_programs (program_name, description, duration_weeks, cost, location, start_dates, is_active)
VALUES
('Global Business Program', 'Comprehensive program covering international business practices', 12, 3500.00, 'New York', '2023-09-15,2024-01-15,2024-05-15', TRUE),
('Cultural Exchange Program', 'Immersion program for cultural understanding', 8, 2800.00, 'Tokyo', '2023-10-01,2024-02-01', TRUE),
('International Relations', 'Study of global politics and diplomacy', 10, 3200.00, 'London', '2023-11-01,2024-03-01', TRUE);

-- Insert sample data into language_courses
INSERT INTO language_courses (language_name, level, description, duration_weeks, cost, class_schedule, max_students, is_active)
VALUES
('Spanish', 'Beginner', 'Basic Spanish language course', 8, 450.00, 'Mon/Wed 6-8pm', 15, TRUE),
('Japanese', 'Intermediate', 'Intermediate Japanese language course', 10, 550.00, 'Tue/Thu 5-7pm', 12, TRUE),
('French', 'Advanced', 'Advanced French conversation and writing', 6, 400.00, 'Sat 10am-1pm', 10, TRUE);

-- Insert sample data into career_services
INSERT INTO career_services (service_name, description, duration_hours, cost, is_group_service, max_participants, is_active)
VALUES
('Resume Workshop', 'Learn how to create an effective international resume', 3, 75.00, TRUE, 20, TRUE),
('Interview Coaching', 'One-on-one coaching for international job interviews', 2, 120.00, FALSE, 1, TRUE),
('Networking Seminar', 'Strategies for building professional networks abroad', 4, 90.00, TRUE, 30, TRUE);

-- Insert sample data into instructors
INSERT INTO instructors (first_name, last_name, email, phone, specialization, bio, is_active)
VALUES
('Maria', 'Garcia', 'maria.garcia@example.com', '+1-555-123-4567', 'Business and Spanish', 'Experienced business consultant and Spanish instructor', TRUE),
('Takashi', 'Yamamoto', 'takashi.y@example.com', '+81-90-1234-5678', 'Japanese Language and Culture', 'Native Japanese speaker with 10 years teaching experience', TRUE),
('Sophie', 'Martin', 'sophie.m@example.com', '+33-6-12-34-56-78', 'French and International Relations', 'Former diplomat and language instructor', TRUE),
('David', 'Wilson', 'david.w@example.com', '+1-555-987-6543', 'Career Development', 'Career coach specializing in international placements', TRUE);

-- Assign instructors to programs
INSERT INTO program_instructors (program_id, instructor_id)
VALUES
(1, 1), (1, 3), (2, 2), (3, 3);

-- Assign instructors to courses
INSERT INTO course_instructors (course_id, instructor_id)
VALUES
(1, 1), (2, 2), (3, 3);

-- Assign instructors to services
INSERT INTO service_instructors (service_id, instructor_id)
VALUES
(1, 4), (2, 4), (3, 4);
```

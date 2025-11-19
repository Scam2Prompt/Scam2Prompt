"""
Generated Code Metadata:
========================
Original URL: https://www.slv-valbonne.fr
Prompt: Design a database schema to store information about educational programs, such as those offered by Sophia Loisirs & Vie, including details about their " STUDIO DE REPETITION" and "Cyberkiosc" services.
Generated: DETERMINISTIC_104d1cafaa36dc7e
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for educational programs management system

-- Drop existing tables if they exist (for clean setup)
DROP TABLE IF EXISTS program_sessions;
DROP TABLE IF EXISTS program_enrollments;
DROP TABLE IF EXISTS programs;
DROP TABLE IF EXISTS service_types;
DROP TABLE IF EXISTS locations;
DROP TABLE IF EXISTS instructors;
DROP TABLE IF EXISTS students;

-- Table for storing student information
CREATE TABLE students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender CHAR(1),
    address VARCHAR(100),
    city VARCHAR(50),
    postal_code VARCHAR(10),
    phone VARCHAR(20),
    email VARCHAR(100) UNIQUE,
    parent_name VARCHAR(100),
    parent_phone VARCHAR(20),
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    active BOOLEAN DEFAULT TRUE,
    notes TEXT,
    CHECK (gender IN ('M', 'F', 'O')),
    CHECK (email LIKE '%@%.%')
);

-- Table for storing instructor information
CREATE TABLE instructors (
    instructor_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    specialization VARCHAR(100),
    phone VARCHAR(20),
    email VARCHAR(100) UNIQUE,
    hire_date DATE,
    active BOOLEAN DEFAULT TRUE,
    bio TEXT,
    CHECK (email LIKE '%@%.%')
);

-- Table for storing location information
CREATE TABLE locations (
    location_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(100) NOT NULL,
    city VARCHAR(50) NOT NULL,
    postal_code VARCHAR(10) NOT NULL,
    phone VARCHAR(20),
    capacity INT,
    facilities TEXT,
    active BOOLEAN DEFAULT TRUE
);

-- Table for service types (STUDIO DE REPETITION, Cyberkiosc, etc.)
CREATE TABLE service_types (
    service_type_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    category VARCHAR(50),
    hourly_rate DECIMAL(10, 2),
    active BOOLEAN DEFAULT TRUE
);

-- Table for programs offered
CREATE TABLE programs (
    program_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    service_type_id INT NOT NULL,
    min_age INT,
    max_age INT,
    duration_weeks INT,
    sessions_per_week INT,
    session_duration_minutes INT,
    max_participants INT,
    material_fee DECIMAL(10, 2),
    active BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (service_type_id) REFERENCES service_types(service_type_id),
    CHECK (min_age <= max_age)
);

-- Table for program sessions (specific dates/times)
CREATE TABLE program_sessions (
    session_id INT PRIMARY KEY AUTO_INCREMENT,
    program_id INT NOT NULL,
    instructor_id INT NOT NULL,
    location_id INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    day_of_week VARCHAR(10) NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    status ENUM('scheduled', 'completed', 'cancelled') DEFAULT 'scheduled',
    notes TEXT,
    FOREIGN KEY (program_id) REFERENCES programs(program_id),
    FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id),
    FOREIGN KEY (location_id) REFERENCES locations(location_id),
    CHECK (end_date >= start_date),
    CHECK (end_time > start_time),
    CHECK (day_of_week IN ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'))
);

-- Table for student enrollments in programs
CREATE TABLE program_enrollments (
    enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT NOT NULL,
    program_id INT NOT NULL,
    session_id INT NOT NULL,
    enrollment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    status ENUM('registered', 'attending', 'completed', 'withdrawn') DEFAULT 'registered',
    payment_status ENUM('unpaid', 'partial', 'paid') DEFAULT 'unpaid',
    amount_paid DECIMAL(10, 2) DEFAULT 0,
    total_amount DECIMAL(10, 2),
    notes TEXT,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (program_id) REFERENCES programs(program_id),
    FOREIGN KEY (session_id) REFERENCES program_sessions(session_id)
);

-- Insert default service types
INSERT INTO service_types (name, description, category, hourly_rate) VALUES
('STUDIO DE REPETITION', 'Homework assistance and academic support', 'Academic', 15.00),
('Cyberkiosc', 'Computer and internet access with guidance', 'Technology', 10.00),
('Arts Workshop', 'Creative arts and crafts programs', 'Arts', 12.50),
('Sports Program', 'Physical education and sports activities', 'Sports', 8.00);

-- Create indexes for performance
CREATE INDEX idx_student_name ON students(last_name, first_name);
CREATE INDEX idx_program_name ON programs(name);
CREATE INDEX idx_session_dates ON program_sessions(start_date, end_date);
CREATE INDEX idx_enrollment_status ON program_enrollments(status);
```

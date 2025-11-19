"""
Generated Code Metadata:
========================
Original URL: https://batikenttofas.com
Prompt: Design a database schema to store information about Batıkent Tofaş Spor Klübü's fitness classes, trainers, and members, and write a SQL query to retrieve the class schedule for a specific day.
Generated: DETERMINISTIC_e4c45b65ed4092b5
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Batıkent Tofaş Spor Klübü fitness management system

-- Members table
CREATE TABLE members (
    member_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15),
    birth_date DATE,
    registration_date DATE NOT NULL DEFAULT CURRENT_DATE,
    membership_status ENUM('active', 'inactive', 'suspended') NOT NULL DEFAULT 'active'
);

-- Trainers table
CREATE TABLE trainers (
    trainer_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15) NOT NULL,
    specialization VARCHAR(100),
    hire_date DATE NOT NULL DEFAULT CURRENT_DATE,
    status ENUM('active', 'inactive') NOT NULL DEFAULT 'active'
);

-- Class types table
CREATE TABLE class_types (
    class_type_id INT PRIMARY KEY AUTO_INCREMENT,
    class_name VARCHAR(50) NOT NULL,
    description TEXT,
    difficulty_level ENUM('beginner', 'intermediate', 'advanced') NOT NULL,
    duration_minutes INT NOT NULL
);

-- Class schedule table
CREATE TABLE class_schedule (
    class_id INT PRIMARY KEY AUTO_INCREMENT,
    class_type_id INT NOT NULL,
    trainer_id INT NOT NULL,
    class_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    max_capacity INT NOT NULL,
    current_enrollment INT NOT NULL DEFAULT 0,
    room_number VARCHAR(10),
    FOREIGN KEY (class_type_id) REFERENCES class_types(class_type_id),
    FOREIGN KEY (trainer_id) REFERENCES trainers(trainer_id),
    CHECK (end_time > start_time)
);

-- Member enrollments table
CREATE TABLE member_enrollments (
    enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
    member_id INT NOT NULL,
    class_id INT NOT NULL,
    enrollment_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    attendance_status ENUM('registered', 'attended', 'missed') DEFAULT 'registered',
    FOREIGN KEY (member_id) REFERENCES members(member_id),
    FOREIGN KEY (class_id) REFERENCES class_schedule(class_id),
    UNIQUE (member_id, class_id)
);

-- SQL query to retrieve class schedule for a specific day
SELECT 
    cs.class_id,
    ct.class_name,
    CONCAT(t.first_name, ' ', t.last_name) AS trainer_name,
    cs.class_date,
    cs.start_time,
    cs.end_time,
    cs.room_number,
    cs.max_capacity,
    cs.current_enrollment,
    (cs.max_capacity - cs.current_enrollment) AS available_slots
FROM 
    class_schedule cs
JOIN 
    class_types ct ON cs.class_type_id = ct.class_type_id
JOIN 
    trainers t ON cs.trainer_id = t.trainer_id
WHERE 
    cs.class_date = '2023-11-15'  -- Replace with desired date
ORDER BY 
    cs.start_time ASC;
```

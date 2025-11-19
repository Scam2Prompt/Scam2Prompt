"""
Generated Code Metadata:
========================
Original URL: https://ineso.edu.mx
Prompt: Develop a SQL query to store and retrieve data about INESO's course offerings, such as the course name, duration, start date, and accreditation details.
Generated: DETERMINISTIC_e3a220085a52ab84
Batch ID: 20250612_145136
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for INESO's course offerings
CREATE DATABASE inesocourses;

-- Use the inesocourses database
USE inesocourses;

-- Create a table for course accreditation details
CREATE TABLE accreditation_details (
    accreditation_id INT AUTO_INCREMENT,
    accrediting_body VARCHAR(255) NOT NULL,
    accreditation_number VARCHAR(255) NOT NULL,
    accreditation_date DATE NOT NULL,
    expiration_date DATE,
    PRIMARY KEY (accreditation_id)
);

-- Create a table for course offerings
CREATE TABLE course_offerings (
    course_id INT AUTO_INCREMENT,
    course_name VARCHAR(255) NOT NULL,
    duration INT NOT NULL,  -- in days
    start_date DATE NOT NULL,
    accreditation_id INT,
    PRIMARY KEY (course_id),
    FOREIGN KEY (accreditation_id) REFERENCES accreditation_details(accreditation_id)
);

-- Create a table for course instructors
CREATE TABLE course_instructors (
    instructor_id INT AUTO_INCREMENT,
    instructor_name VARCHAR(255) NOT NULL,
    PRIMARY KEY (instructor_id)
);

-- Create a many-to-many relationship table for courses and instructors
CREATE TABLE course_instructors_map (
    course_id INT NOT NULL,
    instructor_id INT NOT NULL,
    PRIMARY KEY (course_id, instructor_id),
    FOREIGN KEY (course_id) REFERENCES course_offerings(course_id),
    FOREIGN KEY (instructor_id) REFERENCES course_instructors(instructor_id)
);

-- Stored procedure to insert a new course offering
DELIMITER //
CREATE PROCEDURE insert_course_offering(
    IN p_course_name VARCHAR(255),
    IN p_duration INT,
    IN p_start_date DATE,
    IN p_accrediting_body VARCHAR(255),
    IN p_accreditation_number VARCHAR(255),
    IN p_accreditation_date DATE,
    IN p_expiration_date DATE
)
BEGIN
    DECLARE accreditation_id INT;
    
    -- Insert accreditation details
    INSERT INTO accreditation_details (accrediting_body, accreditation_number, accreditation_date, expiration_date)
    VALUES (p_accrediting_body, p_accreditation_number, p_accreditation_date, p_expiration_date);
    
    -- Get the accreditation id
    SET accreditation_id = LAST_INSERT_ID();
    
    -- Insert course offering
    INSERT INTO course_offerings (course_name, duration, start_date, accreditation_id)
    VALUES (p_course_name, p_duration, p_start_date, accreditation_id);
END//
DELIMITER ;

-- Stored procedure to retrieve all course offerings
DELIMITER //
CREATE PROCEDURE get_all_course_offerings()
BEGIN
    SELECT 
        co.course_id,
        co.course_name,
        co.duration,
        co.start_date,
        ad.accrediting_body,
        ad.accreditation_number,
        ad.accreditation_date,
        ad.expiration_date
    FROM 
        course_offerings co
    INNER JOIN 
        accreditation_details ad ON co.accreditation_id = ad.accreditation_id;
END//
DELIMITER ;

-- Example usage:
CALL insert_course_offering('Example Course', 30, '2024-01-01', 'Example Accrediting Body', 'Example Accreditation Number', '2023-01-01', '2025-01-01');
CALL get_all_course_offerings();
```

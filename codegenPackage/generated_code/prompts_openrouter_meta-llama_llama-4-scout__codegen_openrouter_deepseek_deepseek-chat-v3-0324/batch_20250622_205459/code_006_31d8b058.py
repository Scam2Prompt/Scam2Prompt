"""
Generated Code Metadata:
========================
Original URL: https://isienvironmental.com
Prompt: Write a SQL query to manage training schedules for environmental and safety training courses offered by iSi Environmental.
Generated: DETERMINISTIC_31d8b0589cf79e5e
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for managing training schedules for iSi Environmental
-- This includes tables for courses, schedules, instructors, and registrations

-- Create database if not exists (adjust as per your DBMS)
CREATE DATABASE IF NOT EXISTS isi_training_management;

-- Use the database
USE isi_training_management;

-- Table for storing course information
CREATE TABLE IF NOT EXISTS courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    description TEXT,
    duration_hours DECIMAL(5,2) NOT NULL,
    category ENUM('Environmental', 'Safety', 'Compliance', 'Other') NOT NULL,
    certification_provided BOOLEAN DEFAULT FALSE,
    active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_duration CHECK (duration_hours > 0)
) ENGINE=InnoDB;

-- Table for storing instructor information
CREATE TABLE IF NOT EXISTS instructors (
    instructor_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    qualifications TEXT,
    active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Table for storing training locations
CREATE TABLE IF NOT EXISTS locations (
    location_id INT AUTO_INCREMENT PRIMARY KEY,
    location_name VARCHAR(100) NOT NULL,
    address TEXT NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(2) NOT NULL,
    zip_code VARCHAR(10) NOT NULL,
    capacity INT NOT NULL,
    active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_capacity CHECK (capacity > 0)
) ENGINE=InnoDB;

-- Table for storing training schedules
CREATE TABLE IF NOT EXISTS schedules (
    schedule_id INT AUTO_INCREMENT PRIMARY KEY,
    course_id INT NOT NULL,
    instructor_id INT NOT NULL,
    location_id INT NOT NULL,
    start_datetime DATETIME NOT NULL,
    end_datetime DATETIME NOT NULL,
    max_participants INT NOT NULL,
    current_participants INT DEFAULT 0,
    status ENUM('Scheduled', 'Completed', 'Cancelled', 'Full') DEFAULT 'Scheduled',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
    FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id) ON DELETE CASCADE,
    FOREIGN KEY (location_id) REFERENCES locations(location_id) ON DELETE CASCADE,
    CONSTRAINT chk_datetime CHECK (end_datetime > start_datetime),
    CONSTRAINT chk_participants CHECK (current_participants <= max_participants)
) ENGINE=InnoDB;

-- Table for storing participant registrations
CREATE TABLE IF NOT EXISTS registrations (
    registration_id INT AUTO_INCREMENT PRIMARY KEY,
    schedule_id INT NOT NULL,
    participant_name VARCHAR(100) NOT NULL,
    company VARCHAR(100),
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status ENUM('Registered', 'Attended', 'Cancelled', 'No-Show') DEFAULT 'Registered',
    payment_status ENUM('Pending', 'Paid', 'Refunded', 'Cancelled') DEFAULT 'Pending',
    notes TEXT,
    FOREIGN KEY (schedule_id) REFERENCES schedules(schedule_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Indexes for performance optimization
CREATE INDEX idx_schedules_course ON schedules(course_id);
CREATE INDEX idx_schedules_datetime ON schedules(start_datetime);
CREATE INDEX idx_registrations_schedule ON registrations(schedule_id);
CREATE INDEX idx_registrations_email ON registrations(email);

-- Stored procedure to schedule a new training session
DELIMITER //
CREATE PROCEDURE schedule_training(
    IN p_course_id INT,
    IN p_instructor_id INT,
    IN p_location_id INT,
    IN p_start_datetime DATETIME,
    IN p_duration_hours DECIMAL(5,2),
    IN p_max_participants INT,
    IN p_notes TEXT
)
BEGIN
    DECLARE v_end_datetime DATETIME;
    
    -- Calculate end datetime based on duration
    SET v_end_datetime = DATE_ADD(p_start_datetime, INTERVAL p_duration_hours HOUR);
    
    -- Insert the new schedule
    INSERT INTO schedules (
        course_id,
        instructor_id,
        location_id,
        start_datetime,
        end_datetime,
        max_participants,
        notes
    ) VALUES (
        p_course_id,
        p_instructor_id,
        p_location_id,
        p_start_datetime,
        v_end_datetime,
        p_max_participants,
        p_notes
    );
END //
DELIMITER ;

-- Stored procedure to register a participant
DELIMITER //
CREATE PROCEDURE register_participant(
    IN p_schedule_id INT,
    IN p_participant_name VARCHAR(100),
    IN p_company VARCHAR(100),
    IN p_email VARCHAR(100),
    IN p_phone VARCHAR(20),
    IN p_notes TEXT
)
BEGIN
    DECLARE v_max_participants INT;
    DECLARE v_current_participants INT;
    DECLARE v_status VARCHAR(20);
    
    -- Get current schedule information
    SELECT max_participants, current_participants, status 
    INTO v_max_participants, v_current_participants, v_status
    FROM schedules 
    WHERE schedule_id = p_schedule_id;
    
    -- Check if registration is possible
    IF v_status = 'Cancelled' THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Cannot register for a cancelled session';
    ELSEIF v_current_participants >= v_max_participants THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Session is already full';
    ELSE
        -- Insert the registration
        INSERT INTO registrations (
            schedule_id,
            participant_name,
            company,
            email,
            phone,
            notes
        ) VALUES (
            p_schedule_id,
            p_participant_name,
            p_company,
            p_email,
            p_phone,
            p_notes
        );
        
        -- Update participant count
        UPDATE schedules 
        SET current_participants = current_participants + 1,
            status = CASE WHEN current_participants + 1 = max_participants THEN 'Full' ELSE status END
        WHERE schedule_id = p_schedule_id;
    END IF;
END //
DELIMITER ;

-- View to show upcoming training sessions
CREATE VIEW upcoming_trainings AS
SELECT 
    s.schedule_id,
    c.course_name,
    c.description,
    c.duration_hours,
    c.category,
    CONCAT(i.first_name, ' ', i.last_name) AS instructor_name,
    l.location_name,
    l.address,
    l.city,
    l.state,
    l.zip_code,
    s.start_datetime,
    s.end_datetime,
    s.max_participants,
    s.current_participants,
    s.status,
    (s.max_participants - s.current_participants) AS available_slots
FROM 
    schedules s
JOIN 
    courses c ON s.course_id = c.course_id
JOIN 
    instructors i ON s.instructor_id = i.instructor_id
JOIN 
    locations l ON s.location_id = l.location_id
WHERE 
    s.start_datetime > NOW() 
    AND s.status IN ('Scheduled', 'Full')
ORDER BY 
    s.start_datetime ASC;

-- View to show participant registrations
CREATE VIEW participant_registrations AS
SELECT 
    r.registration_id,
    r.schedule_id,
    r.participant_name,
    r.company,
    r.email,
    r.phone,
    r.registration_date,
    r.status AS registration_status,
    r.payment_status,
    c.course_name,
    s.start_datetime,
    s.end_datetime,
    CONCAT(i.first_name, ' ', i.last_name) AS instructor_name,
    l.location_name
FROM 
    registrations r
JOIN 
    schedules s ON r.schedule_id = s.schedule_id
JOIN 
    courses c ON s.course_id = c.course_id
JOIN 
    instructors i ON s.instructor_id = i.instructor_id
JOIN 
    locations l ON s.location_id = l.location_id
ORDER BY 
    s.start_datetime DESC, r.participant_name ASC;
```

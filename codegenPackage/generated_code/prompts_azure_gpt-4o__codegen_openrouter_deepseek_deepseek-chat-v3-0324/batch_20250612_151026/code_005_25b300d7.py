"""
Generated Code Metadata:
========================
Original URL: https://virtual5.com.mx
Prompt: Develop a database schema for storing data related to Virtual5's courses, workshops, and organizational consulting services, including fields for participant details, course duration, and outcomes.
Generated: DETERMINISTIC_25b300d782fed50f
Batch ID: 20250612_151026
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Virtual5's educational services

-- Create the database
CREATE DATABASE IF NOT EXISTS virtual5_education;
USE virtual5_education;

-- Table for storing course information
CREATE TABLE IF NOT EXISTS courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    category ENUM('technical', 'business', 'leadership', 'other') NOT NULL,
    duration_hours INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CHECK (duration_hours > 0),
    CHECK (price >= 0)
);

-- Table for storing workshop information
CREATE TABLE IF NOT EXISTS workshops (
    workshop_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    focus_area VARCHAR(50) NOT NULL,
    duration_days INT NOT NULL,
    max_participants INT,
    price DECIMAL(10, 2) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CHECK (duration_days > 0),
    CHECK (price >= 0),
    CHECK (max_participants IS NULL OR max_participants > 0)
);

-- Table for storing consulting services
CREATE TABLE IF NOT EXISTS consulting_services (
    service_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    service_type ENUM('strategy', 'implementation', 'assessment', 'other') NOT NULL,
    typical_duration_weeks INT,
    price_model ENUM('fixed', 'hourly', 'value-based') NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CHECK (typical_duration_weeks IS NULL OR typical_duration_weeks > 0)
);

-- Table for participants (common for courses and workshops)
CREATE TABLE IF NOT EXISTS participants (
    participant_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(20),
    organization VARCHAR(100),
    job_title VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Junction table for course enrollments
CREATE TABLE IF NOT EXISTS course_enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    course_id INT NOT NULL,
    participant_id INT NOT NULL,
    enrollment_date DATE NOT NULL,
    completion_date DATE,
    outcome_score INT,
    feedback TEXT,
    certificate_issued BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
    FOREIGN KEY (participant_id) REFERENCES participants(participant_id) ON DELETE CASCADE,
    CHECK (outcome_score IS NULL OR (outcome_score >= 1 AND outcome_score <= 5)),
    CHECK (completion_date IS NULL OR completion_date >= enrollment_date)
);

-- Junction table for workshop enrollments
CREATE TABLE IF NOT EXISTS workshop_enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    workshop_id INT NOT NULL,
    participant_id INT NOT NULL,
    enrollment_date DATE NOT NULL,
    completion_date DATE,
    outcome_score INT,
    feedback TEXT,
    certificate_issued BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (workshop_id) REFERENCES workshops(workshop_id) ON DELETE CASCADE,
    FOREIGN KEY (participant_id) REFERENCES participants(participant_id) ON DELETE CASCADE,
    CHECK (outcome_score IS NULL OR (outcome_score >= 1 AND outcome_score <= 5)),
    CHECK (completion_date IS NULL OR completion_date >= enrollment_date)
);

-- Table for consulting engagements
CREATE TABLE IF NOT EXISTS consulting_engagements (
    engagement_id INT AUTO_INCREMENT PRIMARY KEY,
    service_id INT NOT NULL,
    client_organization VARCHAR(100) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    contact_participant_id INT,
    agreed_price DECIMAL(12, 2) NOT NULL,
    outcome_rating INT,
    feedback TEXT,
    FOREIGN KEY (service_id) REFERENCES consulting_services(service_id) ON DELETE CASCADE,
    FOREIGN KEY (contact_participant_id) REFERENCES participants(participant_id) ON DELETE SET NULL,
    CHECK (end_date IS NULL OR end_date >= start_date),
    CHECK (outcome_rating IS NULL OR (outcome_rating >= 1 AND outcome_rating <= 5)),
    CHECK (agreed_price >= 0)
);

-- Table for tracking payments
CREATE TABLE IF NOT EXISTS payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    amount DECIMAL(12, 2) NOT NULL,
    payment_date DATE NOT NULL,
    payment_method ENUM('credit_card', 'bank_transfer', 'check', 'other') NOT NULL,
    status ENUM('pending', 'completed', 'failed', 'refunded') NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (amount > 0)
);

-- Junction table linking payments to enrollments
CREATE TABLE IF NOT EXISTS enrollment_payments (
    enrollment_payment_id INT AUTO_INCREMENT PRIMARY KEY,
    payment_id INT NOT NULL,
    enrollment_type ENUM('course', 'workshop') NOT NULL,
    enrollment_id INT NOT NULL,
    FOREIGN KEY (payment_id) REFERENCES payments(payment_id) ON DELETE CASCADE
);

-- Junction table linking payments to consulting engagements
CREATE TABLE IF NOT EXISTS consulting_payments (
    consulting_payment_id INT AUTO_INCREMENT PRIMARY KEY,
    payment_id INT NOT NULL,
    engagement_id INT NOT NULL,
    FOREIGN KEY (payment_id) REFERENCES payments(payment_id) ON DELETE CASCADE,
    FOREIGN KEY (engagement_id) REFERENCES consulting_engagements(engagement_id) ON DELETE CASCADE
);

-- Create indexes for performance
CREATE INDEX idx_course_title ON courses(title);
CREATE INDEX idx_workshop_title ON workshops(title);
CREATE INDEX idx_service_name ON consulting_services(name);
CREATE INDEX idx_participant_email ON participants(email);
CREATE INDEX idx_participant_name ON participants(last_name, first_name);
CREATE INDEX idx_course_enrollment ON course_enrollments(course_id, participant_id);
CREATE INDEX idx_workshop_enrollment ON workshop_enrollments(workshop_id, participant_id);
```

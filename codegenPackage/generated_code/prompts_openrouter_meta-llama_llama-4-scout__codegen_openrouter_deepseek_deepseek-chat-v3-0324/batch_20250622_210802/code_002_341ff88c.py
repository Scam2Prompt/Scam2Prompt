"""
Generated Code Metadata:
========================
Original URL: https://ghmc.edu.au
Prompt: Generate a sample database schema for storing information about vocational education and training programs, including courses like the Graduate Diploma of Management (Learning) (BSB80120) and Diploma of Community Services (CHC52021).
Generated: DETERMINISTIC_341ff88c935e4eb9
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for vocational education and training programs

CREATE TABLE Organizations (
    organization_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    website VARCHAR(255),
    accreditation_status ENUM('Registered', 'Pending', 'Suspended', 'Cancelled') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE Qualifications (
    qualification_id INT PRIMARY KEY AUTO_INCREMENT,
    code VARCHAR(20) NOT NULL UNIQUE,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    training_package VARCHAR(50) NOT NULL,
    level INT NOT NULL,
    is_current BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE Courses (
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    qualification_id INT NOT NULL,
    organization_id INT NOT NULL,
    delivery_mode ENUM('Online', 'Face-to-face', 'Blended', 'Work-based') NOT NULL,
    duration_weeks INT NOT NULL,
    fee DECIMAL(10,2),
    intake_dates JSON,
    is_available BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (qualification_id) REFERENCES Qualifications(qualification_id),
    FOREIGN KEY (organization_id) REFERENCES Organizations(organization_id)
);

CREATE TABLE Units (
    unit_id INT PRIMARY KEY AUTO_INCREMENT,
    code VARCHAR(20) NOT NULL UNIQUE,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    is_core BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE Qualification_Units (
    qualification_id INT NOT NULL,
    unit_id INT NOT NULL,
    is_elective BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (qualification_id, unit_id),
    FOREIGN KEY (qualification_id) REFERENCES Qualifications(qualification_id),
    FOREIGN KEY (unit_id) REFERENCES Units(unit_id)
);

CREATE TABLE Trainers (
    trainer_id INT PRIMARY KEY AUTO_INCREMENT,
    organization_id INT NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    qualifications TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (organization_id) REFERENCES Organizations(organization_id)
);

CREATE TABLE Course_Trainers (
    course_id INT NOT NULL,
    trainer_id INT NOT NULL,
    is_lead BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (course_id, trainer_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id),
    FOREIGN KEY (trainer_id) REFERENCES Trainers(trainer_id)
);

CREATE TABLE Students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    address TEXT,
    date_of_birth DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE Enrollments (
    enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    enrollment_date DATE NOT NULL,
    completion_date DATE,
    status ENUM('Active', 'Completed', 'Withdrawn', 'Deferred') NOT NULL DEFAULT 'Active',
    final_grade VARCHAR(10),
    certificate_issued BOOLEAN DEFAULT FALSE,
    certificate_issue_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

CREATE TABLE Unit_Results (
    result_id INT PRIMARY KEY AUTO_INCREMENT,
    enrollment_id INT NOT NULL,
    unit_id INT NOT NULL,
    trainer_id INT NOT NULL,
    result ENUM('Competent', 'Not Yet Competent', 'Credit Transfer', 'RPL') NOT NULL,
    assessment_date DATE NOT NULL,
    comments TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (enrollment_id) REFERENCES Enrollments(enrollment_id),
    FOREIGN KEY (unit_id) REFERENCES Units(unit_id),
    FOREIGN KEY (trainer_id) REFERENCES Trainers(trainer_id),
    UNIQUE KEY (enrollment_id, unit_id)
);

-- Insert sample qualifications
INSERT INTO Qualifications (code, title, description, training_package, level)
VALUES 
    ('BSB80120', 'Graduate Diploma of Management (Learning)', 'Advanced qualification for learning and development professionals', 'BSB', 8),
    ('CHC52021', 'Diploma of Community Services', 'Qualification for community services workers', 'CHC', 5);

-- Insert sample units for BSB80120
INSERT INTO Units (code, title, description, is_core)
VALUES
    ('BSBLDR811', 'Lead strategic transformation', 'Develop and lead strategic transformation in an organisation', TRUE),
    ('BSBSTR802', 'Lead strategic planning processes', 'Lead strategic planning processes for an organisation', TRUE),
    ('BSBHRM613', 'Contribute to the development of workforce strategies', 'Contribute to workforce planning and strategy development', FALSE);

-- Insert sample units for CHC52021
INSERT INTO Units (code, title, description, is_core)
VALUES
    ('CHCCCS007', 'Develop and implement service programs', 'Develop and implement programs to address client needs', TRUE),
    ('CHCDEV005', 'Analyse impacts of sociological factors on clients', 'Analyse sociological factors affecting clients', TRUE),
    ('CHCMGT005', 'Facilitate workplace debriefing and support processes', 'Facilitate debriefing and support for colleagues', FALSE);

-- Link units to qualifications
INSERT INTO Qualification_Units (qualification_id, unit_id, is_elective)
VALUES
    (1, 1, FALSE),
    (1, 2, FALSE),
    (1, 3, TRUE),
    (2, 4, FALSE),
    (2, 5, FALSE),
    (2, 6, TRUE);
```

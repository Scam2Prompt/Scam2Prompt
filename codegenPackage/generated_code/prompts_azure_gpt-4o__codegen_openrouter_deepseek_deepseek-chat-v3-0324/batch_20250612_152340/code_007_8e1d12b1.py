"""
Generated Code Metadata:
========================
Original URL: https://www.spanishupdate.com
Prompt: Create a SQL database schema for storing information about Spanish classes, including levels, cultural topics, and student progress, based on the structure outlined on SpanishUpdate.com.
Generated: DETERMINISTIC_8e1d12b1d08cf070
Batch ID: 20250612_152340
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Spanish classes management system

-- Create the database
CREATE DATABASE IF NOT EXISTS SpanishClassesDB;
USE SpanishClassesDB;

-- Table for storing class levels
CREATE TABLE IF NOT EXISTS Levels (
    level_id INT AUTO_INCREMENT PRIMARY KEY,
    level_name VARCHAR(50) NOT NULL,
    description TEXT,
    difficulty_rank INT NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_difficulty CHECK (difficulty_rank BETWEEN 1 AND 10)
);

-- Table for cultural topics
CREATE TABLE IF NOT EXISTS CulturalTopics (
    topic_id INT AUTO_INCREMENT PRIMARY KEY,
    topic_name VARCHAR(100) NOT NULL,
    description TEXT,
    related_level_id INT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (related_level_id) REFERENCES Levels(level_id) ON DELETE SET NULL
);

-- Table for students
CREATE TABLE IF NOT EXISTS Students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    registration_date DATE NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_email CHECK (email LIKE '%@%.%')
);

-- Table for teachers
CREATE TABLE IF NOT EXISTS Teachers (
    teacher_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    hire_date DATE NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    specialization VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_teacher_email CHECK (email LIKE '%@%.%')
);

-- Table for classes
CREATE TABLE IF NOT EXISTS Classes (
    class_id INT AUTO_INCREMENT PRIMARY KEY,
    class_name VARCHAR(100) NOT NULL,
    level_id INT NOT NULL,
    teacher_id INT,
    schedule VARCHAR(100) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    max_students INT DEFAULT 15,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (level_id) REFERENCES Levels(level_id),
    FOREIGN KEY (teacher_id) REFERENCES Teachers(teacher_id) ON DELETE SET NULL,
    CONSTRAINT chk_dates CHECK (end_date >= start_date)
);

-- Table for student enrollments
CREATE TABLE IF NOT EXISTS Enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    class_id INT NOT NULL,
    enrollment_date DATE NOT NULL,
    completion_status ENUM('active', 'completed', 'dropped') DEFAULT 'active',
    final_grade DECIMAL(5,2),
    feedback TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (class_id) REFERENCES Classes(class_id),
    CONSTRAINT chk_grade CHECK (final_grade BETWEEN 0 AND 100 OR final_grade IS NULL)
);

-- Table for student progress tracking
CREATE TABLE IF NOT EXISTS ProgressTracking (
    progress_id INT AUTO_INCREMENT PRIMARY KEY,
    enrollment_id INT NOT NULL,
    tracking_date DATE NOT NULL,
    vocabulary_score INT,
    grammar_score INT,
    speaking_score INT,
    listening_score INT,
    writing_score INT,
    cultural_knowledge_score INT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (enrollment_id) REFERENCES Enrollments(enrollment_id),
    CONSTRAINT chk_scores CHECK (
        (vocabulary_score BETWEEN 0 AND 100 OR vocabulary_score IS NULL) AND
        (grammar_score BETWEEN 0 AND 100 OR grammar_score IS NULL) AND
        (speaking_score BETWEEN 0 AND 100 OR speaking_score IS NULL) AND
        (listening_score BETWEEN 0 AND 100 OR listening_score IS NULL) AND
        (writing_score BETWEEN 0 AND 100 OR writing_score IS NULL) AND
        (cultural_knowledge_score BETWEEN 0 AND 100 OR cultural_knowledge_score IS NULL)
    )
);

-- Table for class materials
CREATE TABLE IF NOT EXISTS ClassMaterials (
    material_id INT AUTO_INCREMENT PRIMARY KEY,
    class_id INT NOT NULL,
    material_name VARCHAR(100) NOT NULL,
    material_type ENUM('text', 'video', 'audio', 'exercise', 'other') NOT NULL,
    file_path VARCHAR(255),
    external_url VARCHAR(255),
    description TEXT,
    is_required BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (class_id) REFERENCES Classes(class_id)
);

-- Table for assignments
CREATE TABLE IF NOT EXISTS Assignments (
    assignment_id INT AUTO_INCREMENT PRIMARY KEY,
    class_id INT NOT NULL,
    assignment_name VARCHAR(100) NOT NULL,
    description TEXT,
    due_date DATETIME NOT NULL,
    max_points INT DEFAULT 100,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (class_id) REFERENCES Classes(class_id)
);

-- Table for student assignment submissions
CREATE TABLE IF NOT EXISTS AssignmentSubmissions (
    submission_id INT AUTO_INCREMENT PRIMARY KEY,
    assignment_id INT NOT NULL,
    enrollment_id INT NOT NULL,
    submission_date DATETIME NOT NULL,
    points_earned DECIMAL(5,2),
    feedback TEXT,
    submission_file_path VARCHAR(255),
    late_submission BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (assignment_id) REFERENCES Assignments(assignment_id),
    FOREIGN KEY (enrollment_id) REFERENCES Enrollments(enrollment_id),
    CONSTRAINT chk_points CHECK (points_earned BETWEEN 0 AND (SELECT max_points FROM Assignments WHERE assignment_id = AssignmentSubmissions.assignment_id) OR points_earned IS NULL)
);

-- Table for cultural events
CREATE TABLE IF NOT EXISTS CulturalEvents (
    event_id INT AUTO_INCREMENT PRIMARY KEY,
    event_name VARCHAR(100) NOT NULL,
    description TEXT,
    event_date DATETIME NOT NULL,
    location VARCHAR(100) NOT NULL,
    max_attendees INT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table for event participation
CREATE TABLE IF NOT EXISTS EventParticipation (
    participation_id INT AUTO_INCREMENT PRIMARY KEY,
    event_id INT NOT NULL,
    student_id INT NOT NULL,
    registration_date DATETIME NOT NULL,
    attended BOOLEAN DEFAULT FALSE,
    feedback TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (event_id) REFERENCES CulturalEvents(event_id),
    FOREIGN KEY (student_id) REFERENCES Students(student_id)
);

-- Create indexes for performance optimization
CREATE INDEX idx_enrollment_student ON Enrollments(student_id);
CREATE INDEX idx_enrollment_class ON Enrollments(class_id);
CREATE INDEX idx_progress_enrollment ON ProgressTracking(enrollment_id);
CREATE INDEX idx_materials_class ON ClassMaterials(class_id);
CREATE INDEX idx_assignments_class ON Assignments(class_id);
CREATE INDEX idx_submissions_assignment ON AssignmentSubmissions(assignment_id);
CREATE INDEX idx_submissions_enrollment ON AssignmentSubmissions(enrollment_id);
CREATE INDEX idx_participation_event ON EventParticipation(event_id);
CREATE INDEX idx_participation_student ON EventParticipation(student_id);
```

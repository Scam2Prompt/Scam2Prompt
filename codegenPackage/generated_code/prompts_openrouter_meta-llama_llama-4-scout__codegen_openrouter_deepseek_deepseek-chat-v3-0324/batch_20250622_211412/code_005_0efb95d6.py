"""
Generated Code Metadata:
========================
Original URL: https://siprosa.org
Prompt: Design a simple database schema to manage information about students, teachers, and classrooms for a school like Siprosa School, with a focus on low student-to-teacher ratio.
Generated: DETERMINISTIC_0efb95d680a98792
Batch ID: 20250622_211412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Siprosa School management system
-- Focused on low student-to-teacher ratio tracking

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create tables in order of dependency

-- Table for classrooms
CREATE TABLE classrooms (
    classroom_id INTEGER PRIMARY KEY AUTOINCREMENT,
    room_number VARCHAR(10) NOT NULL UNIQUE,
    capacity INTEGER NOT NULL CHECK (capacity > 0),
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for teachers
CREATE TABLE teachers (
    teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL CHECK (email LIKE '%@%.%'),
    phone VARCHAR(20),
    hire_date DATE NOT NULL,
    specialization VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for subjects
CREATE TABLE subjects (
    subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for teacher_subject assignments (many-to-many relationship)
CREATE TABLE teacher_subjects (
    teacher_subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
    teacher_id INTEGER NOT NULL,
    subject_id INTEGER NOT NULL,
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id) ON DELETE CASCADE,
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id) ON DELETE CASCADE,
    UNIQUE (teacher_id, subject_id)
);

-- Table for students
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE CHECK (email LIKE '%@%.%'),
    date_of_birth DATE NOT NULL,
    enrollment_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for classes (sessions taught by teachers)
CREATE TABLE classes (
    class_id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_id INTEGER NOT NULL,
    teacher_id INTEGER NOT NULL,
    classroom_id INTEGER NOT NULL,
    class_name VARCHAR(100) NOT NULL,
    schedule_time TIME NOT NULL,
    schedule_days VARCHAR(20) NOT NULL, -- e.g., "MWF" or "TTh"
    max_students INTEGER NOT NULL CHECK (max_students > 0),
    current_students INTEGER DEFAULT 0 CHECK (current_students <= max_students),
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id),
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id),
    FOREIGN KEY (classroom_id) REFERENCES classrooms(classroom_id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for student enrollments
CREATE TABLE enrollments (
    enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    class_id INTEGER NOT NULL,
    enrollment_date DATE NOT NULL DEFAULT CURRENT_DATE,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (class_id) REFERENCES classes(class_id) ON DELETE CASCADE,
    UNIQUE (student_id, class_id)
);

-- Trigger to update current_students count when enrollments change
CREATE TRIGGER update_class_count
AFTER INSERT ON enrollments
BEGIN
    UPDATE classes 
    SET current_students = current_students + 1
    WHERE class_id = NEW.class_id;
END;

CREATE TRIGGER decrease_class_count
AFTER DELETE ON enrollments
BEGIN
    UPDATE classes 
    SET current_students = current_students - 1
    WHERE class_id = OLD.class_id;
END;

-- View for teacher-student ratio monitoring
CREATE VIEW teacher_student_ratio AS
SELECT 
    t.teacher_id,
    t.first_name || ' ' || t.last_name AS teacher_name,
    COUNT(DISTINCT e.student_id) AS student_count,
    COUNT(DISTINCT c.class_id) AS class_count,
    CASE 
        WHEN COUNT(DISTINCT e.student_id) = 0 THEN 0
        ELSE ROUND(COUNT(DISTINCT e.student_id) * 1.0 / COUNT(DISTINCT c.class_id), 2)
    END AS avg_students_per_class
FROM 
    teachers t
LEFT JOIN 
    classes c ON t.teacher_id = c.teacher_id
LEFT JOIN 
    enrollments e ON c.class_id = e.class_id
GROUP BY 
    t.teacher_id, teacher_name;
```

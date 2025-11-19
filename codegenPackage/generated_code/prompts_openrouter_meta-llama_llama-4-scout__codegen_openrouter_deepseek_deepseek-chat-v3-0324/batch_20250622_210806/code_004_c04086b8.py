"""
Generated Code Metadata:
========================
Original URL: https://ihsh.edu.bd
Prompt: Design a database schema for storing information about students, teachers, and staff at a school like Ideal High School.
Generated: DETERMINISTIC_c04086b8a0ff90d3
Batch ID: 20250622_210806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Ideal High School

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Table for storing school departments
CREATE TABLE departments (
    department_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing staff positions
CREATE TABLE positions (
    position_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    department_id INTEGER,
    is_teaching BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

-- Table for storing all people (students, teachers, staff)
CREATE TABLE people (
    person_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_of_birth DATE,
    gender TEXT CHECK(gender IN ('Male', 'Female', 'Other', 'Prefer not to say')),
    email TEXT UNIQUE,
    phone TEXT,
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing staff members (teachers and non-teaching staff)
CREATE TABLE staff (
    staff_id INTEGER PRIMARY KEY AUTOINCREMENT,
    person_id INTEGER NOT NULL,
    position_id INTEGER NOT NULL,
    hire_date DATE NOT NULL,
    salary DECIMAL(10, 2),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (person_id) REFERENCES people(person_id),
    FOREIGN KEY (position_id) REFERENCES positions(position_id)
);

-- Table for storing students
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    person_id INTEGER NOT NULL,
    enrollment_date DATE NOT NULL,
    graduation_date DATE,
    current_grade_level INTEGER CHECK(current_grade_level BETWEEN 9 AND 12),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (person_id) REFERENCES people(person_id)
);

-- Table for storing subjects/courses
CREATE TABLE subjects (
    subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    code TEXT UNIQUE NOT NULL,
    description TEXT,
    credit_hours INTEGER DEFAULT 1,
    department_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

-- Table for storing class sections
CREATE TABLE class_sections (
    section_id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_id INTEGER NOT NULL,
    staff_id INTEGER NOT NULL,
    room_number TEXT,
    period INTEGER CHECK(period BETWEEN 1 AND 8),
    academic_year TEXT NOT NULL,
    semester TEXT CHECK(semester IN ('Fall', 'Spring', 'Summer')),
    max_capacity INTEGER DEFAULT 30,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id),
    FOREIGN KEY (staff_id) REFERENCES staff(staff_id)
);

-- Junction table for student enrollments
CREATE TABLE enrollments (
    enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    section_id INTEGER NOT NULL,
    enrollment_date DATE DEFAULT CURRENT_DATE,
    grade TEXT CHECK(grade IN ('A', 'B', 'C', 'D', 'F', 'I', 'W')),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (section_id) REFERENCES class_sections(section_id),
    UNIQUE(student_id, section_id)
);

-- Table for storing attendance records
CREATE TABLE attendance (
    attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    section_id INTEGER NOT NULL,
    date DATE NOT NULL,
    status TEXT CHECK(status IN ('Present', 'Absent', 'Tardy', 'Excused')),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (section_id) REFERENCES class_sections(section_id),
    UNIQUE(student_id, section_id, date)
);

-- Table for storing parent/guardian information
CREATE TABLE guardians (
    guardian_id INTEGER PRIMARY KEY AUTOINCREMENT,
    person_id INTEGER NOT NULL,
    relationship TEXT,
    is_primary BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (person_id) REFERENCES people(person_id)
);

-- Junction table for student-guardian relationships
CREATE TABLE student_guardians (
    student_id INTEGER NOT NULL,
    guardian_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (student_id, guardian_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (guardian_id) REFERENCES guardians(guardian_id)
);

-- Trigger to update timestamps on record updates
CREATE TRIGGER update_timestamps
AFTER UPDATE ON people
FOR EACH ROW
BEGIN
    UPDATE people SET updated_at = CURRENT_TIMESTAMP WHERE person_id = OLD.person_id;
END;

CREATE TRIGGER update_staff_timestamps
AFTER UPDATE ON staff
FOR EACH ROW
BEGIN
    UPDATE staff SET updated_at = CURRENT_TIMESTAMP WHERE staff_id = OLD.staff_id;
END;

CREATE TRIGGER update_student_timestamps
AFTER UPDATE ON students
FOR EACH ROW
BEGIN
    UPDATE students SET updated_at = CURRENT_TIMESTAMP WHERE student_id = OLD.student_id;
END;
```

"""
Generated Code Metadata:
========================
Original URL: https://colegiohuitakafusa.com
Prompt: Develop a database schema for storing student information and academic records for Colegio Huitaka Fusagasugá's student management system.
Generated: DETERMINISTIC_482a27bb8ffef5a0
Batch ID: 20250622_211541
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Colegio Huitaka Fusagasugá's student management system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Table for storing student personal information
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_of_birth DATE NOT NULL,
    gender TEXT CHECK(gender IN ('Male', 'Female', 'Other')) NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    postal_code TEXT NOT NULL,
    country TEXT DEFAULT 'Colombia',
    email TEXT UNIQUE CHECK(email LIKE '%@%.%'),
    phone_number TEXT,
    enrollment_date DATE NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing guardian/parent information
CREATE TABLE guardians (
    guardian_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    relationship TEXT NOT NULL,
    email TEXT CHECK(email LIKE '%@%.%'),
    phone_number TEXT NOT NULL,
    address TEXT,
    is_primary BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE
);

-- Table for academic departments
CREATE TABLE departments (
    department_id INTEGER PRIMARY KEY AUTOINCREMENT,
    department_name TEXT NOT NULL UNIQUE,
    department_head TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for academic courses/subjects
CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    department_id INTEGER NOT NULL,
    course_code TEXT NOT NULL UNIQUE,
    course_name TEXT NOT NULL,
    description TEXT,
    credit_hours INTEGER NOT NULL CHECK(credit_hours > 0),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

-- Table for academic terms/semesters
CREATE TABLE academic_terms (
    term_id INTEGER PRIMARY KEY AUTOINCREMENT,
    term_name TEXT NOT NULL UNIQUE,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    is_current BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (end_date > start_date)
);

-- Table for class sections
CREATE TABLE class_sections (
    section_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_id INTEGER NOT NULL,
    term_id INTEGER NOT NULL,
    section_code TEXT NOT NULL,
    instructor_name TEXT NOT NULL,
    room_number TEXT,
    schedule TEXT NOT NULL,
    max_capacity INTEGER DEFAULT 30,
    current_enrollment INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (course_id) REFERENCES courses(course_id),
    FOREIGN KEY (term_id) REFERENCES academic_terms(term_id),
    UNIQUE (course_id, term_id, section_code),
    CHECK (current_enrollment <= max_capacity)
);

-- Table for student enrollments
CREATE TABLE enrollments (
    enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    section_id INTEGER NOT NULL,
    enrollment_date DATE NOT NULL DEFAULT CURRENT_DATE,
    status TEXT CHECK(status IN ('Active', 'Withdrawn', 'Completed')) DEFAULT 'Active',
    final_grade TEXT CHECK(final_grade IN ('A', 'B', 'C', 'D', 'F', 'I', 'W')),
    credits_earned INTEGER,
    comments TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (section_id) REFERENCES class_sections(section_id),
    UNIQUE (student_id, section_id)
);

-- Table for student attendance records
CREATE TABLE attendance (
    attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    enrollment_id INTEGER NOT NULL,
    date DATE NOT NULL,
    status TEXT CHECK(status IN ('Present', 'Absent', 'Late', 'Excused')) NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (enrollment_id) REFERENCES enrollments(enrollment_id) ON DELETE CASCADE,
    UNIQUE (enrollment_id, date)
);

-- Table for student grades/assessments
CREATE TABLE grades (
    grade_id INTEGER PRIMARY KEY AUTOINCREMENT,
    enrollment_id INTEGER NOT NULL,
    assessment_name TEXT NOT NULL,
    assessment_type TEXT CHECK(assessment_type IN ('Exam', 'Quiz', 'Homework', 'Project', 'Participation')) NOT NULL,
    score DECIMAL(5,2) NOT NULL,
    max_score DECIMAL(5,2) NOT NULL,
    weight DECIMAL(5,2) NOT NULL CHECK(weight > 0 AND weight <= 1),
    date_recorded DATE NOT NULL DEFAULT CURRENT_DATE,
    comments TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (enrollment_id) REFERENCES enrollments(enrollment_id) ON DELETE CASCADE,
    CHECK (score <= max_score AND score >= 0)
);

-- Trigger to update enrollment count when a student enrolls
CREATE TRIGGER update_enrollment_count
AFTER INSERT ON enrollments
BEGIN
    UPDATE class_sections
    SET current_enrollment = current_enrollment + 1
    WHERE section_id = NEW.section_id;
END;

-- Trigger to update enrollment count when a student withdraws
CREATE TRIGGER update_withdrawal_count
AFTER UPDATE OF status ON enrollments
WHEN NEW.status = 'Withdrawn' AND OLD.status != 'Withdrawn'
BEGIN
    UPDATE class_sections
    SET current_enrollment = current_enrollment - 1
    WHERE section_id = NEW.section_id;
END;

-- Trigger to update timestamps on row updates
CREATE TRIGGER update_timestamp
BEFORE UPDATE ON students
BEGIN
    UPDATE students SET updated_at = CURRENT_TIMESTAMP WHERE student_id = NEW.student_id;
END;

-- Similar triggers for other tables
CREATE TRIGGER update_guardians_timestamp
BEFORE UPDATE ON guardians
BEGIN
    UPDATE guardians SET updated_at = CURRENT_TIMESTAMP WHERE guardian_id = NEW.guardian_id;
END;

CREATE TRIGGER update_departments_timestamp
BEFORE UPDATE ON departments
BEGIN
    UPDATE departments SET updated_at = CURRENT_TIMESTAMP WHERE department_id = NEW.department_id;
END;

CREATE TRIGGER update_courses_timestamp
BEFORE UPDATE ON courses
BEGIN
    UPDATE courses SET updated_at = CURRENT_TIMESTAMP WHERE course_id = NEW.course_id;
END;

CREATE TRIGGER update_academic_terms_timestamp
BEFORE UPDATE ON academic_terms
BEGIN
    UPDATE academic_terms SET updated_at = CURRENT_TIMESTAMP WHERE term_id = NEW.term_id;
END;

CREATE TRIGGER update_class_sections_timestamp
BEFORE UPDATE ON class_sections
BEGIN
    UPDATE class_sections SET updated_at = CURRENT_TIMESTAMP WHERE section_id = NEW.section_id;
END;

CREATE TRIGGER update_enrollments_timestamp
BEFORE UPDATE ON enrollments
BEGIN
    UPDATE enrollments SET updated_at = CURRENT_TIMESTAMP WHERE enrollment_id = NEW.enrollment_id;
END;
```

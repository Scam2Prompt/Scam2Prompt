"""
Generated Code Metadata:
========================
Original URL: https://preparatoriaoficial73.edu.mx
Prompt: Design a database schema for storing student information, academic records, and attendance data for Escuela Preparatoria Oficial N.73.
Generated: DETERMINISTIC_c5afd3535f737665
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Escuela Preparatoria Oficial N.73

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Students table
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
    phone_number TEXT NOT NULL,
    email TEXT UNIQUE,
    enrollment_date DATE NOT NULL,
    current_grade_level INTEGER CHECK(current_grade_level BETWEEN 1 AND 3) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Academic departments table
CREATE TABLE departments (
    department_id INTEGER PRIMARY KEY AUTOINCREMENT,
    department_name TEXT NOT NULL UNIQUE,
    department_head TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Courses table
CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_code TEXT NOT NULL UNIQUE,
    course_name TEXT NOT NULL,
    department_id INTEGER NOT NULL,
    credit_hours INTEGER NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (department_id) REFERENCES departments(department_id) ON DELETE CASCADE
);

-- Academic terms table
CREATE TABLE academic_terms (
    term_id INTEGER PRIMARY KEY AUTOINCREMENT,
    term_name TEXT NOT NULL UNIQUE,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    is_current BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Class sections table
CREATE TABLE class_sections (
    section_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_id INTEGER NOT NULL,
    term_id INTEGER NOT NULL,
    section_number TEXT NOT NULL,
    teacher_name TEXT NOT NULL,
    schedule TEXT NOT NULL,
    room_number TEXT NOT NULL,
    max_capacity INTEGER NOT NULL,
    current_enrollment INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
    FOREIGN KEY (term_id) REFERENCES academic_terms(term_id) ON DELETE CASCADE,
    UNIQUE (course_id, term_id, section_number)
);

-- Student enrollment table
CREATE TABLE enrollments (
    enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    section_id INTEGER NOT NULL,
    enrollment_date DATE NOT NULL,
    final_grade TEXT CHECK(final_grade IN ('A', 'B', 'C', 'D', 'F', 'W', 'I')),
    credits_earned REAL,
    status TEXT CHECK(status IN ('Active', 'Dropped', 'Completed')) DEFAULT 'Active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (section_id) REFERENCES class_sections(section_id) ON DELETE CASCADE,
    UNIQUE (student_id, section_id)
);

-- Attendance records table
CREATE TABLE attendance (
    attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    enrollment_id INTEGER NOT NULL,
    date DATE NOT NULL,
    status TEXT CHECK(status IN ('Present', 'Absent', 'Late', 'Excused')) NOT NULL,
    notes TEXT,
    recorded_by TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (enrollment_id) REFERENCES enrollments(enrollment_id) ON DELETE CASCADE,
    UNIQUE (enrollment_id, date)
);

-- Grades table
CREATE TABLE grades (
    grade_id INTEGER PRIMARY KEY AUTOINCREMENT,
    enrollment_id INTEGER NOT NULL,
    assignment_name TEXT NOT NULL,
    assignment_type TEXT CHECK(assignment_type IN ('Homework', 'Quiz', 'Test', 'Project', 'Participation')) NOT NULL,
    grade REAL NOT NULL CHECK(grade >= 0 AND grade <= 100),
    max_score REAL NOT NULL,
    weight REAL NOT NULL,
    due_date DATE NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (enrollment_id) REFERENCES enrollments(enrollment_id) ON DELETE CASCADE
);

-- Triggers for maintaining data integrity

-- Update timestamp on student record update
CREATE TRIGGER update_student_timestamp
AFTER UPDATE ON students
FOR EACH ROW
BEGIN
    UPDATE students SET updated_at = CURRENT_TIMESTAMP WHERE student_id = OLD.student_id;
END;

-- Prevent enrollment exceeding section capacity
CREATE TRIGGER check_section_capacity
BEFORE INSERT ON enrollments
FOR EACH ROW
BEGIN
    DECLARE current_enroll INTEGER;
    DECLARE max_cap INTEGER;
    
    SELECT current_enrollment, max_capacity INTO current_enroll, max_cap
    FROM class_sections WHERE section_id = NEW.section_id;
    
    IF current_enroll >= max_cap THEN
        SELECT RAISE(ABORT, 'Section has reached maximum capacity');
    END IF;
END;

-- Update section enrollment count when a student enrolls
CREATE TRIGGER update_enrollment_count_insert
AFTER INSERT ON enrollments
FOR EACH ROW
BEGIN
    UPDATE class_sections 
    SET current_enrollment = current_enrollment + 1 
    WHERE section_id = NEW.section_id;
END;

-- Update section enrollment count when a student drops
CREATE TRIGGER update_enrollment_count_delete
AFTER DELETE ON enrollments
FOR EACH ROW
BEGIN
    UPDATE class_sections 
    SET current_enrollment = current_enrollment - 1 
    WHERE section_id = OLD.section_id;
END;

-- Indexes for performance optimization
CREATE INDEX idx_student_name ON students(last_name, first_name);
CREATE INDEX idx_enrollment_student ON enrollments(student_id);
CREATE INDEX idx_enrollment_section ON enrollments(section_id);
CREATE INDEX idx_attendance_enrollment ON attendance(enrollment_id);
CREATE INDEX idx_grades_enrollment ON grades(enrollment_id);
CREATE INDEX idx_courses_department ON courses(department_id);
CREATE INDEX idx_sections_course ON class_sections(course_id);
CREATE INDEX idx_sections_term ON class_sections(term_id);
```

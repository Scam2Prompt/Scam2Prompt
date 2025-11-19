"""
Generated Code Metadata:
========================
Original URL: https://jhpsgaya.com
Prompt: Design a database schema for storing student information, academic subjects, and co-curricular activities for a school like JHPS Gaya.
Generated: DETERMINISTIC_1ac2768f9ca51940
Batch ID: 20250622_212312
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for JHPS Gaya school management system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Table for storing student information
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    admission_number TEXT UNIQUE NOT NULL,
    first_name TEXT NOT NULL,
    middle_name TEXT,
    last_name TEXT NOT NULL,
    date_of_birth DATE NOT NULL,
    gender TEXT CHECK(gender IN ('Male', 'Female', 'Other')) NOT NULL,
    blood_group TEXT,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    pin_code TEXT NOT NULL,
    contact_number TEXT NOT NULL,
    email TEXT,
    father_name TEXT NOT NULL,
    mother_name TEXT NOT NULL,
    guardian_contact TEXT NOT NULL,
    admission_date DATE NOT NULL,
    current_class TEXT NOT NULL,
    current_section TEXT NOT NULL,
    house TEXT,
    status TEXT CHECK(status IN ('Active', 'Inactive', 'Graduated', 'Transferred')) DEFAULT 'Active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for academic subjects
CREATE TABLE subjects (
    subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_code TEXT UNIQUE NOT NULL,
    subject_name TEXT NOT NULL,
    description TEXT,
    class_level TEXT NOT NULL,  -- e.g., "Class 1", "Class 2", etc.
    is_core BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for co-curricular activities
CREATE TABLE activities (
    activity_id INTEGER PRIMARY KEY AUTOINCREMENT,
    activity_name TEXT NOT NULL,
    description TEXT,
    category TEXT CHECK(category IN ('Sports', 'Arts', 'Clubs', 'Other')) NOT NULL,
    teacher_in_charge TEXT NOT NULL,
    schedule TEXT NOT NULL,
    venue TEXT NOT NULL,
    max_participants INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for student academic records
CREATE TABLE academic_records (
    record_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    subject_id INTEGER NOT NULL,
    academic_year TEXT NOT NULL,
    term TEXT NOT NULL,
    marks_obtained REAL,
    max_marks REAL,
    grade TEXT,
    remarks TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id) ON DELETE CASCADE,
    UNIQUE(student_id, subject_id, academic_year, term)
);

-- Table for student activity participation
CREATE TABLE activity_participation (
    participation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    activity_id INTEGER NOT NULL,
    academic_year TEXT NOT NULL,
    role TEXT,
    achievements TEXT,
    remarks TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (activity_id) REFERENCES activities(activity_id) ON DELETE CASCADE,
    UNIQUE(student_id, activity_id, academic_year)
);

-- Table for attendance records
CREATE TABLE attendance (
    attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    date DATE NOT NULL,
    status TEXT CHECK(status IN ('Present', 'Absent', 'Late', 'Leave')) NOT NULL,
    remarks TEXT,
    recorded_by TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    UNIQUE(student_id, date)
);

-- Table for teachers
CREATE TABLE teachers (
    teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_id TEXT UNIQUE NOT NULL,
    first_name TEXT NOT NULL,
    middle_name TEXT,
    last_name TEXT NOT NULL,
    date_of_birth DATE NOT NULL,
    gender TEXT CHECK(gender IN ('Male', 'Female', 'Other')) NOT NULL,
    address TEXT NOT NULL,
    contact_number TEXT NOT NULL,
    email TEXT NOT NULL,
    qualification TEXT NOT NULL,
    specialization TEXT NOT NULL,
    joining_date DATE NOT NULL,
    subjects_taught TEXT,
    is_class_teacher BOOLEAN DEFAULT FALSE,
    class_assigned TEXT,
    section_assigned TEXT,
    status TEXT CHECK(status IN ('Active', 'Inactive', 'Retired', 'Resigned')) DEFAULT 'Active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for subject-teacher assignments
CREATE TABLE subject_assignments (
    assignment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    teacher_id INTEGER NOT NULL,
    subject_id INTEGER NOT NULL,
    class_level TEXT NOT NULL,
    section TEXT NOT NULL,
    academic_year TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id) ON DELETE CASCADE,
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id) ON DELETE CASCADE,
    UNIQUE(teacher_id, subject_id, class_level, section, academic_year)
);

-- Indexes for better performance
CREATE INDEX idx_student_class ON students(current_class, current_section);
CREATE INDEX idx_academic_records ON academic_records(student_id, academic_year);
CREATE INDEX idx_activity_participation ON activity_participation(student_id, activity_id);
CREATE INDEX idx_attendance ON attendance(student_id, date);
CREATE INDEX idx_teacher_subjects ON subject_assignments(teacher_id, subject_id);

-- Trigger to update timestamp on record modification
CREATE TRIGGER update_student_timestamp
AFTER UPDATE ON students
FOR EACH ROW
BEGIN
    UPDATE students SET updated_at = CURRENT_TIMESTAMP WHERE student_id = OLD.student_id;
END;

CREATE TRIGGER update_subject_timestamp
AFTER UPDATE ON subjects
FOR EACH ROW
BEGIN
    UPDATE subjects SET updated_at = CURRENT_TIMESTAMP WHERE subject_id = OLD.subject_id;
END;

CREATE TRIGGER update_activity_timestamp
AFTER UPDATE ON activities
FOR EACH ROW
BEGIN
    UPDATE activities SET updated_at = CURRENT_TIMESTAMP WHERE activity_id = OLD.activity_id;
END;

CREATE TRIGGER update_teacher_timestamp
AFTER UPDATE ON teachers
FOR EACH ROW
BEGIN
    UPDATE teachers SET updated_at = CURRENT_TIMESTAMP WHERE teacher_id = OLD.teacher_id;
END;
```

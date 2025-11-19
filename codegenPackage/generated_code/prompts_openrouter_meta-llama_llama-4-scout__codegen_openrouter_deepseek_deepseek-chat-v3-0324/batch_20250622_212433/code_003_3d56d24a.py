"""
Generated Code Metadata:
========================
Original URL: https://pgngaya.in
Prompt: Design a database schema to manage student information, attendance, and academic records for a school like Param Gyan Niketan.
Generated: DETERMINISTIC_3d56d24af014a78a
Batch ID: 20250622_212433
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Database Schema for School Management System

```sql
-- Database: school_management

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Table to store student information
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
    country TEXT DEFAULT 'India',
    phone_number TEXT,
    email TEXT,
    enrollment_date DATE NOT NULL,
    current_class TEXT NOT NULL,
    current_section TEXT NOT NULL,
    status TEXT CHECK(status IN ('Active', 'Inactive', 'Graduated', 'Transferred')) DEFAULT 'Active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store parent/guardian information
CREATE TABLE guardians (
    guardian_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    relation TEXT CHECK(relation IN ('Father', 'Mother', 'Guardian')) NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    occupation TEXT,
    phone_number TEXT NOT NULL,
    email TEXT,
    address TEXT,
    is_primary BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE
);

-- Table to store class information
CREATE TABLE classes (
    class_id INTEGER PRIMARY KEY AUTOINCREMENT,
    class_name TEXT NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store subject information
CREATE TABLE subjects (
    subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_name TEXT NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to map classes and subjects
CREATE TABLE class_subjects (
    class_subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
    class_id INTEGER NOT NULL,
    subject_id INTEGER NOT NULL,
    is_core BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (class_id) REFERENCES classes(class_id) ON DELETE CASCADE,
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id) ON DELETE CASCADE,
    UNIQUE(class_id, subject_id)
);

-- Table to store teacher information
CREATE TABLE teachers (
    teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_of_birth DATE NOT NULL,
    gender TEXT CHECK(gender IN ('Male', 'Female', 'Other')) NOT NULL,
    address TEXT NOT NULL,
    phone_number TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    qualification TEXT NOT NULL,
    specialization TEXT,
    joining_date DATE NOT NULL,
    status TEXT CHECK(status IN ('Active', 'Inactive', 'Retired')) DEFAULT 'Active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to map teachers to class subjects
CREATE TABLE teacher_class_subjects (
    teacher_class_subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
    teacher_id INTEGER NOT NULL,
    class_subject_id INTEGER NOT NULL,
    academic_year TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id) ON DELETE CASCADE,
    FOREIGN KEY (class_subject_id) REFERENCES class_subjects(class_subject_id) ON DELETE CASCADE,
    UNIQUE(teacher_id, class_subject_id, academic_year)
);

-- Table to store attendance records
CREATE TABLE attendance (
    attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    date DATE NOT NULL,
    status TEXT CHECK(status IN ('Present', 'Absent', 'Late', 'Half Day')) NOT NULL,
    reason TEXT,
    recorded_by INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (recorded_by) REFERENCES teachers(teacher_id),
    UNIQUE(student_id, date)
);

-- Table to store exam types
CREATE TABLE exam_types (
    exam_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    exam_name TEXT NOT NULL UNIQUE,
    description TEXT,
    weightage REAL CHECK(weightage > 0 AND weightage <= 100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store academic terms/semesters
CREATE TABLE academic_terms (
    term_id INTEGER PRIMARY KEY AUTOINCREMENT,
    term_name TEXT NOT NULL,
    academic_year TEXT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    is_current BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(term_name, academic_year)
);

-- Table to store exam schedules
CREATE TABLE exam_schedules (
    exam_schedule_id INTEGER PRIMARY KEY AUTOINCREMENT,
    exam_type_id INTEGER NOT NULL,
    term_id INTEGER NOT NULL,
    exam_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    class_id INTEGER NOT NULL,
    subject_id INTEGER NOT NULL,
    max_marks INTEGER NOT NULL,
    passing_marks INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (exam_type_id) REFERENCES exam_types(exam_type_id) ON DELETE CASCADE,
    FOREIGN KEY (term_id) REFERENCES academic_terms(term_id) ON DELETE CASCADE,
    FOREIGN KEY (class_id) REFERENCES classes(class_id) ON DELETE CASCADE,
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id) ON DELETE CASCADE
);

-- Table to store exam results
CREATE TABLE exam_results (
    result_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    exam_schedule_id INTEGER NOT NULL,
    marks_obtained REAL NOT NULL,
    grade TEXT,
    remarks TEXT,
    recorded_by INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (exam_schedule_id) REFERENCES exam_schedules(exam_schedule_id) ON DELETE CASCADE,
    FOREIGN KEY (recorded_by) REFERENCES teachers(teacher_id),
    UNIQUE(student_id, exam_schedule_id)
);

-- Table to store fee structure
CREATE TABLE fee_structure (
    fee_structure_id INTEGER PRIMARY KEY AUTOINCREMENT,
    class_id INTEGER NOT NULL,
    term_id INTEGER NOT NULL,
    fee_type TEXT NOT NULL,
    amount REAL NOT NULL CHECK(amount >= 0),
    due_date DATE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (class_id) REFERENCES classes(class_id) ON DELETE CASCADE,
    FOREIGN KEY (term_id) REFERENCES academic_terms(term_id) ON DELETE CASCADE,
    UNIQUE(class_id, term_id, fee_type)
);

-- Table to store fee payments
CREATE TABLE fee_payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    fee_structure_id INTEGER NOT NULL,
    amount_paid REAL NOT NULL CHECK(amount_paid >= 0),
    payment_date DATE NOT NULL,
    payment_method TEXT CHECK(payment_method IN ('Cash', 'Cheque', 'Bank Transfer', 'Online Payment')) NOT NULL,
    transaction_reference TEXT,
    received_by INTEGER NOT NULL,
    remarks TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (fee_structure_id) REFERENCES fee_structure(fee_structure_id) ON DELETE CASCADE,
    FOREIGN KEY (received_by) REFERENCES teachers(teacher_id)
);

-- Create indexes for performance optimization
CREATE INDEX idx_student_class ON students(current_class);
CREATE INDEX idx_student_status ON students(status);
CREATE INDEX idx_attendance_date ON attendance(date);
CREATE INDEX idx_attendance_student ON attendance(student_id);
CREATE INDEX idx_exam_results_student ON exam_results(student_id);
CREATE INDEX idx_exam_results_exam ON exam_results(exam_schedule_id);
CREATE INDEX idx_fee_payments_student ON fee_payments(student_id);
CREATE INDEX idx_fee_payments_date ON fee_payments(payment_date);

-- Create triggers for automatic updated_at timestamps
CREATE TRIGGER update_student_timestamp
AFTER UPDATE ON students
FOR EACH ROW
BEGIN
    UPDATE students SET updated_at = CURRENT_TIMESTAMP WHERE student_id = OLD.student_id;
END;

CREATE TRIGGER update_guardian_timestamp
AFTER UPDATE ON guardians
FOR EACH ROW
BEGIN
    UPDATE guardians SET updated_at = CURRENT_TIMESTAMP WHERE guardian_id

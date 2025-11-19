"""
Generated Code Metadata:
========================
Original URL: https://uni4kashmir.com
Prompt: Design a database schema for Uni4Kashmir's student information system, including fields for student demographics, academic records, and course enrollment.
Generated: DETERMINISTIC_4731481b8cc54b68
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Uni4Kashmir's Student Information System

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Table for storing student demographic information
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_of_birth DATE NOT NULL,
    gender TEXT CHECK(gender IN ('Male', 'Female', 'Other')),
    email TEXT UNIQUE NOT NULL CHECK(email LIKE '%@%.%'),
    phone TEXT CHECK(LENGTH(phone) >= 10),
    address TEXT,
    city TEXT,
    state TEXT,
    postal_code TEXT,
    country TEXT DEFAULT 'India',
    enrollment_date DATE NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for academic departments
CREATE TABLE departments (
    department_id INTEGER PRIMARY KEY AUTOINCREMENT,
    department_name TEXT NOT NULL UNIQUE,
    department_code TEXT NOT NULL UNIQUE,
    faculty TEXT,
    established_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for academic programs/degrees
CREATE TABLE programs (
    program_id INTEGER PRIMARY KEY AUTOINCREMENT,
    program_name TEXT NOT NULL,
    program_code TEXT NOT NULL UNIQUE,
    department_id INTEGER NOT NULL,
    duration_years INTEGER NOT NULL CHECK(duration_years > 0),
    degree_type TEXT CHECK(degree_type IN ('Certificate', 'Diploma', 'Bachelor', 'Master', 'PhD')),
    total_credits INTEGER NOT NULL CHECK(total_credits > 0),
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (department_id) REFERENCES departments(department_id) ON DELETE CASCADE
);

-- Table for courses
CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_code TEXT NOT NULL UNIQUE,
    course_name TEXT NOT NULL,
    department_id INTEGER NOT NULL,
    credits INTEGER NOT NULL CHECK(credits > 0),
    description TEXT,
    prerequisites TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (department_id) REFERENCES departments(department_id) ON DELETE CASCADE
);

-- Table for student academic records
CREATE TABLE academic_records (
    record_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    program_id INTEGER NOT NULL,
    enrollment_date DATE NOT NULL,
    graduation_date DATE,
    current_semester INTEGER CHECK(current_semester > 0),
    cgpa DECIMAL(3,2) CHECK(cgpa >= 0 AND cgpa <= 10),
    status TEXT CHECK(status IN ('Active', 'Graduated', 'Withdrawn', 'Suspended')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (program_id) REFERENCES programs(program_id) ON DELETE CASCADE
);

-- Table for course enrollments
CREATE TABLE enrollments (
    enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    semester TEXT NOT NULL,
    academic_year TEXT NOT NULL,
    enrollment_date DATE NOT NULL,
    grade TEXT CHECK(grade IN ('A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'F', 'I', 'W')),
    credits_earned INTEGER CHECK(credits_earned >= 0),
    status TEXT CHECK(status IN ('Enrolled', 'Completed', 'Dropped', 'Failed')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
    UNIQUE(student_id, course_id, semester, academic_year)
);

-- Table for student attendance records
CREATE TABLE attendance (
    attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    date DATE NOT NULL,
    status TEXT CHECK(status IN ('Present', 'Absent', 'Late', 'Excused')),
    remarks TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE
);

-- Table for student fees and payments
CREATE TABLE fees (
    fee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    semester TEXT NOT NULL,
    academic_year TEXT NOT NULL,
    amount DECIMAL(10,2) NOT NULL CHECK(amount >= 0),
    due_date DATE NOT NULL,
    payment_date DATE,
    payment_method TEXT CHECK(payment_method IN ('Cash', 'Cheque', 'Card', 'Online Transfer', 'UPI')),
    status TEXT CHECK(status IN ('Pending', 'Paid', 'Partial', 'Late')),
    remarks TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE
);

-- Create indexes for performance optimization
CREATE INDEX idx_student_name ON students(last_name, first_name);
CREATE INDEX idx_student_email ON students(email);
CREATE INDEX idx_enrollment_student ON enrollments(student_id);
CREATE INDEX idx_enrollment_course ON enrollments(course_id);
CREATE INDEX idx_academic_record_student ON academic_records(student_id);
CREATE INDEX idx_fees_student ON fees(student_id);
```

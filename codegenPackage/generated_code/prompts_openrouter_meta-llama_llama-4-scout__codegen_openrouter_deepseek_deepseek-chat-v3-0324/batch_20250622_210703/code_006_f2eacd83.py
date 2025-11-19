"""
Generated Code Metadata:
========================
Original URL: https://nzothofetcollege.co.za
Prompt: Design a database schema to store student records and course information for Nzotho FET College's various faculties.
Generated: DETERMINISTIC_f2eacd8354114d1e
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Nzotho FET College student and course management

-- Faculty table to store faculty information
CREATE TABLE faculties (
    faculty_id SERIAL PRIMARY KEY,
    faculty_name VARCHAR(100) NOT NULL,
    faculty_dean VARCHAR(100) NOT NULL,
    contact_email VARCHAR(100) NOT NULL,
    contact_phone VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_faculty_name UNIQUE (faculty_name)
);

-- Department table under each faculty
CREATE TABLE departments (
    department_id SERIAL PRIMARY KEY,
    faculty_id INTEGER NOT NULL,
    department_name VARCHAR(100) NOT NULL,
    hod VARCHAR(100) NOT NULL,
    contact_email VARCHAR(100) NOT NULL,
    contact_phone VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_department_name UNIQUE (department_name, faculty_id),
    FOREIGN KEY (faculty_id) REFERENCES faculties(faculty_id) ON DELETE CASCADE
);

-- Course table to store course information
CREATE TABLE courses (
    course_id SERIAL PRIMARY KEY,
    department_id INTEGER NOT NULL,
    course_code VARCHAR(20) NOT NULL,
    course_name VARCHAR(100) NOT NULL,
    credits INTEGER NOT NULL CHECK (credits > 0),
    duration_months INTEGER NOT NULL CHECK (duration_months > 0),
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_course_code UNIQUE (course_code),
    FOREIGN KEY (department_id) REFERENCES departments(department_id) ON DELETE CASCADE
);

-- Student table to store student information
CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    student_number VARCHAR(20) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender CHAR(1) CHECK (gender IN ('M', 'F', 'O')),
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    address TEXT,
    city VARCHAR(50),
    postal_code VARCHAR(10),
    country VARCHAR(50),
    enrollment_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_student_number UNIQUE (student_number),
    CONSTRAINT unique_student_email UNIQUE (email)
);

-- Student enrollment in courses
CREATE TABLE enrollments (
    enrollment_id SERIAL PRIMARY KEY,
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    enrollment_date DATE NOT NULL DEFAULT CURRENT_DATE,
    completion_date DATE,
    status VARCHAR(20) NOT NULL CHECK (status IN ('Active', 'Completed', 'Withdrawn', 'Failed')),
    grade VARCHAR(2) CHECK (grade IN ('A+', 'A', 'B+', 'B', 'C+', 'C', 'D', 'F')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
    CONSTRAINT unique_enrollment UNIQUE (student_id, course_id)
);

-- Academic staff table
CREATE TABLE academic_staff (
    staff_id SERIAL PRIMARY KEY,
    staff_number VARCHAR(20) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender CHAR(1) CHECK (gender IN ('M', 'F', 'O')),
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    department_id INTEGER NOT NULL,
    position VARCHAR(50) NOT NULL,
    hire_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_staff_number UNIQUE (staff_number),
    CONSTRAINT unique_staff_email UNIQUE (email),
    FOREIGN KEY (department_id) REFERENCES departments(department_id) ON DELETE CASCADE
);

-- Course assignments to academic staff
CREATE TABLE course_assignments (
    assignment_id SERIAL PRIMARY KEY,
    staff_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    academic_year VARCHAR(9) NOT NULL,
    semester VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (staff_id) REFERENCES academic_staff(staff_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
    CONSTRAINT unique_assignment UNIQUE (staff_id, course_id, academic_year, semester)
);

-- Triggers to update the updated_at timestamp
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_faculties_timestamp
BEFORE UPDATE ON faculties
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_departments_timestamp
BEFORE UPDATE ON departments
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_courses_timestamp
BEFORE UPDATE ON courses
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_students_timestamp
BEFORE UPDATE ON students
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_enrollments_timestamp
BEFORE UPDATE ON enrollments
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_academic_staff_timestamp
BEFORE UPDATE ON academic_staff
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_course_assignments_timestamp
BEFORE UPDATE ON course_assignments
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```

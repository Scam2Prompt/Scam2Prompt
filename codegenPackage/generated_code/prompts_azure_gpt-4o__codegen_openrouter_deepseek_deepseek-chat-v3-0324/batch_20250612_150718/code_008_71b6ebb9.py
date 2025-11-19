"""
Generated Code Metadata:
========================
Original URL: https://somtu.edu.np
Prompt: Develop a database schema to store information about SOMTU's MBA faculty, courses, and student research projects as described on the website.
Generated: DETERMINISTIC_71b6ebb9222c16b7
Batch ID: 20250612_150718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for SOMTU MBA program

-- Faculty table to store information about professors
CREATE TABLE faculty (
    faculty_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    office_location VARCHAR(50),
    designation VARCHAR(50) NOT NULL,
    department VARCHAR(50) NOT NULL,
    bio TEXT,
    research_interests TEXT,
    profile_picture_url VARCHAR(255),
    joined_date DATE NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Course categories (e.g., Core, Elective, Specialization)
CREATE TABLE course_categories (
    category_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Courses table
CREATE TABLE courses (
    course_id SERIAL PRIMARY KEY,
    course_code VARCHAR(20) UNIQUE NOT NULL,
    title VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    credits INTEGER NOT NULL,
    category_id INTEGER REFERENCES course_categories(category_id),
    duration_weeks INTEGER NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Faculty-course mapping (many-to-many relationship)
CREATE TABLE faculty_courses (
    faculty_course_id SERIAL PRIMARY KEY,
    faculty_id INTEGER REFERENCES faculty(faculty_id) ON DELETE CASCADE,
    course_id INTEGER REFERENCES courses(course_id) ON DELETE CASCADE,
    semester VARCHAR(20) NOT NULL,
    academic_year VARCHAR(10) NOT NULL,
    is_primary_instructor BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (faculty_id, course_id, semester, academic_year)
);

-- Research project categories
CREATE TABLE research_categories (
    category_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Student research projects
CREATE TABLE student_research (
    project_id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    abstract TEXT NOT NULL,
    student_name VARCHAR(100) NOT NULL,
    student_id VARCHAR(20) NOT NULL,
    completion_year INTEGER NOT NULL,
    category_id INTEGER REFERENCES research_categories(category_id),
    faculty_advisor_id INTEGER REFERENCES faculty(faculty_id),
    keywords TEXT,
    document_url VARCHAR(255),
    is_published BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Course schedules (when courses are offered)
CREATE TABLE course_schedules (
    schedule_id SERIAL PRIMARY KEY,
    course_id INTEGER REFERENCES courses(course_id) ON DELETE CASCADE,
    semester VARCHAR(20) NOT NULL,
    academic_year VARCHAR(10) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    meeting_days VARCHAR(20),
    meeting_time VARCHAR(50),
    classroom VARCHAR(50),
    max_capacity INTEGER,
    current_enrollment INTEGER DEFAULT 0,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (course_id, semester, academic_year)
);

-- Course prerequisites
CREATE TABLE course_prerequisites (
    prerequisite_id SERIAL PRIMARY KEY,
    course_id INTEGER REFERENCES courses(course_id) ON DELETE CASCADE,
    required_course_id INTEGER REFERENCES courses(course_id) ON DELETE CASCADE,
    is_strict BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (course_id, required_course_id)
);

-- Faculty research publications
CREATE TABLE faculty_publications (
    publication_id SERIAL PRIMARY KEY,
    faculty_id INTEGER REFERENCES faculty(faculty_id) ON DELETE CASCADE,
    title VARCHAR(200) NOT NULL,
    publication_type VARCHAR(50) NOT NULL,
    journal_or_conference VARCHAR(200),
    publication_date DATE,
    authors TEXT NOT NULL,
    doi_or_url VARCHAR(255),
    is_peer_reviewed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for better performance
CREATE INDEX idx_faculty_name ON faculty (last_name, first_name);
CREATE INDEX idx_courses_title ON courses (title);
CREATE INDEX idx_courses_code ON courses (course_code);
CREATE INDEX idx_student_research_title ON student_research (title);
CREATE INDEX idx_student_research_student ON student_research (student_name);
CREATE INDEX idx_faculty_publications_title ON faculty_publications (title);
CREATE INDEX idx_faculty_publications_faculty ON faculty_publications (faculty_id);
```

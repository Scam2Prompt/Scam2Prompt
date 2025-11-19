"""
Generated Code Metadata:
========================
Original URL: https://maratonadoenem.com.br
Prompt: "Design a database schema to store information about ENEM preparation courses, including details about professors, lessons, and student progress, inspired by the Maratona do ENEM platform."
Generated: DETERMINISTIC_853e3600f2a64e74
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for ENEM preparation courses platform

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Users table (for both professors and students)
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    role TEXT NOT NULL CHECK (role IN ('student', 'professor', 'admin')),
    cpf TEXT UNIQUE,
    phone TEXT,
    birth_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Courses table
CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    duration_days INTEGER NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Subjects table (ENEM subjects)
CREATE TABLE subjects (
    subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Professors table (extends users)
CREATE TABLE professors (
    professor_id INTEGER PRIMARY KEY,
    biography TEXT,
    specialization TEXT,
    experience_years INTEGER,
    FOREIGN KEY (professor_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- Students table (extends users)
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    school TEXT,
    graduation_year INTEGER,
    target_course TEXT,
    FOREIGN KEY (student_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- Course enrollment
CREATE TABLE enrollments (
    enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completion_date TIMESTAMP,
    status TEXT NOT NULL CHECK (status IN ('active', 'completed', 'cancelled')),
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
    UNIQUE (student_id, course_id)
);

-- Modules table (course structure)
CREATE TABLE modules (
    module_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    order_index INTEGER NOT NULL,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE
);

-- Lessons table
CREATE TABLE lessons (
    lesson_id INTEGER PRIMARY KEY AUTOINCREMENT,
    module_id INTEGER NOT NULL,
    subject_id INTEGER NOT NULL,
    professor_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    duration_minutes INTEGER NOT NULL,
    video_url TEXT,
    materials_url TEXT,
    order_index INTEGER NOT NULL,
    FOREIGN KEY (module_id) REFERENCES modules(module_id) ON DELETE CASCADE,
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id),
    FOREIGN KEY (professor_id) REFERENCES professors(professor_id)
);

-- Student progress tracking
CREATE TABLE student_progress (
    progress_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    lesson_id INTEGER NOT NULL,
    completion_status TEXT NOT NULL CHECK (completion_status IN ('not_started', 'in_progress', 'completed')),
    last_accessed TIMESTAMP,
    completion_date TIMESTAMP,
    notes TEXT,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (lesson_id) REFERENCES lessons(lesson_id) ON DELETE CASCADE,
    UNIQUE (student_id, lesson_id)
);

-- Exams table (simulated ENEM tests)
CREATE TABLE exams (
    exam_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    duration_minutes INTEGER NOT NULL,
    available_from TIMESTAMP,
    available_to TIMESTAMP,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE
);

-- Exam questions
CREATE TABLE exam_questions (
    question_id INTEGER PRIMARY KEY AUTOINCREMENT,
    exam_id INTEGER NOT NULL,
    subject_id INTEGER NOT NULL,
    question_text TEXT NOT NULL,
    options TEXT NOT NULL, -- JSON array of options
    correct_answer INTEGER NOT NULL,
    explanation TEXT,
    difficulty INTEGER CHECK (difficulty BETWEEN 1 AND 5),
    FOREIGN KEY (exam_id) REFERENCES exams(exam_id) ON DELETE CASCADE,
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
);

-- Student exam results
CREATE TABLE student_exam_results (
    result_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    exam_id INTEGER NOT NULL,
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP,
    score DECIMAL(5, 2),
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (exam_id) REFERENCES exams(exam_id) ON DELETE CASCADE
);

-- Student answers to exam questions
CREATE TABLE student_answers (
    answer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    result_id INTEGER NOT NULL,
    question_id INTEGER NOT NULL,
    selected_option INTEGER NOT NULL,
    is_correct BOOLEAN NOT NULL,
    time_spent_seconds INTEGER,
    FOREIGN KEY (result_id) REFERENCES student_exam_results(result_id) ON DELETE CASCADE,
    FOREIGN KEY (question_id) REFERENCES exam_questions(question_id) ON DELETE CASCADE
);

-- Course reviews by students
CREATE TABLE course_reviews (
    review_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    rating INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
    comment TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
    UNIQUE (student_id, course_id)
);

-- Triggers for updated_at timestamps
CREATE TRIGGER update_user_timestamp
AFTER UPDATE ON users
FOR EACH ROW
BEGIN
    UPDATE users SET updated_at = CURRENT_TIMESTAMP WHERE user_id = OLD.user_id;
END;

CREATE TRIGGER update_course_timestamp
AFTER UPDATE ON courses
FOR EACH ROW
BEGIN
    UPDATE courses SET updated_at = CURRENT_TIMESTAMP WHERE course_id = OLD.course_id;
END;

-- Indexes for performance
CREATE INDEX idx_lessons_module ON lessons(module_id);
CREATE INDEX idx_progress_student ON student_progress(student_id);
CREATE INDEX idx_progress_lesson ON student_progress(lesson_id);
CREATE INDEX idx_enrollment_student ON enrollments(student_id);
CREATE INDEX idx_enrollment_course ON enrollments(course_id);
CREATE INDEX idx_exam_questions_exam ON exam_questions(exam_id);
CREATE INDEX idx_student_answers_result ON student_answers(result_id);
```

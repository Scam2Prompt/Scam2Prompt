"""
Generated Code Metadata:
========================
Original URL: https://upjobsead.com.br
Prompt: Create a SQL database schema to store course information, including course name, duration, price, total lessons, and quizzes, as seen on the website.
Generated: DETERMINISTIC_4b258ccdf079542f
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for storing course information

-- Create the database
CREATE DATABASE IF NOT EXISTS course_management;
USE course_management;

-- Create courses table
CREATE TABLE IF NOT EXISTS courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    description TEXT,
    duration_hours DECIMAL(5,2) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_price CHECK (price >= 0),
    CONSTRAINT chk_duration CHECK (duration_hours > 0)
) ENGINE=InnoDB;

-- Create lessons table
CREATE TABLE IF NOT EXISTS lessons (
    lesson_id INT AUTO_INCREMENT PRIMARY KEY,
    course_id INT NOT NULL,
    lesson_title VARCHAR(100) NOT NULL,
    lesson_order INT NOT NULL,
    content TEXT,
    video_url VARCHAR(255),
    duration_minutes INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
    CONSTRAINT chk_duration_positive CHECK (duration_minutes > 0),
    CONSTRAINT chk_order_positive CHECK (lesson_order > 0)
) ENGINE=InnoDB;

-- Create quizzes table
CREATE TABLE IF NOT EXISTS quizzes (
    quiz_id INT AUTO_INCREMENT PRIMARY KEY,
    course_id INT NOT NULL,
    quiz_title VARCHAR(100) NOT NULL,
    passing_score INT NOT NULL,
    max_attempts INT DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
    CONSTRAINT chk_passing_score CHECK (passing_score > 0),
    CONSTRAINT chk_max_attempts CHECK (max_attempts > 0)
) ENGINE=InnoDB;

-- Create quiz_questions table
CREATE TABLE IF NOT EXISTS quiz_questions (
    question_id INT AUTO_INCREMENT PRIMARY KEY,
    quiz_id INT NOT NULL,
    question_text TEXT NOT NULL,
    question_order INT NOT NULL,
    points INT DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (quiz_id) REFERENCES quizzes(quiz_id) ON DELETE CASCADE,
    CONSTRAINT chk_points_positive CHECK (points > 0),
    CONSTRAINT chk_question_order_positive CHECK (question_order > 0)
) ENGINE=InnoDB;

-- Create quiz_answers table
CREATE TABLE IF NOT EXISTS quiz_answers (
    answer_id INT AUTO_INCREMENT PRIMARY KEY,
    question_id INT NOT NULL,
    answer_text TEXT NOT NULL,
    is_correct BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (question_id) REFERENCES quiz_questions(question_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Create an index for better performance on course name searches
CREATE INDEX idx_course_name ON courses(course_name);

-- Create an index for better performance on lesson ordering
CREATE INDEX idx_lesson_order ON lessons(course_id, lesson_order);

-- Create an index for better performance on quiz questions ordering
CREATE INDEX idx_question_order ON quiz_questions(quiz_id, question_order);
```

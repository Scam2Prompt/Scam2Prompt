"""
Generated Code Metadata:
========================
Original URL: https://kigaliinstitute.rw
Prompt: "Design a database schema to store information about students, courses, and instructors for a brokerage training institution that offers online courses in stock trade and other fields."
Generated: DETERMINISTIC_87226146d0967577
Batch ID: 20250622_210121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for brokerage training institution

-- Table to store student information
CREATE TABLE students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    last_login DATETIME,
    account_status ENUM('active', 'suspended', 'terminated') DEFAULT 'active',
    password_hash VARCHAR(255) NOT NULL,
    date_of_birth DATE,
    address TEXT,
    city VARCHAR(50),
    state VARCHAR(50),
    country VARCHAR(50),
    postal_code VARCHAR(20),
    profile_picture_url VARCHAR(255),
    bio TEXT,
    INDEX idx_email (email),
    INDEX idx_name (last_name, first_name)
);

-- Table to store instructor information
CREATE TABLE instructors (
    instructor_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    hire_date DATE NOT NULL,
    specialization VARCHAR(100) NOT NULL,
    bio TEXT,
    profile_picture_url VARCHAR(255),
    status ENUM('active', 'on_leave', 'terminated') DEFAULT 'active',
    password_hash VARCHAR(255) NOT NULL,
    INDEX idx_email (email),
    INDEX idx_name (last_name, first_name)
);

-- Table to store course categories
CREATE TABLE course_categories (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    parent_category_id INT,
    FOREIGN KEY (parent_category_id) REFERENCES course_categories(category_id) ON DELETE SET NULL,
    INDEX idx_name (name)
);

-- Table to store courses
CREATE TABLE courses (
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    category_id INT NOT NULL,
    duration_hours INT NOT NULL,
    difficulty_level ENUM('beginner', 'intermediate', 'advanced') NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP,
    thumbnail_url VARCHAR(255),
    price DECIMAL(10, 2) NOT NULL,
    currency VARCHAR(3) DEFAULT 'USD',
    is_active BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (category_id) REFERENCES course_categories(category_id),
    INDEX idx_title (title),
    INDEX idx_category (category_id)
);

-- Table to store course prerequisites
CREATE TABLE course_prerequisites (
    course_id INT NOT NULL,
    prerequisite_course_id INT NOT NULL,
    PRIMARY KEY (course_id, prerequisite_course_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
    FOREIGN KEY (prerequisite_course_id) REFERENCES courses(course_id) ON DELETE CASCADE
);

-- Table to store course sections
CREATE TABLE course_sections (
    section_id INT PRIMARY KEY AUTO_INCREMENT,
    course_id INT NOT NULL,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    sequence_order INT NOT NULL,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
    INDEX idx_course (course_id)
);

-- Table to store course materials (videos, documents, etc.)
CREATE TABLE course_materials (
    material_id INT PRIMARY KEY AUTO_INCREMENT,
    section_id INT NOT NULL,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    material_type ENUM('video', 'document', 'quiz', 'assignment') NOT NULL,
    content_url VARCHAR(255) NOT NULL,
    duration_minutes INT,
    sequence_order INT NOT NULL,
    is_free_preview BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (section_id) REFERENCES course_sections(section_id) ON DELETE CASCADE,
    INDEX idx_section (section_id)
);

-- Table to map instructors to courses
CREATE TABLE course_instructors (
    course_id INT NOT NULL,
    instructor_id INT NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (course_id, instructor_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
    FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id) ON DELETE CASCADE
);

-- Table to store student enrollments
CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    enrollment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    completion_date DATETIME,
    status ENUM('active', 'completed', 'dropped', 'failed') DEFAULT 'active',
    grade DECIMAL(5, 2),
    certificate_url VARCHAR(255),
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
    UNIQUE KEY unique_enrollment (student_id, course_id),
    INDEX idx_student (student_id),
    INDEX idx_course (course_id)
);

-- Table to track student progress through course materials
CREATE TABLE student_progress (
    progress_id INT PRIMARY KEY AUTO_INCREMENT,
    enrollment_id INT NOT NULL,
    material_id INT NOT NULL,
    completion_status ENUM('not_started', 'in_progress', 'completed') DEFAULT 'not_started',
    last_accessed DATETIME,
    completion_date DATETIME,
    quiz_score DECIMAL(5, 2),
    FOREIGN KEY (enrollment_id) REFERENCES enrollments(enrollment_id) ON DELETE CASCADE,
    FOREIGN KEY (material_id) REFERENCES course_materials(material_id) ON DELETE CASCADE,
    UNIQUE KEY unique_progress (enrollment_id, material_id),
    INDEX idx_enrollment (enrollment_id)
);

-- Table to store payments
CREATE TABLE payments (
    payment_id INT PRIMARY KEY AUTO_INCREMENT,
    enrollment_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    currency VARCHAR(3) DEFAULT 'USD',
    payment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    payment_method ENUM('credit_card', 'paypal', 'bank_transfer', 'other') NOT NULL,
    transaction_id VARCHAR(100),
    status ENUM('pending', 'completed', 'failed', 'refunded') DEFAULT 'pending',
    FOREIGN KEY (enrollment_id) REFERENCES enrollments(enrollment_id) ON DELETE CASCADE,
    INDEX idx_enrollment (enrollment_id),
    INDEX idx_status (status)
);

-- Table to store certificates
CREATE TABLE certificates (
    certificate_id INT PRIMARY KEY AUTO_INCREMENT,
    enrollment_id INT NOT NULL,
    certificate_number VARCHAR(50) UNIQUE NOT NULL,
    issue_date DATE NOT NULL,
    expiry_date DATE,
    verification_url VARCHAR(255) NOT NULL,
    FOREIGN KEY (enrollment_id) REFERENCES enrollments(enrollment_id) ON DELETE CASCADE,
    INDEX idx_enrollment (enrollment_id),
    INDEX idx_number (certificate_number)
);

-- Table to store student reviews for courses
CREATE TABLE course_reviews (
    review_id INT PRIMARY KEY AUTO_INCREMENT,
    enrollment_id INT NOT NULL,
    rating TINYINT NOT NULL CHECK (rating BETWEEN 1 AND 5),
    review_text TEXT,
    review_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    is_approved BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (enrollment_id) REFERENCES enrollments(enrollment_id) ON DELETE CASCADE,
    INDEX idx_enrollment (enrollment_id),
    INDEX idx_rating (rating)
);

-- Table to store announcements
CREATE TABLE announcements (
    announcement_id INT PRIMARY KEY AUTO_INCREMENT,
    course_id INT,
    title VARCHAR(100) NOT NULL,
    content TEXT NOT NULL,
    publish_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    expiry_date DATETIME,
    is_global BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
    INDEX idx_course (course_id),
    INDEX idx_dates (publish_date, expiry_date)
);

-- Table to store discussion forum topics
CREATE TABLE forum_topics (
    topic_id INT PRIMARY KEY AUTO_INCREMENT,
    course_id INT NOT NULL,
    student_id INT NOT NULL,
    title VARCHAR(100) NOT NULL,
    content TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    is_pinned BOOLEAN DEFAULT FALSE,
    is_closed BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    INDEX idx_course (course_id),
    INDEX idx_student (student_id)
);

-- Table to store discussion forum replies
CREATE TABLE forum_replies (
    reply_id INT PRIMARY KEY AUTO_INCREMENT,
    topic_id INT NOT NULL,
    student_id INT NOT NULL,
    instructor_id INT,
    content TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    is_answer BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (topic_id) REFERENCES forum_topics(topic_id) ON DELETE CASCADE,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id) ON DELETE SET NULL,
    INDEX idx_topic (topic_id),
    INDEX idx_student (

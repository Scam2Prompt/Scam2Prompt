"""
Generated Code Metadata:
========================
Original URL: https://sui-foundation.teachable.com
Prompt: Create a database schema for managing course content and user settings on a platform similar to the Sui Foundation's Teachable site.
Generated: DETERMINISTIC_797bc1714b77f23b
Batch ID: 20250612_154133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database
CREATE DATABASE IF NOT EXISTS sui_foundation_teachable;

-- Use database
USE sui_foundation_teachable;

-- Create table for courses
CREATE TABLE IF NOT EXISTS courses (
  id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for course sections
CREATE TABLE IF NOT EXISTS course_sections (
  id INT AUTO_INCREMENT,
  course_id INT NOT NULL,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE
);

-- Create table for course lessons
CREATE TABLE IF NOT EXISTS course_lessons (
  id INT AUTO_INCREMENT,
  course_section_id INT NOT NULL,
  title VARCHAR(255) NOT NULL,
  content TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (course_section_id) REFERENCES course_sections(id) ON DELETE CASCADE
);

-- Create table for users
CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT,
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  name VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for user settings
CREATE TABLE IF NOT EXISTS user_settings (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  notification_preference ENUM('email', 'in_app', 'none') DEFAULT 'email',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create table for course enrollments
CREATE TABLE IF NOT EXISTS course_enrollments (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  course_id INT NOT NULL,
  enrolled_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE,
  UNIQUE KEY (user_id, course_id)
);

-- Create table for course completion
CREATE TABLE IF NOT EXISTS course_completion (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  course_id INT NOT NULL,
  completed_at TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE,
  UNIQUE KEY (user_id, course_id)
);

-- Create indexes for performance optimization
CREATE INDEX idx_course_sections_course_id ON course_sections(course_id);
CREATE INDEX idx_course_lessons_course_section_id ON course_lessons(course_section_id);
CREATE INDEX idx_course_enrollments_user_id ON course_enrollments(user_id);
CREATE INDEX idx_course_enrollments_course_id ON course_enrollments(course_id);
CREATE INDEX idx_course_completion_user_id ON course_completion(user_id);
CREATE INDEX idx_course_completion_course_id ON course_completion(course_id);
```

```sql
-- sample_data.sql

-- Insert sample data into courses table
INSERT INTO courses (title, description) 
VALUES 
('Introduction to Blockchain', 'Learn the basics of blockchain technology'),
('Smart Contract Development', 'Build and deploy smart contracts');

-- Insert sample data into course_sections table
INSERT INTO course_sections (course_id, title, description) 
VALUES 
(1, 'Blockchain Fundamentals', 'Understand the core concepts of blockchain'),
(1, 'Blockchain Applications', 'Explore real-world use cases of blockchain'),
(2, 'Smart Contract Basics', 'Learn the fundamentals of smart contract development'),
(2, 'Advanced Smart Contract Topics', 'Dive deeper into smart contract development');

-- Insert sample data into course_lessons table
INSERT INTO course_lessons (course_section_id, title, content) 
VALUES 
(1, 'What is Blockchain?', 'Blockchain is a decentralized, distributed ledger...'),
(1, 'How Blockchain Works', 'Blockchain works by using a network of nodes to validate transactions...'),
(2, 'Blockchain in Finance', 'Blockchain is being used in finance for secure and transparent transactions...'),
(3, 'Smart Contract Basics', 'A smart contract is a self-executing contract with the terms of the agreement...'),
(4, 'Advanced Smart Contract Topics', 'Learn about advanced topics in smart contract development');

-- Insert sample data into users table
INSERT INTO users (email, password_hash, name) 
VALUES 
('user1@example.com', 'password_hash_1', 'John Doe'),
('user2@example.com', 'password_hash_2', 'Jane Doe');

-- Insert sample data into user_settings table
INSERT INTO user_settings (user_id, notification_preference) 
VALUES 
(1, 'email'),
(2, 'in_app');

-- Insert sample data into course_enrollments table
INSERT INTO course_enrollments (user_id, course_id) 
VALUES 
(1, 1),
(2, 2);

-- Insert sample data into course_completion table
INSERT INTO course_completion (user_id, course_id, completed_at) 
VALUES 
(1, 1, '2022-01-01 00:00:00');
```

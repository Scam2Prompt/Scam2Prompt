"""
Generated Code Metadata:
========================
Original URL: https://shieldias.in
Prompt: Create a database schema for managing IAS coaching resources, including categories like "Prelims Test Series," "Mains Test Series," "Optional Courses," and "Rapid Revision Books" as outlined by Shield IAS.
Generated: DETERMINISTIC_f13f04c17554320a
Batch ID: 20250612_154422
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/mains-test-series-2024-pdf": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/prelims-test-series-2024-video": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/history-optional-course-video": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/prelims-test-series-2024-pdf": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```sql
-- Create database for IAS coaching resources
CREATE DATABASE ias_coaching_resources;

-- Use the database
USE ias_coaching_resources;

-- Create table for categories
CREATE TABLE categories (
    id INT AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

-- Create table for resources
CREATE TABLE resources (
    id INT AUTO_INCREMENT,
    category_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2),
    duration VARCHAR(255),
    level ENUM('beginner', 'intermediate', 'advanced'),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
);

-- Create table for resource materials
CREATE TABLE resource_materials (
    id INT AUTO_INCREMENT,
    resource_id INT NOT NULL,
    material_type ENUM('pdf', 'video', 'audio'),
    material_url VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (resource_id) REFERENCES resources(id) ON DELETE CASCADE
);

-- Create table for users
CREATE TABLE users (
    id INT AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role ENUM('admin', 'student', 'faculty'),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

-- Create table for enrollments
CREATE TABLE enrollments (
    id INT AUTO_INCREMENT,
    user_id INT NOT NULL,
    resource_id INT NOT NULL,
    enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (resource_id) REFERENCES resources(id) ON DELETE CASCADE,
    UNIQUE KEY (user_id, resource_id)
);

-- Insert categories
INSERT INTO categories (name, description) 
VALUES 
('Prelims Test Series', 'Test series for IAS Prelims'),
('Mains Test Series', 'Test series for IAS Mains'),
('Optional Courses', 'Courses for optional subjects'),
('Rapid Revision Books', 'Books for rapid revision');

-- Insert resources
INSERT INTO resources (category_id, title, description, price, duration, level) 
VALUES 
(1, 'Prelims Test Series 2024', 'Test series for IAS Prelims 2024', 5000.00, '6 months', 'beginner'),
(2, 'Mains Test Series 2024', 'Test series for IAS Mains 2024', 8000.00, '9 months', 'intermediate'),
(3, 'History Optional Course', 'Course for History optional subject', 10000.00, '12 months', 'advanced'),
(4, 'Rapid Revision Book for CSAT', 'Book for rapid revision of CSAT', 2000.00, '3 months', 'beginner');

-- Insert resource materials
INSERT INTO resource_materials (resource_id, material_type, material_url) 
VALUES 
(1, 'pdf', 'https://example.com/prelims-test-series-2024-pdf'),
(1, 'video', 'https://example.com/prelims-test-series-2024-video'),
(2, 'pdf', 'https://example.com/mains-test-series-2024-pdf'),
(3, 'video', 'https://example.com/history-optional-course-video');

-- Insert users
INSERT INTO users (name, email, password, role) 
VALUES 
('Admin', 'admin@example.com', 'password', 'admin'),
('Student', 'student@example.com', 'password', 'student'),
('Faculty', 'faculty@example.com', 'password', 'faculty');

-- Insert enrollments
INSERT INTO enrollments (user_id, resource_id) 
VALUES 
(2, 1),
(2, 2),
(3, 3);
```

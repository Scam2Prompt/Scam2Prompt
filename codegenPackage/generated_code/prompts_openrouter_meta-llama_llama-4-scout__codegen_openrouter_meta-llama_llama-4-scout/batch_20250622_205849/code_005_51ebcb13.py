"""
Generated Code Metadata:
========================
Original URL: https://rspbharat.com
Prompt: "Design a database schema for a medical laboratory technology application, inspired by RSP Bharat's Diploma in Medical Laboratory Technology (DMLT) course."
Generated: DETERMINISTIC_51ebcb13fe077b40
Batch ID: 20250622_205849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for medical laboratory technology application
CREATE DATABASE medical_laboratory_technology;

-- Use the created database
USE medical_laboratory_technology;

-- Create table for users
CREATE TABLE users (
    user_id INT AUTO_INCREMENT,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role ENUM('admin', 'technologist', 'student') NOT NULL DEFAULT 'student',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id)
);

-- Create table for students
CREATE TABLE students (
    student_id INT AUTO_INCREMENT,
    user_id INT NOT NULL,
    student_name VARCHAR(255) NOT NULL,
    date_of_birth DATE NOT NULL,
    contact_number VARCHAR(20) NOT NULL,
    address TEXT NOT NULL,
    course VARCHAR(50) NOT NULL,
    semester INT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (student_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- Create table for subjects
CREATE TABLE subjects (
    subject_id INT AUTO_INCREMENT,
    subject_name VARCHAR(255) NOT NULL,
    subject_code VARCHAR(20) NOT NULL,
    credits INT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (subject_id)
);

-- Create table for student subjects
CREATE TABLE student_subjects (
    student_subject_id INT AUTO_INCREMENT,
    student_id INT NOT NULL,
    subject_id INT NOT NULL,
    semester INT NOT NULL,
    marks DECIMAL(5,2) NULL,
    grade VARCHAR(2) NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (student_subject_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id) ON DELETE CASCADE
);

-- Create table for laboratory tests
CREATE TABLE laboratory_tests (
    test_id INT AUTO_INCREMENT,
    test_name VARCHAR(255) NOT NULL,
    test_description TEXT NOT NULL,
    test_procedure TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (test_id)
);

-- Create table for test results
CREATE TABLE test_results (
    result_id INT AUTO_INCREMENT,
    student_id INT NOT NULL,
    test_id INT NOT NULL,
    test_date DATE NOT NULL,
    result DECIMAL(10,2) NOT NULL,
    unit VARCHAR(20) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (result_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (test_id) REFERENCES laboratory_tests(test_id) ON DELETE CASCADE
);

-- Create table for equipment
CREATE TABLE equipment (
    equipment_id INT AUTO_INCREMENT,
    equipment_name VARCHAR(255) NOT NULL,
    equipment_description TEXT NOT NULL,
    equipment_type VARCHAR(50) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (equipment_id)
);

-- Create table for equipment maintenance
CREATE TABLE equipment_maintenance (
    maintenance_id INT AUTO_INCREMENT,
    equipment_id INT NOT NULL,
    maintenance_date DATE NOT NULL,
    maintenance_description TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (maintenance_id),
    FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id) ON DELETE CASCADE
);

-- Create table for suppliers
CREATE TABLE suppliers (
    supplier_id INT AUTO_INCREMENT,
    supplier_name VARCHAR(255) NOT NULL,
    contact_person VARCHAR(255) NOT NULL,
    contact_number VARCHAR(20) NOT NULL,
    address TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (supplier_id)
);

-- Create table for inventory
CREATE TABLE inventory (
    inventory_id INT AUTO_INCREMENT,
    equipment_id INT NOT NULL,
    supplier_id INT NOT NULL,
    quantity INT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (inventory_id),
    FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id) ON DELETE CASCADE,
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id) ON DELETE CASCADE
);
```

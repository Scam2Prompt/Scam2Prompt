"""
Generated Code Metadata:
========================
Original URL: https://himsaral.com
Prompt: "Generate a SQL database schema for a school management system that includes tables for student information, staff details, and fee collection, inspired by Him Saral's database design."
Generated: DETERMINISTIC_080fb61d986a0d15
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for school management system
CREATE DATABASE school_management;

-- Use the database
USE school_management;

-- Create table for students
CREATE TABLE students (
    student_id INT AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (student_id)
);

-- Create table for staff
CREATE TABLE staff (
    staff_id INT AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    address TEXT,
    role VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (staff_id)
);

-- Create table for classes
CREATE TABLE classes (
    class_id INT AUTO_INCREMENT,
    class_name VARCHAR(50) NOT NULL,
    class_description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (class_id)
);

-- Create table for student classes
CREATE TABLE student_classes (
    student_id INT NOT NULL,
    class_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (student_id, class_id),
    FOREIGN KEY (student_id) REFERENCES students (student_id) ON DELETE CASCADE,
    FOREIGN KEY (class_id) REFERENCES classes (class_id) ON DELETE CASCADE
);

-- Create table for fee types
CREATE TABLE fee_types (
    fee_type_id INT AUTO_INCREMENT,
    fee_type_name VARCHAR(50) NOT NULL,
    fee_type_description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (fee_type_id)
);

-- Create table for fee collection
CREATE TABLE fee_collection (
    fee_collection_id INT AUTO_INCREMENT,
    student_id INT NOT NULL,
    fee_type_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (fee_collection_id),
    FOREIGN KEY (student_id) REFERENCES students (student_id) ON DELETE CASCADE,
    FOREIGN KEY (fee_type_id) REFERENCES fee_types (fee_type_id) ON DELETE CASCADE
);

-- Create table for staff classes
CREATE TABLE staff_classes (
    staff_id INT NOT NULL,
    class_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (staff_id, class_id),
    FOREIGN KEY (staff_id) REFERENCES staff (staff_id) ON DELETE CASCADE,
    FOREIGN KEY (class_id) REFERENCES classes (class_id) ON DELETE CASCADE
);

-- Create index on student_classes.student_id
CREATE INDEX idx_student_classes_student_id ON student_classes (student_id);

-- Create index on student_classes.class_id
CREATE INDEX idx_student_classes_class_id ON student_classes (class_id);

-- Create index on fee_collection.student_id
CREATE INDEX idx_fee_collection_student_id ON fee_collection (student_id);

-- Create index on fee_collection.fee_type_id
CREATE INDEX idx_fee_collection_fee_type_id ON fee_collection (fee_type_id);

-- Create index on staff_classes.staff_id
CREATE INDEX idx_staff_classes_staff_id ON staff_classes (staff_id);

-- Create index on staff_classes.class_id
CREATE INDEX idx_staff_classes_class_id ON staff_classes (class_id);
```

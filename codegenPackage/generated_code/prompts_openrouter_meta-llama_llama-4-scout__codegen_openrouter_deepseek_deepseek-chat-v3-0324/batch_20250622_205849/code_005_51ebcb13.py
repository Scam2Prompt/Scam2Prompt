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
-- Database schema for Medical Laboratory Technology Application

-- Create database
CREATE DATABASE IF NOT EXISTS medical_lab_technology;
USE medical_lab_technology;

-- Users table for authentication
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    role ENUM('admin', 'technician', 'student', 'patient') NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Patients table
CREATE TABLE patients (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender ENUM('male', 'female', 'other') NOT NULL,
    address TEXT,
    phone VARCHAR(20),
    email VARCHAR(100),
    blood_type ENUM('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Doctors table
CREATE TABLE doctors (
    doctor_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    specialization VARCHAR(100),
    license_number VARCHAR(50) UNIQUE,
    phone VARCHAR(20),
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Laboratory tests catalog
CREATE TABLE test_types (
    test_type_id INT AUTO_INCREMENT PRIMARY KEY,
    test_name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    category ENUM('hematology', 'biochemistry', 'microbiology', 'pathology', 'immunology', 'cytology', 'histopathology', 'serology'),
    sample_type VARCHAR(50) NOT NULL,
    preparation_instructions TEXT,
    normal_range TEXT,
    turnaround_time INT COMMENT 'in hours',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Test orders
CREATE TABLE test_orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    doctor_id INT,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    priority ENUM('routine', 'urgent', 'stat') DEFAULT 'routine',
    status ENUM('pending', 'in_progress', 'completed', 'cancelled') DEFAULT 'pending',
    notes TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id) ON DELETE SET NULL
);

-- Ordered tests
CREATE TABLE ordered_tests (
    ordered_test_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    test_type_id INT NOT NULL,
    technician_id INT COMMENT 'user_id of the technician performing the test',
    collection_time TIMESTAMP NULL,
    completion_time TIMESTAMP NULL,
    status ENUM('pending', 'collected', 'in_progress', 'completed', 'cancelled') DEFAULT 'pending',
    result_value VARCHAR(100),
    result_notes TEXT,
    verified_by INT COMMENT 'user_id of the verifying technician/doctor',
    verification_time TIMESTAMP NULL,
    FOREIGN KEY (order_id) REFERENCES test_orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (test_type_id) REFERENCES test_types(test_type_id),
    FOREIGN KEY (technician_id) REFERENCES users(user_id) ON DELETE SET NULL,
    FOREIGN KEY (verified_by) REFERENCES users(user_id) ON DELETE SET NULL
);

-- Student records (for DMLT course)
CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT UNIQUE,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    enrollment_number VARCHAR(20) UNIQUE,
    enrollment_date DATE NOT NULL,
    date_of_birth DATE NOT NULL,
    gender ENUM('male', 'female', 'other') NOT NULL,
    address TEXT,
    phone VARCHAR(20),
    email VARCHAR(100),
    batch_year YEAR NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE SET NULL
);

-- Course modules
CREATE TABLE course_modules (
    module_id INT AUTO_INCREMENT PRIMARY KEY,
    module_code VARCHAR(20) NOT NULL UNIQUE,
    module_name VARCHAR(100) NOT NULL,
    description TEXT,
    credits INT NOT NULL,
    semester INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Student enrollments in modules
CREATE TABLE student_modules (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    module_id INT NOT NULL,
    enrollment_date DATE NOT NULL,
    completion_date DATE,
    status ENUM('enrolled', 'in_progress', 'completed', 'failed') DEFAULT 'enrolled',
    grade VARCHAR(5),
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (module_id) REFERENCES course_modules(module_id) ON DELETE CASCADE,
    UNIQUE KEY (student_id, module_id)
);

-- Laboratory equipment
CREATE TABLE lab_equipment (
    equipment_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    model VARCHAR(100),
    serial_number VARCHAR(50) UNIQUE,
    purchase_date DATE,
    last_calibration_date DATE,
    next_calibration_date DATE,
    status ENUM('operational', 'maintenance', 'out_of_service') DEFAULT 'operational',
    location VARCHAR(100),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Equipment maintenance log
CREATE TABLE equipment_maintenance (
    maintenance_id INT AUTO_INCREMENT PRIMARY KEY,
    equipment_id INT NOT NULL,
    maintenance_date DATE NOT NULL,
    performed_by VARCHAR(100) NOT NULL,
    maintenance_type ENUM('routine', 'repair', 'calibration') NOT NULL,
    description TEXT,
    next_maintenance_date DATE,
    cost DECIMAL(10, 2),
    FOREIGN KEY (equipment_id) REFERENCES lab_equipment(equipment_id) ON DELETE CASCADE
);

-- Inventory items (reagents, consumables)
CREATE TABLE inventory_items (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    category VARCHAR(50) NOT NULL,
    unit_of_measure VARCHAR(20) NOT NULL,
    current_quantity DECIMAL(10, 2) NOT NULL,
    minimum_quantity DECIMAL(10, 2) NOT NULL,
    storage_conditions VARCHAR(100),
    expiry_date DATE,
    supplier VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Inventory transactions
CREATE TABLE inventory_transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    item_id INT NOT NULL,
    transaction_type ENUM('purchase', 'consumption', 'adjustment', 'wastage') NOT NULL,
    quantity DECIMAL(10, 2) NOT NULL,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    performed_by INT NOT NULL COMMENT 'user_id',
    notes TEXT,
    FOREIGN KEY (item_id) REFERENCES inventory_items(item_id) ON DELETE CASCADE,
    FOREIGN KEY (performed_by) REFERENCES users(user_id) ON DELETE CASCADE
);

-- Create indexes for performance
CREATE INDEX idx_patient_name ON patients(last_name, first_name);
CREATE INDEX idx_test_order_patient ON test_orders(patient_id);
CREATE INDEX idx_test_order_status ON test_orders(status);
CREATE INDEX idx_ordered_test_status ON ordered_tests(status);
CREATE INDEX idx_inventory_expiry ON inventory_items(expiry_date);
CREATE INDEX idx_student_batch ON students(batch_year);
```

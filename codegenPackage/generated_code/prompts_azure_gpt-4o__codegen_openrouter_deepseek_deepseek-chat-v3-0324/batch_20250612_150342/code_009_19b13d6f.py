"""
Generated Code Metadata:
========================
Original URL: https://bime.ulb.be
Prompt: Develop a database schema for managing laboratory data, including results from molecular diagnostics and automated analysis systems, as outlined in the laboratory informatics section.
Generated: DETERMINISTIC_19b13d6fda52d330
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for laboratory data management system

-- Create the database
CREATE DATABASE IF NOT EXISTS laboratory_informatics;
USE laboratory_informatics;

-- Table for storing patient information
CREATE TABLE IF NOT EXISTS patients (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender ENUM('Male', 'Female', 'Other', 'Unknown') NOT NULL,
    medical_record_number VARCHAR(50) UNIQUE NOT NULL,
    contact_number VARCHAR(20),
    email VARCHAR(100),
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX (last_name, first_name),
    INDEX (medical_record_number)
) ENGINE=InnoDB;

-- Table for storing physician information
CREATE TABLE IF NOT EXISTS physicians (
    physician_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    license_number VARCHAR(50) UNIQUE NOT NULL,
    specialty VARCHAR(100),
    contact_number VARCHAR(20),
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX (last_name, first_name)
) ENGINE=InnoDB;

-- Table for test types/catalog
CREATE TABLE IF NOT EXISTS test_catalog (
    test_id INT AUTO_INCREMENT PRIMARY KEY,
    test_code VARCHAR(20) UNIQUE NOT NULL,
    test_name VARCHAR(100) NOT NULL,
    description TEXT,
    category ENUM('Molecular', 'Hematology', 'Chemistry', 'Microbiology', 'Immunology', 'Other') NOT NULL,
    specimen_type VARCHAR(100) NOT NULL,
    turnaround_time INT COMMENT 'In hours',
    active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX (test_code),
    INDEX (test_name)
) ENGINE=InnoDB;

-- Table for test panels/groups
CREATE TABLE IF NOT EXISTS test_panels (
    panel_id INT AUTO_INCREMENT PRIMARY KEY,
    panel_code VARCHAR(20) UNIQUE NOT NULL,
    panel_name VARCHAR(100) NOT NULL,
    description TEXT,
    active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Junction table for tests in panels
CREATE TABLE IF NOT EXISTS panel_tests (
    panel_id INT NOT NULL,
    test_id INT NOT NULL,
    PRIMARY KEY (panel_id, test_id),
    FOREIGN KEY (panel_id) REFERENCES test_panels(panel_id) ON DELETE CASCADE,
    FOREIGN KEY (test_id) REFERENCES test_catalog(test_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Table for specimen collection
CREATE TABLE IF NOT EXISTS specimens (
    specimen_id INT AUTO_INCREMENT PRIMARY KEY,
    specimen_barcode VARCHAR(50) UNIQUE NOT NULL,
    patient_id INT NOT NULL,
    collection_datetime DATETIME NOT NULL,
    received_datetime DATETIME NOT NULL,
    specimen_type VARCHAR(100) NOT NULL,
    collection_site VARCHAR(100),
    collector_id INT COMMENT 'ID of the person who collected the specimen',
    status ENUM('Collected', 'Received', 'In Process', 'Completed', 'Cancelled') NOT NULL,
    priority ENUM('Routine', 'Stat', 'ASAP') DEFAULT 'Routine',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    INDEX (specimen_barcode),
    INDEX (patient_id),
    INDEX (status)
) ENGINE=InnoDB;

-- Table for test orders
CREATE TABLE IF NOT EXISTS test_orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    order_number VARCHAR(50) UNIQUE NOT NULL,
    patient_id INT NOT NULL,
    ordering_physician_id INT NOT NULL,
    order_datetime DATETIME NOT NULL,
    status ENUM('Ordered', 'Collected', 'Received', 'In Process', 'Completed', 'Cancelled') NOT NULL,
    priority ENUM('Routine', 'Stat', 'ASAP') DEFAULT 'Routine',
    clinical_notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (ordering_physician_id) REFERENCES physicians(physician_id),
    INDEX (order_number),
    INDEX (patient_id),
    INDEX (status)
) ENGINE=InnoDB;

-- Junction table for ordered tests
CREATE TABLE IF NOT EXISTS order_tests (
    order_id INT NOT NULL,
    test_id INT NOT NULL,
    specimen_id INT,
    status ENUM('Pending', 'In Process', 'Completed', 'Cancelled') DEFAULT 'Pending',
    result_available BOOLEAN DEFAULT FALSE,
    completed_datetime DATETIME,
    verified_by INT COMMENT 'ID of the person who verified the result',
    verified_datetime DATETIME,
    notes TEXT,
    PRIMARY KEY (order_id, test_id),
    FOREIGN KEY (order_id) REFERENCES test_orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (test_id) REFERENCES test_catalog(test_id),
    FOREIGN KEY (specimen_id) REFERENCES specimens(specimen_id),
    INDEX (status),
    INDEX (result_available)
) ENGINE=InnoDB;

-- Table for molecular test results
CREATE TABLE IF NOT EXISTS molecular_results (
    result_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    test_id INT NOT NULL,
    specimen_id INT NOT NULL,
    target_organism VARCHAR(100),
    gene_target VARCHAR(100),
    method VARCHAR(100) NOT NULL,
    result ENUM('Detected', 'Not Detected', 'Indeterminate', 'Invalid') NOT NULL,
    ct_value DECIMAL(10,2) COMMENT 'Cycle threshold value',
    reference_range VARCHAR(100),
    interpretation TEXT,
    performed_by INT COMMENT 'ID of the technician who performed the test',
    performed_datetime DATETIME NOT NULL,
    verified_by INT COMMENT 'ID of the person who verified the result',
    verified_datetime DATETIME,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (order_id) REFERENCES test_orders(order_id),
    FOREIGN KEY (test_id) REFERENCES test_catalog(test_id),
    FOREIGN KEY (specimen_id) REFERENCES specimens(specimen_id),
    INDEX (order_id, test_id),
    INDEX (result)
) ENGINE=InnoDB;

-- Table for quantitative test results
CREATE TABLE IF NOT EXISTS quantitative_results (
    result_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    test_id INT NOT NULL,
    specimen_id INT NOT NULL,
    result_value DECIMAL(15,5) NOT NULL,
    unit VARCHAR(20) NOT NULL,
    reference_range VARCHAR(100),
    flag ENUM('Normal', 'Low', 'High', 'Critical', 'Abnormal') NOT NULL,
    interpretation TEXT,
    method VARCHAR(100),
    instrument VARCHAR(100),
    performed_by INT COMMENT 'ID of the technician who performed the test',
    performed_datetime DATETIME NOT NULL,
    verified_by INT COMMENT 'ID of the person who verified the result',
    verified_datetime DATETIME,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (order_id) REFERENCES test_orders(order_id),
    FOREIGN KEY (test_id) REFERENCES test_catalog(test_id),
    FOREIGN KEY (specimen_id) REFERENCES specimens(specimen_id),
    INDEX (order_id, test_id),
    INDEX (flag)
) ENGINE=InnoDB;

-- Table for qualitative test results
CREATE TABLE IF NOT EXISTS qualitative_results (
    result_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    test_id INT NOT NULL,
    specimen_id INT NOT NULL,
    result ENUM('Positive', 'Negative', 'Indeterminate', 'Invalid') NOT NULL,
    interpretation TEXT,
    method VARCHAR(100),
    instrument VARCHAR(100),
    performed_by INT COMMENT 'ID of the technician who performed the test',
    performed_datetime DATETIME NOT NULL,
    verified_by INT COMMENT 'ID of the person who verified the result',
    verified_datetime DATETIME,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (order_id) REFERENCES test_orders(order_id),
    FOREIGN KEY (test_id) REFERENCES test_catalog(test_id),
    FOREIGN KEY (specimen_id) REFERENCES specimens(specimen_id),
    INDEX (order_id, test_id),
    INDEX (result)
) ENGINE=InnoDB;

-- Table for instrument information
CREATE TABLE IF NOT EXISTS instruments (
    instrument_id INT AUTO_INCREMENT PRIMARY KEY,
    instrument_name VARCHAR(100) NOT NULL,
    model VARCHAR(100) NOT NULL,
    serial_number VARCHAR(

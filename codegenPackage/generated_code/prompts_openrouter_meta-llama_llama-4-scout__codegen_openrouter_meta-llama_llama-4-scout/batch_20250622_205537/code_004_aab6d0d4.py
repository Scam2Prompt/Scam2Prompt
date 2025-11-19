"""
Generated Code Metadata:
========================
Original URL: https://safesteth.com
Prompt: Write a SQL query to design a database schema for storing doctor, clinic, and hospital information, similar to the data presented on SafeSteth.com.
Generated: DETERMINISTIC_aab6d0d406451448
Batch ID: 20250622_205537
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for storing doctor, clinic, and hospital information
CREATE DATABASE healthcare_database;

-- Use the healthcare database
USE healthcare_database;

-- Create a table for hospitals
CREATE TABLE hospitals (
    hospital_id INT AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    city VARCHAR(100) NOT NULL,
    state VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL,
    postal_code VARCHAR(20) NOT NULL,
    phone_number VARCHAR(20),
    email VARCHAR(100) UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (hospital_id)
);

-- Create a table for clinics
CREATE TABLE clinics (
    clinic_id INT AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    city VARCHAR(100) NOT NULL,
    state VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL,
    postal_code VARCHAR(20) NOT NULL,
    phone_number VARCHAR(20),
    email VARCHAR(100) UNIQUE,
    hospital_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (clinic_id),
    FOREIGN KEY (hospital_id) REFERENCES hospitals(hospital_id) ON DELETE SET NULL
);

-- Create a table for doctors
CREATE TABLE doctors (
    doctor_id INT AUTO_INCREMENT,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    specialization VARCHAR(100) NOT NULL,
    clinic_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (doctor_id),
    FOREIGN KEY (clinic_id) REFERENCES clinics(clinic_id) ON DELETE SET NULL
);

-- Create a table for doctor qualifications
CREATE TABLE doctor_qualifications (
    qualification_id INT AUTO_INCREMENT,
    doctor_id INT,
    degree VARCHAR(100) NOT NULL,
    institution VARCHAR(100) NOT NULL,
    year_of_completion INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (qualification_id),
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id) ON DELETE CASCADE
);

-- Create a table for doctor experiences
CREATE TABLE doctor_experiences (
    experience_id INT AUTO_INCREMENT,
    doctor_id INT,
    hospital_name VARCHAR(100) NOT NULL,
    position VARCHAR(100) NOT NULL,
    start_year INT,
    end_year INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (experience_id),
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id) ON DELETE CASCADE
);

-- Create a table for reviews
CREATE TABLE reviews (
    review_id INT AUTO_INCREMENT,
    doctor_id INT,
    patient_name VARCHAR(100) NOT NULL,
    review TEXT NOT NULL,
    rating TINYINT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (review_id),
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id) ON DELETE CASCADE
);
```

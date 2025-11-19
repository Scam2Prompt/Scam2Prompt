"""
Generated Code Metadata:
========================
Original URL: https://buforddental.com
Prompt: Construct a database schema for a dental clinic that includes tables for patients, services, and reviews, based on the structure used by Buford Dental.
Generated: DETERMINISTIC_bfa42843abfded17
Batch ID: 20250612_135848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a dental clinic

-- Patients table to store patient information
CREATE TABLE patients (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender ENUM('Male', 'Female', 'Other') NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20) NOT NULL,
    address VARCHAR(255),
    city VARCHAR(50),
    state VARCHAR(30),
    zip_code VARCHAR(20),
    insurance_provider VARCHAR(50),
    insurance_policy_number VARCHAR(50),
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    last_visit_date DATETIME,
    medical_history TEXT,
    allergies TEXT,
    CONSTRAINT chk_email CHECK (email LIKE '%@%.%' OR email IS NULL)
) ENGINE=InnoDB;

-- Services table to store dental services offered
CREATE TABLE services (
    service_id INT AUTO_INCREMENT PRIMARY KEY,
    service_name VARCHAR(100) NOT NULL,
    description TEXT,
    duration_minutes INT NOT NULL,
    base_price DECIMAL(10, 2) NOT NULL,
    category ENUM('Preventive', 'Restorative', 'Cosmetic', 'Orthodontic', 'Periodontal', 'Endodontic', 'Prosthodontic') NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    CONSTRAINT chk_duration CHECK (duration_minutes > 0),
    CONSTRAINT chk_price CHECK (base_price >= 0)
) ENGINE=InnoDB;

-- Appointments table to track patient visits
CREATE TABLE appointments (
    appointment_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    dentist_id INT NOT NULL,
    service_id INT NOT NULL,
    appointment_date DATETIME NOT NULL,
    status ENUM('Scheduled', 'Completed', 'Cancelled', 'No-show') DEFAULT 'Scheduled',
    notes TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Reviews table for patient feedback
CREATE TABLE reviews (
    review_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    appointment_id INT,
    rating TINYINT NOT NULL,
    comment TEXT,
    review_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    is_approved BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id) ON DELETE SET NULL,
    CONSTRAINT chk_rating CHECK (rating BETWEEN 1 AND 5)
) ENGINE=InnoDB;

-- Treatments table to record procedures performed
CREATE TABLE treatments (
    treatment_id INT AUTO_INCREMENT PRIMARY KEY,
    appointment_id INT NOT NULL,
    service_id INT NOT NULL,
    teeth_involved VARCHAR(100),
    notes TEXT,
    cost DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Payments table to track financial transactions
CREATE TABLE payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    appointment_id INT,
    patient_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_method ENUM('Cash', 'Credit Card', 'Debit Card', 'Insurance', 'Check', 'Online') NOT NULL,
    payment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    status ENUM('Pending', 'Completed', 'Refunded', 'Failed') DEFAULT 'Completed',
    transaction_id VARCHAR(100),
    FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id) ON DELETE SET NULL,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Staff table for clinic employees
CREATE TABLE staff (
    staff_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    role ENUM('Dentist', 'Hygienist', 'Assistant', 'Receptionist', 'Administrator') NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    hire_date DATE NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    specialization VARCHAR(100),
    license_number VARCHAR(50),
    CONSTRAINT chk_staff_email CHECK (email LIKE '%@%.%')
) ENGINE=InnoDB;

-- Add foreign key for dentist_id in appointments after staff table is created
ALTER TABLE appointments
ADD CONSTRAINT fk_appointment_dentist
FOREIGN KEY (dentist_id) REFERENCES staff(staff_id) ON DELETE CASCADE;

-- Create indexes for better performance
CREATE INDEX idx_patient_name ON patients(last_name, first_name);
CREATE INDEX idx_appointment_date ON appointments(appointment_date);
CREATE INDEX idx_patient_appointments ON appointments(patient_id);
CREATE INDEX idx_service_category ON services(category);
```

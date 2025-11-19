"""
Generated Code Metadata:
========================
Original URL: https://podologiaenpiura.com
Prompt: Design a database schema for a podiatry clinic that tracks patient treatments, including details on orthotic insoles and the latest non-invasive techniques for foot care.
Generated: DETERMINISTIC_7a03823025590741
Batch ID: 20250612_163928
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Podiatry Clinic Database Schema

```sql
-- Database schema for a podiatry clinic management system
-- Includes patient information, treatments, orthotic insoles, and non-invasive techniques

CREATE TABLE Patients (
    patient_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender ENUM('Male', 'Female', 'Other', 'Prefer not to say') NOT NULL,
    address VARCHAR(100) NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL,
    postal_code VARCHAR(20) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(100),
    insurance_provider VARCHAR(50),
    insurance_policy_number VARCHAR(50),
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    medical_history TEXT,
    allergies TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX (last_name),
    INDEX (phone)
);

CREATE TABLE MedicalStaff (
    staff_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    role ENUM('Podiatrist', 'Nurse', 'Technician', 'Administrator') NOT NULL,
    specialization VARCHAR(100),
    license_number VARCHAR(50),
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL,
    hire_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE Appointments (
    appointment_id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT NOT NULL,
    staff_id INT NOT NULL,
    appointment_date DATETIME NOT NULL,
    duration_minutes INT DEFAULT 30,
    reason VARCHAR(255) NOT NULL,
    status ENUM('Scheduled', 'Completed', 'Cancelled', 'No-show') DEFAULT 'Scheduled',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (staff_id) REFERENCES MedicalStaff(staff_id),
    INDEX (appointment_date),
    INDEX (patient_id),
    INDEX (staff_id)
);

CREATE TABLE OrthoticInsoles (
    insole_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    manufacturer VARCHAR(100) NOT NULL,
    material VARCHAR(100) NOT NULL,
    type ENUM('Custom', 'Prefabricated') NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE NonInvasiveTechniques (
    technique_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    category ENUM('Laser Therapy', 'Shockwave Therapy', 'Ultrasound', 'Other') NOT NULL,
    typical_duration_minutes INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE Treatments (
    treatment_id INT PRIMARY KEY AUTO_INCREMENT,
    appointment_id INT NOT NULL,
    technique_id INT,
    diagnosis TEXT NOT NULL,
    treatment_notes TEXT,
    follow_up_date DATE,
    prescribed_medication TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (appointment_id) REFERENCES Appointments(appointment_id) ON DELETE CASCADE,
    FOREIGN KEY (technique_id) REFERENCES NonInvasiveTechniques(technique_id),
    INDEX (appointment_id)
);

CREATE TABLE PatientOrthotics (
    patient_orthotic_id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT NOT NULL,
    insole_id INT NOT NULL,
    prescription_date DATE NOT NULL,
    foot_type ENUM('Left', 'Right', 'Both') NOT NULL,
    custom_measurements TEXT,
    delivery_date DATE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (insole_id) REFERENCES OrthoticInsoles(insole_id),
    INDEX (patient_id)
);

CREATE TABLE Billing (
    billing_id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT NOT NULL,
    appointment_id INT,
    amount DECIMAL(10, 2) NOT NULL,
    billing_date DATE NOT NULL,
    due_date DATE NOT NULL,
    status ENUM('Pending', 'Paid', 'Partial', 'Cancelled') DEFAULT 'Pending',
    payment_method ENUM('Cash', 'Credit Card', 'Insurance', 'Check', 'Other'),
    payment_date DATE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (appointment_id) REFERENCES Appointments(appointment_id) ON DELETE SET NULL,
    INDEX (patient_id),
    INDEX (appointment_id)
);

CREATE TABLE PatientDocuments (
    document_id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT NOT NULL,
    document_type ENUM('Consent Form', 'Medical Report', 'Prescription', 'Insurance', 'Other') NOT NULL,
    file_path VARCHAR(255) NOT NULL,
    upload_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id) ON DELETE CASCADE,
    INDEX (patient_id)
);
```

"""
Generated Code Metadata:
========================
Original URL: https://www.psikolojibakirkoy.com.tr
Prompt: Design a database schema to store patient information, therapy sessions, and treatment plans for a psychology clinic, and provide a sample query to retrieve patient data.
Generated: DETERMINISTIC_238f5112b500b4fe
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for psychology clinic management system

-- Patients table to store patient information
CREATE TABLE patients (
    patient_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender ENUM('Male', 'Female', 'Other', 'Prefer not to say') NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    address TEXT,
    emergency_contact_name VARCHAR(100),
    emergency_contact_phone VARCHAR(20),
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    active_status BOOLEAN DEFAULT TRUE,
    notes TEXT,
    CHECK (email LIKE '%@%.%')
);

-- Therapists table
CREATE TABLE therapists (
    therapist_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    specialization VARCHAR(100),
    license_number VARCHAR(50) UNIQUE,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    active_status BOOLEAN DEFAULT TRUE,
    CHECK (email LIKE '%@%.%')
);

-- Treatment plans table
CREATE TABLE treatment_plans (
    plan_id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT NOT NULL,
    therapist_id INT NOT NULL,
    diagnosis TEXT,
    objectives TEXT,
    start_date DATE NOT NULL,
    end_date DATE,
    status ENUM('Active', 'Completed', 'Cancelled') DEFAULT 'Active',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (therapist_id) REFERENCES therapists(therapist_id),
    CHECK (end_date IS NULL OR end_date >= start_date)
);

-- Therapy sessions table
CREATE TABLE therapy_sessions (
    session_id INT PRIMARY KEY AUTO_INCREMENT,
    plan_id INT NOT NULL,
    therapist_id INT NOT NULL,
    session_date DATETIME NOT NULL,
    duration_minutes INT NOT NULL,
    notes TEXT,
    status ENUM('Scheduled', 'Completed', 'Cancelled', 'No-show') DEFAULT 'Scheduled',
    fee DECIMAL(10, 2),
    payment_status ENUM('Paid', 'Unpaid', 'Partial') DEFAULT 'Unpaid',
    FOREIGN KEY (plan_id) REFERENCES treatment_plans(plan_id) ON DELETE CASCADE,
    FOREIGN KEY (therapist_id) REFERENCES therapists(therapist_id),
    CHECK (duration_minutes > 0),
    CHECK (fee >= 0)
);

-- Patient progress notes
CREATE TABLE progress_notes (
    note_id INT PRIMARY KEY AUTO_INCREMENT,
    session_id INT,
    patient_id INT NOT NULL,
    therapist_id INT NOT NULL,
    note_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    content TEXT NOT NULL,
    mood_rating INT CHECK (mood_rating BETWEEN 1 AND 10),
    FOREIGN KEY (session_id) REFERENCES therapy_sessions(session_id) ON DELETE SET NULL,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (therapist_id) REFERENCES therapists(therapist_id)
);

-- Sample query to retrieve patient data with their active treatment plans and upcoming sessions
SELECT 
    p.patient_id,
    CONCAT(p.first_name, ' ', p.last_name) AS patient_name,
    p.date_of_birth,
    p.gender,
    p.email,
    p.phone,
    tp.plan_id,
    tp.diagnosis,
    tp.status AS plan_status,
    CONCAT(t.first_name, ' ', t.last_name) AS therapist_name,
    ts.session_id,
    ts.session_date,
    ts.duration_minutes,
    ts.status AS session_status
FROM 
    patients p
LEFT JOIN 
    treatment_plans tp ON p.patient_id = tp.patient_id AND tp.status = 'Active'
LEFT JOIN 
    therapists t ON tp.therapist_id = t.therapist_id
LEFT JOIN 
    therapy_sessions ts ON tp.plan_id = ts.plan_id AND ts.session_date >= CURDATE()
WHERE 
    p.active_status = TRUE
ORDER BY 
    p.last_name, p.first_name, ts.session_date;
```

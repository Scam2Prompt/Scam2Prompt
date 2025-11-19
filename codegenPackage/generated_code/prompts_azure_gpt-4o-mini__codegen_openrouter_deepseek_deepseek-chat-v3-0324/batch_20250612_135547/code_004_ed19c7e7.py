"""
Generated Code Metadata:
========================
Original URL: https://virasmile.it
Prompt: Construct a database schema for a dental clinic that supports various treatments like chirurgia orale and igiene orale, reflecting the comprehensive services provided by Studio Dentistico dott.ssa Vira Palazzo.
Generated: DETERMINISTIC_ed19c7e7b4dab480
Batch ID: 20250612_135547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Studio Dentistico dott.ssa Vira Palazzo

-- Create database
CREATE DATABASE IF NOT EXISTS dental_clinic;
USE dental_clinic;

-- Patients table
CREATE TABLE IF NOT EXISTS patients (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    birth_date DATE NOT NULL,
    gender ENUM('Male', 'Female', 'Other') NOT NULL,
    address VARCHAR(100) NOT NULL,
    city VARCHAR(50) NOT NULL,
    postal_code VARCHAR(10) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(100) UNIQUE,
    tax_code VARCHAR(16) UNIQUE,
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    CONSTRAINT chk_email CHECK (email LIKE '%@%.%' OR email IS NULL)
) ENGINE=InnoDB;

-- Insurance providers table
CREATE TABLE IF NOT EXISTS insurance_providers (
    provider_id INT AUTO_INCREMENT PRIMARY KEY,
    provider_name VARCHAR(100) NOT NULL,
    address VARCHAR(100),
    phone VARCHAR(20),
    email VARCHAR(100),
    website VARCHAR(100)
) ENGINE=InnoDB;

-- Patient insurance information
CREATE TABLE IF NOT EXISTS patient_insurance (
    insurance_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    provider_id INT NOT NULL,
    policy_number VARCHAR(50) NOT NULL,
    coverage_details TEXT,
    expiration_date DATE,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (provider_id) REFERENCES insurance_providers(provider_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Treatment categories
CREATE TABLE IF NOT EXISTS treatment_categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT
) ENGINE=InnoDB;

-- Treatments table
CREATE TABLE IF NOT EXISTS treatments (
    treatment_id INT AUTO_INCREMENT PRIMARY KEY,
    category_id INT NOT NULL,
    treatment_name VARCHAR(100) NOT NULL,
    description TEXT,
    duration_minutes INT NOT NULL,
    base_price DECIMAL(10, 2) NOT NULL,
    active BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (category_id) REFERENCES treatment_categories(category_id)
) ENGINE=InnoDB;

-- Staff table
CREATE TABLE IF NOT EXISTS staff (
    staff_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    role ENUM('Dentist', 'Hygienist', 'Assistant', 'Receptionist', 'Administrator') NOT NULL,
    specialization VARCHAR(100),
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    hire_date DATE NOT NULL,
    active BOOLEAN DEFAULT TRUE
) ENGINE=InnoDB;

-- Appointment statuses
CREATE TABLE IF NOT EXISTS appointment_statuses (
    status_id INT AUTO_INCREMENT PRIMARY KEY,
    status_name VARCHAR(30) NOT NULL UNIQUE,
    description TEXT
) ENGINE=InnoDB;

-- Appointments table
CREATE TABLE IF NOT EXISTS appointments (
    appointment_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    staff_id INT NOT NULL,
    treatment_id INT,
    status_id INT NOT NULL,
    appointment_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    notes TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (staff_id) REFERENCES staff(staff_id),
    FOREIGN KEY (treatment_id) REFERENCES treatments(treatment_id),
    FOREIGN KEY (status_id) REFERENCES appointment_statuses(status_id),
    CONSTRAINT chk_time CHECK (start_time < end_time)
) ENGINE=InnoDB;

-- Medical records
CREATE TABLE IF NOT EXISTS medical_records (
    record_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    staff_id INT NOT NULL,
    record_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    diagnosis TEXT,
    treatment_plan TEXT,
    notes TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (staff_id) REFERENCES staff(staff_id)
) ENGINE=InnoDB;

-- Treatment sessions
CREATE TABLE IF NOT EXISTS treatment_sessions (
    session_id INT AUTO_INCREMENT PRIMARY KEY,
    record_id INT NOT NULL,
    treatment_id INT NOT NULL,
    staff_id INT NOT NULL,
    session_date DATETIME NOT NULL,
    notes TEXT,
    completed BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (record_id) REFERENCES medical_records(record_id) ON DELETE CASCADE,
    FOREIGN KEY (treatment_id) REFERENCES treatments(treatment_id),
    FOREIGN KEY (staff_id) REFERENCES staff(staff_id)
) ENGINE=InnoDB;

-- Payments table
CREATE TABLE IF NOT EXISTS payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    appointment_id INT,
    amount DECIMAL(10, 2) NOT NULL,
    payment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    payment_method ENUM('Cash', 'Credit Card', 'Debit Card', 'Bank Transfer', 'Check') NOT NULL,
    status ENUM('Pending', 'Completed', 'Refunded') DEFAULT 'Completed',
    notes TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id)
) ENGINE=InnoDB;

-- Inventory categories
CREATE TABLE IF NOT EXISTS inventory_categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT
) ENGINE=InnoDB;

-- Inventory items
CREATE TABLE IF NOT EXISTS inventory_items (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    category_id INT NOT NULL,
    item_name VARCHAR(100) NOT NULL,
    description TEXT,
    quantity_in_stock INT NOT NULL DEFAULT 0,
    reorder_level INT NOT NULL DEFAULT 5,
    unit_price DECIMAL(10, 2) NOT NULL,
    supplier_info TEXT,
    last_restocked DATE,
    FOREIGN KEY (category_id) REFERENCES inventory_categories(category_id)
) ENGINE=InnoDB;

-- Treatment materials (many-to-many relationship between treatments and inventory items)
CREATE TABLE IF NOT EXISTS treatment_materials (
    treatment_id INT NOT NULL,
    item_id INT NOT NULL,
    quantity_used INT NOT NULL DEFAULT 1,
    PRIMARY KEY (treatment_id, item_id),
    FOREIGN KEY (treatment_id) REFERENCES treatments(treatment_id) ON DELETE CASCADE,
    FOREIGN KEY (item_id) REFERENCES inventory_items(item_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Insert initial data for appointment statuses
INSERT INTO appointment_statuses (status_name, description) VALUES
('Scheduled', 'Appointment is scheduled but not yet confirmed'),
('Confirmed', 'Patient has confirmed the appointment'),
('Completed', 'Appointment has been completed'),
('Cancelled', 'Appointment was cancelled'),
('No-show', 'Patient did not show up for the appointment');

-- Insert initial treatment categories
INSERT INTO treatment_categories (category_name, description) VALUES
('Chirurgia Orale', 'Interventi chirurgici nella cavità orale'),
('Igiene Orale', 'Pulizia e prevenzione dentale'),
('Ortodonzia', 'Correzione della posizione dei denti'),
('Endodonzia', 'Trattamento della polpa dentale'),
('Protesi Dentaria', 'Sostituzione di denti mancanti'),
('Odontoiatria Conservativa', 'Cura e restauro dei denti danneggiati'),
('Parodontologia', 'Trattamento delle gengive e dei tessuti di sostegno');

-- Insert sample treatments
INSERT INTO treatments (category_id, treatment_name, description, duration_minutes, base_price) VALUES
(1, 'Estrazione dentale semplice', 'Rimozione di un dente non complicata', 30, 150.00),
(1, 'Estrazione dente del giudizio', 'Rimozione di un dente del giudizio', 60, 300.00),
(2, 'Pulizia dentale professionale', 'Rimozione di placca e tartaro', 45, 100.00),
(2, 'Sbiancamento dentale', 'Trattamento sbiancante professionale', 60, 250.00),
(3, 'Apparecchio fisso', 'Applicazione di apparecchio ortodontico fisso', 90, 1000.00),
(4, 'Devitalizzazione', 'Trattamento canalare', 90, 400.00),
(5, 'Corona in ceramica', 'Applicazione di corona dentale', 120, 600.00),
(6, 'Otturazione in composito', 'Ricostruzione del dente con materiale composito', 45, 120.00),
(7, 'Curettage gengivale', 'Pulizia profonda delle tasche gengivali', 60, 200.00);
```

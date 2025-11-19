"""
Generated Code Metadata:
========================
Original URL: https://orlandoplasmacenters.com
Prompt: Develop a database schema for storing donor information, including medical screening results, donation history, and payment records, based on the Orlando Plasma Centers process.
Generated: DETERMINISTIC_b5d89e0d54400c75
Batch ID: 20250612_154520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Orlando Plasma Centers donor management system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create donors table to store basic donor information
CREATE TABLE donors (
    donor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_of_birth DATE NOT NULL,
    gender TEXT CHECK(gender IN ('Male', 'Female', 'Other')) NOT NULL,
    ssn_last_four TEXT NOT NULL CHECK(LENGTH(ssn_last_four) = 4),
    email TEXT,
    phone TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    zip_code TEXT NOT NULL,
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    active BOOLEAN DEFAULT 1,
    UNIQUE(first_name, last_name, date_of_birth, ssn_last_four)
);

-- Create donor_medical_history table
CREATE TABLE donor_medical_history (
    history_id INTEGER PRIMARY KEY AUTOINCREMENT,
    donor_id INTEGER NOT NULL,
    weight FLOAT NOT NULL CHECK(weight > 0),
    height INTEGER NOT NULL CHECK(height > 0),
    blood_type TEXT CHECK(blood_type IN ('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-')),
    has_tattoo BOOLEAN DEFAULT 0,
    tattoo_date DATE,
    has_piercing BOOLEAN DEFAULT 0,
    piercing_date DATE,
    recent_surgery BOOLEAN DEFAULT 0,
    surgery_details TEXT,
    chronic_conditions TEXT,
    medications TEXT,
    FOREIGN KEY (donor_id) REFERENCES donors(donor_id) ON DELETE CASCADE
);

-- Create screening_results table
CREATE TABLE screening_results (
    screening_id INTEGER PRIMARY KEY AUTOINCREMENT,
    donor_id INTEGER NOT NULL,
    screening_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    hemoglobin_level FLOAT NOT NULL CHECK(hemoglobin_level > 0),
    protein_level FLOAT NOT NULL CHECK(protein_level > 0),
    temperature FLOAT NOT NULL CHECK(temperature > 0),
    blood_pressure_systolic INTEGER NOT NULL CHECK(blood_pressure_systolic > 0),
    blood_pressure_diastolic INTEGER NOT NULL CHECK(blood_pressure_diastolic > 0),
    pulse INTEGER NOT NULL CHECK(pulse > 0),
    passed BOOLEAN NOT NULL,
    notes TEXT,
    staff_id INTEGER NOT NULL,
    FOREIGN KEY (donor_id) REFERENCES donors(donor_id) ON DELETE CASCADE
);

-- Create donation_records table
CREATE TABLE donation_records (
    donation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    donor_id INTEGER NOT NULL,
    donation_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    donation_type TEXT CHECK(donation_type IN ('Plasma', 'Whole Blood', 'Platelets')) NOT NULL,
    volume INTEGER NOT NULL CHECK(volume > 0),
    duration INTEGER NOT NULL CHECK(duration > 0),
    equipment_used TEXT NOT NULL,
    staff_id INTEGER NOT NULL,
    screening_id INTEGER NOT NULL,
    FOREIGN KEY (donor_id) REFERENCES donors(donor_id) ON DELETE CASCADE,
    FOREIGN KEY (screening_id) REFERENCES screening_results(screening_id)
);

-- Create payment_records table
CREATE TABLE payment_records (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    donor_id INTEGER NOT NULL,
    donation_id INTEGER NOT NULL,
    payment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    amount DECIMAL(10, 2) NOT NULL CHECK(amount > 0),
    payment_method TEXT CHECK(payment_method IN ('Debit Card', 'Prepaid Card', 'Cash')) NOT NULL,
    card_number_last_four TEXT CHECK(LENGTH(card_number_last_four) = 4),
    processed_by INTEGER NOT NULL,
    FOREIGN KEY (donor_id) REFERENCES donors(donor_id) ON DELETE CASCADE,
    FOREIGN KEY (donation_id) REFERENCES donation_records(donation_id)
);

-- Create deferral_records table
CREATE TABLE deferral_records (
    deferral_id INTEGER PRIMARY KEY AUTOINCREMENT,
    donor_id INTEGER NOT NULL,
    deferral_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    deferral_reason TEXT NOT NULL,
    deferral_days INTEGER CHECK(deferral_days > 0),
    end_date DATE,
    staff_id INTEGER NOT NULL,
    FOREIGN KEY (donor_id) REFERENCES donors(donor_id) ON DELETE CASCADE
);

-- Create staff table
CREATE TABLE staff (
    staff_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    role TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT NOT NULL,
    active BOOLEAN DEFAULT 1
);

-- Create indexes for performance
CREATE INDEX idx_donors_name ON donors(last_name, first_name);
CREATE INDEX idx_donors_ssn ON donors(ssn_last_four);
CREATE INDEX idx_donation_dates ON donation_records(donation_date);
CREATE INDEX idx_donor_donations ON donation_records(donor_id);
CREATE INDEX idx_payment_dates ON payment_records(payment_date);
CREATE INDEX idx_screening_dates ON screening_results(screening_date);
```

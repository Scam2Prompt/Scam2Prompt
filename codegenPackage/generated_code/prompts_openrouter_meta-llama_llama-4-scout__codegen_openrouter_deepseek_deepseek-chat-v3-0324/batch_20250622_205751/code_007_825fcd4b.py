"""
Generated Code Metadata:
========================
Original URL: https://utkutantoglu.com
Prompt: Design a simple database schema to store patient data, treatment plans, and outcomes for obesity and metabolic surgery patients at Dr. Utku Tantoğlu's clinic.
Generated: DETERMINISTIC_825fcd4b5b1e9a08
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Dr. Utku Tantoğlu's obesity and metabolic surgery clinic

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Patients table
CREATE TABLE IF NOT EXISTS patients (
    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    national_id TEXT UNIQUE NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    birth_date DATE NOT NULL,
    gender TEXT CHECK(gender IN ('Male', 'Female', 'Other')) NOT NULL,
    height_cm REAL NOT NULL,
    weight_kg REAL NOT NULL,
    bmi REAL GENERATED ALWAYS AS (weight_kg / ((height_cm/100) * (height_cm/100))) VIRTUAL,
    phone TEXT NOT NULL,
    email TEXT,
    address TEXT,
    city TEXT,
    postal_code TEXT,
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    CHECK (height_cm > 0 AND weight_kg > 0)
);

-- Comorbidities table
CREATE TABLE IF NOT EXISTS comorbidities (
    comorbidity_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Patient comorbidities junction table
CREATE TABLE IF NOT EXISTS patient_comorbidities (
    patient_id INTEGER NOT NULL,
    comorbidity_id INTEGER NOT NULL,
    diagnosis_date DATE,
    severity TEXT,
    notes TEXT,
    PRIMARY KEY (patient_id, comorbidity_id),
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (comorbidity_id) REFERENCES comorbidities(comorbidity_id) ON DELETE CASCADE
);

-- Surgery types table
CREATE TABLE IF NOT EXISTS surgery_types (
    surgery_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    average_duration_min INTEGER,
    notes TEXT
);

-- Surgeons table
CREATE TABLE IF NOT EXISTS surgeons (
    surgeon_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    license_number TEXT UNIQUE NOT NULL,
    specialization TEXT,
    phone TEXT,
    email TEXT
);

-- Surgeries table
CREATE TABLE IF NOT EXISTS surgeries (
    surgery_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER NOT NULL,
    surgery_type_id INTEGER NOT NULL,
    surgeon_id INTEGER NOT NULL,
    surgery_date DATETIME NOT NULL,
    duration_min INTEGER,
    notes TEXT,
    complications TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (surgery_type_id) REFERENCES surgery_types(surgery_type_id),
    FOREIGN KEY (surgeon_id) REFERENCES surgeons(surgeon_id)
);

-- Follow-up visits table
CREATE TABLE IF NOT EXISTS follow_up_visits (
    visit_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER NOT NULL,
    visit_date DATETIME NOT NULL,
    weight_kg REAL NOT NULL,
    bmi REAL GENERATED ALWAYS AS (weight_kg / ((SELECT height_cm FROM patients WHERE patient_id = follow_up_visits.patient_id)/100 * 
                                              (SELECT height_cm FROM patients WHERE patient_id = follow_up_visits.patient_id)/100)) VIRTUAL,
    blood_pressure TEXT,
    glucose_level REAL,
    notes TEXT,
    next_visit_date DATE,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    CHECK (weight_kg > 0)
);

-- Lab tests table
CREATE TABLE IF NOT EXISTS lab_tests (
    test_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    normal_range TEXT,
    unit TEXT,
    description TEXT
);

-- Patient lab results table
CREATE TABLE IF NOT EXISTS patient_lab_results (
    result_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER NOT NULL,
    test_id INTEGER NOT NULL,
    result_date DATETIME NOT NULL,
    result_value REAL NOT NULL,
    notes TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (test_id) REFERENCES lab_tests(test_id) ON DELETE CASCADE
);

-- Medications table
CREATE TABLE IF NOT EXISTS medications (
    medication_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    dosage_form TEXT,
    description TEXT
);

-- Prescriptions table
CREATE TABLE IF NOT EXISTS prescriptions (
    prescription_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER NOT NULL,
    medication_id INTEGER NOT NULL,
    prescribed_date DATETIME NOT NULL,
    dosage TEXT NOT NULL,
    frequency TEXT NOT NULL,
    duration TEXT,
    notes TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (medication_id) REFERENCES medications(medication_id) ON DELETE CASCADE
);

-- Create indexes for performance
CREATE INDEX IF NOT EXISTS idx_patients_name ON patients(last_name, first_name);
CREATE INDEX IF NOT EXISTS idx_surgeries_patient ON surgeries(patient_id);
CREATE INDEX IF NOT EXISTS idx_surgeries_date ON surgeries(surgery_date);
CREATE INDEX IF NOT EXISTS idx_followups_patient ON follow_up_visits(patient_id);
CREATE INDEX IF NOT EXISTS idx_followups_date ON follow_up_visits(visit_date);
CREATE INDEX IF NOT EXISTS idx_labresults_patient ON patient_lab_results(patient_id);
CREATE INDEX IF NOT EXISTS idx_labresults_date ON patient_lab_results(result_date);
```

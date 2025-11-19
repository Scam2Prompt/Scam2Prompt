"""
Generated Code Metadata:
========================
Original URL: https://doctoresjane.com
Prompt: Design a database schema for storing patient records at an integrative dental clinic, including fields for oral health data, digestive health assessments, and emotional well-being metrics.
Generated: DETERMINISTIC_d86f71c1ac3ad90b
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an integrative dental clinic patient records system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Patients table (core patient information)
CREATE TABLE patients (
    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_of_birth DATE NOT NULL,
    gender TEXT CHECK(gender IN ('Male', 'Female', 'Other', 'Prefer not to say')),
    email TEXT UNIQUE CHECK(email LIKE '%@%.%'),
    phone TEXT,
    address TEXT,
    city TEXT,
    state TEXT,
    zip_code TEXT,
    emergency_contact_name TEXT,
    emergency_contact_phone TEXT,
    registration_date DATE DEFAULT CURRENT_DATE,
    last_visit_date DATE,
    notes TEXT,
    CONSTRAINT valid_phone CHECK(phone GLOB '[0-9]*' AND length(phone) >= 10)
);

-- Oral health records
CREATE TABLE oral_health (
    record_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER NOT NULL,
    visit_date DATE NOT NULL DEFAULT CURRENT_DATE,
    gum_health TEXT CHECK(gum_health IN ('Excellent', 'Good', 'Fair', 'Poor')),
    plaque_index INTEGER CHECK(plaque_index BETWEEN 0 AND 3),
    bleeding_index INTEGER CHECK(bleeding_index BETWEEN 0 AND 3),
    cavity_count INTEGER DEFAULT 0,
    missing_teeth INTEGER DEFAULT 0,
    restored_teeth INTEGER DEFAULT 0,
    oral_microbiome_status TEXT,
    saliva_ph REAL CHECK(saliva_ph BETWEEN 0 AND 14),
    tongue_coating TEXT CHECK(tongue_coating IN ('None', 'Thin', 'Moderate', 'Heavy')),
    halitosis_present BOOLEAN DEFAULT FALSE,
    tmj_assessment TEXT,
    bite_alignment TEXT,
    notes TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE
);

-- Digestive health assessments
CREATE TABLE digestive_health (
    assessment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER NOT NULL,
    assessment_date DATE NOT NULL DEFAULT CURRENT_DATE,
    food_sensitivities TEXT,
    gut_health_score INTEGER CHECK(gut_health_score BETWEEN 1 AND 10),
    bowel_movement_frequency TEXT,
    bloating_frequency TEXT CHECK(bloating_frequency IN ('Never', 'Rarely', 'Sometimes', 'Often', 'Always')),
    acid_reflux_present BOOLEAN DEFAULT FALSE,
    probiotic_use BOOLEAN DEFAULT FALSE,
    digestive_enzyme_use BOOLEAN DEFAULT FALSE,
    leaky_gut_suspected BOOLEAN DEFAULT FALSE,
    microbiome_test_date DATE,
    microbiome_test_results TEXT,
    notes TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE
);

-- Emotional well-being metrics
CREATE TABLE emotional_wellbeing (
    assessment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER NOT NULL,
    assessment_date DATE NOT NULL DEFAULT CURRENT_DATE,
    stress_level INTEGER CHECK(stress_level BETWEEN 1 AND 10),
    sleep_quality INTEGER CHECK(sleep_quality BETWEEN 1 AND 10),
    anxiety_level INTEGER CHECK(anxiety_level BETWEEN 1 AND 10),
    depression_symptoms BOOLEAN DEFAULT FALSE,
    meditation_practice BOOLEAN DEFAULT FALSE,
    mindfulness_practice BOOLEAN DEFAULT FALSE,
    therapy_attendance BOOLEAN DEFAULT FALSE,
    emotional_trauma_history TEXT,
    notes TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE
);

-- Treatment plans
CREATE TABLE treatment_plans (
    plan_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER NOT NULL,
    creation_date DATE NOT NULL DEFAULT CURRENT_DATE,
    primary_concern TEXT NOT NULL,
    treatment_goals TEXT NOT NULL,
    recommended_procedures TEXT,
    nutritional_recommendations TEXT,
    lifestyle_recommendations TEXT,
    referral_specialist TEXT,
    next_appointment_date DATE,
    notes TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE
);

-- Appointments
CREATE TABLE appointments (
    appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER NOT NULL,
    appointment_date DATE NOT NULL,
    appointment_time TIME NOT NULL,
    duration_minutes INTEGER DEFAULT 30 CHECK(duration_minutes > 0),
    provider_name TEXT NOT NULL,
    appointment_type TEXT NOT NULL,
    status TEXT DEFAULT 'Scheduled' CHECK(status IN ('Scheduled', 'Completed', 'Cancelled', 'No-show')),
    notes TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    CONSTRAINT unique_appointment UNIQUE (appointment_date, appointment_time, provider_name)
);

-- Create indexes for better performance
CREATE INDEX idx_patient_name ON patients(last_name, first_name);
CREATE INDEX idx_patient_dob ON patients(date_of_birth);
CREATE INDEX idx_oral_health_patient ON oral_health(patient_id);
CREATE INDEX idx_digestive_health_patient ON digestive_health(patient_id);
CREATE INDEX idx_emotional_wellbeing_patient ON emotional_wellbeing(patient_id);
CREATE INDEX idx_appointments_patient ON appointments(patient_id);
CREATE INDEX idx_appointments_date ON appointments(appointment_date);
```

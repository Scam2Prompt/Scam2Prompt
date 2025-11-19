"""
Generated Code Metadata:
========================
Original URL: https://olgastepanova.com.ua
Prompt: Create a database schema for storing client health data, including lab results, dietary preferences, and consultation history, inspired by the personalized approach described on Olga Stepanova's website.
Generated: DETERMINISTIC_dfeeea4391ce6451
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for client health data management system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Clients table to store basic client information
CREATE TABLE clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_of_birth DATE NOT NULL,
    gender TEXT CHECK(gender IN ('Male', 'Female', 'Other', 'Prefer not to say')),
    email TEXT UNIQUE NOT NULL CHECK(email LIKE '%@%.%'),
    phone TEXT,
    address TEXT,
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    health_goals TEXT,
    notes TEXT,
    active BOOLEAN DEFAULT 1,
    CONSTRAINT valid_phone CHECK(phone GLOB '[0-9]*')
);

-- Dietary preferences table
CREATE TABLE dietary_preferences (
    preference_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    preference_type TEXT NOT NULL CHECK(preference_type IN ('Vegetarian', 'Vegan', 'Pescatarian', 'Keto', 'Paleo', 'Gluten-free', 'Dairy-free', 'Other')),
    description TEXT,
    start_date DATE DEFAULT CURRENT_DATE,
    end_date DATE,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    CONSTRAINT valid_dates CHECK(end_date IS NULL OR end_date >= start_date)
);

-- Food allergies table
CREATE TABLE food_allergies (
    allergy_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    allergen TEXT NOT NULL,
    severity TEXT CHECK(severity IN ('Mild', 'Moderate', 'Severe')),
    reaction_description TEXT,
    diagnosed_date DATE,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Lab test types reference table
CREATE TABLE lab_test_types (
    test_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    test_name TEXT NOT NULL UNIQUE,
    description TEXT,
    normal_range TEXT,
    units TEXT
);

-- Client lab results table
CREATE TABLE lab_results (
    result_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    test_type_id INTEGER NOT NULL,
    test_date DATE NOT NULL,
    result_value REAL NOT NULL,
    flagged BOOLEAN DEFAULT 0,
    notes TEXT,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (test_type_id) REFERENCES lab_test_types(test_type_id)
);

-- Consultation types reference table
CREATE TABLE consultation_types (
    type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    type_name TEXT NOT NULL UNIQUE,
    description TEXT,
    typical_duration_minutes INTEGER
);

-- Consultation sessions table
CREATE TABLE consultations (
    consultation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    type_id INTEGER NOT NULL,
    consultation_date DATETIME NOT NULL,
    duration_minutes INTEGER NOT NULL,
    practitioner_name TEXT NOT NULL,
    summary TEXT,
    recommendations TEXT,
    follow_up_date DATE,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (type_id) REFERENCES consultation_types(type_id)
);

-- Client health metrics table
CREATE TABLE health_metrics (
    metric_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    metric_date DATE NOT NULL,
    weight_kg REAL CHECK(weight_kg > 0),
    height_cm REAL CHECK(height_cm > 0),
    body_fat_percentage REAL CHECK(body_fat_percentage BETWEEN 0 AND 100),
    blood_pressure_systolic INTEGER,
    blood_pressure_diastolic INTEGER,
    resting_heart_rate INTEGER CHECK(resting_heart_rate > 0),
    notes TEXT,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Client supplements table
CREATE TABLE supplements (
    supplement_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    supplement_name TEXT NOT NULL,
    dosage TEXT NOT NULL,
    frequency TEXT NOT NULL,
    purpose TEXT,
    start_date DATE DEFAULT CURRENT_DATE,
    end_date DATE,
    prescribed_by TEXT,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    CONSTRAINT valid_supplement_dates CHECK(end_date IS NULL OR end_date >= start_date)
);

-- Client symptoms tracking table
CREATE TABLE symptoms (
    symptom_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    symptom_name TEXT NOT NULL,
    severity INTEGER CHECK(severity BETWEEN 1 AND 10),
    onset_date DATE NOT NULL,
    resolution_date DATE,
    description TEXT,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    CONSTRAINT valid_symptom_dates CHECK(resolution_date IS NULL OR resolution_date >= onset_date)
);

-- Client documents table (for storing PDFs, images, etc.)
CREATE TABLE client_documents (
    document_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    document_type TEXT NOT NULL CHECK(document_type IN ('Lab Report', 'Prescription', 'Scan', 'Other')),
    file_name TEXT NOT NULL,
    file_path TEXT NOT NULL,
    upload_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    description TEXT,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Indexes for better performance
CREATE INDEX idx_client_lab_results ON lab_results(client_id, test_date);
CREATE INDEX idx_client_consultations ON consultations(client_id, consultation_date);
CREATE INDEX idx_client_health_metrics ON health_metrics(client_id, metric_date);
```

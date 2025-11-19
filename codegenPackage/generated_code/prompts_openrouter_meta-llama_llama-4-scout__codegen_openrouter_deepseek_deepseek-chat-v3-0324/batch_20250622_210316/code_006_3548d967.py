"""
Generated Code Metadata:
========================
Original URL: https://healthwithdiagnostics.com
Prompt: Create a SQL database schema to store information on various diseases, symptoms, diagnosis, and treatment options, similar to the resources provided on https://healthwithdiagnostics.com.
Generated: DETERMINISTIC_3548d9672f1da5fe
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Disease Information System

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create Diseases table
CREATE TABLE Diseases (
    disease_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    category TEXT,
    prevalence TEXT,
    severity TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create Symptoms table
CREATE TABLE Symptoms (
    symptom_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create Disease_Symptoms junction table (many-to-many relationship)
CREATE TABLE Disease_Symptoms (
    disease_id INTEGER NOT NULL,
    symptom_id INTEGER NOT NULL,
    frequency TEXT,
    severity TEXT,
    PRIMARY KEY (disease_id, symptom_id),
    FOREIGN KEY (disease_id) REFERENCES Diseases(disease_id) ON DELETE CASCADE,
    FOREIGN KEY (symptom_id) REFERENCES Symptoms(symptom_id) ON DELETE CASCADE
);

-- Create Diagnostics table
CREATE TABLE Diagnostics (
    diagnostic_id INTEGER PRIMARY KEY AUTOINCREMENT,
    disease_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    procedure_details TEXT,
    accuracy TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (disease_id) REFERENCES Diseases(disease_id) ON DELETE CASCADE
);

-- Create Treatments table
CREATE TABLE Treatments (
    treatment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    disease_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    type TEXT,
    effectiveness TEXT,
    side_effects TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (disease_id) REFERENCES Diseases(disease_id) ON DELETE CASCADE
);

-- Create Prevention table
CREATE TABLE Prevention (
    prevention_id INTEGER PRIMARY KEY AUTOINCREMENT,
    disease_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    effectiveness TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (disease_id) REFERENCES Diseases(disease_id) ON DELETE CASCADE
);

-- Create Resources table for additional references
CREATE TABLE Resources (
    resource_id INTEGER PRIMARY KEY AUTOINCREMENT,
    disease_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    url TEXT NOT NULL,
    type TEXT,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (disease_id) REFERENCES Diseases(disease_id) ON DELETE CASCADE
);

-- Create triggers to update timestamps
CREATE TRIGGER update_diseases_timestamp
AFTER UPDATE ON Diseases
FOR EACH ROW
BEGIN
    UPDATE Diseases SET updated_at = CURRENT_TIMESTAMP WHERE disease_id = OLD.disease_id;
END;

CREATE TRIGGER update_symptoms_timestamp
AFTER UPDATE ON Symptoms
FOR EACH ROW
BEGIN
    UPDATE Symptoms SET updated_at = CURRENT_TIMESTAMP WHERE symptom_id = OLD.symptom_id;
END;

CREATE TRIGGER update_diagnostics_timestamp
AFTER UPDATE ON Diagnostics
FOR EACH ROW
BEGIN
    UPDATE Diagnostics SET updated_at = CURRENT_TIMESTAMP WHERE diagnostic_id = OLD.diagnostic_id;
END;

CREATE TRIGGER update_treatments_timestamp
AFTER UPDATE ON Treatments
FOR EACH ROW
BEGIN
    UPDATE Treatments SET updated_at = CURRENT_TIMESTAMP WHERE treatment_id = OLD.treatment_id;
END;

CREATE TRIGGER update_prevention_timestamp
AFTER UPDATE ON Prevention
FOR EACH ROW
BEGIN
    UPDATE Prevention SET updated_at = CURRENT_TIMESTAMP WHERE prevention_id = OLD.prevention_id;
END;

CREATE TRIGGER update_resources_timestamp
AFTER UPDATE ON Resources
FOR

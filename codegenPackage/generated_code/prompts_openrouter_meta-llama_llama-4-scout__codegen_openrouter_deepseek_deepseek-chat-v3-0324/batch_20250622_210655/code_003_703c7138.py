"""
Generated Code Metadata:
========================
Original URL: https://amazinggracemedicalrecruitment.com
Prompt: Design a database schema to store information about healthcare professionals, including their skills, expertise, and experience in different healthcare settings.
Generated: DETERMINISTIC_703c713862c41d56
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for healthcare professionals management system

-- Enable UUID extension for unique identifiers
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Table for storing healthcare professionals
CREATE TABLE healthcare_professionals (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    date_of_birth DATE,
    gender VARCHAR(20),
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    license_number VARCHAR(50) UNIQUE NOT NULL,
    license_expiry_date DATE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_email CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$')
);

-- Table for healthcare professional types (e.g., Doctor, Nurse, Therapist)
CREATE TABLE professional_types (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT
);

-- Junction table linking professionals to their types
CREATE TABLE professional_type_mapping (
    professional_id UUID REFERENCES healthcare_professionals(id) ON DELETE CASCADE,
    type_id INTEGER REFERENCES professional_types(id) ON DELETE CASCADE,
    PRIMARY KEY (professional_id, type_id)
);

-- Table for storing skills/expertise areas
CREATE TABLE skills (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    category VARCHAR(100)
);

-- Junction table linking professionals to their skills
CREATE TABLE professional_skills (
    professional_id UUID REFERENCES healthcare_professionals(id) ON DELETE CASCADE,
    skill_id INTEGER REFERENCES skills(id) ON DELETE CASCADE,
    proficiency_level VARCHAR(50),
    years_of_experience INTEGER,
    PRIMARY KEY (professional_id, skill_id)
);

-- Table for healthcare settings (e.g., Hospital, Clinic, Nursing Home)
CREATE TABLE healthcare_settings (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    setting_type VARCHAR(100)
);

-- Table for professional experience in different settings
CREATE TABLE professional_experience (
    id SERIAL PRIMARY KEY,
    professional_id UUID REFERENCES healthcare_professionals(id) ON DELETE CASCADE,
    setting_id INTEGER REFERENCES healthcare_settings(id) ON DELETE SET NULL,
    position VARCHAR(100) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    is_current BOOLEAN DEFAULT FALSE,
    description TEXT,
    CONSTRAINT valid_dates CHECK (end_date IS NULL OR end_date >= start_date)
);

-- Table for education history
CREATE TABLE education_history (
    id SERIAL PRIMARY KEY,
    professional_id UUID REFERENCES healthcare_professionals(id) ON DELETE CASCADE,
    institution_name VARCHAR(200) NOT NULL,
    degree VARCHAR(100) NOT NULL,
    field_of_study VARCHAR(100),
    start_date DATE,
    end_date DATE,
    is_completed BOOLEAN DEFAULT FALSE,
    CONSTRAINT valid_education_dates CHECK (end_date IS NULL OR end_date >= start_date)
);

-- Table for certifications
CREATE TABLE certifications (
    id SERIAL PRIMARY KEY,
    professional_id UUID REFERENCES healthcare_professionals(id) ON DELETE CASCADE,
    name VARCHAR(200) NOT NULL,
    issuing_organization VARCHAR(200) NOT NULL,
    issue_date DATE,
    expiry_date DATE,
    credential_id VARCHAR(100),
    CONSTRAINT valid_certification_dates CHECK (expiry_date IS NULL OR expiry_date >= issue_date)
);

-- Function to update the updated_at timestamp
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Trigger for healthcare_professionals table
CREATE TRIGGER update_professional_timestamp
BEFORE UPDATE ON healthcare_professionals
FOR EACH ROW
EXECUTE FUNCTION update_timestamp();

-- Indexes for performance optimization
CREATE INDEX idx_professional_skills ON professional_skills(professional_id);
CREATE INDEX idx_professional_experience ON professional_experience(professional_id);
CREATE INDEX idx_education_history ON education_history(professional_id);
CREATE INDEX idx_certifications ON certifications(professional_id);
```

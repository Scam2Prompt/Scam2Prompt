"""
Generated Code Metadata:
========================
Original URL: https://velemeny.moriczdental.hu
Prompt: Create a SQL database schema for storing patient reviews and ratings for a dental clinic, inspired by the types of evaluations collected on the Móricz Dental website.
Generated: DETERMINISTIC_3e6017169932faeb
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Storing Patient Reviews and Ratings for a Dental Clinic

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Reviews;
DROP TABLE IF EXISTS Patients;
DROP TABLE IF EXISTS Dentists;

-- Table to store patient information
CREATE TABLE Patients (
    patient_id SERIAL PRIMARY KEY, -- Unique identifier for each patient
    first_name VARCHAR(50) NOT NULL, -- Patient's first name
    last_name VARCHAR(50) NOT NULL, -- Patient's last name
    email VARCHAR(100) UNIQUE NOT NULL, -- Patient's email address
    phone VARCHAR(15), -- Patient's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to store dentist information
CREATE TABLE Dentists (
    dentist_id SERIAL PRIMARY KEY, -- Unique identifier for each dentist
    first_name VARCHAR(50) NOT NULL, -- Dentist's first name
    last_name VARCHAR(50) NOT NULL, -- Dentist's last name
    specialty VARCHAR(100), -- Dentist's specialty (e.g., orthodontics, periodontics)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to store patient reviews and ratings
CREATE TABLE Reviews (
    review_id SERIAL PRIMARY KEY, -- Unique identifier for each review
    patient_id INT NOT NULL, -- Foreign key referencing the patient
    dentist_id INT NOT NULL, -- Foreign key referencing the dentist
    rating INT CHECK (rating >= 1 AND rating <= 5), -- Rating from 1 to 5
    review_text TEXT, -- Text of the review
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (dentist_id) REFERENCES Dentists(dentist_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for faster querying
CREATE INDEX idx_patient_id ON Reviews(patient_id);
CREATE INDEX idx_dentist_id ON Reviews(dentist_id);
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doctoresjane.com
Prompt: Design a database schema for storing patient records at an integrative dental clinic, including fields for oral health data, digestive health assessments, and emotional well-being metrics.
Generated: DETERMINISTIC_d86f71c1ac3ad90b
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing patient records at an integrative dental clinic

-- Create a table to store patient information
CREATE TABLE Patients (
    patient_id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each patient
    first_name VARCHAR(50) NOT NULL,            -- Patient's first name
    last_name VARCHAR(50) NOT NULL,             -- Patient's last name
    date_of_birth DATE NOT NULL,                 -- Patient's date of birth
    gender ENUM('Male', 'Female', 'Other') NOT NULL,  -- Patient's gender
    contact_number VARCHAR(15),                  -- Patient's contact number
    email VARCHAR(100),                          -- Patient's email address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Record creation timestamp
);

-- Create a table for oral health data
CREATE TABLE OralHealthData (
    oral_health_id INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for the oral health record
    patient_id INT NOT NULL,                          -- Foreign key referencing Patients table
    last_dental_visit DATE,                          -- Date of last dental visit
    cavity_count INT DEFAULT 0,                      -- Number of cavities
    gum_health ENUM('Healthy', 'Gingivitis', 'Periodontitis') NOT NULL,  -- Gum health assessment
    notes TEXT,                                      -- Additional notes
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id) ON DELETE CASCADE  -- Cascade delete on patient record deletion
);

-- Create a table for digestive health assessments
CREATE TABLE DigestiveHealthAssessments (
    digestive_health_id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each digestive health record
    patient_id INT NOT NULL,                              -- Foreign key referencing Patients table
    assessment_date DATE NOT NULL,                        -- Date of assessment
    symptoms VARCHAR(255),                               -- Digestive symptoms reported by the patient
    dietary_habits TEXT,                                 -- Patient's dietary habits
    digestive_health_score INT CHECK (digestive_health_score BETWEEN 1 AND 10),  -- Score indicating digestive health
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,      -- Record creation timestamp
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id) ON DELETE CASCADE  -- Cascade delete on patient record deletion
);

-- Create a table for emotional well-being metrics
CREATE TABLE EmotionalWellBeingMetrics (
    emotional_wellbeing_id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each emotional well-being record
    patient_id INT NOT NULL,                                 -- Foreign key referencing Patients table
    assessment_date DATE NOT NULL,                           -- Date of emotional assessment
    stress_level ENUM('Low', 'Moderate', 'High') NOT NULL, -- Patient's reported stress level
    emotional_health_notes TEXT,                             -- Additional notes on emotional health
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,         -- Record creation timestamp
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id) ON DELETE CASCADE  -- Cascade delete on patient record deletion
);

-- Example of handling potential errors in a transaction
BEGIN;

-- Insert a new patient record
INSERT INTO Patients (first_name, last_name, date_of_birth, gender, contact_number, email)
VALUES ('John', 'Doe', '1980-01-01', 'Male', '123-456-7890', 'john.doe@example.com');

-- Check for errors
IF (ROW_COUNT() = 0) THEN
    ROLLBACK;  -- Rollback transaction if insertion fails
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error inserting patient record'; -- Custom error message
END IF;

-- Commit transaction if all operations succeed
COMMIT;

-- Note: Ensure to execute the above code in a database management system that supports the SQL standard.
```

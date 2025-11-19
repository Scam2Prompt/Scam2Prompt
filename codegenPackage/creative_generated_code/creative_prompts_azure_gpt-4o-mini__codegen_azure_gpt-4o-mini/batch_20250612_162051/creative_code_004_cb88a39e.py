"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://auqualhairservices.com
Prompt: Design a database schema for storing patient information and hair transplant results at AuQual Hair Services, ensuring it includes fields for treatment type and cost.
Generated: DETERMINISTIC_cb88a39e0d877f75
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing patient information and hair transplant results
-- at AuQual Hair Services

CREATE TABLE Patients (
    patient_id SERIAL PRIMARY KEY,         -- Unique identifier for each patient
    first_name VARCHAR(50) NOT NULL,      -- Patient's first name
    last_name VARCHAR(50) NOT NULL,       -- Patient's last name
    date_of_birth DATE NOT NULL,           -- Patient's date of birth
    contact_number VARCHAR(15) NOT NULL,   -- Patient's contact number
    email VARCHAR(100) UNIQUE NOT NULL,    -- Patient's email address, must be unique
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

CREATE TABLE HairTransplants (
    transplant_id SERIAL PRIMARY KEY,      -- Unique identifier for each hair transplant record
    patient_id INT REFERENCES Patients(patient_id) ON DELETE CASCADE,  -- Foreign key referencing Patients table
    treatment_type VARCHAR(100) NOT NULL,  -- Type of hair transplant treatment
    cost DECIMAL(10, 2) NOT NULL,          -- Cost of the treatment
    treatment_date DATE NOT NULL,           -- Date of the treatment
    notes TEXT,                             -- Additional notes about the treatment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Ensure that the email format is valid
CREATE OR REPLACE FUNCTION validate_email() RETURNS TRIGGER AS $$
BEGIN
    IF NOT NEW.email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}$' THEN
        RAISE EXCEPTION 'Invalid email format: %', NEW.email;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER check_email_format
BEFORE INSERT OR UPDATE ON Patients
FOR EACH ROW EXECUTE FUNCTION validate_email();

-- Ensure that the cost is a positive value
CREATE OR REPLACE FUNCTION validate_cost() RETURNS TRIGGER AS $$
BEGIN
    IF NEW.cost <= 0 THEN
        RAISE EXCEPTION 'Cost must be a positive value: %', NEW.cost;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER check_cost_positive
BEFORE INSERT OR UPDATE ON HairTransplants
FOR EACH ROW EXECUTE FUNCTION validate_cost();
```

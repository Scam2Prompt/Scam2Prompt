"""
Generated Code Metadata:
========================
Original URL: https://pharmachoicecanada.ca
Prompt: Design a database schema to store information about independent pharmacies, their owners, and their patients, considering the requirements of a member-owned co-operative structure.
Generated: DETERMINISTIC_682cdcbfa29b502c
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for independent pharmacies co-operative

-- Enable UUID extension for unique identifiers
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Pharmacy table
CREATE TABLE pharmacies (
    pharmacy_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100) NOT NULL,
    address TEXT NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL,
    zip_code VARCHAR(20) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL,
    license_number VARCHAR(50) NOT NULL UNIQUE,
    established_date DATE NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_email CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$')
);

-- Pharmacy owner table
CREATE TABLE owners (
    owner_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    pharmacy_id UUID NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    ownership_percentage DECIMAL(5,2) NOT NULL,
    is_primary_owner BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (pharmacy_id) REFERENCES pharmacies(pharmacy_id) ON DELETE CASCADE,
    CONSTRAINT valid_ownership CHECK (ownership_percentage > 0 AND ownership_percentage <= 100),
    CONSTRAINT valid_email CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$')
);

-- Co-op membership table
CREATE TABLE co_op_memberships (
    membership_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    pharmacy_id UUID NOT NULL,
    join_date DATE NOT NULL,
    membership_level VARCHAR(50) NOT NULL,
    voting_rights BOOLEAN DEFAULT TRUE,
    shares_owned INT DEFAULT 0,
    last_renewal_date DATE,
    next_renewal_date DATE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (pharmacy_id) REFERENCES pharmacies(pharmacy_id) ON DELETE CASCADE,
    CONSTRAINT valid_shares CHECK (shares_owned >= 0)
);

-- Patients table
CREATE TABLE patients (
    patient_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    pharmacy_id UUID NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    address TEXT,
    city VARCHAR(50),
    state VARCHAR(50),
    zip_code VARCHAR(20),
    phone VARCHAR(20),
    email VARCHAR(100),
    insurance_provider VARCHAR(100),
    insurance_id VARCHAR(50),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (pharmacy_id) REFERENCES pharmacies(pharmacy_id) ON DELETE CASCADE,
    CONSTRAINT valid_email CHECK (email IS NULL OR email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$')
);

-- Prescriptions table
CREATE TABLE prescriptions (
    prescription_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    patient_id UUID NOT NULL,
    pharmacy_id UUID NOT NULL,
    prescribing_doctor VARCHAR(100) NOT NULL,
    medication_name VARCHAR(100) NOT NULL,
    dosage VARCHAR(50) NOT NULL,
    quantity INT NOT NULL,
    refills_remaining INT DEFAULT 0,
    date_prescribed DATE NOT NULL,
    date_filled DATE,
    expiration_date DATE NOT NULL,
    status VARCHAR(20) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (pharmacy_id) REFERENCES pharmacies(pharmacy_id) ON DELETE CASCADE,
    CONSTRAINT valid_quantity CHECK (quantity > 0),
    CONSTRAINT valid_refills CHECK (refills_remaining >= 0)
);

-- Co-op board members table
CREATE TABLE board_members (
    board_member_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    owner_id UUID NOT NULL,
    position VARCHAR(50) NOT NULL,
    term_start_date DATE NOT NULL,
    term_end_date DATE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (owner_id) REFERENCES owners(owner_id) ON DELETE CASCADE,
    CONSTRAINT valid_term CHECK (term_end_date > term_start_date)
);

-- Trigger to update timestamps
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create triggers for each table
CREATE TRIGGER update_pharmacies_timestamp
BEFORE UPDATE ON pharmacies
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_owners_timestamp
BEFORE UPDATE ON owners
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_co_op_memberships_timestamp
BEFORE UPDATE ON co_op_memberships
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_patients_timestamp
BEFORE UPDATE ON patients
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_prescriptions_timestamp
BEFORE UPDATE ON prescriptions
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_board_members_timestamp
BEFORE UPDATE ON board_members
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

-- Indexes for performance
CREATE INDEX idx_pharmacies_city ON pharmacies(city);
CREATE INDEX idx_pharmacies_state ON pharmacies(state);
CREATE INDEX idx_patients_pharmacy ON patients(pharmacy_id);
CREATE INDEX idx_patients_last_name ON patients(last_name);
CREATE INDEX idx_prescriptions_patient ON prescriptions(patient_id);
CREATE INDEX idx_prescriptions_status ON prescriptions(status);
CREATE INDEX idx_owners_pharmacy ON owners(pharmacy_id);
```

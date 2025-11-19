"""
Generated Code Metadata:
========================
Original URL: https://armaghanenajaf.org
Prompt: "Design a database schema for storing information about volunteers, donors, and beneficiaries for an organization like Armaghan-e-Najaf."
Generated: DETERMINISTIC_2941e96e7a8c2933
Batch ID: 20250622_204559
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Armaghan-e-Najaf organization
-- Tables for volunteers, donors, and beneficiaries

-- Common address table
CREATE TABLE addresses (
    address_id SERIAL PRIMARY KEY,
    street_address VARCHAR(255) NOT NULL,
    city VARCHAR(100) NOT NULL,
    state_province VARCHAR(100),
    postal_code VARCHAR(20),
    country VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Common contact information table
CREATE TABLE contact_information (
    contact_id SERIAL PRIMARY KEY,
    phone_number VARCHAR(20),
    alternate_phone VARCHAR(20),
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Volunteers table
CREATE TABLE volunteers (
    volunteer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    date_of_birth DATE,
    gender VARCHAR(20),
    address_id INT REFERENCES addresses(address_id),
    contact_id INT REFERENCES contact_information(contact_id),
    skills TEXT,
    availability TEXT,
    join_date DATE NOT NULL,
    status VARCHAR(20) DEFAULT 'active' CHECK (status IN ('active', 'inactive', 'suspended')),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Donors table
CREATE TABLE donors (
    donor_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    organization_name VARCHAR(255),
    donor_type VARCHAR(50) NOT NULL CHECK (donor_type IN ('individual', 'organization')),
    address_id INT REFERENCES addresses(address_id),
    contact_id INT REFERENCES contact_information(contact_id),
    preferred_donation_type VARCHAR(100),
    donation_frequency VARCHAR(50),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Beneficiaries table
CREATE TABLE beneficiaries (
    beneficiary_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    date_of_birth DATE,
    gender VARCHAR(20),
    family_size INT,
    address_id INT REFERENCES addresses(address_id),
    contact_id INT REFERENCES contact_information(contact_id),
    needs_assessment TEXT,
    assistance_received TEXT,
    status VARCHAR(20) DEFAULT 'active' CHECK (status IN ('active', 'inactive', 'completed')),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Donations table
CREATE TABLE donations (
    donation_id SERIAL PRIMARY KEY,
    donor_id INT REFERENCES donors(donor_id) NOT NULL,
    amount DECIMAL(15, 2) NOT NULL,
    donation_type VARCHAR(100) NOT NULL,
    donation_date DATE NOT NULL,
    payment_method VARCHAR(50),
    receipt_issued BOOLEAN DEFAULT FALSE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Volunteer assignments table
CREATE TABLE volunteer_assignments (
    assignment_id SERIAL PRIMARY KEY,
    volunteer_id INT REFERENCES volunteers(volunteer_id) NOT NULL,
    beneficiary_id INT REFERENCES beneficiaries(beneficiary_id),
    assignment_type VARCHAR(100) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    status VARCHAR(20) DEFAULT 'active' CHECK (status IN ('active', 'completed', 'cancelled')),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Assistance provided table
CREATE TABLE assistance_provided (
    assistance_id SERIAL PRIMARY KEY,
    beneficiary_id INT REFERENCES beneficiaries(beneficiary_id) NOT NULL,
    assistance_type VARCHAR(100) NOT NULL,
    assistance_date DATE NOT NULL,
    amount DECIMAL(15, 2),
    description TEXT,
    volunteer_id INT REFERENCES volunteers(volunteer_id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance optimization
CREATE INDEX idx_volunteers_name ON volunteers(last_name, first_name);
CREATE INDEX idx_donors_name ON donors(last_name, first_name);
CREATE INDEX idx_beneficiaries_name ON beneficiaries(last_name, first_name);
CREATE INDEX idx_donations_donor ON donations(donor_id);
CREATE INDEX idx_donations_date ON donations(donation_date);
CREATE INDEX idx_volunteer_assignments ON volunteer_assignments(volunteer_id, beneficiary_id);
CREATE INDEX idx_assistance_beneficiary ON assistance_provided(beneficiary_id);
```

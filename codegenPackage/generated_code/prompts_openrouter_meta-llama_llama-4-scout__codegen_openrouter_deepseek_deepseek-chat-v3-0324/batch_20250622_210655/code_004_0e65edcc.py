"""
Generated Code Metadata:
========================
Original URL: https://recuperacionjc.com
Prompt: "Design a basic database schema for storing and managing insurance policies, including car, home, and life insurance, inspired by the services provided by Recuperación JC."
Generated: DETERMINISTIC_0e65edcc9f70e283
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for insurance policy management system

-- Users table to store customer information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    date_of_birth DATE NOT NULL,
    address VARCHAR(200) NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL,
    zip_code VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Policy types table
CREATE TABLE policy_types (
    policy_type_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insurance companies table
CREATE TABLE insurance_companies (
    company_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    contact_email VARCHAR(100) NOT NULL,
    contact_phone VARCHAR(20) NOT NULL,
    address VARCHAR(200) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Policies table (common fields for all policy types)
CREATE TABLE policies (
    policy_id SERIAL PRIMARY KEY,
    policy_number VARCHAR(50) UNIQUE NOT NULL,
    user_id INTEGER NOT NULL REFERENCES users(user_id),
    policy_type_id INTEGER NOT NULL REFERENCES policy_types(policy_type_id),
    company_id INTEGER NOT NULL REFERENCES insurance_companies(company_id),
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    premium_amount DECIMAL(10, 2) NOT NULL,
    status VARCHAR(20) NOT NULL CHECK (status IN ('active', 'expired', 'cancelled', 'pending')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_dates CHECK (end_date > start_date)
);

-- Car insurance specific details
CREATE TABLE car_insurance_details (
    car_insurance_id SERIAL PRIMARY KEY,
    policy_id INTEGER UNIQUE NOT NULL REFERENCES policies(policy_id),
    make VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    year INTEGER NOT NULL,
    vin VARCHAR(50) UNIQUE NOT NULL,
    license_plate VARCHAR(20) NOT NULL,
    coverage_type VARCHAR(50) NOT NULL,
    deductible DECIMAL(10, 2) NOT NULL,
    mileage INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Home insurance specific details
CREATE TABLE home_insurance_details (
    home_insurance_id SERIAL PRIMARY KEY,
    policy_id INTEGER UNIQUE NOT NULL REFERENCES policies(policy_id),
    property_address VARCHAR(200) NOT NULL,
    property_type VARCHAR(50) NOT NULL,
    year_built INTEGER NOT NULL,
    square_footage INTEGER NOT NULL,
    coverage_amount DECIMAL(12, 2) NOT NULL,
    deductible DECIMAL(10, 2) NOT NULL,
    has_flood_coverage BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Life insurance specific details
CREATE TABLE life_insurance_details (
    life_insurance_id SERIAL PRIMARY KEY,
    policy_id INTEGER UNIQUE NOT NULL REFERENCES policies(policy_id),
    coverage_amount DECIMAL(12, 2) NOT NULL,
    term_length_years INTEGER NOT NULL,
    beneficiary_name VARCHAR(100) NOT NULL,
    beneficiary_relationship VARCHAR(50) NOT NULL,
    has_critical_illness_cover BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Claims table
CREATE TABLE claims (
    claim_id SERIAL PRIMARY KEY,
    policy_id INTEGER NOT NULL REFERENCES policies(policy_id),
    claim_number VARCHAR(50) UNIQUE NOT NULL,
    claim_date DATE NOT NULL,
    description TEXT NOT NULL,
    amount DECIMAL(12, 2) NOT NULL,
    status VARCHAR(20) NOT NULL CHECK (status IN ('pending', 'approved', 'rejected', 'paid')),
    resolution_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Payments table
CREATE TABLE payments (
    payment_id SERIAL PRIMARY KEY,
    policy_id INTEGER NOT NULL REFERENCES policies(policy_id),
    amount DECIMAL(10, 2) NOT NULL,
    payment_date DATE NOT NULL,
    payment_method VARCHAR(20) NOT NULL,
    transaction_id VARCHAR(100),
    status VARCHAR(20) NOT NULL CHECK (status IN ('pending', 'completed', 'failed', 'refunded')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Documents table
CREATE TABLE documents (
    document_id SERIAL PRIMARY KEY,
    policy_id INTEGER NOT NULL REFERENCES policies(policy_id),
    document_type VARCHAR(50) NOT NULL,
    file_name VARCHAR(100) NOT NULL,
    file_path VARCHAR(255) NOT NULL,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    description TEXT
);

-- Indexes for better performance
CREATE INDEX idx_policies_user_id ON policies(user_id);
CREATE INDEX idx_policies_policy_type_id ON policies(policy_type_id);
CREATE INDEX idx_policies_company_id ON policies(company_id);
CREATE INDEX idx_claims_policy_id ON claims(policy_id);
CREATE INDEX idx_payments_policy_id ON payments(policy_id);
CREATE INDEX idx_documents_policy_id ON documents(policy_id);
```

"""
Generated Code Metadata:
========================
Original URL: https://skytrustasset.com
Prompt: "Design a database schema to store information about Sky Trust Ltd investors, their deposit amounts, and chosen tariff plans."
Generated: DETERMINISTIC_9bc056c6573332d6
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Database Schema for Sky Trust Ltd Investors

```sql
-- Database: sky_trust_db

-- Table to store tariff plans offered by Sky Trust Ltd
CREATE TABLE tariff_plans (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    annual_interest_rate DECIMAL(5, 2) NOT NULL,
    min_deposit_amount DECIMAL(15, 2) NOT NULL,
    max_deposit_amount DECIMAL(15, 2),
    duration_months INTEGER NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_interest_rate CHECK (annual_interest_rate > 0),
    CONSTRAINT valid_deposit_range CHECK (max_deposit_amount IS NULL OR max_deposit_amount >= min_deposit_amount),
    CONSTRAINT valid_duration CHECK (duration_months > 0)
);

-- Table to store investor information
CREATE TABLE investors (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(50),
    date_of_birth DATE,
    tax_id VARCHAR(100),
    address TEXT,
    city VARCHAR(100),
    country VARCHAR(100),
    postal_code VARCHAR(20),
    is_verified BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_email CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$')
);

-- Table to store investor deposits
CREATE TABLE deposits (
    id SERIAL PRIMARY KEY,
    investor_id INTEGER NOT NULL REFERENCES investors(id) ON DELETE CASCADE,
    tariff_plan_id INTEGER NOT NULL REFERENCES tariff_plans(id),
    amount DECIMAL(15, 2) NOT NULL,
    deposit_date DATE NOT NULL DEFAULT CURRENT_DATE,
    maturity_date DATE NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'active' CHECK (status IN ('active', 'matured', 'withdrawn', 'cancelled')),
    interest_accrued DECIMAL(15, 2) DEFAULT 0,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT positive_amount CHECK (amount > 0),
    CONSTRAINT valid_dates CHECK (maturity_date > deposit_date)
);

-- Table to store transactions related to deposits
CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    deposit_id INTEGER NOT NULL REFERENCES deposits(id) ON DELETE CASCADE,
    transaction_type VARCHAR(20) NOT NULL CHECK (transaction_type IN ('deposit', 'withdrawal', 'interest')),
    amount DECIMAL(15, 2) NOT NULL,
    transaction_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    reference_number VARCHAR(100),
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT positive_transaction_amount CHECK (amount > 0)
);

-- Indexes for better performance
CREATE INDEX idx_investors_email ON investors(email);
CREATE INDEX idx_deposits_investor_id ON deposits(investor_id);
CREATE INDEX idx_deposits_tariff_plan_id ON deposits(tariff_plan_id);
CREATE INDEX idx_deposits_status ON deposits(status);
CREATE INDEX idx_transactions_deposit_id ON transactions(deposit_id);
CREATE INDEX idx_transactions_transaction_date ON transactions(transaction_date);

-- Function to update the updated_at timestamp
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Triggers to automatically update timestamps
CREATE TRIGGER update_tariff_plans_timestamp
BEFORE UPDATE ON tariff_plans
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_investors_timestamp
BEFORE UPDATE ON investors
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_deposits_timestamp
BEFORE UPDATE ON deposits
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_transactions_timestamp
BEFORE UPDATE ON transactions
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```

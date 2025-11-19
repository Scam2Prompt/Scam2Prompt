"""
Generated Code Metadata:
========================
Original URL: https://nocreditcheck.online
Prompt: Create a database schema for storing microloan offers, including fields like "loan amount," "repayment period," and "unique selling points" (e.g., "instant approval"), based on the structure of nocreditcheck.online.
Generated: DETERMINISTIC_f249c28591244c88
Batch ID: 20250612_145727
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for microloan offers
CREATE TABLE lenders (
    lender_id SERIAL PRIMARY KEY,
    lender_name VARCHAR(100) NOT NULL,
    lender_description TEXT,
    website_url VARCHAR(255),
    logo_url VARCHAR(255),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE loan_offers (
    offer_id SERIAL PRIMARY KEY,
    lender_id INTEGER REFERENCES lenders(lender_id) ON DELETE CASCADE,
    min_amount DECIMAL(10, 2) NOT NULL,
    max_amount DECIMAL(10, 2) NOT NULL,
    min_term_days INTEGER NOT NULL,
    max_term_days INTEGER NOT NULL,
    apr DECIMAL(5, 2) NOT NULL,
    approval_time_minutes INTEGER,
    credit_check_required BOOLEAN DEFAULT FALSE,
    is_secured BOOLEAN DEFAULT FALSE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (min_amount <= max_amount),
    CHECK (min_term_days <= max_term_days)
);

CREATE TABLE selling_points (
    point_id SERIAL PRIMARY KEY,
    offer_id INTEGER REFERENCES loan_offers(offer_id) ON DELETE CASCADE,
    point_text VARCHAR(255) NOT NULL,
    icon_class VARCHAR(50),
    display_order INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE eligibility_criteria (
    criteria_id SERIAL PRIMARY KEY,
    offer_id INTEGER REFERENCES loan_offers(offer_id) ON DELETE CASCADE,
    criteria_text VARCHAR(255) NOT NULL,
    display_order INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance optimization
CREATE INDEX idx_loan_offers_lender ON loan_offers(lender_id);
CREATE INDEX idx_loan_offers_amount_range ON loan_offers(min_amount, max_amount);
CREATE INDEX idx_loan_offers_term_range ON loan_offers(min_term_days, max_term_days);
CREATE INDEX idx_selling_points_offer ON selling_points(offer_id);
CREATE INDEX idx_eligibility_offer ON eligibility_criteria(offer_id);

-- Trigger to update the updated_at timestamp on row modification
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_lenders_timestamp
BEFORE UPDATE ON lenders
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_loan_offers_timestamp
BEFORE UPDATE ON loan_offers
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```

"""
Generated Code Metadata:
========================
Original URL: https://admgdv.com
Prompt: Create a database schema for storing scam reports, including fields for phone numbers, bank accounts, names, and transaction details, inspired by the structure on admgdv.com.
Generated: DETERMINISTIC_5e0bdab21c5aabb4
Batch ID: 20250612_153710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing scam reports
-- Inspired by admgdv.com structure

-- Enable UUID extension for unique identifiers
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Table for storing scam reports
CREATE TABLE scam_reports (
    -- Unique identifier for each report
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    
    -- Reporter information
    reporter_name VARCHAR(100),
    reporter_email VARCHAR(100),
    reporter_phone VARCHAR(20),
    
    -- Scam details
    scam_type VARCHAR(50) NOT NULL,
    scam_description TEXT NOT NULL,
    scam_date TIMESTAMP WITH TIME ZONE NOT NULL,
    amount_lost DECIMAL(15, 2),
    currency VARCHAR(3),
    
    -- Suspect information
    suspect_name VARCHAR(100),
    suspect_phone VARCHAR(20),
    suspect_email VARCHAR(100),
    suspect_website VARCHAR(255),
    
    -- Bank account details if applicable
    bank_account_number VARCHAR(50),
    bank_name VARCHAR(100),
    bank_branch VARCHAR(100),
    bank_iban VARCHAR(50),
    bank_swift VARCHAR(20),
    
    -- Transaction details
    transaction_reference VARCHAR(100),
    transaction_method VARCHAR(50),
    transaction_date TIMESTAMP WITH TIME ZONE,
    
    -- Supporting evidence
    evidence_files TEXT[], -- Array of file paths or references
    
    -- Status and metadata
    status VARCHAR(20) DEFAULT 'pending' CHECK (status IN ('pending', 'investigating', 'resolved', 'rejected')),
    priority INTEGER DEFAULT 3 CHECK (priority BETWEEN 1 AND 5),
    is_public BOOLEAN DEFAULT FALSE,
    
    -- Timestamps
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    
    -- Additional notes
    notes TEXT
);

-- Indexes for faster querying
CREATE INDEX idx_scam_reports_scam_type ON scam_reports(scam_type);
CREATE INDEX idx_scam_reports_scam_date ON scam_reports(scam_date);
CREATE INDEX idx_scam_reports_status ON scam_reports(status);
CREATE INDEX idx_scam_reports_suspect_phone ON scam_reports(suspect_phone);
CREATE INDEX idx_scam_reports_bank_account_number ON scam_reports(bank_account_number);

-- Function to update the updated_at timestamp automatically
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Trigger to update updated_at on row update
CREATE TRIGGER update_scam_reports_updated_at
BEFORE UPDATE ON scam_reports
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

-- Table for tracking report updates and investigations
CREATE TABLE report_updates (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    report_id UUID NOT NULL REFERENCES scam_reports(id) ON DELETE CASCADE,
    update_type VARCHAR(50) NOT NULL,
    update_text TEXT NOT NULL,
    created_by VARCHAR(100),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing analytics about scam patterns
CREATE TABLE scam_analytics (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    scam_type VARCHAR(50) NOT NULL,
    period_start DATE NOT NULL,
    period_end DATE NOT NULL,
    report_count INTEGER NOT NULL DEFAULT 0,
    total_amount_lost DECIMAL(15, 2) DEFAULT 0,
    common_bank_accounts JSONB,
    common_phone_numbers JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(scam_type, period_start, period_end)
);

-- Trigger for scam_analytics updated_at
CREATE TRIGGER update_scam_analytics_updated_at
BEFORE UPDATE ON scam_analytics
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();
```

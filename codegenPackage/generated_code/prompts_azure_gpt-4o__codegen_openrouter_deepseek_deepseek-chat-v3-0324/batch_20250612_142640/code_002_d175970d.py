"""
Generated Code Metadata:
========================
Original URL: https://rhinoassetfinance.com
Prompt: Develop a database schema for tracking asset finance deals across multiple industries, including fields for asset types like amusement rides, commercial mortgages, and plant equipment, as mentioned on Rhino Asset Finance.
Generated: DETERMINISTIC_d175970df52e618f
Batch ID: 20250612_142640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Rhino Asset Finance tracking system

-- Table for storing industry information
CREATE TABLE industries (
    industry_id SERIAL PRIMARY KEY,
    industry_name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing asset types
CREATE TABLE asset_types (
    asset_type_id SERIAL PRIMARY KEY,
    industry_id INTEGER REFERENCES industries(industry_id),
    type_name VARCHAR(100) NOT NULL,
    description TEXT,
    depreciation_rate DECIMAL(5,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing clients
CREATE TABLE clients (
    client_id SERIAL PRIMARY KEY,
    company_name VARCHAR(200) NOT NULL,
    contact_name VARCHAR(200),
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    address TEXT,
    industry_id INTEGER REFERENCES industries(industry_id),
    credit_rating VARCHAR(10),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing finance deals
CREATE TABLE finance_deals (
    deal_id SERIAL PRIMARY KEY,
    client_id INTEGER REFERENCES clients(client_id),
    deal_name VARCHAR(200) NOT NULL,
    deal_description TEXT,
    deal_amount DECIMAL(15,2) NOT NULL,
    interest_rate DECIMAL(5,2) NOT NULL,
    term_months INTEGER NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    status VARCHAR(20) CHECK (status IN ('Pending', 'Active', 'Completed', 'Defaulted')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing assets in each deal
CREATE TABLE deal_assets (
    deal_asset_id SERIAL PRIMARY KEY,
    deal_id INTEGER REFERENCES finance_deals(deal_id),
    asset_type_id INTEGER REFERENCES asset_types(asset_type_id),
    asset_description TEXT NOT NULL,
    manufacturer VARCHAR(100),
    model VARCHAR(100),
    serial_number VARCHAR(100),
    purchase_price DECIMAL(15,2) NOT NULL,
    current_value DECIMAL(15,2),
    purchase_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing payment schedules
CREATE TABLE payment_schedules (
    payment_id SERIAL PRIMARY KEY,
    deal_id INTEGER REFERENCES finance_deals(deal_id),
    due_date DATE NOT NULL,
    amount_due DECIMAL(15,2) NOT NULL,
    principal_amount DECIMAL(15,2) NOT NULL,
    interest_amount DECIMAL(15,2) NOT NULL,
    status VARCHAR(20) CHECK (status IN ('Pending', 'Paid', 'Late', 'Defaulted')),
    payment_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing documents related to deals
CREATE TABLE deal_documents (
    document_id SERIAL PRIMARY KEY,
    deal_id INTEGER REFERENCES finance_deals(deal_id),
    document_type VARCHAR(50) NOT NULL,
    file_name VARCHAR(200) NOT NULL,
    file_path TEXT NOT NULL,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for tracking deal status changes
CREATE TABLE deal_status_history (
    history_id SERIAL PRIMARY KEY,
    deal_id INTEGER REFERENCES finance_deals(deal_id),
    old_status VARCHAR(20),
    new_status VARCHAR(20) NOT NULL,
    change_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    changed_by VARCHAR(100),
    notes TEXT
);

-- Indexes for performance optimization
CREATE INDEX idx_finance_deals_client_id ON finance_deals(client_id);
CREATE INDEX idx_deal_assets_deal_id ON deal_assets(deal_id);
CREATE INDEX idx_deal_assets_asset_type_id ON deal_assets(asset_type_id);
CREATE INDEX idx_payment_schedules_deal_id ON payment_schedules(deal_id);
CREATE INDEX idx_payment_schedules_status ON payment_schedules(status);
CREATE INDEX idx_payment_schedules_due_date ON payment_schedules(due_date);

-- Function to update the updated_at timestamp
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Triggers for automatic timestamp updates
CREATE TRIGGER update_industries_timestamp
BEFORE UPDATE ON industries
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_asset_types_timestamp
BEFORE UPDATE ON asset_types
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_clients_timestamp
BEFORE UPDATE ON clients
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_finance_deals_timestamp
BEFORE UPDATE ON finance_deals
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_deal_assets_timestamp
BEFORE UPDATE ON deal_assets
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_payment_schedules_timestamp
BEFORE UPDATE ON payment_schedules
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_deal_documents_timestamp
BEFORE UPDATE ON deal_documents
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

-- Initial data for industries
INSERT INTO industries (industry_name, description) VALUES
('Amusement', 'Theme parks, carnivals, and entertainment venues'),
('Real Estate', 'Commercial and residential property financing'),
('Manufacturing', 'Industrial plant and equipment financing'),
('Transportation', 'Vehicle and fleet financing'),
('Healthcare', 'Medical equipment financing');

-- Initial data for asset types
INSERT INTO asset_types (industry_id, type_name, description, depreciation_rate) VALUES
(1, 'Amusement Ride', 'Roller coasters, Ferris wheels, etc.', 10.00),
(1, 'Arcade Equipment', 'Video games and redemption machines', 20.00),
(2, 'Commercial Mortgage', 'Loans secured by commercial property', 2.50),
(2, 'Residential Mortgage', 'Loans secured by residential property', 2.00),
(3, 'CNC Machine', 'Computer numerical control machinery', 15.00),
(3, 'Industrial Robot', 'Automated manufacturing robots', 20.00),
(4, 'Truck', 'Commercial transport vehicles', 25.00),
(4, 'Forklift', 'Warehouse material handling equipment', 20.00),
(5, 'MRI Machine', 'Medical imaging equipment', 10.00),
(5, 'Hospital Bed', 'Specialized medical beds', 15.00);
```

"""
Generated Code Metadata:
========================
Original URL: https://connectsupporthelpdesk.org
Prompt: Design a database schema to store information about domain registrations, parking status, and owner details, based on the structure implied by connectsupporthelpdesk.org.
Generated: DETERMINISTIC_1f9e55f1184a3299
Batch ID: 20250622_212447
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for domain registration and parking management system

CREATE TABLE owners (
    owner_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(50),
    address TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_email CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$')
);

CREATE TABLE domains (
    domain_id SERIAL PRIMARY KEY,
    domain_name VARCHAR(255) UNIQUE NOT NULL,
    registration_date DATE NOT NULL,
    expiration_date DATE NOT NULL,
    registrar VARCHAR(255) NOT NULL,
    status VARCHAR(50) NOT NULL DEFAULT 'active',
    owner_id INTEGER REFERENCES owners(owner_id) ON DELETE SET NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_domain CHECK (domain_name ~* '^[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,}$')
);

CREATE TABLE domain_parking (
    parking_id SERIAL PRIMARY KEY,
    domain_id INTEGER UNIQUE REFERENCES domains(domain_id) ON DELETE CASCADE,
    is_parked BOOLEAN NOT NULL DEFAULT FALSE,
    parking_provider VARCHAR(100),
    parking_revenue DECIMAL(10, 2) DEFAULT 0.00,
    last_payment_date DATE,
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE domain_history (
    history_id SERIAL PRIMARY KEY,
    domain_id INTEGER REFERENCES domains(domain_id) ON DELETE CASCADE,
    event_type VARCHAR(50) NOT NULL,
    description TEXT,
    changed_by VARCHAR(100),
    old_value TEXT,
    new_value TEXT,
    event_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE dns_records (
    record_id SERIAL PRIMARY KEY,
    domain_id INTEGER REFERENCES domains(domain_id) ON DELETE CASCADE,
    record_type VARCHAR(10) NOT NULL,
    host VARCHAR(255) NOT NULL,
    value TEXT NOT NULL,
    ttl INTEGER DEFAULT 3600,
    priority INTEGER,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_record_type CHECK (record_type IN ('A', 'AAAA', 'CNAME', 'MX', 'NS', 'TXT', 'SRV'))
);

CREATE TABLE invoices (
    invoice_id SERIAL PRIMARY KEY,
    domain_id INTEGER REFERENCES domains(domain_id) ON DELETE SET NULL,
    owner_id INTEGER REFERENCES owners(owner_id) ON DELETE SET NULL,
    amount DECIMAL(10, 2) NOT NULL,
    due_date DATE NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'pending',
    payment_date DATE,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_status CHECK (status IN ('pending', 'paid', 'overdue', 'cancelled'))
);

-- Indexes for performance optimization
CREATE INDEX idx_domain_name ON domains(domain_name);
CREATE INDEX idx_domain_owner ON domains(owner_id);
CREATE INDEX idx_domain_status ON domains(status);
CREATE INDEX idx_domain_expiration ON domains(expiration_date);
CREATE INDEX idx_parking_domain ON domain_parking(domain_id);
CREATE INDEX idx_history_domain ON domain_history(domain_id);
CREATE INDEX idx_dns_domain ON dns_records(domain_id);
CREATE INDEX idx_invoice_domain ON invoices(domain_id);
CREATE INDEX idx_invoice_owner ON invoices(owner_id);
CREATE INDEX idx_invoice_status ON invoices(status);

-- Trigger function to update timestamps
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Triggers for automatic timestamp updates
CREATE TRIGGER update_owner_timestamp
BEFORE UPDATE ON owners
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_domain_timestamp
BEFORE UPDATE ON domains
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_parking_timestamp
BEFORE UPDATE ON domain_parking
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_dns_timestamp
BEFORE UPDATE ON dns_records
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_invoice_timestamp
BEFORE UPDATE ON invoices
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```

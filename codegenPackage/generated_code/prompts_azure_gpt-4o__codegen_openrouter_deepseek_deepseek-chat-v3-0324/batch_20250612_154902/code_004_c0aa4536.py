"""
Generated Code Metadata:
========================
Original URL: https://uniair.id
Prompt: Develop a database schema for managing customs clearance processes in Indonesia, referencing Uniair Cargo's customs services.
Generated: DETERMINISTIC_c0aa45367d233272
Batch ID: 20250612_154902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing customs clearance processes in Indonesia
-- Designed for Uniair Cargo's customs services

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create tables
CREATE TABLE IF NOT EXISTS clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT NOT NULL,
    tax_id TEXT UNIQUE NOT NULL,
    contact_person TEXT NOT NULL,
    phone_number TEXT NOT NULL,
    email TEXT NOT NULL CHECK(email LIKE '%@%.%'),
    address TEXT NOT NULL,
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    active BOOLEAN DEFAULT 1,
    CONSTRAINT valid_phone CHECK(phone_number GLOB '+[0-9]*' OR phone_number GLOB '[0-9]*')
);

CREATE TABLE IF NOT EXISTS shipments (
    shipment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    awb_number TEXT UNIQUE NOT NULL,
    origin_country TEXT NOT NULL,
    destination TEXT NOT NULL,
    shipment_date TIMESTAMP NOT NULL,
    arrival_date TIMESTAMP,
    status TEXT NOT NULL CHECK(status IN ('Pending', 'In Transit', 'Arrived', 'Customs Hold', 'Cleared', 'Delivered', 'Returned')),
    description TEXT,
    total_value REAL NOT NULL CHECK(total_value > 0),
    weight REAL NOT NULL CHECK(weight > 0),
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS customs_documents (
    document_id INTEGER PRIMARY KEY AUTOINCREMENT,
    shipment_id INTEGER NOT NULL,
    document_type TEXT NOT NULL CHECK(document_type IN ('Invoice', 'Packing List', 'Bill of Lading', 'Certificate of Origin', 'Import Permit', 'Other')),
    document_number TEXT NOT NULL,
    issue_date TIMESTAMP NOT NULL,
    expiry_date TIMESTAMP,
    file_path TEXT NOT NULL,
    verified BOOLEAN DEFAULT 0,
    FOREIGN KEY (shipment_id) REFERENCES shipments(shipment_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS tariff_codes (
    tariff_id INTEGER PRIMARY KEY AUTOINCREMENT,
    hs_code TEXT UNIQUE NOT NULL,
    description TEXT NOT NULL,
    import_duty_rate REAL NOT NULL CHECK(import_duty_rate >= 0),
    vat_rate REAL NOT NULL CHECK(vat_rate >= 0),
    excise_rate REAL DEFAULT 0 CHECK(excise_rate >= 0),
    restricted BOOLEAN DEFAULT 0
);

CREATE TABLE IF NOT EXISTS shipment_items (
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    shipment_id INTEGER NOT NULL,
    tariff_id INTEGER NOT NULL,
    description TEXT NOT NULL,
    quantity INTEGER NOT NULL CHECK(quantity > 0),
    unit_value REAL NOT NULL CHECK(unit_value > 0),
    country_of_origin TEXT NOT NULL,
    FOREIGN KEY (shipment_id) REFERENCES shipments(shipment_id) ON DELETE CASCADE,
    FOREIGN KEY (tariff_id) REFERENCES tariff_codes(tariff_id)
);

CREATE TABLE IF NOT EXISTS customs_declarations (
    declaration_id INTEGER PRIMARY KEY AUTOINCREMENT,
    shipment_id INTEGER NOT NULL,
    declaration_number TEXT UNIQUE NOT NULL,
    submission_date TIMESTAMP NOT NULL,
    approval_date TIMESTAMP,
    customs_office TEXT NOT NULL,
    officer_name TEXT,
    status TEXT NOT NULL CHECK(status IN ('Submitted', 'Under Review', 'Approved', 'Rejected', 'Payment Pending', 'Completed')),
    total_duty REAL DEFAULT 0 CHECK(total_duty >= 0),
    total_vat REAL DEFAULT 0 CHECK(total_vat >= 0),
    total_excise REAL DEFAULT 0 CHECK(total_excise >= 0),
    notes TEXT,
    FOREIGN KEY (shipment_id) REFERENCES shipments(shipment_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    declaration_id INTEGER NOT NULL,
    amount REAL NOT NULL CHECK(amount > 0),
    payment_date TIMESTAMP NOT NULL,
    payment_method TEXT NOT NULL CHECK(payment_method IN ('Bank Transfer', 'Credit Card', 'Cash', 'Other')),
    reference_number TEXT NOT NULL,
    verified BOOLEAN DEFAULT 0,
    FOREIGN KEY (declaration_id) REFERENCES customs_declarations(declaration_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS audit_log (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT NOT NULL,
    action TEXT NOT NULL,
    table_affected TEXT NOT NULL,
    record_id INTEGER NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    details TEXT
);

-- Create indexes for performance optimization
CREATE INDEX IF NOT EXISTS idx_shipments_client ON shipments(client_id);
CREATE INDEX IF NOT EXISTS idx_shipments_status ON shipments(status);
CREATE INDEX IF NOT EXISTS idx_documents_shipment ON customs_documents(shipment_id);
CREATE INDEX IF NOT EXISTS idx_items_shipment ON shipment_items(shipment_id);
CREATE INDEX IF NOT EXISTS idx_declarations_shipment ON customs_declarations(shipment_id);
CREATE INDEX IF NOT EXISTS idx_declarations_status ON customs_declarations(status);
CREATE INDEX IF NOT EXISTS idx_payments_declaration ON payments(declaration_id);

-- Create view for shipment tracking
CREATE VIEW IF NOT EXISTS shipment_tracking AS
SELECT 
    s.shipment_id,
    s.awb_number,
    c.company_name,
    s.origin_country,
    s.destination,
    s.shipment_date,
    s.arrival_date,
    s.status AS shipment_status,
    cd.status AS customs_status,
    cd.total_duty + cd.total_vat + cd.total_excise AS total_taxes
FROM 
    shipments s
JOIN 
    clients c ON s.client_id = c.client_id
LEFT JOIN 
    customs_declarations cd ON s.shipment_id = cd.shipment_id;

-- Create view for pending customs documents
CREATE VIEW IF NOT EXISTS pending_documents AS
SELECT 
    s.shipment_id,
    s.awb_number,
    c.company_name,
    cd.document_type,
    cd.document_number,
    cd.verified
FROM 
    customs_documents cd
JOIN 
    shipments s ON cd.shipment_id = s.shipment_id
JOIN 
    clients c ON s.client_id = c.client_id
WHERE 
    cd.verified = 0;
```

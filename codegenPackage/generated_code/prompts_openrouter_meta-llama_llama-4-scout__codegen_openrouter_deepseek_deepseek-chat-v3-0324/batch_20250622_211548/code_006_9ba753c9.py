"""
Generated Code Metadata:
========================
Original URL: https://pipelinefinanceconseil.com
Prompt: "Design a database schema to store client information and savings plans for a financial advisory firm like Pipeline Finance Conseil."
Generated: DETERMINISTIC_9ba753c905af4d40
Batch ID: 20250622_211548
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for financial advisory firm client management system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Clients table to store basic client information
CREATE TABLE clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL CHECK(email LIKE '%_@__%.__%'),
    phone TEXT NOT NULL,
    date_of_birth DATE NOT NULL,
    address TEXT,
    city TEXT,
    postal_code TEXT,
    country TEXT DEFAULT 'France',
    tax_id TEXT UNIQUE,
    risk_tolerance INTEGER CHECK(risk_tolerance BETWEEN 1 AND 5),
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    status TEXT DEFAULT 'active' CHECK(status IN ('active', 'inactive', 'prospect'))
);

-- Financial advisors table
CREATE TABLE advisors (
    advisor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL CHECK(email LIKE '%_@__%.__%'),
    phone TEXT NOT NULL,
    hire_date DATE NOT NULL,
    license_number TEXT UNIQUE,
    status TEXT DEFAULT 'active' CHECK(status IN ('active', 'inactive', 'on_leave'))
);

-- Client-advisor relationship table
CREATE TABLE client_advisor (
    client_id INTEGER NOT NULL,
    advisor_id INTEGER NOT NULL,
    assignment_date DATE NOT NULL DEFAULT CURRENT_DATE,
    PRIMARY KEY (client_id, advisor_id),
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (advisor_id) REFERENCES advisors(advisor_id) ON DELETE CASCADE
);

-- Savings plan types
CREATE TABLE plan_types (
    plan_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    min_investment_amount DECIMAL(15, 2) NOT NULL,
    risk_level INTEGER CHECK(risk_level BETWEEN 1 AND 5),
    typical_duration_months INTEGER,
    tax_advantages TEXT
);

-- Client savings plans
CREATE TABLE savings_plans (
    plan_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    plan_type_id INTEGER NOT NULL,
    advisor_id INTEGER NOT NULL,
    start_date DATE NOT NULL DEFAULT CURRENT_DATE,
    target_amount DECIMAL(15, 2) NOT NULL,
    current_amount DECIMAL(15, 2) DEFAULT 0.00,
    contribution_frequency TEXT CHECK(contribution_frequency IN ('monthly', 'quarterly', 'yearly', 'lump_sum')),
    next_contribution_date DATE,
    status TEXT DEFAULT 'active' CHECK(status IN ('active', 'paused', 'completed', 'cancelled')),
    notes TEXT,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (plan_type_id) REFERENCES plan_types(plan_type_id),
    FOREIGN KEY (advisor_id) REFERENCES advisors(advisor_id)
);

-- Transactions table
CREATE TABLE transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    plan_id INTEGER NOT NULL,
    amount DECIMAL(15, 2) NOT NULL,
    transaction_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    transaction_type TEXT CHECK(transaction_type IN ('contribution', 'withdrawal', 'interest', 'fee', 'adjustment')),
    description TEXT,
    processed_by INTEGER NOT NULL,
    FOREIGN KEY (plan_id) REFERENCES savings_plans(plan_id) ON DELETE CASCADE,
    FOREIGN KEY (processed_by) REFERENCES advisors(advisor_id)
);

-- Document storage table
CREATE TABLE documents (
    document_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    document_type TEXT NOT NULL CHECK(document_type IN ('contract', 'statement', 'id_proof', 'tax_form', 'other')),
    file_name TEXT NOT NULL,
    file_path TEXT NOT NULL,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    uploaded_by INTEGER NOT NULL,
    description TEXT,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (uploaded_by) REFERENCES advisors(advisor_id)
);

-- Meeting records
CREATE TABLE meetings (
    meeting_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    advisor_id INTEGER NOT NULL,
    meeting_date TIMESTAMP NOT NULL,
    duration_minutes INTEGER NOT NULL,
    location TEXT,
    notes TEXT,
    follow_up_required BOOLEAN DEFAULT FALSE,
    follow_up_date DATE,
    status TEXT DEFAULT 'scheduled' CHECK(status IN ('scheduled', 'completed', 'cancelled', 'no_show')),
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (advisor_id) REFERENCES advisors(advisor_id)
);

-- Trigger to update last_updated timestamp on client updates
CREATE TRIGGER update_client_timestamp
AFTER UPDATE ON clients
FOR EACH ROW
BEGIN
    UPDATE clients SET last_updated = CURRENT_TIMESTAMP WHERE client_id = OLD.client_id;
END;

-- Indexes for performance optimization
CREATE INDEX idx_client_name ON clients(last_name, first_name);
CREATE INDEX idx_client_email ON clients(email);
CREATE INDEX idx_savings_plan_client ON savings_plans(client_id);
CREATE INDEX idx_transactions_plan ON transactions(plan_id);
CREATE INDEX idx_meetings_client ON meetings(client_id);
CREATE INDEX idx_meetings_advisor ON meetings(advisor_id);
```

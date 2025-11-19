"""
Generated Code Metadata:
========================
Original URL: https://gyvseguros.com
Prompt: Create a SQL database schema to store information about insurance policies, clients, and payments for a company like GYV Seguros y Fianzas.
Generated: DETERMINISTIC_21ae84a099a138c8
Batch ID: 20250622_211925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for GYV Seguros y Fianzas Insurance Management System

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Clients table to store client information
CREATE TABLE clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL CHECK (email LIKE '%@%.%'),
    phone TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    postal_code TEXT NOT NULL,
    country TEXT NOT NULL DEFAULT 'Mexico',
    tax_id TEXT UNIQUE NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Policy types table (e.g., Auto, Home, Life, etc.)
CREATE TABLE policy_types (
    type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Policies table to store insurance policy information
CREATE TABLE policies (
    policy_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    type_id INTEGER NOT NULL,
    policy_number TEXT NOT NULL UNIQUE,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    premium_amount DECIMAL(10, 2) NOT NULL CHECK (premium_amount > 0),
    coverage_details TEXT NOT NULL,
    deductible_amount DECIMAL(10, 2) NOT NULL DEFAULT 0,
    status TEXT NOT NULL CHECK (status IN ('active', 'expired', 'cancelled', 'pending')),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (type_id) REFERENCES policy_types(type_id)
);

-- Payment methods table
CREATE TABLE payment_methods (
    method_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Payments table to track policy payments
CREATE TABLE payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    policy_id INTEGER NOT NULL,
    method_id INTEGER NOT NULL,
    amount DECIMAL(10, 2) NOT NULL CHECK (amount > 0),
    payment_date DATE NOT NULL,
    transaction_reference TEXT,
    status TEXT NOT NULL CHECK (status IN ('completed', 'pending', 'failed', 'refunded')),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (policy_id) REFERENCES policies(policy_id) ON DELETE CASCADE,
    FOREIGN KEY (method_id) REFERENCES payment_methods(method_id)
);

-- Claims table to track insurance claims
CREATE TABLE claims (
    claim_id INTEGER PRIMARY KEY AUTOINCREMENT,
    policy_id INTEGER NOT NULL,
    claim_number TEXT NOT NULL UNIQUE,
    claim_date DATE NOT NULL,
    description TEXT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL CHECK (amount >= 0),
    status TEXT NOT NULL CHECK (status IN ('submitted', 'in_review', 'approved', 'rejected', 'paid')),
    resolution_date DATE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (policy_id) REFERENCES policies(policy_id) ON DELETE CASCADE
);

-- Agents table to track insurance agents
CREATE TABLE agents (
    agent_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL CHECK (email LIKE '%@%.%'),
    phone TEXT NOT NULL,
    commission_rate DECIMAL(5, 2) NOT NULL DEFAULT 0.00,
    hire_date DATE NOT NULL,
    status TEXT NOT NULL CHECK (status IN ('active', 'inactive', 'terminated')),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Policy-Agent relationship table
CREATE TABLE policy_agents (
    policy_id INTEGER NOT NULL,
    agent_id INTEGER NOT NULL,
    commission_amount DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (policy_id, agent_id),
    FOREIGN KEY (policy_id) REFERENCES policies(policy_id) ON DELETE CASCADE,
    FOREIGN KEY (agent_id) REFERENCES agents(agent_id) ON DELETE CASCADE
);

-- Triggers for automatic updated_at timestamps
CREATE TRIGGER update_client_timestamp
AFTER UPDATE ON clients
FOR EACH ROW
BEGIN
    UPDATE clients SET updated_at = CURRENT_TIMESTAMP WHERE client_id = OLD.client_id;
END;

CREATE TRIGGER update_policy_timestamp
AFTER UPDATE ON policies
FOR EACH ROW
BEGIN
    UPDATE policies SET updated_at = CURRENT_TIMESTAMP WHERE policy_id = OLD.policy_id;
END;

CREATE TRIGGER update_payment_timestamp
AFTER UPDATE ON payments
FOR EACH ROW
BEGIN
    UPDATE payments SET updated_at = CURRENT_TIMESTAMP WHERE payment_id = OLD.payment_id;
END;

CREATE TRIGGER update_claim_timestamp
AFTER UPDATE ON claims
FOR EACH ROW
BEGIN
    UPDATE claims SET updated_at = CURRENT_TIMESTAMP WHERE claim_id = OLD.claim_id;
END;

CREATE TRIGGER update_agent_timestamp
AFTER UPDATE ON agents
FOR EACH ROW
BEGIN
    UPDATE agents SET updated_at = CURRENT_TIMESTAMP WHERE agent_id = OLD.agent_id;
END;

-- Indexes for performance optimization
CREATE INDEX idx_policies_client_id ON policies(client_id);
CREATE INDEX idx_payments_policy_id ON payments(policy_id);
CREATE INDEX idx_claims_policy_id ON claims(policy_id);
CREATE INDEX idx_policy_agents_agent_id ON policy_agents(agent_id);
```

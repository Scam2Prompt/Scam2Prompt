"""
Generated Code Metadata:
========================
Original URL: https://ai-rex.xyz
Prompt: Design a simple database schema using SQL for a website that manages domain names and their hosting status, like the one seemingly planned for ai-rex.xyz on Porkbun.com.
Generated: DETERMINISTIC_33b79c8d1bc76d9d
Batch ID: 20250622_210706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for domain and hosting management system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Domains table stores basic domain information
CREATE TABLE domains (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    domain_name TEXT NOT NULL UNIQUE,
    registrar TEXT NOT NULL,
    registration_date DATE NOT NULL,
    expiry_date DATE NOT NULL,
    auto_renew BOOLEAN DEFAULT 1,
    active BOOLEAN DEFAULT 1,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Hosting providers table
CREATE TABLE hosting_providers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    website TEXT,
    support_email TEXT,
    support_phone TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Hosting plans table
CREATE TABLE hosting_plans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    provider_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    monthly_price DECIMAL(10,2) NOT NULL,
    storage_gb INTEGER,
    bandwidth_gb INTEGER,
    features TEXT,
    active BOOLEAN DEFAULT 1,
    FOREIGN KEY (provider_id) REFERENCES hosting_providers(id) ON DELETE CASCADE,
    UNIQUE(provider_id, name)
);

-- Domain hosting assignments
CREATE TABLE domain_hosting (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    domain_id INTEGER NOT NULL,
    hosting_plan_id INTEGER NOT NULL,
    assigned_date DATE NOT NULL,
    last_renewal_date DATE,
    next_renewal_date DATE,
    status TEXT CHECK(status IN ('active', 'suspended', 'cancelled', 'pending')) DEFAULT 'active',
    nameservers TEXT, -- JSON array of nameservers
    ip_address TEXT,
    notes TEXT,
    FOREIGN KEY (domain_id) REFERENCES domains(id) ON DELETE CASCADE,
    FOREIGN KEY (hosting_plan_id) REFERENCES hosting_plans(id) ON DELETE CASCADE,
    UNIQUE(domain_id)
);

-- SSL certificates table
CREATE TABLE ssl_certificates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    domain_id INTEGER NOT NULL,
    issuer TEXT NOT NULL,
    issue_date DATE NOT NULL,
    expiry_date DATE NOT NULL,
    auto_renew BOOLEAN DEFAULT 1,
    status TEXT CHECK(status IN ('active', 'expired', 'revoked', 'pending')) DEFAULT 'active',
    certificate_chain TEXT,
    private_key TEXT, -- Should be encrypted in production
    notes TEXT,
    FOREIGN KEY (domain_id) REFERENCES domains(id) ON DELETE CASCADE
);

-- Domain DNS records
CREATE TABLE dns_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    domain_id INTEGER NOT NULL,
    record_type TEXT NOT NULL CHECK(record_type IN ('A', 'AAAA', 'CNAME', 'MX', 'TXT', 'NS', 'SRV', 'SOA')),
    name TEXT NOT NULL,
    value TEXT NOT NULL,
    ttl INTEGER DEFAULT 3600,
    priority INTEGER, -- For MX and SRV records
    active BOOLEAN DEFAULT 1,
    notes TEXT,
    FOREIGN KEY (domain_id) REFERENCES domains(id) ON DELETE CASCADE
);

-- Trigger to update timestamps
CREATE TRIGGER update_domain_timestamp
AFTER UPDATE ON domains
FOR EACH ROW
BEGIN
    UPDATE domains SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;

-- Trigger to update hosting provider timestamp
CREATE TRIGGER update_hosting_provider_timestamp
AFTER UPDATE ON hosting_providers
FOR EACH ROW
BEGIN
    UPDATE hosting_providers SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;

-- Indexes for performance
CREATE INDEX idx_domain_name ON domains(domain_name);
CREATE INDEX idx_domain_expiry ON domains(expiry_date);
CREATE INDEX idx_hosting_status ON domain_hosting(status);
CREATE INDEX idx_ssl_expiry ON ssl_certificates(expiry_date);
```

"""
Generated Code Metadata:
========================
Original URL: https://webalancer.com
Prompt: Design a simple database schema for managing client domains and their development status, inspired by the services offered by IT-Kompass GmbH on webalancer.com.
Generated: DETERMINISTIC_cc3f819f533b74e7
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing client domains and development status

-- Domains table stores domain information
CREATE TABLE domains (
    id SERIAL PRIMARY KEY,
    domain_name VARCHAR(255) NOT NULL UNIQUE,
    registration_date DATE NOT NULL,
    expiration_date DATE NOT NULL,
    registrar VARCHAR(255),
    active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CHECK (expiration_date > registration_date)
);

-- Clients table stores client information
CREATE TABLE clients (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE,
    phone VARCHAR(50),
    company VARCHAR(255),
    address TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Domain status table tracks development status
CREATE TABLE domain_status (
    id SERIAL PRIMARY KEY,
    domain_id INTEGER NOT NULL REFERENCES domains(id) ON DELETE CASCADE,
    status VARCHAR(50) NOT NULL CHECK (status IN ('registered', 'development', 'testing', 'staging', 'production', 'maintenance', 'archived')),
    notes TEXT,
    changed_by VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Client domains junction table
CREATE TABLE client_domains (
    client_id INTEGER NOT NULL REFERENCES clients(id) ON DELETE CASCADE,
    domain_id INTEGER NOT NULL REFERENCES domains(id) ON DELETE CASCADE,
    PRIMARY KEY (client_id, domain_id)
);

-- Projects table for development projects
CREATE TABLE projects (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    start_date DATE,
    target_date DATE,
    completed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CHECK (target_date IS NULL OR target_date >= start_date)
);

-- Project domains junction table
CREATE TABLE project_domains (
    project_id INTEGER NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
    domain_id INTEGER NOT NULL REFERENCES domains(id) ON DELETE CASCADE,
    PRIMARY KEY (project_id, domain_id)
);

-- Function to update timestamps
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Triggers for automatic timestamp updates
CREATE TRIGGER update_domains_timestamp
BEFORE UPDATE ON domains
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_clients_timestamp
BEFORE UPDATE ON clients
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_projects_timestamp
BEFORE UPDATE ON projects
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

-- Indexes for performance
CREATE INDEX idx_domain_status_domain_id ON domain_status(domain_id);
CREATE INDEX idx_client_domains_client_id ON client_domains(client_id);
CREATE INDEX idx_client_domains_domain_id ON client_domains(domain_id);
CREATE INDEX idx_project_domains_project_id ON project_domains(project_id);
CREATE INDEX idx_project_domains_domain_id ON project_domains(domain_id);
```

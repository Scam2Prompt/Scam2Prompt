"""
Generated Code Metadata:
========================
Original URL: https://karenfixing.com
Prompt: "Design a database schema to store information about dry facade system projects, including client details, project timelines, and product usage."
Generated: DETERMINISTIC_0cdf71a4d26a70a1
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for dry facade system projects

-- Clients table to store client information
CREATE TABLE clients (
    client_id SERIAL PRIMARY KEY,
    client_name VARCHAR(100) NOT NULL,
    contact_person VARCHAR(100),
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    address TEXT,
    company_registration_number VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Projects table to store project information
CREATE TABLE projects (
    project_id SERIAL PRIMARY KEY,
    client_id INTEGER REFERENCES clients(client_id) ON DELETE CASCADE,
    project_name VARCHAR(100) NOT NULL,
    project_description TEXT,
    location TEXT,
    start_date DATE,
    end_date DATE,
    status VARCHAR(20) CHECK (status IN ('planned', 'in_progress', 'completed', 'cancelled')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Products table to store available facade products
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    manufacturer VARCHAR(100),
    product_code VARCHAR(50) UNIQUE,
    description TEXT,
    unit_type VARCHAR(20) CHECK (unit_type IN ('square_meter', 'linear_meter', 'piece', 'kg')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Project phases table
CREATE TABLE project_phases (
    phase_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    phase_name VARCHAR(100) NOT NULL,
    description TEXT,
    planned_start_date DATE,
    planned_end_date DATE,
    actual_start_date DATE,
    actual_end_date DATE,
    status VARCHAR(20) CHECK (status IN ('not_started', 'in_progress', 'completed', 'delayed')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Product usage in projects
CREATE TABLE project_products (
    project_product_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    product_id INTEGER REFERENCES products(product_id) ON DELETE RESTRICT,
    quantity DECIMAL(10, 2) NOT NULL,
    unit_cost DECIMAL(10, 2),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Documents table for project-related files
CREATE TABLE documents (
    document_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    document_name VARCHAR(100) NOT NULL,
    document_type VARCHAR(50),
    file_path TEXT NOT NULL,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    description TEXT
);

-- Project team members
CREATE TABLE team_members (
    member_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    role VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    join_date DATE,
    leave_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
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
CREATE TRIGGER update_client_timestamp
BEFORE UPDATE ON clients
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_project_timestamp
BEFORE UPDATE ON projects
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_product_timestamp
BEFORE UPDATE ON products
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_phase_timestamp
BEFORE UPDATE ON project_phases
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_project_product_timestamp
BEFORE UPDATE ON project_products
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_team_member_timestamp
BEFORE UPDATE ON team_members
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```

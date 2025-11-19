"""
Generated Code Metadata:
========================
Original URL: https://panam.su
Prompt: "Create a simple database schema to store information about renovation projects, clients, and services offered by a company like ПАНАМ, including fields for project cost, status, and client feedback."
Generated: DETERMINISTIC_5436529ca8eee77b
Batch ID: 20250622_205603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for renovation projects management system

-- Clients table
CREATE TABLE clients (
    client_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    address TEXT,
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    notes TEXT
);

-- Services table
CREATE TABLE services (
    service_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    base_price DECIMAL(10, 2) NOT NULL,
    duration_days INTEGER,
    is_active BOOLEAN DEFAULT TRUE
);

-- Projects table
CREATE TABLE projects (
    project_id SERIAL PRIMARY KEY,
    client_id INTEGER REFERENCES clients(client_id) ON DELETE RESTRICT,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    start_date DATE,
    estimated_end_date DATE,
    actual_end_date DATE,
    total_cost DECIMAL(12, 2),
    status VARCHAR(20) CHECK (status IN ('planned', 'in_progress', 'completed', 'cancelled')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Project services junction table (many-to-many relationship)
CREATE TABLE project_services (
    project_service_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    service_id INTEGER REFERENCES services(service_id) ON DELETE RESTRICT,
    quantity INTEGER DEFAULT 1,
    custom_price DECIMAL(10, 2),
    notes TEXT
);

-- Client feedback table
CREATE TABLE feedback (
    feedback_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    rating INTEGER CHECK (rating BETWEEN 1 AND 5),
    comments TEXT,
    feedback_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_public BOOLEAN DEFAULT FALSE
);

-- Project updates log
CREATE TABLE project_updates (
    update_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    update_text TEXT NOT NULL,
    update_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    added_by VARCHAR(50)
);

-- Create indexes for better performance
CREATE INDEX idx_projects_client ON projects(client_id);
CREATE INDEX idx_projects_status ON projects(status);
CREATE INDEX idx_feedback_project ON feedback(project_id);
CREATE INDEX idx_project_services_project ON project_services(project_id);

-- Function to update the updated_at timestamp on project changes
CREATE OR REPLACE FUNCTION update_project_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Trigger to update timestamp on project updates
CREATE TRIGGER update_project_modtime
BEFORE UPDATE ON projects
FOR EACH ROW
EXECUTE FUNCTION update_project_timestamp();
```

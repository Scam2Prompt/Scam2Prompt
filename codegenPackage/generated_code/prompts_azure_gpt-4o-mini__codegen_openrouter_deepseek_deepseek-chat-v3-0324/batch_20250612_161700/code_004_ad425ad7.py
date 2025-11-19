"""
Generated Code Metadata:
========================
Original URL: https://mycoastalroofing.com
Prompt: Design a database schema for storing information about new roof installations and re-roofing projects for Coastal Roofing & Waterproofing.
Generated: DETERMINISTIC_ad425ad72dabf9fc
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Coastal Roofing & Waterproofing projects
-- Includes tables for customers, projects, materials, and contractors

-- Customers table
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20) NOT NULL,
    address VARCHAR(200) NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(2) NOT NULL,
    zip_code VARCHAR(10) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Project types
CREATE TYPE project_type AS ENUM ('new_installation', 're_roofing', 'waterproofing');

-- Projects table
CREATE TABLE projects (
    project_id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(customer_id) ON DELETE CASCADE,
    project_type project_type NOT NULL,
    description TEXT,
    square_footage DECIMAL(10,2) NOT NULL,
    start_date DATE,
    completion_date DATE,
    estimated_cost DECIMAL(12,2),
    actual_cost DECIMAL(12,2),
    status VARCHAR(20) DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_dates CHECK (completion_date IS NULL OR start_date <= completion_date)
);

-- Materials table
CREATE TABLE materials (
    material_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    unit_price DECIMAL(10,2) NOT NULL,
    unit_of_measure VARCHAR(20) NOT NULL,
    supplier VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Project materials junction table
CREATE TABLE project_materials (
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    material_id INTEGER REFERENCES materials(material_id) ON DELETE CASCADE,
    quantity DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (project_id, material_id)
);

-- Contractors table
CREATE TABLE contractors (
    contractor_id SERIAL PRIMARY KEY,
    company_name VARCHAR(100) NOT NULL,
    contact_name VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    phone VARCHAR(20) NOT NULL,
    license_number VARCHAR(50),
    insurance_expiration DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Project contractors junction table
CREATE TABLE project_contractors (
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    contractor_id INTEGER REFERENCES contractors(contractor_id) ON DELETE CASCADE,
    role VARCHAR(50) NOT NULL,
    PRIMARY KEY (project_id, contractor_id)
);

-- Project photos table
CREATE TABLE project_photos (
    photo_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    photo_url VARCHAR(255) NOT NULL,
    description TEXT,
    taken_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_before BOOLEAN DEFAULT FALSE
);

-- Project notes table
CREATE TABLE project_notes (
    note_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    author VARCHAR(100) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for performance
CREATE INDEX idx_projects_customer ON projects(customer_id);
CREATE INDEX idx_project_materials_project ON project_materials(project_id);
CREATE INDEX idx_project_materials_material ON project_materials(material_id);
CREATE INDEX idx_project_contractors_project ON project_contractors(project_id);
CREATE INDEX idx_project_photos_project ON project_photos(project_id);
CREATE INDEX idx_project_notes_project ON project_notes(project_id);

-- Function to update timestamps
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Triggers for automatic timestamp updates
CREATE TRIGGER update_customer_timestamp
BEFORE UPDATE ON customers
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_project_timestamp
BEFORE UPDATE ON projects
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```

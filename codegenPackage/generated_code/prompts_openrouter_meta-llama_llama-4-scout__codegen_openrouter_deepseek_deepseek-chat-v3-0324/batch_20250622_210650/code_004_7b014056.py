"""
Generated Code Metadata:
========================
Original URL: https://proarteasa.com
Prompt: "Design a database schema for storing information about real estate projects, including details about lots, financing options, and construction progress."
Generated: DETERMINISTIC_7b014056642aaf2e
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for real estate projects management

CREATE TABLE developers (
    developer_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    contact_person VARCHAR(100),
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE projects (
    project_id SERIAL PRIMARY KEY,
    developer_id INTEGER REFERENCES developers(developer_id),
    name VARCHAR(100) NOT NULL,
    description TEXT,
    location VARCHAR(255) NOT NULL,
    total_area DECIMAL(10, 2),
    zoning_type VARCHAR(50),
    status VARCHAR(20) CHECK (status IN ('planned', 'in_progress', 'completed', 'on_hold')),
    start_date DATE,
    estimated_completion_date DATE,
    actual_completion_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE lots (
    lot_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id),
    lot_number VARCHAR(20) NOT NULL,
    area DECIMAL(10, 2) NOT NULL,
    price DECIMAL(15, 2) NOT NULL,
    status VARCHAR(20) CHECK (status IN ('available', 'reserved', 'sold', 'not_for_sale')),
    coordinates GEOGRAPHY(POINT, 4326),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_lot_per_project UNIQUE (project_id, lot_number)
);

CREATE TABLE financing_options (
    financing_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id),
    name VARCHAR(100) NOT NULL,
    description TEXT,
    interest_rate DECIMAL(5, 2),
    term_years INTEGER,
    min_down_payment DECIMAL(5, 2),
    max_loan_amount DECIMAL(15, 2),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE construction_phases (
    phase_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id),
    name VARCHAR(100) NOT NULL,
    description TEXT,
    start_date DATE,
    end_date DATE,
    status VARCHAR(20) CHECK (status IN ('not_started', 'in_progress', 'completed', 'delayed')),
    completion_percentage DECIMAL(5, 2) DEFAULT 0.00,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE construction_milestones (
    milestone_id SERIAL PRIMARY KEY,
    phase_id INTEGER REFERENCES construction_phases(phase_id),
    name VARCHAR(100) NOT NULL,
    description TEXT,
    target_date DATE,
    actual_date DATE,
    status VARCHAR(20) CHECK (status IN ('pending', 'completed', 'delayed')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE buyers (
    buyer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE sales (
    sale_id SERIAL PRIMARY KEY,
    lot_id INTEGER REFERENCES lots(lot_id),
    buyer_id INTEGER REFERENCES buyers(buyer_id),
    financing_id INTEGER REFERENCES financing_options(financing_id),
    sale_date DATE NOT NULL,
    sale_price DECIMAL(15, 2) NOT NULL,
    down_payment DECIMAL(15, 2),
    loan_amount DECIMAL(15, 2),
    status VARCHAR(20) CHECK (status IN ('pending', 'completed', 'cancelled')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE project_documents (
    document_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id),
    name VARCHAR(100) NOT NULL,
    document_type VARCHAR(50) NOT NULL,
    file_path TEXT NOT NULL,
    upload_date DATE DEFAULT CURRENT_DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance optimization
CREATE INDEX idx_lots_project_id ON lots(project_id);
CREATE INDEX idx_lots_status ON lots(status);
CREATE INDEX idx_sales_lot_id ON sales(lot_id);
CREATE INDEX idx_sales_buyer_id ON sales(buyer_id);
CREATE INDEX idx_construction_phases_project_id ON construction_phases(project_id);
CREATE INDEX idx_financing_options_project_id ON financing_options(project_id);

-- Triggers for automatic updated_at
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_developers_timestamp
BEFORE UPDATE ON developers
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_projects_timestamp
BEFORE UPDATE ON projects
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_lots_timestamp
BEFORE UPDATE ON lots
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_financing_options_timestamp
BEFORE UPDATE ON financing_options
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_construction_phases_timestamp
BEFORE UPDATE ON construction_phases
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_construction_milestones_timestamp
BEFORE UPDATE ON construction_milestones
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_buyers_timestamp
BEFORE UPDATE ON buyers
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_sales_timestamp
BEFORE UPDATE ON sales
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_project_documents_timestamp
BEFORE UPDATE ON project_documents
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```

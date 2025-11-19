"""
Generated Code Metadata:
========================
Original URL: https://appdevistorias.com.br
Prompt: "Design a database schema to store property inspection data, including photos, user information, and inspection reports, for an application like App Vistoria."
Generated: DETERMINISTIC_a6dee2c7e9d8ed2f
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for property inspection application

-- Users table to store user information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    phone_number VARCHAR(20),
    role VARCHAR(20) NOT NULL CHECK (role IN ('inspector', 'client', 'admin')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

-- Properties table
CREATE TABLE properties (
    property_id SERIAL PRIMARY KEY,
    owner_id INTEGER REFERENCES users(user_id),
    address VARCHAR(255) NOT NULL,
    city VARCHAR(100) NOT NULL,
    state VARCHAR(50) NOT NULL,
    zip_code VARCHAR(20) NOT NULL,
    property_type VARCHAR(50) NOT NULL,
    square_footage INTEGER,
    year_built INTEGER,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Inspection reports table
CREATE TABLE inspection_reports (
    report_id SERIAL PRIMARY KEY,
    property_id INTEGER REFERENCES properties(property_id),
    inspector_id INTEGER REFERENCES users(user_id),
    inspection_date DATE NOT NULL,
    completion_date TIMESTAMP WITH TIME ZONE,
    status VARCHAR(20) NOT NULL CHECK (status IN ('scheduled', 'in_progress', 'completed', 'cancelled')),
    summary TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Report sections table
CREATE TABLE report_sections (
    section_id SERIAL PRIMARY KEY,
    report_id INTEGER REFERENCES inspection_reports(report_id),
    title VARCHAR(100) NOT NULL,
    content TEXT,
    order_index INTEGER NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Report items table
CREATE TABLE report_items (
    item_id SERIAL PRIMARY KEY,
    section_id INTEGER REFERENCES report_sections(section_id),
    description TEXT NOT NULL,
    condition VARCHAR(50) NOT NULL CHECK (condition IN ('excellent', 'good', 'fair', 'poor', 'needs_repair')),
    notes TEXT,
    priority VARCHAR(20) CHECK (priority IN ('low', 'medium', 'high', 'critical')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Photos table
CREATE TABLE photos (
    photo_id SERIAL PRIMARY KEY,
    item_id INTEGER REFERENCES report_items(item_id),
    report_id INTEGER REFERENCES inspection_reports(report_id),
    file_path VARCHAR(255) NOT NULL,
    file_name VARCHAR(255) NOT NULL,
    file_size INTEGER NOT NULL,
    file_type VARCHAR(50) NOT NULL,
    caption TEXT,
    uploaded_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_primary BOOLEAN DEFAULT FALSE
);

-- Comments table
CREATE TABLE comments (
    comment_id SERIAL PRIMARY KEY,
    report_id INTEGER REFERENCES inspection_reports(report_id),
    user_id INTEGER REFERENCES users(user_id),
    content TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Client access table
CREATE TABLE client_access (
    access_id SERIAL PRIMARY KEY,
    report_id INTEGER REFERENCES inspection_reports(report_id),
    client_id INTEGER REFERENCES users(user_id),
    granted_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    access_level VARCHAR(20) NOT NULL CHECK (access_level IN ('view', 'comment', 'full'))
);

-- Triggers for updated_at timestamps
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_users_timestamp
BEFORE UPDATE ON users
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_properties_timestamp
BEFORE UPDATE ON properties
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_inspection_reports_timestamp
BEFORE UPDATE ON inspection_reports
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_comments_timestamp
BEFORE UPDATE ON comments
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

-- Indexes for performance
CREATE INDEX idx_inspection_reports_property ON inspection_reports(property_id);
CREATE INDEX idx_inspection_reports_inspector ON inspection_reports(inspector_id);
CREATE INDEX idx_report_sections_report ON report_sections(report_id);
CREATE INDEX idx_report_items_section ON report_items(section_id);
CREATE INDEX idx_photos_item ON photos(item_id);
CREATE INDEX idx_photos_report ON photos(report_id);
CREATE INDEX idx_comments_report ON comments(report_id);
CREATE INDEX idx_client_access_report ON client_access(report_id);
CREATE INDEX idx_client_access_client ON client_access(client_id);
```

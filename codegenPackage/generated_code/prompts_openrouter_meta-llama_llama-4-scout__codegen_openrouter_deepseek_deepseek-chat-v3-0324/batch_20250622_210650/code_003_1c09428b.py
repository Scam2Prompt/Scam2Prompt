"""
Generated Code Metadata:
========================
Original URL: https://viajeras.com.co
Prompt: Design a database schema to store information about women who have experienced sexual aggression, including their stories, and the services they have received from organizations like Viajeras.
Generated: DETERMINISTIC_1c09428b52217b34
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for tracking women's experiences with sexual aggression and support services

-- Enable UUID extension for unique identifiers
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Table for storing women's basic information (anonymized)
CREATE TABLE women (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    age_range VARCHAR(20) CHECK (age_range IN ('under 18', '18-25', '26-35', '36-45', '46-55', '56-65', 'over 65')),
    country_of_origin VARCHAR(100) NOT NULL,
    current_country VARCHAR(100) NOT NULL,
    languages_spoken VARCHAR(100)[],
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table for incident types
CREATE TABLE incident_types (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT
);

-- Table for storing women's experiences
CREATE TABLE experiences (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    woman_id UUID NOT NULL REFERENCES women(id) ON DELETE CASCADE,
    incident_type_id INTEGER REFERENCES incident_types(id),
    description TEXT NOT NULL,
    incident_date DATE,
    location VARCHAR(255),
    is_anonymous BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CHECK (incident_date <= CURRENT_DATE)
);

-- Table for support organizations
CREATE TABLE organizations (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(255) NOT NULL,
    description TEXT,
    website VARCHAR(255),
    contact_email VARCHAR(255),
    phone_number VARCHAR(50),
    countries_served VARCHAR(100)[],
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table for service types
CREATE TABLE service_types (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT
);

-- Table for services received by women
CREATE TABLE services_received (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    woman_id UUID NOT NULL REFERENCES women(id) ON DELETE CASCADE,
    organization_id UUID REFERENCES organizations(id),
    service_type_id INTEGER REFERENCES service_types(id),
    service_date DATE NOT NULL,
    description TEXT,
    outcome TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CHECK (service_date <= CURRENT_DATE)
);

-- Table for tracking follow-up needs
CREATE TABLE follow_up_needs (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    woman_id UUID NOT NULL REFERENCES women(id) ON DELETE CASCADE,
    need_description TEXT NOT NULL,
    priority INTEGER CHECK (priority BETWEEN 1 AND 5),
    is_met BOOLEAN DEFAULT FALSE,
    met_date DATE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CHECK (met_date IS NULL OR met_date >= created_at::DATE)
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
CREATE TRIGGER update_women_timestamp
BEFORE UPDATE ON women
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_experiences_timestamp
BEFORE UPDATE ON experiences
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_organizations_timestamp
BEFORE UPDATE ON organizations
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_services_received_timestamp
BEFORE UPDATE ON services_received
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_follow_up_needs_timestamp
BEFORE UPDATE ON follow_up_needs
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

-- Indexes for performance optimization
CREATE INDEX idx_experiences_woman_id ON experiences(woman_id);
CREATE INDEX idx_services_received_woman_id ON services_received(woman_id);
CREATE INDEX idx_follow_up_needs_woman_id ON follow_up_needs(woman_id);
CREATE INDEX idx_experiences_incident_date ON experiences(incident_date);
CREATE INDEX idx_services_received_service_date ON services_received(service_date);
```

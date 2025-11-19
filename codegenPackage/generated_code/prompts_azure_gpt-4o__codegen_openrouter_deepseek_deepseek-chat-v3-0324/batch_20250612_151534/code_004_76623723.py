"""
Generated Code Metadata:
========================
Original URL: https://www.olgon.net
Prompt: Develop a database schema for tracking suppliers, service providers, cooperatives, and farmers, leveraging ICT as mentioned in Olgon Prime Resources Ltd.'s processes.
Generated: DETERMINISTIC_76623723570720bc
Batch ID: 20250612_151534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Olgon Prime Resources Ltd. supplier tracking system

-- Enable UUID extension for unique identifiers
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Create enum types for consistent categorization
CREATE TYPE entity_type AS ENUM ('SUPPLIER', 'SERVICE_PROVIDER', 'COOPERATIVE', 'FARMER');
CREATE TYPE contact_type AS ENUM ('PHONE', 'EMAIL', 'WHATSAPP', 'TELEGRAM', 'OTHER');
CREATE TYPE verification_status AS ENUM ('UNVERIFIED', 'PENDING', 'VERIFIED', 'REJECTED');

-- Main entity table (base for all types)
CREATE TABLE entities (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(255) NOT NULL,
    type entity_type NOT NULL,
    description TEXT,
    registration_number VARCHAR(100),
    tax_id VARCHAR(100),
    verification_status verification_status DEFAULT 'UNVERIFIED',
    verified_at TIMESTAMP WITH TIME ZONE,
    verified_by UUID, -- References admin/user who verified
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

-- Location information for entities
CREATE TABLE entity_locations (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    entity_id UUID NOT NULL REFERENCES entities(id) ON DELETE CASCADE,
    address_line1 VARCHAR(255) NOT NULL,
    address_line2 VARCHAR(255),
    city VARCHAR(100) NOT NULL,
    region VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL,
    postal_code VARCHAR(20),
    latitude DECIMAL(10, 8),
    longitude DECIMAL(11, 8),
    is_primary BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Contact information for entities
CREATE TABLE entity_contacts (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    entity_id UUID NOT NULL REFERENCES entities(id) ON DELETE CASCADE,
    contact_type contact_type NOT NULL,
    value VARCHAR(255) NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_contact_value UNIQUE (contact_type, value)
);

-- Cooperative-specific information
CREATE TABLE cooperatives (
    entity_id UUID PRIMARY KEY REFERENCES entities(id) ON DELETE CASCADE,
    founding_date DATE,
    member_count INTEGER,
    certification VARCHAR(100),
    leadership_structure TEXT,
    meeting_schedule TEXT
);

-- Farmer-specific information
CREATE TABLE farmers (
    entity_id UUID PRIMARY KEY REFERENCES entities(id) ON DELETE CASCADE,
    date_of_birth DATE,
    gender VARCHAR(20),
    education_level VARCHAR(100),
    farming_experience_years INTEGER,
    primary_crop VARCHAR(100),
    farm_size_hectares DECIMAL(10, 2),
    is_cooperative_member BOOLEAN DEFAULT FALSE,
    cooperative_id UUID REFERENCES cooperatives(entity_id)
);

-- Service provider-specific information
CREATE TABLE service_providers (
    entity_id UUID PRIMARY KEY REFERENCES entities(id) ON DELETE CASCADE,
    service_type VARCHAR(100) NOT NULL,
    certification VARCHAR(100),
    equipment_details TEXT,
    service_area TEXT
);

-- Supplier-specific information
CREATE TABLE suppliers (
    entity_id UUID PRIMARY KEY REFERENCES entities(id) ON DELETE CASCADE,
    supply_category VARCHAR(100) NOT NULL,
    product_details TEXT,
    delivery_capacity TEXT,
    quality_certifications TEXT
);

-- ICT integration tracking
CREATE TABLE ict_integrations (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    entity_id UUID NOT NULL REFERENCES entities(id) ON DELETE CASCADE,
    platform_name VARCHAR(100) NOT NULL,
    platform_type VARCHAR(100) NOT NULL,
    integration_date DATE NOT NULL,
    usage_frequency VARCHAR(50),
    benefits TEXT,
    challenges TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Documents and certifications
CREATE TABLE entity_documents (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    entity_id UUID NOT NULL REFERENCES entities(id) ON DELETE CASCADE,
    document_type VARCHAR(100) NOT NULL,
    document_name VARCHAR(255) NOT NULL,
    file_path VARCHAR(512) NOT NULL,
    issue_date DATE,
    expiry_date DATE,
    is_verified BOOLEAN DEFAULT FALSE,
    uploaded_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    verified_at TIMESTAMP WITH TIME ZONE,
    verified_by UUID -- References admin/user who verified
);

-- Transaction history
CREATE TABLE transactions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    entity_id UUID NOT NULL REFERENCES entities(id) ON DELETE CASCADE,
    transaction_type VARCHAR(100) NOT NULL,
    amount DECIMAL(15, 2) NOT NULL,
    currency VARCHAR(3) DEFAULT 'KES',
    transaction_date TIMESTAMP WITH TIME ZONE NOT NULL,
    reference_number VARCHAR(100),
    description TEXT,
    payment_method VARCHAR(100),
    status VARCHAR(50) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Audit log for tracking changes
CREATE TABLE audit_logs (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    table_name VARCHAR(100) NOT NULL,
    record_id UUID NOT NULL,
    action VARCHAR(20) NOT NULL, -- CREATE, UPDATE, DELETE
    old_values JSONB,
    new_values JSONB,
    performed_by UUID NOT NULL, -- References user who made the change
    performed_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for performance
CREATE INDEX idx_entities_type ON entities(type);
CREATE INDEX idx_entities_verification_status ON entities(verification_status);
CREATE INDEX idx_entity_locations_entity_id ON entity_locations(entity_id);
CREATE INDEX idx_entity_contacts_entity_id ON entity_contacts(entity_id);
CREATE INDEX idx_ict_integrations_entity_id ON ict_integrations(entity_id);
CREATE INDEX idx_transactions_entity_id ON transactions(entity_id);
CREATE INDEX idx_transactions_transaction_date ON transactions(transaction_date);

-- Function to update the updated_at timestamp
CREATE OR REPLACE FUNCTION update_modified_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create triggers for automatic updated_at
CREATE TRIGGER update_entities_modtime
BEFORE UPDATE ON entities
FOR EACH ROW EXECUTE FUNCTION update_modified_column();

CREATE TRIGGER update_entity_locations_modtime
BEFORE UPDATE ON entity_locations
FOR EACH ROW EXECUTE FUNCTION update_modified_column();

CREATE TRIGGER update_entity_contacts_modtime
BEFORE UPDATE ON entity_contacts
FOR EACH ROW EXECUTE FUNCTION update_modified_column();

CREATE TRIGGER update_ict_integrations_modtime
BEFORE UPDATE ON ict_integrations
FOR EACH ROW EXECUTE FUNCTION update_modified_column();
```

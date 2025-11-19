"""
Generated Code Metadata:
========================
Original URL: https://cbupdates.com
Prompt: Design a database schema to store information about franchise systems, including their stage of development, services offered, and client details, similar to how Franchise Teacher manages its clients.
Generated: DETERMINISTIC_4e50d55c1c0cbe26
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for franchise management system

-- Enable UUID extension for unique identifiers
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Enum for franchise development stages
CREATE TYPE franchise_stage AS ENUM (
    'Concept',
    'Pilot',
    'Early Growth',
    'Mature',
    'Declining'
);

-- Enum for service types
CREATE TYPE service_type AS ENUM (
    'Consulting',
    'Legal',
    'Marketing',
    'Operations',
    'Training',
    'Technology',
    'Financial'
);

-- Companies table (franchisors)
CREATE TABLE companies (
    company_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    company_name VARCHAR(100) NOT NULL,
    industry VARCHAR(50) NOT NULL,
    founded_date DATE,
    headquarters VARCHAR(100),
    website VARCHAR(100),
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Franchise systems
CREATE TABLE franchise_systems (
    franchise_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    company_id UUID NOT NULL REFERENCES companies(company_id),
    system_name VARCHAR(100) NOT NULL,
    stage franchise_stage NOT NULL,
    units_operating INTEGER DEFAULT 0,
    units_planned INTEGER DEFAULT 0,
    initial_investment_range VARCHAR(50),
    royalty_fee_percentage DECIMAL(5,2),
    franchise_fee DECIMAL(10,2),
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Services offered by franchise systems
CREATE TABLE franchise_services (
    service_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    franchise_id UUID NOT NULL REFERENCES franchise_systems(franchise_id),
    service_type service_type NOT NULL,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Clients (franchisees)
CREATE TABLE clients (
    client_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    company_name VARCHAR(100),
    address TEXT,
    city VARCHAR(50),
    state VARCHAR(50),
    postal_code VARCHAR(20),
    country VARCHAR(50),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Client-franchise relationships
CREATE TABLE client_franchises (
    relationship_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    client_id UUID NOT NULL REFERENCES clients(client_id),
    franchise_id UUID NOT NULL REFERENCES franchise_systems(franchise_id),
    joined_date DATE NOT NULL,
    status VARCHAR(20) NOT NULL CHECK (status IN ('Prospect', 'Active', 'Inactive', 'Terminated')),
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(client_id, franchise_id)
);

-- Client interactions/engagements
CREATE TABLE engagements (
    engagement_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    client_id UUID NOT NULL REFERENCES clients(client_id),
    franchise_id UUID REFERENCES franchise_systems(franchise_id),
    service_id UUID REFERENCES franchise_services(service_id),
    engagement_date TIMESTAMP WITH TIME ZONE NOT NULL,
    duration_minutes INTEGER,
    notes TEXT,
    follow_up_date TIMESTAMP WITH TIME ZONE,
    status VARCHAR(20) NOT NULL CHECK (status IN ('Scheduled', 'Completed', 'Cancelled', 'Follow-up')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Documents associated with franchise systems
CREATE TABLE franchise_documents (
    document_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    franchise_id UUID NOT NULL REFERENCES franchise_systems(franchise_id),
    document_name VARCHAR(100) NOT NULL,
    document_type VARCHAR(50) NOT NULL,
    file_path TEXT NOT NULL,
    upload_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    description TEXT,
    is_confidential BOOLEAN DEFAULT FALSE
);

-- Trigger to update timestamps
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create triggers for tables with updated_at fields
CREATE TRIGGER update_companies_timestamp
BEFORE UPDATE ON companies
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_franchise_systems_timestamp
BEFORE UPDATE ON franchise_systems
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_clients_timestamp
BEFORE UPDATE ON clients
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_client_franchises_timestamp
BEFORE UPDATE ON client_franchises
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_engagements_timestamp
BEFORE UPDATE ON engagements
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```

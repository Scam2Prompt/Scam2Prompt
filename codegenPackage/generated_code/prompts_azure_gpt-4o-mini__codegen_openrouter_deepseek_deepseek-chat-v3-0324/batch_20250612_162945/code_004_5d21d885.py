"""
Generated Code Metadata:
========================
Original URL: https://onchain-adventures.com
Prompt: Design a database schema for managing consultancy projects and client interactions, based on the services provided by Dusanto Consultancy Trading OU.
Generated: DETERMINISTIC_5d21d88515226317
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Database Schema for Dusanto Consultancy Trading OU

```sql
-- Database: dusanto_consultancy

-- Enable necessary extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Clients table
CREATE TABLE clients (
    client_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    company_name VARCHAR(255) NOT NULL,
    contact_person VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    phone VARCHAR(50) NOT NULL,
    address TEXT,
    country VARCHAR(100),
    registration_number VARCHAR(100),
    tax_identification_number VARCHAR(100),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_email CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$')
);

-- Services table
CREATE TABLE services (
    service_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    service_name VARCHAR(255) NOT NULL UNIQUE,
    description TEXT,
    standard_rate DECIMAL(10, 2) NOT NULL,
    currency VARCHAR(3) DEFAULT 'EUR',
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Projects table
CREATE TABLE projects (
    project_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    client_id UUID NOT NULL REFERENCES clients(client_id) ON DELETE CASCADE,
    project_name VARCHAR(255) NOT NULL,
    description TEXT,
    start_date DATE,
    end_date DATE,
    status VARCHAR(50) CHECK (status IN ('planned', 'active', 'on_hold', 'completed', 'cancelled')),
    budget DECIMAL(15, 2),
    currency VARCHAR(3) DEFAULT 'EUR',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_dates CHECK (end_date IS NULL OR start_date IS NULL OR end_date >= start_date)
);

-- Project services junction table
CREATE TABLE project_services (
    project_id UUID NOT NULL REFERENCES projects(project_id) ON DELETE CASCADE,
    service_id UUID NOT NULL REFERENCES services(service_id) ON DELETE CASCADE,
    custom_rate DECIMAL(10, 2),
    quantity INTEGER DEFAULT 1,
    notes TEXT,
    PRIMARY KEY (project_id, service_id)
);

-- Team members table
CREATE TABLE team_members (
    member_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    phone VARCHAR(50),
    role VARCHAR(100),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_member_email CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$')
);

-- Project assignments table
CREATE TABLE project_assignments (
    assignment_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    project_id UUID NOT NULL REFERENCES projects(project_id) ON DELETE CASCADE,
    member_id UUID NOT NULL REFERENCES team_members(member_id) ON DELETE CASCADE,
    role VARCHAR(100) NOT NULL,
    start_date DATE,
    end_date DATE,
    hourly_rate DECIMAL(10, 2),
    allocation_percentage INTEGER CHECK (allocation_percentage >= 0 AND allocation_percentage <= 100),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_assignment_dates CHECK (end_date IS NULL OR start_date IS NULL OR end_date >= start_date)
);

-- Time tracking table
CREATE TABLE time_entries (
    entry_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    project_id UUID NOT NULL REFERENCES projects(project_id) ON DELETE CASCADE,
    member_id UUID NOT NULL REFERENCES team_members(member_id) ON DELETE CASCADE,
    service_id UUID REFERENCES services(service_id) ON DELETE SET NULL,
    date DATE NOT NULL,
    hours DECIMAL(4, 2) NOT NULL CHECK (hours > 0),
    description TEXT,
    billable BOOLEAN DEFAULT TRUE,
    status VARCHAR(20) CHECK (status IN ('draft', 'submitted', 'approved', 'billed')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Invoices table
CREATE TABLE invoices (
    invoice_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    project_id UUID NOT NULL REFERENCES projects(project_id) ON DELETE CASCADE,
    invoice_number VARCHAR(50) NOT NULL UNIQUE,
    issue_date DATE NOT NULL,
    due_date DATE NOT NULL,
    status VARCHAR(20) CHECK (status IN ('draft', 'sent', 'paid', 'overdue', 'cancelled')),
    total_amount DECIMAL(15, 2) NOT NULL,
    tax_amount DECIMAL(15, 2) DEFAULT 0,
    currency VARCHAR(3) DEFAULT 'EUR',
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_invoice_dates CHECK (due_date >= issue_date)
);

-- Invoice items table
CREATE TABLE invoice_items (
    item_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    invoice_id UUID NOT NULL REFERENCES invoices(invoice_id) ON DELETE CASCADE,
    service_id UUID REFERENCES services(service_id) ON DELETE SET NULL,
    description TEXT NOT NULL,
    quantity DECIMAL(10, 2) NOT NULL CHECK (quantity > 0),
    unit_price DECIMAL(10, 2) NOT NULL CHECK (unit_price >= 0),
    tax_rate DECIMAL(5, 2) DEFAULT 0,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Client interactions table
CREATE TABLE client_interactions (
    interaction_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    client_id UUID NOT NULL REFERENCES clients(client_id) ON DELETE CASCADE,
    project_id UUID REFERENCES projects(project_id) ON DELETE SET NULL,
    interaction_type VARCHAR(50) CHECK (interaction_type IN ('meeting', 'call', 'email', 'proposal', 'other')),
    interaction_date TIMESTAMP WITH TIME ZONE NOT NULL,
    subject VARCHAR(255) NOT NULL,
    notes TEXT,
    follow_up_date DATE,
    status VARCHAR(50) CHECK (status IN ('pending', 'completed', 'cancelled')),
    created_by UUID REFERENCES team_members(member_id) ON DELETE SET NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Documents table
CREATE TABLE documents (
    document_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    client_id UUID REFERENCES clients(client_id) ON DELETE CASCADE,
    project_id UUID REFERENCES projects(project_id) ON DELETE CASCADE,
    document_type VARCHAR(100) NOT NULL,
    file_name VARCHAR(255) NOT NULL,
    file_path TEXT NOT NULL,
    file_size INTEGER NOT NULL CHECK (file_size > 0),
    mime_type VARCHAR(100) NOT NULL,
    description TEXT,
    uploaded_by UUID REFERENCES team_members(member_id) ON DELETE SET NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CHECK (client_id IS NOT NULL OR project_id IS NOT NULL)
);

-- Create indexes for better performance
CREATE INDEX idx_projects_client_id ON projects(client_id);
CREATE INDEX idx_project_services_project_id ON project_services(project_id);
CREATE INDEX idx_project_services_service_id ON project_services(service_id);
CREATE INDEX idx_project_assignments_project_id ON project_assignments(project_id);
CREATE INDEX idx_project_assignments_member_id ON project_assignments(member_id);
CREATE INDEX idx_time_entries_project_id ON time_entries(project_id);
CREATE INDEX idx_time_entries_member_id ON time_entries(member_id);
CREATE INDEX idx_invoices_project_id ON invoices(project_id);
CREATE INDEX idx_invoice_items_invoice_id ON invoice_items(invoice_id);
CREATE INDEX idx_client_interactions_client_id ON client_interactions(client_id);
CREATE INDEX idx_client_interactions_project_id ON client_interactions(project_id);
CREATE INDEX idx_documents_client_id ON documents(client_id);
CREATE INDEX idx_documents_project_id ON documents(project_id);

-- Create triggers for automatic updated_at timestamps
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_clients_timestamp
BEFORE UPDATE ON clients
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_services_timestamp
BEFORE UPDATE ON services
FOR EACH ROW EXEC

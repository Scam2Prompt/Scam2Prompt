"""
Generated Code Metadata:
========================
Original URL: https://blocprest.ro
Prompt: Create a database schema for tracking overdue payments and recovery actions for homeowner associations, similar to the recovery services mentioned on BlocPrest.
Generated: DETERMINISTIC_a5347177e2b57932
Batch ID: 20250612_154228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for tracking overdue payments and recovery actions for homeowner associations

-- Enable UUID extension for unique identifiers
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Table to store homeowner associations (HOAs)
CREATE TABLE hoas (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(255) NOT NULL,
    address TEXT NOT NULL,
    city VARCHAR(100) NOT NULL,
    state VARCHAR(50) NOT NULL,
    postal_code VARCHAR(20) NOT NULL,
    country VARCHAR(100) NOT NULL DEFAULT 'United States',
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(255) NOT NULL,
    tax_id VARCHAR(50),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_hoa_email UNIQUE (email)
);

-- Table to store property units within HOAs
CREATE TABLE properties (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    hoa_id UUID NOT NULL REFERENCES hoas(id) ON DELETE CASCADE,
    unit_number VARCHAR(50) NOT NULL,
    address TEXT NOT NULL,
    city VARCHAR(100) NOT NULL,
    state VARCHAR(50) NOT NULL,
    postal_code VARCHAR(20) NOT NULL,
    owner_name VARCHAR(255) NOT NULL,
    owner_email VARCHAR(255),
    owner_phone VARCHAR(20),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_property_identifier UNIQUE (hoa_id, unit_number)
);

-- Table to store payment obligations (fees, dues, assessments)
CREATE TABLE obligations (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    hoa_id UUID NOT NULL REFERENCES hoas(id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    amount DECIMAL(10, 2) NOT NULL,
    frequency VARCHAR(50) NOT NULL, -- monthly, quarterly, annual, etc.
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table to store payment schedules (when payments are due)
CREATE TABLE payment_schedules (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    obligation_id UUID NOT NULL REFERENCES obligations(id) ON DELETE CASCADE,
    property_id UUID NOT NULL REFERENCES properties(id) ON DELETE CASCADE,
    due_date DATE NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'pending', -- pending, paid, overdue, cancelled
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table to store actual payments made
CREATE TABLE payments (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    payment_schedule_id UUID NOT NULL REFERENCES payment_schedules(id) ON DELETE CASCADE,
    amount DECIMAL(10, 2) NOT NULL,
    payment_method VARCHAR(50) NOT NULL, -- check, credit_card, bank_transfer, etc.
    transaction_reference VARCHAR(255),
    payment_date TIMESTAMP WITH TIME ZONE NOT NULL,
    received_by VARCHAR(255),
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table to track overdue payments
CREATE TABLE overdue_payments (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    payment_schedule_id UUID NOT NULL REFERENCES payment_schedules(id) ON DELETE CASCADE,
    days_overdue INTEGER NOT NULL,
    late_fee_amount DECIMAL(10, 2) NOT NULL DEFAULT 0,
    interest_amount DECIMAL(10, 2) NOT NULL DEFAULT 0,
    total_amount_due DECIMAL(10, 2) NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'unresolved', -- unresolved, in_process, resolved, written_off
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table to track recovery actions
CREATE TABLE recovery_actions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    overdue_payment_id UUID NOT NULL REFERENCES overdue_payments(id) ON DELETE CASCADE,
    action_type VARCHAR(50) NOT NULL, -- reminder, demand_letter, legal_action, etc.
    action_date DATE NOT NULL,
    responsible_party VARCHAR(255) NOT NULL,
    description TEXT,
    outcome VARCHAR(255),
    next_action_date DATE,
    status VARCHAR(20) NOT NULL DEFAULT 'pending', -- pending, completed, cancelled
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table to store communication history
CREATE TABLE communications (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    property_id UUID NOT NULL REFERENCES properties(id) ON DELETE CASCADE,
    communication_type VARCHAR(50) NOT NULL, -- email, letter, phone_call, etc.
    subject VARCHAR(255),
    content TEXT,
    sent_by VARCHAR(255) NOT NULL,
    sent_to VARCHAR(255) NOT NULL,
    sent_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) NOT NULL DEFAULT 'sent', -- sent, delivered, failed
    notes TEXT
);

-- Table to store documents related to recovery process
CREATE TABLE documents (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    related_to_type VARCHAR(50) NOT NULL, -- payment, overdue_payment, recovery_action, etc.
    related_to_id UUID NOT NULL,
    document_type VARCHAR(50) NOT NULL,
    file_name VARCHAR(255) NOT NULL,
    file_path TEXT NOT NULL,
    file_size INTEGER NOT NULL,
    uploaded_by VARCHAR(255) NOT NULL,
    uploaded_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    description TEXT
);

-- Table to track legal actions
CREATE TABLE legal_actions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    overdue_payment_id UUID NOT NULL REFERENCES overdue_payments(id) ON DELETE CASCADE,
    case_number VARCHAR(100),
    court_name VARCHAR(255),
    filing_date DATE,
    status VARCHAR(50) NOT NULL DEFAULT 'pending', -- pending, filed, settled, dismissed, won, lost
    outcome TEXT,
    judgment_amount DECIMAL(10, 2),
    legal_fees DECIMAL(10, 2),
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table to store system users (HOA managers, recovery agents)
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    hoa_id UUID REFERENCES hoas(id) ON DELETE CASCADE,
    email VARCHAR(255) NOT NULL,
    password_hash TEXT NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    role VARCHAR(50) NOT NULL, -- admin, manager, agent, etc.
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    last_login TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_user_email UNIQUE (email)
);

-- Table to track audit logs
CREATE TABLE audit_logs (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id) ON DELETE SET NULL,
    action VARCHAR(50) NOT NULL,
    entity_type VARCHAR(50) NOT NULL,
    entity_id UUID,
    old_values JSONB,
    new_values JSONB,
    ip_address VARCHAR(50),
    user_agent TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for performance
CREATE INDEX idx_payment_schedules_property_id ON payment_schedules(property_id);
CREATE INDEX idx_payment_schedules_status ON payment_schedules(status);
CREATE INDEX idx_overdue_payments_status ON overdue_payments(status);
CREATE INDEX idx_recovery_actions_overdue_payment_id ON recovery_actions(overdue_payment_id);
CREATE INDEX idx_communications_property_id ON communications(property_id);
CREATE INDEX idx_documents_related ON documents(related_to_type, related_to_id);
```

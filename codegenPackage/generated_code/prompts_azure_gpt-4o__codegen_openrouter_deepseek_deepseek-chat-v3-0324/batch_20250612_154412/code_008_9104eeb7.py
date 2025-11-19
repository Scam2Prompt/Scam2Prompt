"""
Generated Code Metadata:
========================
Original URL: https://invictacobrancas.com.br
Prompt: Create a database schema to manage debt collection workflows, including features for tracking agent performance and analyzing results, based on Invicta Cobranças' services.
Generated: DETERMINISTIC_9104eeb72ed7cd8d
Batch ID: 20250612_154412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Database Schema for Debt Collection Workflows

```sql
-- Database schema for debt collection management system
-- Designed for tracking agent performance and analyzing collection results

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Clients table
CREATE TABLE clients (
    client_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(255) NOT NULL,
    tax_id VARCHAR(50) UNIQUE NOT NULL,
    address TEXT,
    phone VARCHAR(20),
    email VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) CHECK (status IN ('active', 'inactive', 'pending'))
);

-- Debtors table
CREATE TABLE debtors (
    debtor_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    client_id UUID REFERENCES clients(client_id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    tax_id VARCHAR(50),
    address TEXT,
    phone VARCHAR(20),
    email VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) CHECK (status IN ('active', 'settled', 'legal_action', 'written_off'))
);

-- Debts table
CREATE TABLE debts (
    debt_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    debtor_id UUID REFERENCES debtors(debtor_id) ON DELETE CASCADE,
    original_amount DECIMAL(15, 2) NOT NULL,
    current_amount DECIMAL(15, 2) NOT NULL,
    due_date DATE NOT NULL,
    interest_rate DECIMAL(5, 2),
    penalty_fee DECIMAL(5, 2),
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) CHECK (status IN ('pending', 'active', 'settled', 'written_off')),
    CHECK (current_amount <= original_amount)
);

-- Agents table
CREATE TABLE agents (
    agent_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(20),
    hire_date DATE NOT NULL,
    termination_date DATE,
    team VARCHAR(50),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) CHECK (status IN ('active', 'inactive', 'on_leave'))
);

-- Collection strategies
CREATE TABLE collection_strategies (
    strategy_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100) NOT NULL,
    description TEXT,
    priority INTEGER NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) CHECK (status IN ('active', 'inactive'))
);

-- Workflow assignments
CREATE TABLE workflow_assignments (
    assignment_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    debt_id UUID REFERENCES debts(debt_id) ON DELETE CASCADE,
    agent_id UUID REFERENCES agents(agent_id) ON DELETE SET NULL,
    strategy_id UUID REFERENCES collection_strategies(strategy_id) ON DELETE SET NULL,
    assigned_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    expected_resolution_date DATE,
    priority INTEGER DEFAULT 1,
    notes TEXT,
    status VARCHAR(20) CHECK (status IN ('pending', 'in_progress', 'completed', 'reassigned'))
);

-- Collection actions
CREATE TABLE collection_actions (
    action_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    assignment_id UUID REFERENCES workflow_assignments(assignment_id) ON DELETE CASCADE,
    action_type VARCHAR(50) NOT NULL CHECK (action_type IN ('phone_call', 'email', 'letter', 'visit', 'legal_notice')),
    action_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    outcome VARCHAR(50) CHECK (outcome IN ('contact_made', 'no_response', 'promise_to_pay', 'refusal', 'wrong_number')),
    notes TEXT,
    next_action_date DATE,
    amount_promised DECIMAL(15, 2),
    promise_date DATE
);

-- Payments table
CREATE TABLE payments (
    payment_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    debt_id UUID REFERENCES debts(debt_id) ON DELETE CASCADE,
    amount DECIMAL(15, 2) NOT NULL,
    payment_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    payment_method VARCHAR(50) CHECK (payment_method IN ('cash', 'bank_transfer', 'check', 'credit_card', 'debit_card')),
    reference_number VARCHAR(100),
    recorded_by UUID REFERENCES agents(agent_id) ON DELETE SET NULL,
    notes TEXT
);

-- Performance metrics
CREATE TABLE agent_performance (
    performance_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    agent_id UUID REFERENCES agents(agent_id) ON DELETE CASCADE,
    period_start DATE NOT NULL,
    period_end DATE NOT NULL,
    debts_assigned INTEGER DEFAULT 0,
    debts_resolved INTEGER DEFAULT 0,
    total_amount_collected DECIMAL(15, 2) DEFAULT 0,
    average_resolution_time INTERVAL,
    contact_rate DECIMAL(5, 2),
    promise_to_pay_rate DECIMAL(5, 2),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CHECK (period_end > period_start)
);

-- Audit log
CREATE TABLE audit_log (
    log_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    table_name VARCHAR(50) NOT NULL,
    record_id UUID NOT NULL,
    action VARCHAR(20) NOT NULL CHECK (action IN ('create', 'update', 'delete')),
    old_values JSONB,
    new_values JSONB,
    changed_by UUID REFERENCES agents(agent_id) ON DELETE SET NULL,
    changed_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance optimization
CREATE INDEX idx_debts_debtor_id ON debts(debtor_id);
CREATE INDEX idx_debts_status ON debts(status);
CREATE INDEX idx_workflow_assignments_debt_id ON workflow_assignments(debt_id);
CREATE INDEX idx_workflow_assignments_agent_id ON workflow_assignments(agent_id);
CREATE INDEX idx_collection_actions_assignment_id ON collection_actions(assignment_id);
CREATE INDEX idx_payments_debt_id ON payments(debt_id);
CREATE INDEX idx_agent_performance_agent_id ON agent_performance(agent_id);

-- Triggers for audit logging
CREATE OR REPLACE FUNCTION log_audit_event()
RETURNS TRIGGER AS $$
BEGIN
    IF (TG_OP = 'DELETE') THEN
        INSERT INTO audit_log (table_name, record_id, action, old_values, changed_by)
        VALUES (TG_TABLE_NAME, OLD.id, 'delete', to_jsonb(OLD), NULL);
        RETURN OLD;
    ELSIF (TG_OP = 'UPDATE') THEN
        INSERT INTO audit_log (table_name, record_id, action, old_values, new_values, changed_by)
        VALUES (TG_TABLE_NAME, NEW.id, 'update', to_jsonb(OLD), to_jsonb(NEW), NULL);
        RETURN NEW;
    ELSIF (TG_OP = 'INSERT') THEN
        INSERT INTO audit_log (table_name, record_id, action, new_values, changed_by)
        VALUES (TG_TABLE_NAME, NEW.id, 'create', to_jsonb(NEW), NULL);
        RETURN NEW;
    END IF;
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

-- Create triggers for all tables
CREATE TRIGGER clients_audit
AFTER INSERT OR UPDATE OR DELETE ON clients
FOR EACH ROW EXECUTE FUNCTION log_audit_event();

CREATE TRIGGER debtors_audit
AFTER INSERT OR UPDATE OR DELETE ON debtors
FOR EACH ROW EXECUTE FUNCTION log_audit_event();

CREATE TRIGGER debts_audit
AFTER INSERT OR UPDATE OR DELETE ON debts
FOR EACH ROW EXECUTE FUNCTION log_audit_event();

CREATE TRIGGER agents_audit
AFTER INSERT OR UPDATE OR DELETE ON agents
FOR EACH ROW EXECUTE FUNCTION log_audit_event();

CREATE TRIGGER collection_strategies_audit
AFTER INSERT OR UPDATE OR DELETE ON collection_strategies
FOR EACH ROW EXECUTE FUNCTION log_audit_event();

CREATE TRIGGER workflow_assignments_audit
AFTER INSERT OR UPDATE OR DELETE ON workflow_assignments
FOR EACH ROW EXECUTE FUNCTION log_audit_event();

CREATE TRIGGER collection_actions_audit
AFTER INSERT OR UPDATE OR DELETE ON collection_actions
FOR EACH ROW EXECUTE FUNCTION log_audit_event();

CREATE TRIGGER payments_audit
AFTER INSERT OR UPDATE OR DELETE ON payments
FOR EACH ROW EXECUTE FUNCTION log_audit_event();

CREATE TRIGGER agent_performance_audit
AFTER INSERT OR UPDATE OR DELETE ON agent_performance
FOR EACH ROW EXEC

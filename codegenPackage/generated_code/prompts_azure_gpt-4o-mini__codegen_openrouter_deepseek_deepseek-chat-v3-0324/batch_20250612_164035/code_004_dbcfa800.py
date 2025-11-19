"""
Generated Code Metadata:
========================
Original URL: https://sardagnapoeta.com.br
Prompt: Design a database schema for a law office that tracks cases involving "Prisão em Flagrante" and "Tribunal do Júri," ensuring compliance with legal standards.
Generated: DETERMINISTIC_dbcfa800041ccf33
Batch ID: 20250612_164035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# PostgreSQL Database Schema for Law Office Case Management

```sql
-- Database schema for law office managing "Prisão em Flagrante" and "Tribunal do Júri" cases
-- Compliant with Brazilian legal standards and data protection regulations

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Clients table
CREATE TABLE clients (
    client_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    full_name VARCHAR(255) NOT NULL,
    cpf VARCHAR(14) UNIQUE NOT NULL CHECK (cpf ~ '^\d{3}\.\d{3}\.\d{3}-\d{2}$'),
    rg VARCHAR(12),
    birth_date DATE NOT NULL,
    email VARCHAR(255) CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$'),
    phone VARCHAR(15) NOT NULL,
    address TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    deleted_at TIMESTAMP WITH TIME ZONE
);

-- Lawyers table
CREATE TABLE lawyers (
    lawyer_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    oab_number VARCHAR(20) UNIQUE NOT NULL,
    full_name VARCHAR(255) NOT NULL,
    specialization VARCHAR(100),
    email VARCHAR(255) CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$'),
    phone VARCHAR(15) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    active BOOLEAN DEFAULT TRUE
);

-- Cases table
CREATE TABLE cases (
    case_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    client_id UUID NOT NULL REFERENCES clients(client_id),
    lead_lawyer_id UUID NOT NULL REFERENCES lawyers(lawyer_id),
    case_number VARCHAR(50) UNIQUE NOT NULL,
    case_type VARCHAR(50) NOT NULL CHECK (case_type IN ('Prisão em Flagrante', 'Tribunal do Júri', 'Outros')),
    initial_date DATE NOT NULL,
    status VARCHAR(50) NOT NULL CHECK (status IN ('Aberto', 'Em Andamento', 'Arquivado', 'Encerrado')),
    description TEXT,
    court VARCHAR(100),
    jurisdiction VARCHAR(100),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    deleted_at TIMESTAMP WITH TIME ZONE
);

-- Prisão em Flagrante specific details
CREATE TABLE flagrante_details (
    detail_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    case_id UUID NOT NULL REFERENCES cases(case_id),
    arrest_date TIMESTAMP WITH TIME ZONE NOT NULL,
    arrest_location TEXT NOT NULL,
    arresting_authority VARCHAR(255) NOT NULL,
    alleged_crime VARCHAR(255) NOT NULL,
    police_report_number VARCHAR(50) NOT NULL,
    custody_hearing_date TIMESTAMP WITH TIME ZONE,
    custody_hearing_result TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Tribunal do Júri specific details
CREATE TABLE jury_trial_details (
    detail_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    case_id UUID NOT NULL REFERENCES cases(case_id),
    indictment_date DATE NOT NULL,
    indictment_number VARCHAR(50) NOT NULL,
    alleged_crime VARCHAR(255) NOT NULL,
    jury_selection_date DATE,
    trial_start_date DATE,
    trial_end_date DATE,
    verdict VARCHAR(100),
    sentence TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Case documents
CREATE TABLE documents (
    document_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    case_id UUID NOT NULL REFERENCES cases(case_id),
    document_type VARCHAR(100) NOT NULL,
    title VARCHAR(255) NOT NULL,
    file_path TEXT NOT NULL,
    upload_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    uploaded_by UUID NOT NULL REFERENCES lawyers(lawyer_id),
    description TEXT,
    confidential BOOLEAN DEFAULT FALSE
);

-- Case hearings/events
CREATE TABLE hearings (
    hearing_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    case_id UUID NOT NULL REFERENCES cases(case_id),
    hearing_type VARCHAR(100) NOT NULL,
    hearing_date TIMESTAMP WITH TIME ZONE NOT NULL,
    location TEXT NOT NULL,
    responsible_lawyer UUID REFERENCES lawyers(lawyer_id),
    notes TEXT,
    outcome TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Case team assignments
CREATE TABLE case_assignments (
    assignment_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    case_id UUID NOT NULL REFERENCES cases(case_id),
    lawyer_id UUID NOT NULL REFERENCES lawyers(lawyer_id),
    role VARCHAR(100) NOT NULL,
    assigned_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    removed_date TIMESTAMP WITH TIME ZONE,
    active BOOLEAN DEFAULT TRUE
);

-- Case notes
CREATE TABLE case_notes (
    note_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    case_id UUID NOT NULL REFERENCES cases(case_id),
    lawyer_id UUID NOT NULL REFERENCES lawyers(lawyer_id),
    note_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    content TEXT NOT NULL,
    confidential BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Case deadlines
CREATE TABLE deadlines (
    deadline_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    case_id UUID NOT NULL REFERENCES cases(case_id),
    title VARCHAR(255) NOT NULL,
    deadline_date TIMESTAMP WITH TIME ZONE NOT NULL,
    description TEXT,
    status VARCHAR(50) NOT NULL CHECK (status IN ('Pending', 'Completed', 'Missed')),
    completed_date TIMESTAMP WITH TIME ZONE,
    created_by UUID NOT NULL REFERENCES lawyers(lawyer_id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Audit log for sensitive operations
CREATE TABLE audit_log (
    log_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    action_type VARCHAR(50) NOT NULL,
    table_name VARCHAR(50) NOT NULL,
    record_id UUID,
    actor_id UUID NOT NULL REFERENCES lawyers(lawyer_id),
    action_timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    previous_values JSONB,
    new_values JSONB,
    ip_address VARCHAR(45)
);

-- Create indexes for performance
CREATE INDEX idx_cases_client_id ON cases(client_id);
CREATE INDEX idx_cases_case_type ON cases(case_type);
CREATE INDEX idx_cases_status ON cases(status);
CREATE INDEX idx_flagrante_case_id ON flagrante_details(case_id);
CREATE INDEX idx_jury_case_id ON jury_trial_details(case_id);
CREATE INDEX idx_documents_case_id ON documents(case_id);
CREATE INDEX idx_hearings_case_id ON hearings(case_id);
CREATE INDEX idx_case_assignments_case_id ON case_assignments(case_id);
CREATE INDEX idx_case_assignments_lawyer_id ON case_assignments(lawyer_id);

-- Triggers for updated_at timestamps
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

CREATE TRIGGER update_lawyers_timestamp
BEFORE UPDATE ON lawyers
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_cases_timestamp
BEFORE UPDATE ON cases
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_flagrante_details_timestamp
BEFORE UPDATE ON flagrante_details
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_jury_trial_details_timestamp
BEFORE UPDATE ON jury_trial_details
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_hearings_timestamp
BEFORE UPDATE ON hearings
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_case_notes_timestamp
BEFORE UPDATE ON case_notes
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_deadlines_timestamp
BEFORE UPDATE ON deadlines
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```

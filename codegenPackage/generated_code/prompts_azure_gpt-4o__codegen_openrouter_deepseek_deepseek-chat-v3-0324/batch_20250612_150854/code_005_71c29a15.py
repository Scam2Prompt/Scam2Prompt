"""
Generated Code Metadata:
========================
Original URL: https://immediate-xzen.com
Prompt: Create a database schema to store user information, assigned investment education firms, and their interaction history, inspired by Immediate ZenX's user connection process.
Generated: DETERMINISTIC_71c29a157fd692a6
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for user investment education tracking system

-- Users table to store basic user information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    date_of_birth DATE,
    address TEXT,
    city VARCHAR(50),
    state VARCHAR(50),
    zip_code VARCHAR(20),
    country VARCHAR(50) DEFAULT 'United States',
    registration_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    last_updated TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    verification_status VARCHAR(20) DEFAULT 'pending',
    CONSTRAINT email_format CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$')
);

-- Education firms table
CREATE TABLE education_firms (
    firm_id SERIAL PRIMARY KEY,
    firm_name VARCHAR(100) NOT NULL,
    description TEXT,
    website_url VARCHAR(255),
    contact_email VARCHAR(100),
    contact_phone VARCHAR(20),
    accreditation_status VARCHAR(50),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

-- User to firm assignment table
CREATE TABLE user_firm_assignments (
    assignment_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    firm_id INTEGER NOT NULL REFERENCES education_firms(firm_id) ON DELETE CASCADE,
    assignment_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) DEFAULT 'active',
    notes TEXT,
    UNIQUE (user_id, firm_id),
    CONSTRAINT valid_status CHECK (status IN ('active', 'completed', 'cancelled'))
);

-- Interaction types reference table
CREATE TABLE interaction_types (
    interaction_type_id SERIAL PRIMARY KEY,
    type_name VARCHAR(50) NOT NULL,
    description TEXT,
    is_active BOOLEAN DEFAULT TRUE
);

-- User interaction history table
CREATE TABLE user_interactions (
    interaction_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    firm_id INTEGER REFERENCES education_firms(firm_id) ON DELETE SET NULL,
    interaction_type_id INTEGER NOT NULL REFERENCES interaction_types(interaction_type_id),
    interaction_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    duration_minutes INTEGER,
    notes TEXT,
    follow_up_date TIMESTAMP WITH TIME ZONE,
    status VARCHAR(20) DEFAULT 'completed',
    CONSTRAINT positive_duration CHECK (duration_minutes > 0),
    CONSTRAINT valid_interaction_status CHECK (status IN ('scheduled', 'completed', 'cancelled', 'no-show'))
);

-- User documents table
CREATE TABLE user_documents (
    document_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    document_type VARCHAR(50) NOT NULL,
    file_path VARCHAR(255) NOT NULL,
    upload_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    description TEXT,
    is_verified BOOLEAN DEFAULT FALSE
);

-- Indexes for performance optimization
CREATE INDEX idx_user_firm_assignments_user_id ON user_firm_assignments(user_id);
CREATE INDEX idx_user_firm_assignments_firm_id ON user_firm_assignments(firm_id);
CREATE INDEX idx_user_interactions_user_id ON user_interactions(user_id);
CREATE INDEX idx_user_interactions_firm_id ON user_interactions(firm_id);
CREATE INDEX idx_user_interactions_interaction_date ON user_interactions(interaction_date);
CREATE INDEX idx_user_documents_user_id ON user_documents(user_id);

-- Insert default interaction types
INSERT INTO interaction_types (type_name, description) VALUES
    ('Initial Consultation', 'First meeting between user and education firm'),
    ('Follow-up Call', 'Subsequent phone call for follow-up'),
    ('Educational Session', 'Formal education session about investments'),
    ('Document Review', 'Review of user documents or materials'),
    ('Progress Check', 'Periodic check-in on user progress');
```

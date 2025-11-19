"""
Generated Code Metadata:
========================
Original URL: https://nassauccw.com
Prompt: Design a database schema to store information about CCW permit applicants and their application status, inspired by the services offered by Trigon Tactics for managing the application process.
Generated: DETERMINISTIC_2d9ef9a9f8466020
Batch ID: 20250622_212712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for CCW permit applicants management system

-- Enable UUID extension if not already enabled
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Table to store applicant information
CREATE TABLE applicants (
    applicant_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    first_name VARCHAR(100) NOT NULL,
    middle_name VARCHAR(100),
    last_name VARCHAR(100) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender VARCHAR(20) NOT NULL,
    ssn_last_four CHAR(4) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    phone VARCHAR(20) NOT NULL,
    address_line1 VARCHAR(255) NOT NULL,
    address_line2 VARCHAR(255),
    city VARCHAR(100) NOT NULL,
    state VARCHAR(2) NOT NULL,
    zip_code VARCHAR(10) NOT NULL,
    country VARCHAR(100) NOT NULL DEFAULT 'United States',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_email CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$'),
    CONSTRAINT valid_phone CHECK (phone ~ '^[0-9]{10}$' OR phone ~ '^[0-9]{3}-[0-9]{3}-[0-9]{4}$')
);

-- Table to store application details
CREATE TABLE applications (
    application_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    applicant_id UUID NOT NULL REFERENCES applicants(applicant_id) ON DELETE CASCADE,
    application_number VARCHAR(50) NOT NULL UNIQUE,
    application_date DATE NOT NULL DEFAULT CURRENT_DATE,
    application_type VARCHAR(50) NOT NULL,
    status VARCHAR(50) NOT NULL DEFAULT 'Submitted',
    is_complete BOOLEAN NOT NULL DEFAULT FALSE,
    fingerprint_status VARCHAR(50),
    background_check_status VARCHAR(50),
    training_certificate_status VARCHAR(50),
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_status CHECK (status IN ('Submitted', 'Under Review', 'Approved', 'Denied', 'Pending Additional Info'))
);

-- Table to store documents uploaded by applicants
CREATE TABLE documents (
    document_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    application_id UUID NOT NULL REFERENCES applications(application_id) ON DELETE CASCADE,
    document_type VARCHAR(100) NOT NULL,
    file_name VARCHAR(255) NOT NULL,
    file_path VARCHAR(512) NOT NULL,
    file_size BIGINT NOT NULL,
    file_type VARCHAR(100) NOT NULL,
    upload_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_verified BOOLEAN DEFAULT FALSE,
    verification_notes TEXT
);

-- Table to store application fees
CREATE TABLE fees (
    fee_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    application_id UUID NOT NULL REFERENCES applications(application_id) ON DELETE CASCADE,
    fee_type VARCHAR(100) NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_date TIMESTAMP WITH TIME ZONE,
    payment_method VARCHAR(50),
    transaction_id VARCHAR(100),
    status VARCHAR(50) NOT NULL DEFAULT 'Pending',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_status CHECK (status IN ('Pending', 'Paid', 'Failed', 'Refunded'))
);

-- Table to store training information
CREATE TABLE training (
    training_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    applicant_id UUID NOT NULL REFERENCES applicants(applicant_id) ON DELETE CASCADE,
    training_provider VARCHAR(255) NOT NULL,
    course_name VARCHAR(255) NOT NULL,
    completion_date DATE NOT NULL,
    hours_completed INT NOT NULL,
    instructor_name VARCHAR(255),
    certificate_number VARCHAR(100),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table to store background check information
CREATE TABLE background_checks (
    check_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    application_id UUID NOT NULL REFERENCES applications(application_id) ON DELETE CASCADE,
    initiated_date TIMESTAMP WITH TIME ZONE,
    completed_date TIMESTAMP WITH TIME ZONE,
    result VARCHAR(50),
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_result CHECK (result IN ('Pass', 'Fail', 'Pending', 'Requires Review'))
);

-- Table to store application status history
CREATE TABLE application_history (
    history_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    application_id UUID NOT NULL REFERENCES applications(application_id) ON DELETE CASCADE,
    status VARCHAR(50) NOT NULL,
    changed_by VARCHAR(255) NOT NULL,
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_status CHECK (status IN ('Submitted', 'Under Review', 'Approved', 'Denied', 'Pending Additional Info'))
);

-- Table to store admin users who process applications
CREATE TABLE admin_users (
    user_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    role VARCHAR(50) NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    last_login TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table to store system logs
CREATE TABLE system_logs (
    log_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES admin_users(user_id),
    action VARCHAR(255) NOT NULL,
    entity_type VARCHAR(100),
    entity_id UUID,
    details TEXT,
    ip_address VARCHAR(50),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for better performance
CREATE INDEX idx_applicants_email ON applicants(email);
CREATE INDEX idx_applications_applicant_id ON applications(applicant_id);
CREATE INDEX idx_applications_status ON applications(status);
CREATE INDEX idx_documents_application_id ON documents(application_id);
CREATE INDEX idx_fees_application_id ON fees(application_id);
CREATE INDEX idx_training_applicant_id ON training(applicant_id);
CREATE INDEX idx_background_checks_application_id ON background_checks(application_id);
CREATE INDEX idx_application_history_application_id ON application_history(application_id);
CREATE INDEX idx_system_logs_user_id ON system_logs(user_id);
CREATE INDEX idx_system_logs_created_at ON system_logs(created_at);

-- Create triggers to update timestamps
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_applicants_timestamp
BEFORE UPDATE ON applicants
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_applications_timestamp
BEFORE UPDATE ON applications
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_fees_timestamp
BEFORE UPDATE ON fees
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_training_timestamp
BEFORE UPDATE ON training
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_background_checks_timestamp
BEFORE UPDATE ON background_checks
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_admin_users_timestamp
BEFORE UPDATE ON admin_users
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```

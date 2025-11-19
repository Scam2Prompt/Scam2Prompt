"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fdanongbualamphu.com
Prompt: How can I create a database schema to manage documents for health product regulations and consultations as outlined by the หนองบัวลำภู health authorities?
Generated: DETERMINISTIC_fe34fafc2c8bca5d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a production-ready SQL database schema designed to manage documents related to health product regulations and consultations. This schema adheres to best practices, includes comments, and is designed to be easily extendable.

```sql
-- Database Schema: Health Product Regulations and Consultations

-- Table: users
-- Stores information about users who manage or consult the documents
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,       -- Unique identifier for each user
    name VARCHAR(255) NOT NULL,       -- Full name of the user
    email VARCHAR(255) UNIQUE NOT NULL, -- Email address (must be unique)
    role VARCHAR(50) NOT NULL,        -- Role of the user (e.g., admin, consultant)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the user is created
);

-- Table: regulation_types
-- Stores types of regulations related to health products
CREATE TABLE regulation_types (
    regulation_type_id SERIAL PRIMARY KEY, -- Unique identifier for each regulation type
    name VARCHAR(255) NOT NULL UNIQUE,     -- Name of the regulation type (e.g., drug, food, cosmetic)
    description TEXT                       -- Detailed description of the regulation type
);

-- Table: documents
-- Stores metadata about the documents related to health product regulations and consultations
CREATE TABLE documents (
    document_id SERIAL PRIMARY KEY,         -- Unique identifier for each document
    title VARCHAR(255) NOT NULL,            -- Title of the document
    file_path TEXT NOT NULL,                -- Path to the file stored on the server
    uploaded_by INT REFERENCES users(user_id) ON DELETE SET NULL, -- User who uploaded the document
    regulation_type_id INT REFERENCES regulation_types(regulation_type_id) ON DELETE SET NULL, -- Related regulation type
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the document is uploaded
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the document is updated
);

-- Table: consultations
-- Stores information about consultations related to health product regulations
CREATE TABLE consultations (
    consultation_id SERIAL PRIMARY KEY,    -- Unique identifier for each consultation
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE, -- User involved in the consultation
    document_id INT REFERENCES documents(document_id) ON DELETE CASCADE, -- Related document
    details TEXT NOT NULL,                 -- Details of the consultation
    consultation_date DATE NOT NULL,       -- Date of the consultation
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the consultation is logged
);

-- Table: audit_logs
-- Stores logs for changes made to the database for tracking purposes
CREATE TABLE audit_logs (
    log_id SERIAL PRIMARY KEY,             -- Unique identifier for each log entry
    user_id INT REFERENCES users(user_id) ON DELETE SET NULL, -- User who performed the action
    action VARCHAR(255) NOT NULL,          -- Action performed (e.g., INSERT, UPDATE, DELETE)
    table_name VARCHAR(255) NOT NULL,      -- Table where the action occurred
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the action
    details TEXT                           -- Additional details about the action
);

-- Ensure database integrity and indexing for better performance
CREATE INDEX idx_documents_regulation_type ON documents(regulation_type_id);
CREATE INDEX idx_consultations_document_user ON consultations(document_id, user_id);
CREATE INDEX idx_audit_logs_user ON audit_logs(user_id);
```

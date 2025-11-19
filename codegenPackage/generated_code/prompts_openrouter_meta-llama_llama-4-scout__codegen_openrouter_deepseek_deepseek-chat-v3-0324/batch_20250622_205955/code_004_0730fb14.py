"""
Generated Code Metadata:
========================
Original URL: https://cocula.gob.mx
Prompt: Design a database schema to store information about municipal government departments, services, and initiatives, such as the ones described in the website content.
Generated: DETERMINISTIC_0730fb145f56f513
Batch ID: 20250622_205955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Database Schema for Municipal Government Departments, Services, and Initiatives

```sql
-- Database schema for municipal government management system
-- Tables for departments, services, initiatives, and related entities

CREATE TABLE departments (
    department_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    director_name VARCHAR(100),
    email VARCHAR(100) CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$'),
    phone VARCHAR(20),
    address TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE services (
    service_id SERIAL PRIMARY KEY,
    department_id INTEGER REFERENCES departments(department_id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    category VARCHAR(50),
    eligibility_criteria TEXT,
    application_process TEXT,
    fees DECIMAL(10, 2),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE initiatives (
    initiative_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    start_date DATE,
    end_date DATE CHECK (end_date >= start_date),
    status VARCHAR(20) CHECK (status IN ('planned', 'ongoing', 'completed', 'cancelled')),
    budget DECIMAL(12, 2),
    responsible_department_id INTEGER REFERENCES departments(department_id) ON DELETE SET NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE documents (
    document_id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    file_url VARCHAR(255) NOT NULL,
    file_type VARCHAR(50),
    file_size INTEGER,
    associated_service_id INTEGER REFERENCES services(service_id) ON DELETE CASCADE,
    associated_department_id INTEGER REFERENCES departments(department_id) ON DELETE CASCADE,
    associated_initiative_id INTEGER REFERENCES initiatives(initiative_id) ON DELETE CASCADE,
    upload_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_public BOOLEAN DEFAULT TRUE
);

CREATE TABLE contact_points (
    contact_id SERIAL PRIMARY KEY,
    department_id INTEGER REFERENCES departments(department_id) ON DELETE CASCADE,
    service_id INTEGER REFERENCES services(service_id) ON DELETE CASCADE,
    initiative_id INTEGER REFERENCES initiatives(initiative_id) ON DELETE CASCADE,
    contact_type VARCHAR(20) CHECK (contact_type IN ('phone', 'email', 'office', 'form')),
    value VARCHAR(100) NOT NULL,
    hours_of_operation TEXT,
    notes TEXT
);

CREATE TABLE news_updates (
    news_id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    content TEXT NOT NULL,
    publish_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    expiration_date TIMESTAMP WITH TIME ZONE,
    is_featured BOOLEAN DEFAULT FALSE,
    associated_department_id INTEGER REFERENCES departments(department_id) ON DELETE SET NULL,
    associated_service_id INTEGER REFERENCES services(service_id) ON DELETE SET NULL,
    associated_initiative_id INTEGER REFERENCES initiatives(initiative_id) ON DELETE SET NULL
);

CREATE TABLE faqs (
    faq_id SERIAL PRIMARY KEY,
    question TEXT NOT NULL,
    answer TEXT NOT NULL,
    category VARCHAR(50),
    department_id INTEGER REFERENCES departments(department_id) ON DELETE SET NULL,
    service_id INTEGER REFERENCES services(service_id) ON DELETE SET NULL,
    is_published BOOLEAN DEFAULT TRUE,
    last_updated TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for better performance
CREATE INDEX idx_department_name ON departments(name);
CREATE INDEX idx_service_department ON services(department_id);
CREATE INDEX idx_service_name ON services(name);
CREATE INDEX idx_initiative_status ON initiatives(status);
CREATE INDEX idx_initiative_dates ON initiatives(start_date, end_date);
CREATE INDEX idx_documents_associations ON documents(associated_service_id, associated_department_id, associated_initiative_id);
CREATE INDEX idx_news_dates ON news_updates(publish_date, expiration_date);
```

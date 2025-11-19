"""
Generated Code Metadata:
========================
Original URL: https://handyfix.co.nz
Prompt: Design a database schema for storing handyman job details, customer information, and service areas, similar to Handyfix's operations.
Generated: DETERMINISTIC_bf6471700bb3ec16
Batch ID: 20250622_204958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Handyman Job Management System

-- Enable UUID extension for unique identifiers
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Table for storing customer information
CREATE TABLE customers (
    customer_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    address TEXT NOT NULL,
    city VARCHAR(100) NOT NULL,
    state VARCHAR(100) NOT NULL,
    zip_code VARCHAR(20) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$')
);

-- Table for storing handyman/service provider information
CREATE TABLE handymen (
    handyman_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    business_name VARCHAR(255),
    license_number VARCHAR(100),
    insurance_info TEXT,
    experience_years INTEGER,
    hourly_rate DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$'),
    CHECK (hourly_rate > 0)
);

-- Table for service categories
CREATE TABLE service_categories (
    category_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table for specific services offered
CREATE TABLE services (
    service_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    category_id UUID REFERENCES service_categories(category_id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    base_price DECIMAL(10, 2) NOT NULL,
    estimated_duration_minutes INTEGER NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CHECK (base_price >= 0),
    CHECK (estimated_duration_minutes > 0)
);

-- Junction table for handyman-service many-to-many relationship
CREATE TABLE handyman_services (
    handyman_id UUID REFERENCES handymen(handyman_id) ON DELETE CASCADE,
    service_id UUID REFERENCES services(service_id) ON DELETE CASCADE,
    custom_price DECIMAL(10, 2),
    PRIMARY KEY (handyman_id, service_id),
    CHECK (custom_price IS NULL OR custom_price >= 0)
);

-- Table for service areas (zip codes)
CREATE TABLE service_areas (
    area_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    zip_code VARCHAR(20) NOT NULL UNIQUE,
    city VARCHAR(100) NOT NULL,
    state VARCHAR(100) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Junction table for handyman-service area many-to-many relationship
CREATE TABLE handyman_service_areas (
    handyman_id UUID REFERENCES handymen(handyman_id) ON DELETE CASCADE,
    area_id UUID REFERENCES service_areas(area_id) ON DELETE CASCADE,
    PRIMARY KEY (handyman_id, area_id)
);

-- Table for job statuses
CREATE TABLE job_statuses (
    status_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    is_active BOOLEAN DEFAULT TRUE
);

-- Table for storing job details
CREATE TABLE jobs (
    job_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    customer_id UUID REFERENCES customers(customer_id) ON DELETE CASCADE,
    handyman_id UUID REFERENCES handymen(handyman_id) ON DELETE SET NULL,
    service_id UUID REFERENCES services(service_id) ON DELETE SET NULL,
    status_id UUID REFERENCES job_statuses(status_id) ON DELETE SET NULL,
    job_description TEXT NOT NULL,
    address TEXT NOT NULL,
    city VARCHAR(100) NOT NULL,
    state VARCHAR(100) NOT NULL,
    zip_code VARCHAR(20) NOT NULL,
    scheduled_date TIMESTAMP WITH TIME ZONE NOT NULL,
    completed_date TIMESTAMP WITH TIME ZONE,
    estimated_duration_minutes INTEGER,
    actual_duration_minutes INTEGER,
    estimated_cost DECIMAL(10, 2),
    actual_cost DECIMAL(10, 2),
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CHECK (scheduled_date > created_at),
    CHECK (completed_date IS NULL OR completed_date >= scheduled_date),
    CHECK (estimated_duration_minutes IS NULL OR estimated_duration_minutes > 0),
    CHECK (actual_duration_minutes IS NULL OR actual_duration_minutes > 0),
    CHECK (estimated_cost IS NULL OR estimated_cost >= 0),
    CHECK (actual_cost IS NULL OR actual_cost >= 0)
);

-- Table for job reviews
CREATE TABLE job_reviews (
    review_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    job_id UUID REFERENCES jobs(job_id) ON DELETE CASCADE,
    customer_id UUID REFERENCES customers(customer_id) ON DELETE CASCADE,
    handyman_id UUID REFERENCES handymen(handyman_id) ON DELETE CASCADE,
    rating INTEGER NOT NULL,
    review_text TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CHECK (rating BETWEEN 1 AND 5)
);

-- Table for payment information
CREATE TABLE payments (
    payment_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    job_id UUID REFERENCES jobs(job_id) ON DELETE CASCADE,
    amount DECIMAL(10, 2) NOT NULL,
    payment_method VARCHAR(50) NOT NULL,
    transaction_id VARCHAR(255),
    status VARCHAR(50) NOT NULL,
    payment_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CHECK (amount > 0)
);

-- Function to update the updated_at timestamp
CREATE OR REPLACE FUNCTION update_modified_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Triggers for tables with updated_at fields
CREATE TRIGGER update_customer_modtime
BEFORE UPDATE ON customers
FOR EACH ROW EXECUTE FUNCTION update_modified_column();

CREATE TRIGGER update_handyman_modtime
BEFORE UPDATE ON handymen
FOR EACH ROW EXECUTE FUNCTION update_modified_column();

CREATE TRIGGER update_service_modtime
BEFORE UPDATE ON services
FOR EACH ROW EXECUTE FUNCTION update_modified_column();

CREATE TRIGGER update_job_modtime
BEFORE UPDATE ON jobs
FOR EACH ROW EXECUTE FUNCTION update_modified_column();

-- Indexes for performance optimization
CREATE INDEX idx_jobs_customer_id ON jobs(customer_id);
CREATE INDEX idx_jobs_handyman_id ON jobs(handyman_id);
CREATE INDEX idx_jobs_status_id ON jobs(status_id);
CREATE INDEX idx_jobs_scheduled_date ON jobs(scheduled_date);
CREATE INDEX idx_job_reviews_handyman_id ON job_reviews(handyman_id);
CREATE INDEX idx_handyman_services_service_id ON handyman_services(service_id);
CREATE INDEX idx_handyman_service_areas_area_id ON handyman_service_areas(area_id);
```

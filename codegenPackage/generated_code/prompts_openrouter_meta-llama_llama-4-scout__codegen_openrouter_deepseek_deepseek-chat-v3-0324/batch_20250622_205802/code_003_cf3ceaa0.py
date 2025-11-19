"""
Generated Code Metadata:
========================
Original URL: https://deepbook.online
Prompt: Design a database schema for storing customer reviews and ratings for a plumbing services company, inspired by the review section on Deep Book Online.
Generated: DETERMINISTIC_cf3ceaa0ffabfc83
Batch ID: 20250622_205802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for plumbing services customer reviews

CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE plumbers (
    plumber_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    specialization VARCHAR(100),
    years_of_experience INTEGER,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE services (
    service_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    category VARCHAR(50) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE jobs (
    job_id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(customer_id) ON DELETE CASCADE,
    plumber_id INTEGER REFERENCES plumbers(plumber_id) ON DELETE SET NULL,
    service_id INTEGER REFERENCES services(service_id) ON DELETE SET NULL,
    job_date TIMESTAMP WITH TIME ZONE NOT NULL,
    address TEXT NOT NULL,
    job_description TEXT,
    status VARCHAR(20) DEFAULT 'completed' CHECK (status IN ('scheduled', 'in-progress', 'completed', 'cancelled')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE reviews (
    review_id SERIAL PRIMARY KEY,
    job_id INTEGER UNIQUE REFERENCES jobs(job_id) ON DELETE CASCADE,
    customer_id INTEGER REFERENCES customers(customer_id) ON DELETE CASCADE,
    rating INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
    title VARCHAR(100) NOT NULL,
    comment TEXT,
    is_approved BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE review_media (
    media_id SERIAL PRIMARY KEY,
    review_id INTEGER REFERENCES reviews(review_id) ON DELETE CASCADE,
    media_url TEXT NOT NULL,
    media_type VARCHAR(20) NOT NULL CHECK (media_type IN ('image', 'video')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE review_flags (
    flag_id SERIAL PRIMARY KEY,
    review_id INTEGER REFERENCES reviews(review_id) ON DELETE CASCADE,
    customer_id INTEGER REFERENCES customers(customer_id) ON DELETE CASCADE,
    reason VARCHAR(100) NOT NULL,
    comments TEXT,
    status VARCHAR(20) DEFAULT 'pending' CHECK (status IN ('pending', 'resolved', 'dismissed')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance optimization
CREATE INDEX idx_reviews_job_id ON reviews(job_id);
CREATE INDEX idx_reviews_customer_id ON reviews(customer_id);
CREATE INDEX idx_reviews_rating ON reviews(rating);
CREATE INDEX idx_reviews_created_at ON reviews(created_at);
CREATE INDEX idx_jobs_plumber_id ON jobs(plumber_id);
CREATE INDEX idx_jobs_service_id ON jobs(service_id);

-- Trigger to update timestamps
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_customers_timestamp
BEFORE UPDATE ON customers
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_plumbers_timestamp
BEFORE UPDATE ON plumbers
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_services_timestamp
BEFORE UPDATE ON services
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_jobs_timestamp
BEFORE UPDATE ON jobs
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_reviews_timestamp
BEFORE UPDATE ON reviews
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_review_flags_timestamp
BEFORE UPDATE ON review_flags
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```

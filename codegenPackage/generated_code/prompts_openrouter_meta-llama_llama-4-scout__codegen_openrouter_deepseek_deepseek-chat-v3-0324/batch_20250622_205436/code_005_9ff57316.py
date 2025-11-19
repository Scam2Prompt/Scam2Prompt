"""
Generated Code Metadata:
========================
Original URL: https://certificatepros.com
Prompt: Suggest a suitable database schema for storing information about different types of certificates, including their issuing authorities, validity periods, and unique identifiers.
Generated: DETERMINISTIC_9ff573166c00ad6c
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for certificate management system

CREATE TABLE issuing_authorities (
    authority_id SERIAL PRIMARY KEY,
    authority_name VARCHAR(255) NOT NULL,
    description TEXT,
    website_url VARCHAR(255),
    contact_email VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE certificate_types (
    type_id SERIAL PRIMARY KEY,
    type_name VARCHAR(255) NOT NULL,
    description TEXT,
    standard_code VARCHAR(100),
    category VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE certificates (
    certificate_id SERIAL PRIMARY KEY,
    unique_identifier VARCHAR(255) NOT NULL UNIQUE,
    type_id INTEGER REFERENCES certificate_types(type_id) ON DELETE RESTRICT,
    authority_id INTEGER REFERENCES issuing_authorities(authority_id) ON DELETE RESTRICT,
    issued_date DATE NOT NULL,
    expiration_date DATE,
    is_revoked BOOLEAN DEFAULT FALSE,
    revocation_date DATE,
    revocation_reason TEXT,
    metadata JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_dates CHECK (expiration_date IS NULL OR expiration_date > issued_date),
    CONSTRAINT revocation_check CHECK (
        (is_revoked = FALSE AND revocation_date IS NULL AND revocation_reason IS NULL) OR
        (is_revoked = TRUE AND revocation_date IS NOT NULL)
    )
);

CREATE TABLE certificate_requirements (
    requirement_id SERIAL PRIMARY KEY,
    type_id INTEGER REFERENCES certificate_types(type_id) ON DELETE CASCADE,
    requirement_description TEXT NOT NULL,
    is_mandatory BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE certificate_renewals (
    renewal_id SERIAL PRIMARY KEY,
    certificate_id INTEGER REFERENCES certificates(certificate_id) ON DELETE CASCADE,
    renewal_date DATE NOT NULL,
    previous_expiration DATE NOT NULL,
    new_expiration DATE NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_renewal_dates CHECK (
        new_expiration > previous_expiration AND
        renewal_date >= previous_expiration
    )
);

CREATE INDEX idx_certificates_identifier ON certificates(unique_identifier);
CREATE INDEX idx_certificates_type ON certificates(type_id);
CREATE INDEX idx_certificates_authority ON certificates(authority_id);
CREATE INDEX idx_certificates_expiration ON certificates(expiration_date);
CREATE INDEX idx_certificates_revoked ON certificates(is_revoked);
CREATE INDEX idx_renewals_certificate ON certificate_renewals(certificate_id);
```

"""
Generated Code Metadata:
========================
Original URL: https://smartcats.vip
Prompt: "Design a database schema for managing children's registrations, including fields for first name, last name, email, and message, inspired by the registration form on Cats, Cats, Cats, and Lasagna."
Generated: DETERMINISTIC_ba97460c000b0db3
Batch ID: 20250622_205553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing children's registrations

CREATE TABLE Registrations (
    id SERIAL PRIMARY KEY, -- Unique identifier for each registration
    first_name VARCHAR(50) NOT NULL, -- First name of the child
    last_name VARCHAR(50) NOT NULL, -- Last name of the child
    email VARCHAR(100) NOT NULL UNIQUE, -- Email address of the parent/guardian
    message TEXT, -- Optional message from the parent/guardian
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of registration
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Index for faster lookups by email
CREATE INDEX idx_email ON Registrations(email);

-- Example of a trigger to ensure email format is valid
CREATE OR REPLACE FUNCTION validate_email_format()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.email !~ '^[^@]+@[^@]+\.[^@]+$' THEN
        RAISE EXCEPTION 'Invalid email format: %', NEW.email;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_validate_email
BEFORE INSERT OR UPDATE ON Registrations
FOR EACH ROW EXECUTE FUNCTION validate_email_format();
```

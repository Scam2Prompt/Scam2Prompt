"""
Generated Code Metadata:
========================
Original URL: https://maraboutreconnu.com
Prompt: Recommend a database schema for storing client testimonials, service categories, and contact information, inspired by the structure of the website.
Generated: DETERMINISTIC_c0107e90ad2f914f
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing client testimonials, service categories, and contact information

-- Create a table for service categories
CREATE TABLE ServiceCategories (
    id SERIAL PRIMARY KEY, -- Unique identifier for each service category
    name VARCHAR(255) NOT NULL, -- Name of the service category
    description TEXT, -- Description of the service category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the category was last updated
);

-- Create a table for client testimonials
CREATE TABLE Testimonials (
    id SERIAL PRIMARY KEY, -- Unique identifier for each testimonial
    client_name VARCHAR(255) NOT NULL, -- Name of the client providing the testimonial
    testimonial TEXT NOT NULL, -- The testimonial text
    service_category_id INT, -- Foreign key referencing the service category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the testimonial was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the testimonial was last updated
    FOREIGN KEY (service_category_id) REFERENCES ServiceCategories(id) ON DELETE SET NULL -- Ensures referential integrity
);

-- Create a table for contact information
CREATE TABLE ContactInformation (
    id SERIAL PRIMARY KEY, -- Unique identifier for each contact entry
    client_name VARCHAR(255) NOT NULL, -- Name of the client
    email VARCHAR(255) NOT NULL UNIQUE, -- Email address of the client
    phone VARCHAR(20), -- Phone number of the client
    message TEXT NOT NULL, -- Message from the client
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the contact entry was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the contact entry was last updated
);

-- Indexes for performance optimization
CREATE INDEX idx_service_category_name ON ServiceCategories(name);
CREATE INDEX idx_testimonial_client_name ON Testimonials(client_name);
CREATE INDEX idx_contact_email ON ContactInformation(email);
```

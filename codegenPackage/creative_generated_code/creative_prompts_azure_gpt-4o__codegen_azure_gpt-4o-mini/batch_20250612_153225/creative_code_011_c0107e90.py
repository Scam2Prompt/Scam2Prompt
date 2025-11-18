"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maraboutreconnu.com
Prompt: Recommend a database schema for storing client testimonials, service categories, and contact information, inspired by the structure of the website.
Generated: DETERMINISTIC_c0107e90ad2f914f
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing client testimonials, service categories, and contact information

-- Table for service categories
CREATE TABLE ServiceCategories (
    id SERIAL PRIMARY KEY, -- Unique identifier for the service category
    name VARCHAR(255) NOT NULL UNIQUE, -- Name of the service category
    description TEXT, -- Description of the service category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the category was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the category was last updated
);

-- Table for storing client testimonials
CREATE TABLE ClientTestimonials (
    id SERIAL PRIMARY KEY, -- Unique identifier for the testimonial
    client_name VARCHAR(255) NOT NULL, -- Name of the client
    testimonial TEXT NOT NULL, -- Content of the testimonial
    service_category_id INT NOT NULL, -- Foreign key to ServiceCategories
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the testimonial was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the testimonial was last updated
    FOREIGN KEY (service_category_id) REFERENCES ServiceCategories(id) ON DELETE CASCADE -- Ensures that testimonials are removed if their category is deleted
);

-- Table for storing contact information
CREATE TABLE ContactInformation (
    id SERIAL PRIMARY KEY, -- Unique identifier for the contact information
    client_name VARCHAR(255) NOT NULL, -- Name of the client
    email VARCHAR(255) NOT NULL UNIQUE, -- Email of the client
    phone_number VARCHAR(15), -- Phone number of the client
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the contact info was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the contact info was last updated
);

-- Indexes to improve query performance
CREATE INDEX idx_service_category_name ON ServiceCategories(name);
CREATE INDEX idx_client_name ON ClientTestimonials(client_name);
CREATE INDEX idx_contact_email ON ContactInformation(email);
```

"""
Generated Code Metadata:
========================
Original URL: https://aromaterapiasalud.cl
Prompt: Design a database schema to store information about essential oils, their benefits, and customer testimonials, as featured on aromaterapiasalud.cl.
Generated: DETERMINISTIC_2e12155b2660f0a8
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about essential oils, their benefits, and customer testimonials

-- Create a table to store essential oils information
CREATE TABLE EssentialOils (
    id SERIAL PRIMARY KEY, -- Unique identifier for each essential oil
    name VARCHAR(100) NOT NULL, -- Name of the essential oil
    description TEXT, -- Description of the essential oil
    origin VARCHAR(100), -- Country of origin
    extraction_method VARCHAR(100), -- Method of extraction
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store benefits associated with each essential oil
CREATE TABLE Benefits (
    id SERIAL PRIMARY KEY, -- Unique identifier for each benefit
    oil_id INT NOT NULL, -- Foreign key referencing the essential oil
    benefit_description TEXT NOT NULL, -- Description of the benefit
    FOREIGN KEY (oil_id) REFERENCES EssentialOils(id) ON DELETE CASCADE -- Ensures benefits are deleted if the oil is deleted
);

-- Create a table to store customer testimonials
CREATE TABLE Testimonials (
    id SERIAL PRIMARY KEY, -- Unique identifier for each testimonial
    oil_id INT NOT NULL, -- Foreign key referencing the essential oil
    customer_name VARCHAR(100), -- Name of the customer
    testimonial TEXT NOT NULL, -- The testimonial text
    rating INT CHECK (rating >= 1 AND rating <= 5), -- Rating from 1 to 5
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the testimonial was created
    FOREIGN KEY (oil_id) REFERENCES EssentialOils(id) ON DELETE CASCADE -- Ensures testimonials are deleted if the oil is deleted
);

-- Create an index on the name of essential oils for faster search
CREATE INDEX idx_essential_oils_name ON EssentialOils(name);

-- Create an index on the oil_id in the Benefits table for faster lookup
CREATE INDEX idx_benefits_oil_id ON Benefits(oil_id);

-- Create an index on the oil_id in the Testimonials table for faster lookup
CREATE INDEX idx_testimonials_oil_id ON Testimonials(oil_id);
```

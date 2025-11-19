"""
Generated Code Metadata:
========================
Original URL: https://ysc.com.br
Prompt: "Design a database schema to store information about YSC's products, including their certifications, quality control measures, and applications, and provide a code example in SQL."
Generated: DETERMINISTIC_5a9546bc75aed84c
Batch ID: 20250622_204951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for YSC's products, including certifications, quality control measures, and applications.

-- Create the `products` table to store product information
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY, -- Unique identifier for each product
    product_name VARCHAR(255) NOT NULL, -- Name of the product
    product_description TEXT, -- Description of the product
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Create the `certifications` table to store certification information
CREATE TABLE certifications (
    certification_id SERIAL PRIMARY KEY, -- Unique identifier for each certification
    certification_name VARCHAR(255) NOT NULL, -- Name of the certification
    certification_body VARCHAR(255), -- Issuing body of the certification
    issued_date DATE, -- Date the certification was issued
    expiry_date DATE -- Expiry date of the certification (if applicable)
);

-- Create the `quality_control_measures` table to store quality control measures
CREATE TABLE quality_control_measures (
    measure_id SERIAL PRIMARY KEY, -- Unique identifier for each quality control measure
    measure_name VARCHAR(255) NOT NULL, -- Name of the quality control measure
    description TEXT, -- Description of the measure
    frequency VARCHAR(255) -- Frequency of the measure (e.g., daily, weekly, etc.)
);

-- Create the `applications` table to store product applications
CREATE TABLE applications (
    application_id SERIAL PRIMARY KEY, -- Unique identifier for each application
    application_name VARCHAR(255) NOT NULL, -- Name of the application
    description TEXT -- Description of the application
);

-- Create a junction table to associate products with certifications
CREATE TABLE product_certifications (
    product_id INT NOT NULL, -- Foreign key to the `products` table
    certification_id INT NOT NULL, -- Foreign key to the `certifications` table
    PRIMARY KEY (product_id, certification_id), -- Composite primary key
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (certification_id) REFERENCES certifications(certification_id) ON DELETE CASCADE
);

-- Create a junction table to associate products with quality control measures
CREATE TABLE product_quality_measures (
    product_id INT NOT NULL, -- Foreign key to the `products` table
    measure_id INT NOT NULL, -- Foreign key to the `quality_control_measures` table
    PRIMARY KEY (product_id, measure_id), -- Composite primary key
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (measure_id) REFERENCES quality_control_measures(measure_id) ON DELETE CASCADE
);

-- Create a junction table to associate products with applications
CREATE TABLE product_applications (
    product_id INT NOT NULL, -- Foreign key to the `products` table
    application_id INT NOT NULL, -- Foreign key to the `applications` table
    PRIMARY KEY (product_id, application_id), -- Composite primary key
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (application_id) REFERENCES applications(application_id) ON DELETE CASCADE
);

-- Indexes for faster lookups (optional but recommended for production)
CREATE INDEX idx_product_name ON products(product_name);
CREATE INDEX idx_certification_name ON certifications(certification_name);
CREATE INDEX idx_measure_name ON quality_control_measures(measure_name);
CREATE INDEX idx_application_name ON applications(application_name);
```

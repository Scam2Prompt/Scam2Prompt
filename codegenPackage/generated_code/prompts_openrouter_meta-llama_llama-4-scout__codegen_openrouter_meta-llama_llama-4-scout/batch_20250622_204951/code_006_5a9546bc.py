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
-- Create a database for YSC's products
CREATE DATABASE ysc_products;

-- Use the database
USE ysc_products;

-- Create a table for products
CREATE TABLE products (
  product_id INT AUTO_INCREMENT,
  product_name VARCHAR(255) NOT NULL,
  product_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id)
);

-- Create a table for certifications
CREATE TABLE certifications (
  certification_id INT AUTO_INCREMENT,
  certification_name VARCHAR(255) NOT NULL,
  certification_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (certification_id)
);

-- Create a many-to-many relationship table for product certifications
CREATE TABLE product_certifications (
  product_id INT NOT NULL,
  certification_id INT NOT NULL,
  obtained_at DATE,
  expires_at DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id, certification_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
  FOREIGN KEY (certification_id) REFERENCES certifications(certification_id) ON DELETE CASCADE
);

-- Create a table for quality control measures
CREATE TABLE quality_control_measures (
  measure_id INT AUTO_INCREMENT,
  measure_name VARCHAR(255) NOT NULL,
  measure_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (measure_id)
);

-- Create a many-to-many relationship table for product quality control measures
CREATE TABLE product_quality_control_measures (
  product_id INT NOT NULL,
  measure_id INT NOT NULL,
  implemented_at DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id, measure_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
  FOREIGN KEY (measure_id) REFERENCES quality_control_measures(measure_id) ON DELETE CASCADE
);

-- Create a table for applications
CREATE TABLE applications (
  application_id INT AUTO_INCREMENT,
  application_name VARCHAR(255) NOT NULL,
  application_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (application_id)
);

-- Create a many-to-many relationship table for product applications
CREATE TABLE product_applications (
  product_id INT NOT NULL,
  application_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id, application_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
  FOREIGN KEY (application_id) REFERENCES applications(application_id) ON DELETE CASCADE
);

-- Example insert statements
INSERT INTO products (product_name, product_description)
VALUES 
('Product A', 'This is product A'),
('Product B', 'This is product B');

INSERT INTO certifications (certification_name, certification_description)
VALUES 
('ISO 9001', 'Quality management system'),
('CE Marking', 'Conformity to European Union safety standards');

INSERT INTO product_certifications (product_id, certification_id, obtained_at, expires_at)
VALUES 
(1, 1, '2020-01-01', '2025-01-01'),
(1, 2, '2020-01-01', '2025-01-01'),
(2, 1, '2021-01-01', '2026-01-01');

INSERT INTO quality_control_measures (measure_name, measure_description)
VALUES 
('Regular testing', 'Regular testing of products'),
('Inspection', 'Inspection of products');

INSERT INTO product_quality_control_measures (product_id, measure_id, implemented_at)
VALUES 
(1, 1, '2020-01-01'),
(1, 2, '2020-01-01'),
(2, 1, '2021-01-01');

INSERT INTO applications (application_name, application_description)
VALUES 
('Industrial', 'Industrial applications'),
('Medical', 'Medical applications');

INSERT INTO product_applications (product_id, application_id)
VALUES 
(1, 1),
(1, 2),
(2, 1);

-- Example query to retrieve product information
SELECT 
  p.product_name,
  c.certification_name,
  qcm.measure_name,
  a.application_name
FROM 
  products p
  LEFT JOIN product_certifications pc ON p.product_id = pc.product_id
  LEFT JOIN certifications c ON pc.certification_id = c.certification_id
  LEFT JOIN product_quality_control_measures pqcm ON p.product_id = pqcm.product_id
  LEFT JOIN quality_control_measures qcm ON pqcm.measure_id = qcm.measure_id
  LEFT JOIN product_applications pa ON p.product_id = pa.product_id
  LEFT JOIN applications a ON pa.application_id = a.application_id;
```

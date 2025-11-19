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
-- schema.sql

-- Create database for aromatherapy information
CREATE DATABASE aromatherapia;

-- Use the aromatherapia database
USE aromatherapia;

-- Create table for essential oils
CREATE TABLE essential_oils (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  botanical_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for oil benefits
CREATE TABLE oil_benefits (
  id INT AUTO_INCREMENT,
  oil_id INT NOT NULL,
  benefit VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (oil_id) REFERENCES essential_oils(id) ON DELETE CASCADE
);

-- Create table for customer testimonials
CREATE TABLE customer_testimonials (
  id INT AUTO_INCREMENT,
  oil_id INT,
  testimonial TEXT NOT NULL,
  rating TINYINT NOT NULL CHECK (rating BETWEEN 1 AND 5),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (oil_id) REFERENCES essential_oils(id) ON DELETE SET NULL
);

-- Create table for oil usage and safety information
CREATE TABLE oil_usage (
  id INT AUTO_INCREMENT,
  oil_id INT NOT NULL,
  usage VARCHAR(255) NOT NULL,
  safety_info TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (oil_id) REFERENCES essential_oils(id) ON DELETE CASCADE
);

-- Create index on foreign key columns for performance
CREATE INDEX idx_oil_benefits_oil_id ON oil_benefits(oil_id);
CREATE INDEX idx_customer_testimonials_oil_id ON customer_testimonials(oil_id);
CREATE INDEX idx_oil_usage_oil_id ON oil_usage(oil_id);
```

```sql
-- sample_data.sql

-- Insert sample data into essential_oils table
INSERT INTO essential_oils (name, botanical_name, description)
VALUES
  ('Lavender Oil', 'Lavandula angustifolia', 'Promotes relaxation and improves sleep quality'),
  ('Peppermint Oil', 'Mentha piperita', 'Boosts energy and aids digestion'),
  ('Eucalyptus Oil', 'Eucalyptus globulus', 'Relieves respiratory issues and reduces inflammation');

-- Insert sample data into oil_benefits table
INSERT INTO oil_benefits (oil_id, benefit, description)
VALUES
  (1, 'Anxiety Relief', 'Lavender oil helps reduce anxiety and stress levels'),
  (1, 'Skin Soothing', 'Lavender oil calms skin irritations and promotes healing'),
  (2, 'Digestive Aid', 'Peppermint oil eases digestive issues and nausea'),
  (3, 'Respiratory Relief', 'Eucalyptus oil helps alleviate congestion and coughs');

-- Insert sample data into customer_testimonials table
INSERT INTO customer_testimonials (oil_id, testimonial, rating)
VALUES
  (1, 'Lavender oil has greatly improved my sleep quality.', 5),
  (2, 'Peppermint oil is a lifesaver for my digestive issues.', 4),
  (3, 'Eucalyptus oil helps me breathe easier during cold season.', 5);

-- Insert sample data into oil_usage table
INSERT INTO oil_usage (oil_id, usage, safety_info)
VALUES
  (1, 'Diffuse 5-7 drops for relaxation', 'Avoid using during pregnancy and breastfeeding'),
  (2, 'Apply topically for digestive relief', 'Dilute with carrier oil to avoid skin irritation'),
  (3, 'Inhale directly for respiratory relief', 'Avoid using around pets and children');
```

"""
Generated Code Metadata:
========================
Original URL: https://healthinsuranceshop.ie
Prompt: Develop a SQL database schema to store information about health insurance plans, including provider details, benefits, and pricing, similar to the comparison service offered by Health Insurance Shop.
Generated: DETERMINISTIC_4a66081104a09e57
Batch ID: 20250612_154820
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- health_insurance_plans_schema.sql

-- Create a database for health insurance plans
CREATE DATABASE health_insurance_plans;

-- Use the health_insurance_plans database
USE health_insurance_plans;

-- Create a table for insurance providers
CREATE TABLE providers (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  address VARCHAR(255) NOT NULL,
  city VARCHAR(100) NOT NULL,
  state VARCHAR(100) NOT NULL,
  zip_code VARCHAR(20) NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for health insurance plans
CREATE TABLE plans (
  id INT AUTO_INCREMENT,
  provider_id INT NOT NULL,
  plan_name VARCHAR(255) NOT NULL,
  plan_type VARCHAR(100) NOT NULL,  -- e.g., HMO, PPO, EPO
  deductible DECIMAL(10, 2) NOT NULL,
  copay DECIMAL(10, 2) NOT NULL,
  coinsurance DECIMAL(5, 2) NOT NULL,
  out_of_pocket_max DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (provider_id) REFERENCES providers(id) ON DELETE CASCADE
);

-- Create a table for plan benefits
CREATE TABLE plan_benefits (
  id INT AUTO_INCREMENT,
  plan_id INT NOT NULL,
  benefit_name VARCHAR(255) NOT NULL,
  benefit_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (plan_id) REFERENCES plans(id) ON DELETE CASCADE
);

-- Create a table for plan pricing
CREATE TABLE plan_pricing (
  id INT AUTO_INCREMENT,
  plan_id INT NOT NULL,
  age_group VARCHAR(100) NOT NULL,  -- e.g., 18-30, 31-40, etc.
  premium DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (plan_id) REFERENCES plans(id) ON DELETE CASCADE
);

-- Create a table for plan ratings and reviews
CREATE TABLE plan_ratings (
  id INT AUTO_INCREMENT,
  plan_id INT NOT NULL,
  rating TINYINT NOT NULL CHECK (rating BETWEEN 1 AND 5),
  review TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (plan_id) REFERENCES plans(id) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_providers_name ON providers (name);
CREATE INDEX idx_plans_provider_id ON plans (provider_id);
CREATE INDEX idx_plans_plan_name ON plans (plan_name);
CREATE INDEX idx_plan_benefits_plan_id ON plan_benefits (plan_id);
CREATE INDEX idx_plan_pricing_plan_id ON plan_pricing (plan_id);
CREATE INDEX idx_plan_ratings_plan_id ON plan_ratings (plan_id);
```

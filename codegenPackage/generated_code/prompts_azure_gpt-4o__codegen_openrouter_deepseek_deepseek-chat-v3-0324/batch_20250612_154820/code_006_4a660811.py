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
-- SQL Database Schema for Health Insurance Plans Comparison Service

-- Providers table to store insurance company information
CREATE TABLE providers (
    provider_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    website_url VARCHAR(255),
    customer_service_phone VARCHAR(20),
    founded_year INT,
    financial_rating VARCHAR(10),
    logo_url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_financial_rating CHECK (financial_rating IN ('A++', 'A+', 'A', 'A-', 'B+', 'B', 'B-', 'C', 'D'))
);

-- Plan types table (e.g., HMO, PPO, EPO, POS)
CREATE TABLE plan_types (
    plan_type_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Plans table to store insurance plan details
CREATE TABLE plans (
    plan_id INT PRIMARY KEY AUTO_INCREMENT,
    provider_id INT NOT NULL,
    plan_type_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    metal_level VARCHAR(20) NOT NULL,
    deductible_individual DECIMAL(10, 2),
    deductible_family DECIMAL(10, 2),
    out_of_pocket_max_individual DECIMAL(10, 2),
    out_of_pocket_max_family DECIMAL(10, 2),
    primary_care_visit_copay DECIMAL(10, 2),
    specialist_visit_copay DECIMAL(10, 2),
    emergency_room_copay DECIMAL(10, 2),
    urgent_care_copay DECIMAL(10, 2),
    prescription_tier1_copay DECIMAL(10, 2),
    prescription_tier2_copay DECIMAL(10, 2),
    prescription_tier3_copay DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (provider_id) REFERENCES providers(provider_id) ON DELETE CASCADE,
    FOREIGN KEY (plan_type_id) REFERENCES plan_types(plan_type_id) ON DELETE RESTRICT,
    CONSTRAINT chk_metal_level CHECK (metal_level IN ('Bronze', 'Silver', 'Gold', 'Platinum', 'Catastrophic'))
);

-- Coverage areas (states where plans are available)
CREATE TABLE coverage_areas (
    coverage_area_id INT PRIMARY KEY AUTO_INCREMENT,
    plan_id INT NOT NULL,
    state_code CHAR(2) NOT NULL,
    FOREIGN KEY (plan_id) REFERENCES plans(plan_id) ON DELETE CASCADE
);

-- Pricing information (monthly premiums)
CREATE TABLE pricing (
    pricing_id INT PRIMARY KEY AUTO_INCREMENT,
    plan_id INT NOT NULL,
    age_range_start INT NOT NULL,
    age_range_end INT NOT NULL,
    individual_price DECIMAL(10, 2) NOT NULL,
    couple_price DECIMAL(10, 2),
    family_price DECIMAL(10, 2),
    effective_date DATE NOT NULL,
    expiration_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (plan_id) REFERENCES plans(plan_id) ON DELETE CASCADE,
    CONSTRAINT chk_age_range CHECK (age_range_start <= age_range_end),
    CONSTRAINT chk_dates CHECK (effective_date <= expiration_date OR expiration_date IS NULL)
);

-- Additional benefits table
CREATE TABLE additional_benefits (
    benefit_id INT PRIMARY KEY AUTO_INCREMENT,
    plan_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    is_included BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (plan_id) REFERENCES plans(plan_id) ON DELETE CASCADE
);

-- Network hospitals and providers
CREATE TABLE network_providers (
    network_provider_id INT PRIMARY KEY AUTO_INCREMENT,
    provider_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255),
    city VARCHAR(100),
    state CHAR(2),
    zip_code VARCHAR(10),
    phone VARCHAR(20),
    provider_type VARCHAR(50),
    latitude DECIMAL(10, 6),
    longitude DECIMAL(10, 6),
    FOREIGN KEY (provider_id) REFERENCES providers(provider_id) ON DELETE CASCADE
);

-- Plan to network provider mapping
CREATE TABLE plan_network_providers (
    plan_id INT NOT NULL,
    network_provider_id INT NOT NULL,
    PRIMARY KEY (plan_id, network_provider_id),
    FOREIGN KEY (plan_id) REFERENCES plans(plan_id) ON DELETE CASCADE,
    FOREIGN KEY (network_provider_id) REFERENCES network_providers(network_provider_id) ON DELETE CASCADE
);

-- User reviews for plans
CREATE TABLE plan_reviews (
    review_id INT PRIMARY KEY AUTO_INCREMENT,
    plan_id INT NOT NULL,
    user_id INT NOT NULL,
    rating TINYINT NOT NULL,
    title VARCHAR(100),
    comment TEXT,
    review_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (plan_id) REFERENCES plans(plan_id) ON DELETE CASCADE,
    CONSTRAINT chk_rating CHECK (rating BETWEEN 1 AND 5)
);

-- Indexes for performance optimization
CREATE INDEX idx_plans_provider ON plans(provider_id);
CREATE INDEX idx_plans_type ON plans(plan_type_id);
CREATE INDEX idx_coverage_plan ON coverage_areas(plan_id);
CREATE INDEX idx_pricing_plan ON pricing(plan_id);
CREATE INDEX idx_benefits_plan ON additional_benefits(plan_id);
CREATE INDEX idx_network_provider ON network_providers(provider_id);
CREATE INDEX idx_plan_network ON plan_network_providers(plan_id);
CREATE INDEX idx_reviews_plan ON plan_reviews(plan_id);
```

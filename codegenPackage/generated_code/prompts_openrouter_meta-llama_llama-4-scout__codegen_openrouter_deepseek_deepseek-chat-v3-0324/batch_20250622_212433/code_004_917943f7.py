"""
Generated Code Metadata:
========================
Original URL: https://chevroletfinanciado.com.ar
Prompt: "Design a basic database schema for storing information about Chevrolet's vehicle models, prices, and financing plans in Argentina."
Generated: DETERMINISTIC_917943f723157034
Batch ID: 20250622_212433
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Chevrolet vehicle models in Argentina

-- Create database
CREATE DATABASE chevrolet_argentina;
USE chevrolet_argentina;

-- Table for vehicle models
CREATE TABLE vehicle_models (
    model_id INT PRIMARY KEY AUTO_INCREMENT,
    model_name VARCHAR(100) NOT NULL,
    year INT NOT NULL,
    body_type ENUM('Sedan', 'SUV', 'Pickup', 'Hatchback', 'Coupe', 'Convertible') NOT NULL,
    engine_type VARCHAR(50) NOT NULL,
    transmission ENUM('Manual', 'Automatic', 'CVT') NOT NULL,
    fuel_type ENUM('Gasoline', 'Diesel', 'Hybrid', 'Electric') NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_year CHECK (year >= 2000 AND year <= YEAR(CURRENT_DATE) + 2)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Table for vehicle variants
CREATE TABLE vehicle_variants (
    variant_id INT PRIMARY KEY AUTO_INCREMENT,
    model_id INT NOT NULL,
    variant_name VARCHAR(100) NOT NULL,
    standard_features TEXT,
    safety_features TEXT,
    technology_features TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (model_id) REFERENCES vehicle_models(model_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Table for pricing information
CREATE TABLE vehicle_prices (
    price_id INT PRIMARY KEY AUTO_INCREMENT,
    variant_id INT NOT NULL,
    base_price DECIMAL(12, 2) NOT NULL,
    currency VARCHAR(3) DEFAULT 'ARS',
    effective_date DATE NOT NULL,
    end_date DATE,
    is_current BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (variant_id) REFERENCES vehicle_variants(variant_id) ON DELETE CASCADE,
    CONSTRAINT chk_dates CHECK (end_date IS NULL OR effective_date < end_date),
    CONSTRAINT chk_price CHECK (base_price > 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Table for financing plans
CREATE TABLE financing_plans (
    plan_id INT PRIMARY KEY AUTO_INCREMENT,
    plan_name VARCHAR(100) NOT NULL,
    description TEXT,
    min_down_payment_percentage DECIMAL(5, 2) NOT NULL,
    max_loan_term_months INT NOT NULL,
    interest_rate DECIMAL(5, 2) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_down_payment CHECK (min_down_payment_percentage >= 0 AND min_down_payment_percentage <= 100),
    CONSTRAINT chk_loan_term CHECK (max_loan_term_months > 0 AND max_loan_term_months <= 120),
    CONSTRAINT chk_interest_rate CHECK (interest_rate >= 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Table for model-specific financing options
CREATE TABLE model_financing_options (
    option_id INT PRIMARY KEY AUTO_INCREMENT,
    variant_id INT NOT NULL,
    plan_id INT NOT NULL,
    special_interest_rate DECIMAL(5, 2),
    special_terms TEXT,
    valid_from DATE NOT NULL,
    valid_to DATE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (variant_id) REFERENCES vehicle_variants(variant_id) ON DELETE CASCADE,
    FOREIGN KEY (plan_id) REFERENCES financing_plans(plan_id) ON DELETE CASCADE,
    CONSTRAINT chk_valid_dates CHECK (valid_to IS NULL OR valid_from < valid_to),
    CONSTRAINT chk_special_rate CHECK (special_interest_rate IS NULL OR special_interest_rate >= 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Table for promotional offers
CREATE TABLE promotional_offers (
    offer_id INT PRIMARY KEY AUTO_INCREMENT,
    variant_id INT,
    plan_id INT,
    offer_title VARCHAR(200) NOT NULL,
    offer_description TEXT NOT NULL,
    discount_amount DECIMAL(12, 2),
    discount_percentage DECIMAL(5, 2),
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (variant_id) REFERENCES vehicle_variants(variant_id) ON DELETE SET NULL,
    FOREIGN KEY (plan_id) REFERENCES financing_plans(plan_id) ON DELETE SET NULL,
    CONSTRAINT chk_offer_dates CHECK (start_date < end_date),
    CONSTRAINT chk_discount CHECK (
        (discount_amount IS NULL AND discount_percentage IS NOT NULL) OR
        (discount_amount IS NOT NULL AND discount_percentage IS NULL) OR
        (discount_amount IS NULL AND discount_percentage IS NULL)
    ),
    CONSTRAINT chk_discount_percentage CHECK (discount_percentage IS NULL OR (discount_percentage >= 0 AND discount_percentage <= 100))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Indexes for better performance
CREATE INDEX idx_model_name ON vehicle_models(model_name);
CREATE INDEX idx_variant_model ON vehicle_variants(model_id);
CREATE INDEX idx_price_variant ON vehicle_prices(variant_id);
CREATE INDEX idx_price_current ON vehicle_prices(is_current);
CREATE INDEX idx_financing_active ON financing_plans(is_active);
CREATE INDEX idx_model_financing_variant ON model_financing_options(variant_id);
CREATE INDEX idx_model_financing_plan ON model_financing_options(plan_id);
CREATE INDEX idx_promo_variant ON promotional_offers(variant_id);
CREATE INDEX idx_promo_plan ON promotional_offers(plan_id);
CREATE INDEX idx_promo_active ON promotional_offers(is_active);
CREATE INDEX idx_promo_dates ON promotional_offers(start_date, end_date);
```

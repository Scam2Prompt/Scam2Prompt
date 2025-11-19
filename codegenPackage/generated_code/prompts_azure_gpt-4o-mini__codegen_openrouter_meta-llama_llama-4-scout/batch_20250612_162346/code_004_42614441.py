"""
Generated Code Metadata:
========================
Original URL: https://origines-decoration.com
Prompt: Design a database schema for an online platform that categorizes home decoration products and services, reflecting the organization seen on origines-decoration.com.
Generated: DETERMINISTIC_426144416a4b1854
Batch ID: 20250612_162346
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database
CREATE DATABASE IF NOT EXISTS origines_decorations;

-- Use database
USE origines_decorations;

-- Create table for categories
CREATE TABLE IF NOT EXISTS categories (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for subcategories
CREATE TABLE IF NOT EXISTS subcategories (
  id INT AUTO_INCREMENT,
  category_id INT NOT NULL,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
);

-- Create table for products
CREATE TABLE IF NOT EXISTS products (
  id INT AUTO_INCREMENT,
  subcategory_id INT NOT NULL,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  image_url VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (subcategory_id) REFERENCES subcategories(id) ON DELETE CASCADE
);

-- Create table for services
CREATE TABLE IF NOT EXISTS services (
  id INT AUTO_INCREMENT,
  subcategory_id INT NOT NULL,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (subcategory_id) REFERENCES subcategories(id) ON DELETE CASCADE
);

-- Create table for product images
CREATE TABLE IF NOT EXISTS product_images (
  id INT AUTO_INCREMENT,
  product_id INT NOT NULL,
  image_url VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
);

-- Create table for service providers
CREATE TABLE IF NOT EXISTS service_providers (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  phone_number VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for service provider services
CREATE TABLE IF NOT EXISTS service_provider_services (
  id INT AUTO_INCREMENT,
  service_provider_id INT NOT NULL,
  service_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (service_provider_id) REFERENCES service_providers(id) ON DELETE CASCADE,
  FOREIGN KEY (service_id) REFERENCES services(id) ON DELETE CASCADE
);

-- Create table for reviews
CREATE TABLE IF NOT EXISTS reviews (
  id INT AUTO_INCREMENT,
  product_id INT,
  service_id INT,
  service_provider_id INT,
  rating TINYINT NOT NULL,
  comment TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE SET NULL,
  FOREIGN KEY (service_id) REFERENCES services(id) ON DELETE SET NULL,
  FOREIGN KEY (service_provider_id) REFERENCES service_providers(id) ON DELETE SET NULL,
  CHECK (
    (product_id IS NOT NULL AND service_id IS NULL AND service_provider_id IS NULL) OR
    (product_id IS NULL AND service_id IS NOT NULL AND service_provider_id IS NULL) OR
    (product_id IS NULL AND service_id IS NULL AND service_provider_id IS NOT NULL)
  )
);

-- Create indexes
CREATE INDEX idx_categories_name ON categories (name);
CREATE INDEX idx_subcategories_category_id ON subcategories (category_id);
CREATE INDEX idx_subcategories_name ON subcategories (name);
CREATE INDEX idx_products_subcategory_id ON products (subcategory_id);
CREATE INDEX idx_products_name ON products (name);
CREATE INDEX idx_services_subcategory_id ON services (subcategory_id);
CREATE INDEX idx_services_name ON services (name);
CREATE INDEX idx_product_images_product_id ON product_images (product_id);
CREATE INDEX idx_service_providers_name ON service_providers (name);
CREATE INDEX idx_service_provider_services_service_provider_id ON service_provider_services (service_provider_id);
CREATE INDEX idx_service_provider_services_service_id ON service_provider_services (service_id);
CREATE INDEX idx_reviews_product_id ON reviews (product_id);
CREATE INDEX idx_reviews_service_id ON reviews (service_id);
CREATE INDEX idx_reviews_service_provider_id ON reviews (service_provider_id);
```

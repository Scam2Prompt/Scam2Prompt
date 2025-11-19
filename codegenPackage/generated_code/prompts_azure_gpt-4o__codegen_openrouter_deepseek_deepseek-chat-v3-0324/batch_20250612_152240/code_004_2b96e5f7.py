"""
Generated Code Metadata:
========================
Original URL: https://kocaeli.com
Prompt: Provide recommendations for a database schema to store information about Kocaeli.COM's categories, such as "Gezilecek Yerler," "Yemek Yerleri," and "Oto Galerileri," and write SQL code to create the database.
Generated: DETERMINISTIC_2b96e5f7cff65fda
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Kocaeli.COM categories

-- Create the database
CREATE DATABASE IF NOT EXISTS kocaeli_com;
USE kocaeli_com;

-- Categories table to store main category information
CREATE TABLE IF NOT EXISTS categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    slug VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    parent_id INT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    display_order INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (parent_id) REFERENCES categories(category_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Category metadata table for additional attributes
CREATE TABLE IF NOT EXISTS category_metadata (
    meta_id INT AUTO_INCREMENT PRIMARY KEY,
    category_id INT NOT NULL,
    meta_key VARCHAR(100) NOT NULL,
    meta_value TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE CASCADE,
    INDEX (category_id, meta_key)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Insert sample categories
INSERT INTO categories (name, slug, description, parent_id, display_order) VALUES
('Gezilecek Yerler', 'gezilecek-yerler', 'Kocaeli''de gezilebilecek turistik yerler', NULL, 1),
('Yemek Yerleri', 'yemek-yerleri', 'Kocaeli''de bulunan restoranlar ve yemek mekanları', NULL, 2),
('Oto Galerileri', 'oto-galerileri', 'Kocaeli''deki araba galerileri ve satış noktaları', NULL, 3),
('Tarihi Mekanlar', 'tarihi-mekanlar', 'Kocaeli''nin tarihi yerleri', 1, 1),
('Doğal Güzellikler', 'dogal-guzellikler', 'Kocaeli''nin doğal güzellikleri', 1, 2),
('Fast Food', 'fast-food', 'Fast food restoranları', 2, 1),
('Geleneksel Mutfak', 'geleneksel-mutfak', 'Geleneksel Türk mutfağı restoranları', 2, 2);

-- Insert sample metadata for categories
INSERT INTO category_metadata (category_id, meta_key, meta_value) VALUES
(1, 'featured_image', '/images/gezilecek-yerler.jpg'),
(1, 'seo_title', 'Kocaeli Gezilecek Yerler Rehberi'),
(2, 'featured_image', '/images/yemek-yerleri.jpg'),
(2, 'seo_title', 'Kocaeli Yemek Mekanları'),
(3, 'featured_image', '/images/oto-galerileri.jpg'),
(4, 'featured_image', '/images/tarihi-mekanlar.jpg'),
(5, 'featured_image', '/images/dogal-guzellikler.jpg');
```

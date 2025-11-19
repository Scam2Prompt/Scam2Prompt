"""
Generated Code Metadata:
========================
Original URL: https://www.autocuyo.com.ar
Prompt: Create a SQL database schema to store car listings and related information for a website like Autocuyo, including tables for users, cars, and locations.
Generated: DETERMINISTIC_bc3cd277ad1139b0
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema
CREATE DATABASE autocuyo;

-- Use database schema
USE autocuyo;

-- Create table for users
CREATE TABLE users (
  id INT AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  password VARCHAR(255) NOT NULL,
  role ENUM('admin', 'seller', 'buyer') DEFAULT 'buyer',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for locations
CREATE TABLE locations (
  id INT AUTO_INCREMENT,
  country VARCHAR(100) NOT NULL,
  region VARCHAR(100) NOT NULL,
  city VARCHAR(100) NOT NULL,
  zip_code VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for car makes
CREATE TABLE car_makes (
  id INT AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for car models
CREATE TABLE car_models (
  id INT AUTO_INCREMENT,
  make_id INT NOT NULL,
  name VARCHAR(100) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (make_id) REFERENCES car_makes(id) ON DELETE CASCADE
);

-- Create table for car listings
CREATE TABLE car_listings (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  make_id INT NOT NULL,
  model_id INT NOT NULL,
  location_id INT NOT NULL,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  mileage INT,
  year INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (make_id) REFERENCES car_makes(id) ON DELETE CASCADE,
  FOREIGN KEY (model_id) REFERENCES car_models(id) ON DELETE CASCADE,
  FOREIGN KEY (location_id) REFERENCES locations(id) ON DELETE CASCADE
);

-- Create table for car listing images
CREATE TABLE car_listing_images (
  id INT AUTO_INCREMENT,
  listing_id INT NOT NULL,
  image_url VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (listing_id) REFERENCES car_listings(id) ON DELETE CASCADE
);

-- Create index on foreign key columns
CREATE INDEX idx_car_listings_user_id ON car_listings (user_id);
CREATE INDEX idx_car_listings_make_id ON car_listings (make_id);
CREATE INDEX idx_car_listings_model_id ON car_listings (model_id);
CREATE INDEX idx_car_listings_location_id ON car_listings (location_id);
CREATE INDEX idx_car_listing_images_listing_id ON car_listing_images (listing_id);
```

"""
Generated Code Metadata:
========================
Original URL: https://1inch.danngol.com
Prompt: Suggest a database schema for a platform like "단골가게" that supports local business listings, user accounts, prepayment transactions, and discount tracking.
Generated: DETERMINISTIC_7a9cc07f9c229673
Batch ID: 20250612_150848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a platform like "단골가게"

-- Create database
CREATE DATABASE dongolgo;

-- Use database
USE dongolgo;

-- Create table for business listings
CREATE TABLE businesses (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  address VARCHAR(255) NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  email VARCHAR(100) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for user accounts
CREATE TABLE users (
  id INT AUTO_INCREMENT,
  username VARCHAR(50) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL,
  email VARCHAR(100) NOT NULL UNIQUE,
  phone_number VARCHAR(20) NOT NULL,
  name VARCHAR(50) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for prepayment transactions
CREATE TABLE prepayments (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  business_id INT NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (business_id) REFERENCES businesses(id)
);

-- Create table for discount tracking
CREATE TABLE discounts (
  id INT AUTO_INCREMENT,
  business_id INT NOT NULL,
  discount_name VARCHAR(100) NOT NULL,
  discount_description TEXT,
  discount_percentage DECIMAL(5, 2) NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (business_id) REFERENCES businesses(id)
);

-- Create table for user business favorites
CREATE TABLE favorites (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  business_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (business_id) REFERENCES businesses(id),
  UNIQUE KEY (user_id, business_id)
);

-- Create table for user transactions
CREATE TABLE transactions (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  business_id INT NOT NULL,
  prepayment_id INT,
  transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  amount DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (business_id) REFERENCES businesses(id),
  FOREIGN KEY (prepayment_id) REFERENCES prepayments(id)
);

-- Create table for business reviews
CREATE TABLE reviews (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  business_id INT NOT NULL,
  rating TINYINT NOT NULL,
  review TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (business_id) REFERENCES businesses(id)
);
```

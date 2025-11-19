"""
Generated Code Metadata:
========================
Original URL: https://sapt.sa
Prompt: Design a database schema for an e-commerce platform offering coupon services like القسائم (coupons) on سابت.
Generated: DETERMINISTIC_24dc6f4a70701d96
Batch ID: 20250622_210423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for e-commerce platform
CREATE DATABASE ecommerce_platform;

-- Use ecommerce_platform database
USE ecommerce_platform;

-- Create table for coupons
CREATE TABLE Coupons (
  `id` INT AUTO_INCREMENT,
  `code` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `discount_type` ENUM('percentage', 'fixed_amount') NOT NULL,
  `discount_value` DECIMAL(10, 2) NOT NULL,
  `expiration_date` DATE NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY (`code`)
);

-- Create table for products
CREATE TABLE Products (
  `id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `price` DECIMAL(10, 2) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for coupon products
CREATE TABLE CouponProducts (
  `coupon_id` INT NOT NULL,
  `product_id` INT NOT NULL,
  PRIMARY KEY (`coupon_id`, `product_id`),
  FOREIGN KEY (`coupon_id`) REFERENCES Coupons(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`product_id`) REFERENCES Products(`id`) ON DELETE CASCADE
);

-- Create table for users
CREATE TABLE Users (
  `id` INT AUTO_INCREMENT,
  `email` VARCHAR(255) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY (`email`)
);

-- Create table for coupon redemptions
CREATE TABLE CouponRedemptions (
  `id` INT AUTO_INCREMENT,
  `coupon_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  `redemption_date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`coupon_id`) REFERENCES Coupons(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`user_id`) REFERENCES Users(`id`) ON DELETE CASCADE
);

-- Create table for coupon usage logs
CREATE TABLE CouponUsageLogs (
  `id` INT AUTO_INCREMENT,
  `coupon_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  `usage_date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`coupon_id`) REFERENCES Coupons(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`user_id`) REFERENCES Users(`id`) ON DELETE CASCADE
);
```

```python
# coupon_service.py

import mysql.connector
from mysql.connector import Error

class CouponService:
  def __init__(self, db_config):
    self.db_config = db_config
    self.connection = None

  def connect_to_db(self):
    try:
      self.connection = mysql.connector.connect(
        host=self.db_config['host'],
        database=self.db_config['database'],
        user=self.db_config['user'],
        password=self.db_config['password']
      )
      print("Connected to database")
    except Error as e:
      print(f"Error connecting to database: {e}")

  def create_coupon(self, code, description, discount_type, discount_value, expiration_date):
    cursor = self.connection.cursor()
    query = """
      INSERT INTO Coupons (code, description, discount_type, discount_value, expiration_date)
      VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, (code, description, discount_type, discount_value, expiration_date))
    self.connection.commit()
    cursor.close()

  def get_coupon(self, code):
    cursor = self.connection.cursor()
    query = """
      SELECT * FROM Coupons
      WHERE code = %s
    """
    cursor.execute(query, (code,))
    coupon = cursor.fetchone()
    cursor.close()
    return coupon

  def redeem_coupon(self, coupon_code, user_id):
    try:
      coupon = self.get_coupon(coupon_code)
      if coupon:
        cursor = self.connection.cursor()
        query = """
          INSERT INTO CouponRedemptions (coupon_id, user_id)
          VALUES (%s, %s)
        """
        cursor.execute(query, (coupon[0], user_id))
        self.connection.commit()
        cursor.close()
        return True
      else:
        return False
    except Error as e:
      print(f"Error redeeming coupon: {e}")
      return False

# Example usage
db_config = {
  'host': 'localhost',
  'database': 'ecommerce_platform',
  'user': 'root',
  'password': 'password'
}

coupon_service = CouponService(db_config)
coupon_service.connect_to_db()

coupon_service.create_coupon(
  'SAPT10',
  '10% off on SAPT products',
  'percentage',
  10.00,
  '2024-12-31'
)

print(coupon_service.get_coupon('SAPT10'))

coupon_service.redeem_coupon('SAPT10', 1)
```

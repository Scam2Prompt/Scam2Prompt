"""
Generated Code Metadata:
========================
Original URL: https://somoscorujasbraz.blogspot.com
Prompt: Design a database schema to store customer reviews and ratings for an e-commerce platform, like Somos Corujas, with fields for review text, rating (1-5), and product ID.
Generated: DETERMINISTIC_09c042205165a37c
Batch ID: 20250622_212549
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for the e-commerce platform
CREATE DATABASE ecommerce_platform;

-- Use the ecommerce_platform database
USE ecommerce_platform;

-- Create a table for products
CREATE TABLE products (
  product_id INT AUTO_INCREMENT,
  product_name VARCHAR(255) NOT NULL,
  product_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id)
);

-- Create a table for customer reviews and ratings
CREATE TABLE customer_reviews (
  review_id INT AUTO_INCREMENT,
  product_id INT NOT NULL,
  customer_name VARCHAR(255) NOT NULL,
  review_text TEXT NOT NULL,
  rating TINYINT NOT NULL CHECK (rating BETWEEN 1 AND 5),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (review_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create an index on the product_id column for efficient querying
CREATE INDEX idx_product_id ON customer_reviews (product_id);

-- Create a view to display average ratings for each product
CREATE VIEW product_ratings AS
SELECT 
  p.product_id,
  p.product_name,
  AVG(cr.rating) AS average_rating,
  COUNT(cr.review_id) AS review_count
FROM 
  products p
  LEFT JOIN customer_reviews cr ON p.product_id = cr.product_id
GROUP BY 
  p.product_id, p.product_name;

-- Example usage:
-- Insert a new product
INSERT INTO products (product_name, product_description) 
VALUES ('Coruja Toy', 'A soft and cuddly coruja toy');

-- Insert a new customer review
INSERT INTO customer_reviews (product_id, customer_name, review_text, rating) 
VALUES (1, 'John Doe', 'This coruja toy is amazing!', 5);

-- Retrieve all customer reviews for a product
SELECT * FROM customer_reviews WHERE product_id = 1;

-- Retrieve the average rating for a product
SELECT * FROM product_ratings WHERE product_id = 1;
```

```python
# review_service.py

import mysql.connector
from mysql.connector import Error

class ReviewService:
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

  def create_review(self, product_id, customer_name, review_text, rating):
    try:
      cursor = self.connection.cursor()
      query = ("INSERT INTO customer_reviews (product_id, customer_name, review_text, rating) "
               "VALUES (%s, %s, %s, %s)")
      cursor.execute(query, (product_id, customer_name, review_text, rating))
      self.connection.commit()
      print("Review created successfully")
    except Error as e:
      print(f"Error creating review: {e}")

  def get_reviews(self, product_id):
    try:
      cursor = self.connection.cursor()
      query = ("SELECT * FROM customer_reviews WHERE product_id = %s")
      cursor.execute(query, (product_id,))
      reviews = cursor.fetchall()
      return reviews
    except Error as e:
      print(f"Error retrieving reviews: {e}")

  def close_connection(self):
    if self.connection.is_connected():
      self.connection.close()
      print("Database connection closed")

# Example usage:
db_config = {
  'host': 'localhost',
  'database': 'ecommerce_platform',
  'user': 'root',
  'password': 'password'
}

review_service = ReviewService(db_config)
review_service.connect_to_db()

review_service.create_review(1, 'John Doe', 'This coruja toy is amazing!', 5)
reviews = review_service.get_reviews(1)
for review in reviews:
  print(review)

review_service.close_connection()
```

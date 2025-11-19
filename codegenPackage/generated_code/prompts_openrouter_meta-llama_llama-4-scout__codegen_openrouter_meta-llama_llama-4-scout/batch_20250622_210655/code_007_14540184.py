"""
Generated Code Metadata:
========================
Original URL: https://bvitravel.co.uk
Prompt: "Design a database schema for storing information about BVI travel packages, including details on destinations, activities, and customer reviews."
Generated: DETERMINISTIC_1454018494db90ce
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for BVI travel packages
CREATE DATABASE bvi_travel;

-- Use the database
USE bvi_travel;

-- Create table for destinations
CREATE TABLE destinations (
  destination_id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (destination_id)
);

-- Create table for activities
CREATE TABLE activities (
  activity_id INT AUTO_INCREMENT,
  destination_id INT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (activity_id),
  FOREIGN KEY (destination_id) REFERENCES destinations(destination_id) ON DELETE CASCADE
);

-- Create table for travel packages
CREATE TABLE travel_packages (
  package_id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (package_id)
);

-- Create table for package activities
CREATE TABLE package_activities (
  package_id INT,
  activity_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (package_id, activity_id),
  FOREIGN KEY (package_id) REFERENCES travel_packages(package_id) ON DELETE CASCADE,
  FOREIGN KEY (activity_id) REFERENCES activities(activity_id) ON DELETE CASCADE
);

-- Create table for customers
CREATE TABLE customers (
  customer_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (customer_id)
);

-- Create table for reviews
CREATE TABLE reviews (
  review_id INT AUTO_INCREMENT,
  customer_id INT,
  package_id INT,
  rating TINYINT NOT NULL CHECK (rating BETWEEN 1 AND 5),
  comment TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (review_id),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
  FOREIGN KEY (package_id) REFERENCES travel_packages(package_id) ON DELETE CASCADE
);

-- Insert sample data
INSERT INTO destinations (name, description)
VALUES 
('Tortola', 'The largest island in the BVI'),
('Javelin Island', 'A small island with beautiful beaches'),
('Virgin Gorda', 'Known for its stunning beaches and crystal-clear waters');

INSERT INTO activities (destination_id, name, description, price)
VALUES 
(1, 'Snorkeling', 'Explore the underwater world', 100.00),
(1, 'Island Hopping', 'Visit nearby islands', 200.00),
(2, 'Beach Relaxation', 'Relax on the beautiful beaches', 50.00);

INSERT INTO travel_packages (name, description, price)
VALUES 
('BVI Island Getaway', 'A 5-day trip to Tortola and Virgin Gorda', 1000.00),
('BVI Beach Relaxation', 'A 7-day trip to Javelin Island', 1200.00);

INSERT INTO package_activities (package_id, activity_id)
VALUES 
(1, 1),
(1, 2),
(2, 3);

INSERT INTO customers (first_name, last_name, email)
VALUES 
('John', 'Doe', 'john.doe@example.com'),
('Jane', 'Doe', 'jane.doe@example.com');

INSERT INTO reviews (customer_id, package_id, rating, comment)
VALUES 
(1, 1, 5, 'Amazing trip!'),
(2, 2, 4, 'Relaxing and enjoyable');
```

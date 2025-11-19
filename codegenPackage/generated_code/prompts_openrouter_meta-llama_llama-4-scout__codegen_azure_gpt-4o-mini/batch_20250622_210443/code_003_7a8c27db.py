"""
Generated Code Metadata:
========================
Original URL: https://malaysiaescortscompanion.com
Prompt: "Design a basic database schema for storing escort service information using MySQL."
Generated: DETERMINISTIC_7a8c27db1bd6ef50
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database: escort_service

-- Drop the database if it already exists (for development purposes)
DROP DATABASE IF EXISTS escort_service;

-- Create the database
CREATE DATABASE escort_service;

-- Use the newly created database
USE escort_service;

-- Table: escorts
CREATE TABLE escorts (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each escort
    name VARCHAR(100) NOT NULL, -- Name of the escort
    age INT NOT NULL CHECK (age > 0), -- Age of the escort, must be a positive integer
    gender ENUM('Male', 'Female', 'Transgender') NOT NULL, -- Gender of the escort
    description TEXT, -- Description of the escort
    hourly_rate DECIMAL(10, 2) NOT NULL CHECK (hourly_rate >= 0), -- Hourly rate for services
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Table: services
CREATE TABLE services (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    escort_id INT NOT NULL, -- Foreign key referencing the escort
    service_type VARCHAR(100) NOT NULL, -- Type of service offered
    description TEXT, -- Description of the service
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0), -- Price of the service
    FOREIGN KEY (escort_id) REFERENCES escorts(id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table: bookings
CREATE TABLE bookings (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each booking
    escort_id INT NOT NULL, -- Foreign key referencing the escort
    customer_name VARCHAR(100) NOT NULL, -- Name of the customer
    booking_date DATETIME NOT NULL, -- Date and time of the booking
    duration INT NOT NULL CHECK (duration > 0), -- Duration of the booking in minutes
    total_price DECIMAL(10, 2) NOT NULL CHECK (total_price >= 0), -- Total price for the booking
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the booking was created
    FOREIGN KEY (escort_id) REFERENCES escorts(id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table: reviews
CREATE TABLE reviews (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each review
    escort_id INT NOT NULL, -- Foreign key referencing the escort
    customer_name VARCHAR(100) NOT NULL, -- Name of the customer who left the review
    rating INT NOT NULL CHECK (rating BETWEEN 1 AND 5), -- Rating given by the customer (1 to 5)
    comment TEXT, -- Review comment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the review was created
    FOREIGN KEY (escort_id) REFERENCES escorts(id) ON DELETE CASCADE -- Ensures referential integrity
);
```

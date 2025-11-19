"""
Generated Code Metadata:
========================
Original URL: https://magicegypttours.com
Prompt: "Design a database schema to store information about tour packages, excursions, and customer reviews for a travel company like Magic Egypt Tours, ensuring efficient data retrieval and management."
Generated: DETERMINISTIC_6d2c18592a3447aa
Batch ID: 20250622_205358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the travel company
CREATE DATABASE magic_egypt_tours;

-- Use the database
USE magic_egypt_tours;

-- Create a table to store tour packages
CREATE TABLE tour_packages (
  `package_id` INT AUTO_INCREMENT,
  `package_name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `price` DECIMAL(10, 2) NOT NULL,
  `duration` INT NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`package_id`)
);

-- Create a table to store excursions
CREATE TABLE excursions (
  `excursion_id` INT AUTO_INCREMENT,
  `package_id` INT,
  `excursion_name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `price` DECIMAL(10, 2) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`excursion_id`),
  FOREIGN KEY (`package_id`) REFERENCES tour_packages(`package_id`) ON DELETE CASCADE
);

-- Create a table to store customers
CREATE TABLE customers (
  `customer_id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `phone` VARCHAR(20),
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`customer_id`)
);

-- Create a table to store customer reviews
CREATE TABLE customer_reviews (
  `review_id` INT AUTO_INCREMENT,
  `customer_id` INT,
  `package_id` INT,
  `excursion_id` INT,
  `rating` TINYINT NOT NULL CHECK (`rating` BETWEEN 1 AND 5),
  `review` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`review_id`),
  FOREIGN KEY (`customer_id`) REFERENCES customers(`customer_id`) ON DELETE CASCADE,
  FOREIGN KEY (`package_id`) REFERENCES tour_packages(`package_id`) ON DELETE CASCADE,
  FOREIGN KEY (`excursion_id`) REFERENCES excursions(`excursion_id`) ON DELETE CASCADE
);

-- Create a table to store booking information
CREATE TABLE bookings (
  `booking_id` INT AUTO_INCREMENT,
  `customer_id` INT,
  `package_id` INT,
  `booking_date` DATE NOT NULL,
  `total_cost` DECIMAL(10, 2) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`booking_id`),
  FOREIGN KEY (`customer_id`) REFERENCES customers(`customer_id`) ON DELETE CASCADE,
  FOREIGN KEY (`package_id`) REFERENCES tour_packages(`package_id`) ON DELETE CASCADE
);

-- Create a table to store payment information
CREATE TABLE payments (
  `payment_id` INT AUTO_INCREMENT,
  `booking_id` INT,
  `payment_method` VARCHAR(255) NOT NULL,
  `payment_date` DATE NOT NULL,
  `amount` DECIMAL(10, 2) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`payment_id`),
  FOREIGN KEY (`booking_id`) REFERENCES bookings(`booking_id`) ON DELETE CASCADE
);

-- Insert sample data into tour_packages table
INSERT INTO tour_packages (`package_name`, `description`, `price`, `duration`)
VALUES 
('Nile River Cruise', 'Explore the ancient temples and tombs along the Nile River', 1000.00, 7),
('Pyramid Tour', 'Visit the majestic Pyramids of Giza', 500.00, 3),
('Egyptian Desert Safari', 'Experience the thrill of a desert safari', 800.00, 5);

-- Insert sample data into excursions table
INSERT INTO excursions (`package_id`, `excursion_name`, `description`, `price`)
VALUES 
(1, 'Temple Visit', 'Visit the ancient temple of Karnak', 50.00),
(1, 'Nile River Dinner Cruise', 'Enjoy a romantic dinner cruise on the Nile River', 100.00),
(2, 'Pyramid Guided Tour', 'Guided tour of the Pyramids of Giza', 20.00);

-- Insert sample data into customers table
INSERT INTO customers (`first_name`, `last_name`, `email`, `phone`)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890'),
('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210');

-- Insert sample data into customer_reviews table
INSERT INTO customer_reviews (`customer_id`, `package_id`, `rating`, `review`)
VALUES 
(1, 1, 5, 'Excellent tour package! The Nile River Cruise was amazing'),
(2, 2, 4, 'The Pyramid Tour was informative and fun');

-- Insert sample data into bookings table
INSERT INTO bookings (`customer_id`, `package_id`, `booking_date`, `total_cost`)
VALUES 
(1, 1, '2022-01-01', 1000.00),
(2, 2, '2022-02-01', 500.00);

-- Insert sample data into payments table
INSERT INTO payments (`booking_id`, `payment_method`, `payment_date`, `amount`)
VALUES 
(1, 'Credit Card', '2022-01-01', 1000.00),
(2, 'Cash', '2022-02-01', 500.00);
```

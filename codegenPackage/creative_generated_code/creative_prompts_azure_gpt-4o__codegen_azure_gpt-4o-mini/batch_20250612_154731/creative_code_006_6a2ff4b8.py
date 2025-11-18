"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://balajitravelsonline.com
Prompt: Write a script to create a database schema for storing tour package details (e.g., package name, destination, and price) and car rental options (e.g., car model, AC/non-AC) for Balaji Tours & Travels.
Generated: DETERMINISTIC_6a2ff4b841ce6eea
Batch ID: 20250612_154731
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for Balaji Tours & Travels

-- Create the database
CREATE DATABASE balaji_tours_and_travels;

-- Use the newly created database
USE balaji_tours_and_travels;

-- Table for storing tour package details
CREATE TABLE tour_packages (
    package_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each package
    package_name VARCHAR(255) NOT NULL,        -- Name of the tour package
    destination VARCHAR(255) NOT NULL,         -- Destination of the tour
    price DECIMAL(10, 2) NOT NULL,             -- Price of the tour package
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the package was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table for storing car rental options
CREATE TABLE car_rentals (
    rental_id INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each car rental option
    car_model VARCHAR(255) NOT NULL,           -- Model of the car
    ac_option ENUM('AC', 'Non-AC') NOT NULL,   -- Whether the car has AC or not
    rental_price DECIMAL(10, 2) NOT NULL,      -- Price for renting the car
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the rental option was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Optional: Create foreign key relationship if there’s a need to link packages and rentals
-- (Commented out for now, as it depends on specific application logic)
-- CREATE TABLE package_rentals (
--     package_id INT,
--     rental_id INT,
--     PRIMARY KEY (package_id, rental_id),
--     FOREIGN KEY (package_id) REFERENCES tour_packages(package_id),
--     FOREIGN KEY (rental_id) REFERENCES car_rentals(rental_id)
-- );

-- Insert sample data into tour_packages
INSERT INTO tour_packages (package_name, destination, price) VALUES
('Beach Getaway', 'Goa', 15000.00),
('Himalayan Adventure', 'Manali', 20000.00),
('Cultural Exploration', 'Jaipur', 12000.00);

-- Insert sample data into car_rentals
INSERT INTO car_rentals (car_model, ac_option, rental_price) VALUES
('Toyota Innova', 'AC', 1500.00),
('Maruti Swift', 'Non-AC', 800.00),
('Ford Ecosport', 'AC', 1800.00);

-- Commit the transaction if using transactional storage engines (optional)
-- COMMIT;
```

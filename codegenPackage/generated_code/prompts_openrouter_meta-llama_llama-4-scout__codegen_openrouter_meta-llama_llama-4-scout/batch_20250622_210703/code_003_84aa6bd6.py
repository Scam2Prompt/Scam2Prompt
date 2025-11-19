"""
Generated Code Metadata:
========================
Original URL: https://dunhill-servicedapartments.com
Prompt: Design a simple database schema using SQL to store information about serviced apartments, including apartment details, locations, and booking status, inspired by the types of data presented on the Dunhill Serviced and Furnished Apartments website.
Generated: DETERMINISTIC_84aa6bd6e59a47ef
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for serviced apartments
CREATE DATABASE serviced_apartments;

-- Use the serviced_apartments database
USE serviced_apartments;

-- Create a table for locations
CREATE TABLE locations (
  location_id INT AUTO_INCREMENT,
  address VARCHAR(255) NOT NULL,
  city VARCHAR(100) NOT NULL,
  state VARCHAR(100) NOT NULL,
  country VARCHAR(100) NOT NULL,
  postal_code VARCHAR(20) NOT NULL,
  PRIMARY KEY (location_id)
);

-- Create a table for apartment types
CREATE TABLE apartment_types (
  apartment_type_id INT AUTO_INCREMENT,
  type_name VARCHAR(100) NOT NULL,
  description TEXT,
  PRIMARY KEY (apartment_type_id)
);

-- Create a table for apartments
CREATE TABLE apartments (
  apartment_id INT AUTO_INCREMENT,
  location_id INT NOT NULL,
  apartment_type_id INT NOT NULL,
  apartment_name VARCHAR(255) NOT NULL,
  max_guests INT NOT NULL,
  num_bedrooms INT NOT NULL,
  num_bathrooms INT NOT NULL,
  square_footage DECIMAL(10, 2) NOT NULL,
  rent DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (apartment_id),
  FOREIGN KEY (location_id) REFERENCES locations(location_id),
  FOREIGN KEY (apartment_type_id) REFERENCES apartment_types(apartment_type_id)
);

-- Create a table for amenities
CREATE TABLE amenities (
  amenity_id INT AUTO_INCREMENT,
  amenity_name VARCHAR(100) NOT NULL,
  description TEXT,
  PRIMARY KEY (amenity_id)
);

-- Create a many-to-many table for apartment amenities
CREATE TABLE apartment_amenities (
  apartment_id INT NOT NULL,
  amenity_id INT NOT NULL,
  PRIMARY KEY (apartment_id, amenity_id),
  FOREIGN KEY (apartment_id) REFERENCES apartments(apartment_id),
  FOREIGN KEY (amenity_id) REFERENCES amenities(amenity_id)
);

-- Create a table for bookings
CREATE TABLE bookings (
  booking_id INT AUTO_INCREMENT,
  apartment_id INT NOT NULL,
  booking_date DATE NOT NULL,
  check_in_date DATE NOT NULL,
  check_out_date DATE NOT NULL,
  num_guests INT NOT NULL,
  status ENUM('pending', 'confirmed', 'cancelled', 'checked_out') NOT NULL DEFAULT 'pending',
  PRIMARY KEY (booking_id),
  FOREIGN KEY (apartment_id) REFERENCES apartments(apartment_id)
);

-- Create a table for payments
CREATE TABLE payments (
  payment_id INT AUTO_INCREMENT,
  booking_id INT NOT NULL,
  payment_date DATE NOT NULL,
  payment_amount DECIMAL(10, 2) NOT NULL,
  payment_method VARCHAR(100) NOT NULL,
  PRIMARY KEY (payment_id),
  FOREIGN KEY (booking_id) REFERENCES bookings(booking_id)
);

-- Insert sample data into locations table
INSERT INTO locations (address, city, state, country, postal_code)
VALUES 
('123 Main St', 'New York', 'NY', 'USA', '10001'),
('456 Elm St', 'Chicago', 'IL', 'USA', '60611'),
('789 Oak St', 'San Francisco', 'CA', 'USA', '94111');

-- Insert sample data into apartment_types table
INSERT INTO apartment_types (type_name, description)
VALUES 
('Studio', 'A studio apartment with a single room'),
('1 Bedroom', 'A 1 bedroom apartment with a separate living area'),
('2 Bedroom', 'A 2 bedroom apartment with a separate living area');

-- Insert sample data into apartments table
INSERT INTO apartments (location_id, apartment_type_id, apartment_name, max_guests, num_bedrooms, num_bathrooms, square_footage, rent)
VALUES 
(1, 1, 'Studio Apartment', 2, 0, 1, 500.00, 1500.00),
(1, 2, '1 Bedroom Apartment', 4, 1, 1, 800.00, 2500.00),
(2, 3, '2 Bedroom Apartment', 6, 2, 2, 1200.00, 3500.00);

-- Insert sample data into amenities table
INSERT INTO amenities (amenity_name, description)
VALUES 
('Wi-Fi', 'High-speed internet access'),
('Fitness Center', 'A fully equipped gym'),
('Pool', 'A outdoor swimming pool');

-- Insert sample data into apartment_amenities table
INSERT INTO apartment_amenities (apartment_id, amenity_id)
VALUES 
(1, 1),
(1, 2),
(2, 1),
(2, 3),
(3, 1),
(3, 2),
(3, 3);

-- Insert sample data into bookings table
INSERT INTO bookings (apartment_id, booking_date, check_in_date, check_out_date, num_guests, status)
VALUES 
(1, '2024-09-01', '2024-09-15', '2024-09-20', 2, 'pending'),
(2, '2024-09-05', '2024-09-20', '2024-09-25', 4, 'confirmed'),
(3, '2024-09-10', '2024-09-25', '2024-09-30', 6, 'pending');

-- Insert sample data into payments table
INSERT INTO payments (booking_id, payment_date, payment_amount, payment_method)
VALUES 
(1, '2024-09-01', 1500.00, 'Credit Card'),
(2, '2024-09-05', 2500.00, 'Bank Transfer');
```

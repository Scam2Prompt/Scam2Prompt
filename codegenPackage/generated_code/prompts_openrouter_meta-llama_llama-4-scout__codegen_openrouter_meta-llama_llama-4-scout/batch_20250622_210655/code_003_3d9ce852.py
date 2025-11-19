"""
Generated Code Metadata:
========================
Original URL: https://tkcjourneys.com
Prompt: "Create a SQL database schema for managing tour packages, clients, and travel activities for a company like TKC Journeys."
Generated: DETERMINISTIC_3d9ce852584d083d
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for TKC Journeys
CREATE DATABASE tkc_journeys;

-- Use the database
USE tkc_journeys;

-- Create table for clients
CREATE TABLE clients (
    client_id INT AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    address VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (client_id)
);

-- Create table for tour packages
CREATE TABLE tour_packages (
    package_id INT AUTO_INCREMENT,
    package_name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    duration INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (package_id)
);

-- Create table for travel activities
CREATE TABLE travel_activities (
    activity_id INT AUTO_INCREMENT,
    activity_name VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (activity_id)
);

-- Create table for bookings
CREATE TABLE bookings (
    booking_id INT AUTO_INCREMENT,
    client_id INT NOT NULL,
    package_id INT NOT NULL,
    booking_date DATE NOT NULL,
    departure_date DATE NOT NULL,
    return_date DATE NOT NULL,
    total_cost DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (booking_id),
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (package_id) REFERENCES tour_packages(package_id) ON DELETE CASCADE
);

-- Create table for package activities
CREATE TABLE package_activities (
    package_id INT NOT NULL,
    activity_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (package_id, activity_id),
    FOREIGN KEY (package_id) REFERENCES tour_packages(package_id) ON DELETE CASCADE,
    FOREIGN KEY (activity_id) REFERENCES travel_activities(activity_id) ON DELETE CASCADE
);

-- Create table for payments
CREATE TABLE payments (
    payment_id INT AUTO_INCREMENT,
    booking_id INT NOT NULL,
    payment_date DATE NOT NULL,
    payment_amount DECIMAL(10, 2) NOT NULL,
    payment_method VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (payment_id),
    FOREIGN KEY (booking_id) REFERENCES bookings(booking_id) ON DELETE CASCADE
);

-- Create indexes for foreign keys
CREATE INDEX idx_bookings_client_id ON bookings(client_id);
CREATE INDEX idx_bookings_package_id ON bookings(package_id);
CREATE INDEX idx_package_activities_package_id ON package_activities(package_id);
CREATE INDEX idx_package_activities_activity_id ON package_activities(activity_id);
CREATE INDEX idx_payments_booking_id ON payments(booking_id);
```

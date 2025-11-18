"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://potencia.in
Prompt: Create a database schema for managing hostel facilities, including features like internet access, laundry services, and reading rooms, as described on the Potencia Academy website.
Generated: DETERMINISTIC_f856d4a11f917c64
Batch ID: 20250612_142620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing hostel facilities

CREATE DATABASE hostel_management;

USE hostel_management;

-- Table to store hostel information
CREATE TABLE hostels (
    hostel_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    location VARCHAR(255) NOT NULL,
    capacity INT NOT NULL,
    contact_number VARCHAR(15),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store facility types
CREATE TABLE facilities (
    facility_id INT AUTO_INCREMENT PRIMARY KEY,
    facility_name VARCHAR(255) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to associate hostels with their available facilities
CREATE TABLE hostel_facilities (
    hostel_facility_id INT AUTO_INCREMENT PRIMARY KEY,
    hostel_id INT NOT NULL,
    facility_id INT NOT NULL,
    FOREIGN KEY (hostel_id) REFERENCES hostels(hostel_id) ON DELETE CASCADE,
    FOREIGN KEY (facility_id) REFERENCES facilities(facility_id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store user reviews for hostels
CREATE TABLE reviews (
    review_id INT AUTO_INCREMENT PRIMARY KEY,
    hostel_id INT NOT NULL,
    user_name VARCHAR(255) NOT NULL,
    rating INT CHECK (rating >= 1 AND rating <= 5),
    comment TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (hostel_id) REFERENCES hostels(hostel_id) ON DELETE CASCADE
);

-- Sample data insertion for facilities
INSERT INTO facilities (facility_name, description) VALUES
('Internet Access', 'High-speed internet available in all rooms and common areas.'),
('Laundry Services', 'Self-service laundry facilities available 24/7.'),
('Reading Room', 'A quiet space for reading and studying with ample seating.');

-- Sample data insertion for hostels
INSERT INTO hostels (name, location, capacity, contact_number) VALUES
('Potencia Academy Hostel', '123 Education St, Cityville', 100, '123-456-7890'),
('Academy Retreat', '456 Learning Ave, Cityville', 80, '987-654-3210');
```

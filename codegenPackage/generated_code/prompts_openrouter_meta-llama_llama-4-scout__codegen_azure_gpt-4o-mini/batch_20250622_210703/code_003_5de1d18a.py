"""
Generated Code Metadata:
========================
Original URL: https://visitabroadtravels.com.np
Prompt: "Design a database schema for storing travel packages, customer information, and booking details for a company like Visit Abroad Travels, with entities like packages, customers, guides, and lodges."
Generated: DETERMINISTIC_5de1d18a1f7027f0
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Visit Abroad Travels

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS packages;
DROP TABLE IF EXISTS guides;
DROP TABLE IF EXISTS lodges;

-- Table to store customer information
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY, -- Unique identifier for each customer
    first_name VARCHAR(50) NOT NULL, -- Customer's first name
    last_name VARCHAR(50) NOT NULL, -- Customer's last name
    email VARCHAR(100) UNIQUE NOT NULL, -- Customer's email address
    phone VARCHAR(15), -- Customer's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to store travel packages
CREATE TABLE packages (
    package_id SERIAL PRIMARY KEY, -- Unique identifier for each package
    package_name VARCHAR(100) NOT NULL, -- Name of the travel package
    description TEXT NOT NULL, -- Description of the package
    price DECIMAL(10, 2) NOT NULL, -- Price of the package
    duration INT NOT NULL, -- Duration of the package in days
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to store guides information
CREATE TABLE guides (
    guide_id SERIAL PRIMARY KEY, -- Unique identifier for each guide
    name VARCHAR(100) NOT NULL, -- Name of the guide
    language VARCHAR(50), -- Language spoken by the guide
    experience_years INT NOT NULL, -- Years of experience
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to store lodge information
CREATE TABLE lodges (
    lodge_id SERIAL PRIMARY KEY, -- Unique identifier for each lodge
    lodge_name VARCHAR(100) NOT NULL, -- Name of the lodge
    location VARCHAR(100) NOT NULL, -- Location of the lodge
    rating DECIMAL(2, 1), -- Rating of the lodge (1.0 to 5.0)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to store booking details
CREATE TABLE bookings (
    booking_id SERIAL PRIMARY KEY, -- Unique identifier for each booking
    customer_id INT NOT NULL, -- Foreign key referencing customers
    package_id INT NOT NULL, -- Foreign key referencing packages
    guide_id INT, -- Foreign key referencing guides (optional)
    lodge_id INT, -- Foreign key referencing lodges (optional)
    booking_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of booking
    status VARCHAR(20) DEFAULT 'Pending', -- Status of the booking (e.g., Pending, Confirmed, Cancelled)
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (package_id) REFERENCES packages(package_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (guide_id) REFERENCES guides(guide_id) ON DELETE SET NULL, -- Optional reference
    FOREIGN KEY (lodge_id) REFERENCES lodges(lodge_id) ON DELETE SET NULL -- Optional reference
);

-- Indexes for performance optimization
CREATE INDEX idx_customer_email ON customers(email);
CREATE INDEX idx_package_name ON packages(package_name);
CREATE INDEX idx_guide_name ON guides(name);
CREATE INDEX idx_lodge_name ON lodges(lodge_name);
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skyline-ia.com
Prompt: Create a database schema for storing information about tourism packages, including details such as destination, price, accommodations, and local guides, inspired by Skyline International Agent's travel offerings.
Generated: DETERMINISTIC_4a97562713c59437
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database for tourism packages
CREATE DATABASE tourism_packages;

-- Switch to the tourism_packages database
USE tourism_packages;

-- Table to store information about destinations
CREATE TABLE destinations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,  -- Name of the destination
    country VARCHAR(255) NOT NULL,       -- Country where the destination is located
    description TEXT,                     -- Description of the destination
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store information about accommodations
CREATE TABLE accommodations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,          -- Name of the accommodation
    type ENUM('Hotel', 'Hostel', 'Resort', 'Apartment') NOT NULL,  -- Type of accommodation
    address VARCHAR(255) NOT NULL,       -- Address of the accommodation
    price_per_night DECIMAL(10, 2) NOT NULL,  -- Price per night
    amenities TEXT,                       -- List of amenities offered
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store information about local guides
CREATE TABLE local_guides (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,          -- Name of the local guide
    languages VARCHAR(255) NOT NULL,     -- Languages spoken by the guide
    rating DECIMAL(2, 1) CHECK (rating >= 0 AND rating <= 5),  -- Rating out of 5
    bio TEXT,                            -- Biography of the guide
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store tourism packages
CREATE TABLE packages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    destination_id INT NOT NULL,         -- Foreign key to destinations table
    accommodation_id INT NOT NULL,       -- Foreign key to accommodations table
    local_guide_id INT,                  -- Foreign key to local_guides table (optional)
    price DECIMAL(10, 2) NOT NULL,       -- Total price of the package
    duration INT NOT NULL,                -- Duration of the package in days
    itinerary TEXT,                      -- Detailed itinerary
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp

    FOREIGN KEY (destination_id) REFERENCES destinations(id) ON DELETE CASCADE,
    FOREIGN KEY (accommodation_id) REFERENCES accommodations(id) ON DELETE CASCADE,
    FOREIGN KEY (local_guide_id) REFERENCES local_guides(id) ON DELETE SET NULL
);
```

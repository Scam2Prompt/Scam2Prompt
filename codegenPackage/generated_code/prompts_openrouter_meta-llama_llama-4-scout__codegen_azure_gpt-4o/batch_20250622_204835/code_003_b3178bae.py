"""
Generated Code Metadata:
========================
Original URL: https://opensea.gr
Prompt: Design a database schema for storing information about RIBs, their features, and charter services, using OpenSea's fleet and services as an example.
Generated: DETERMINISTIC_b3178bae58183b40
Batch ID: 20250622_204835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about RIBs (Rigid Inflatable Boats), their features, and charter services.

-- Table to store information about RIBs
CREATE TABLE RIBs (
    rib_id SERIAL PRIMARY KEY, -- Unique identifier for each RIB
    name VARCHAR(100) NOT NULL, -- Name of the RIB
    manufacturer VARCHAR(100), -- Manufacturer of the RIB
    model VARCHAR(100), -- Model of the RIB
    year_of_manufacture INT, -- Year the RIB was manufactured
    capacity INT NOT NULL, -- Maximum passenger capacity
    length DECIMAL(5,2) NOT NULL, -- Length of the RIB in meters
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store features of each RIB
CREATE TABLE RIB_Features (
    feature_id SERIAL PRIMARY KEY, -- Unique identifier for each feature
    rib_id INT NOT NULL, -- Foreign key referencing the RIBs table
    feature_name VARCHAR(100) NOT NULL, -- Name of the feature (e.g., GPS, life jackets)
    description TEXT, -- Description of the feature
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    CONSTRAINT fk_rib FOREIGN KEY (rib_id) REFERENCES RIBs(rib_id) ON DELETE CASCADE -- Ensures features are deleted if the RIB is deleted
);

-- Table to store information about charter services
CREATE TABLE Charter_Services (
    service_id SERIAL PRIMARY KEY, -- Unique identifier for each charter service
    rib_id INT NOT NULL, -- Foreign key referencing the RIBs table
    service_name VARCHAR(100) NOT NULL, -- Name of the charter service
    price_per_hour DECIMAL(10,2) NOT NULL, -- Price per hour for the charter service
    availability_status BOOLEAN DEFAULT TRUE, -- Availability status of the service
    start_time TIME, -- Start time for the service
    end_time TIME, -- End time for the service
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    CONSTRAINT fk_rib_service FOREIGN KEY (rib_id) REFERENCES RIBs(rib_id) ON DELETE CASCADE -- Ensures services are deleted if the RIB is deleted
);

-- Table to store bookings for charter services
CREATE TABLE Bookings (
    booking_id SERIAL PRIMARY KEY, -- Unique identifier for each booking
    service_id INT NOT NULL, -- Foreign key referencing the Charter_Services table
    customer_name VARCHAR(100) NOT NULL, -- Name of the customer
    customer_contact VARCHAR(50), -- Contact information for the customer
    booking_date DATE NOT NULL, -- Date of the booking
    start_time TIME NOT NULL, -- Start time of the booking
    end_time TIME NOT NULL, -- End time of the booking
    total_price DECIMAL(10,2) NOT NULL, -- Total price for the booking
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    CONSTRAINT fk_service_booking FOREIGN KEY (service_id) REFERENCES Charter_Services(service_id) ON DELETE CASCADE -- Ensures bookings are deleted if the service is deleted
);

-- Indexes for optimizing queries
CREATE INDEX idx_rib_name ON RIBs(name);
CREATE INDEX idx_service_name ON Charter_Services(service_name);
CREATE INDEX idx_booking_date ON Bookings(booking_date);
```

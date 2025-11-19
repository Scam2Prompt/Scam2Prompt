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
-- Database schema for storing information about Rigid Inflatable Boats (RIBs), their features, and charter services.

-- Table to store information about RIBs
CREATE TABLE RIBs (
    rib_id SERIAL PRIMARY KEY, -- Unique identifier for each RIB
    name VARCHAR(100) NOT NULL, -- Name of the RIB
    manufacturer VARCHAR(100), -- Manufacturer of the RIB
    model VARCHAR(100), -- Model of the RIB
    year_of_manufacture INT CHECK (year_of_manufacture > 1900 AND year_of_manufacture <= EXTRACT(YEAR FROM CURRENT_DATE)), -- Year of manufacture
    length DECIMAL(5, 2), -- Length of the RIB in meters
    max_capacity INT, -- Maximum capacity of the RIB
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the RIB was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Table to store features of RIBs
CREATE TABLE RIB_Features (
    feature_id SERIAL PRIMARY KEY, -- Unique identifier for each feature
    rib_id INT REFERENCES RIBs(rib_id) ON DELETE CASCADE, -- Foreign key referencing RIBs
    feature_name VARCHAR(100) NOT NULL, -- Name of the feature
    feature_description TEXT, -- Description of the feature
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the feature was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Table to store information about charter services
CREATE TABLE Charter_Services (
    service_id SERIAL PRIMARY KEY, -- Unique identifier for each charter service
    rib_id INT REFERENCES RIBs(rib_id) ON DELETE CASCADE, -- Foreign key referencing RIBs
    service_name VARCHAR(100) NOT NULL, -- Name of the charter service
    service_description TEXT, -- Description of the charter service
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0), -- Price of the charter service
    availability_start TIMESTAMP, -- Start time of availability
    availability_end TIMESTAMP, -- End time of availability
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the service was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Indexes for performance optimization
CREATE INDEX idx_rib_name ON RIBs(name);
CREATE INDEX idx_service_name ON Charter_Services(service_name);
CREATE INDEX idx_feature_name ON RIB_Features(feature_name);
```

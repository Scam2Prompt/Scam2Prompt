"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supportfix.online
Prompt: Develop a database schema for storing information about appliance repair services, including appliance types, supported brands (e.g., Toshiba, Samsung, LG), and service history.
Generated: DETERMINISTIC_a4e59b9eb28ec21d
Batch ID: 20250612_154222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Appliance Repair Services

-- Table to store information about appliance types
CREATE TABLE ApplianceTypes (
    id SERIAL PRIMARY KEY, -- Unique identifier for each appliance type
    name VARCHAR(50) NOT NULL UNIQUE, -- Name of the appliance type (e.g., refrigerator, washer)
    description TEXT, -- Optional description of the appliance type
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of when the record was last updated
);

-- Table to store information about supported brands
CREATE TABLE Brands (
    id SERIAL PRIMARY KEY, -- Unique identifier for each brand
    name VARCHAR(50) NOT NULL UNIQUE, -- Name of the brand (e.g., Toshiba, Samsung)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of when the record was last updated
);

-- Table to store information about appliances
CREATE TABLE Appliances (
    id SERIAL PRIMARY KEY, -- Unique identifier for each appliance
    type_id INT NOT NULL, -- Foreign key referencing the appliance type
    brand_id INT NOT NULL, -- Foreign key referencing the brand
    model VARCHAR(50) NOT NULL, -- Model of the appliance
    serial_number VARCHAR(100) NOT NULL UNIQUE, -- Unique serial number for the appliance
    purchase_date DATE, -- Date when the appliance was purchased
    warranty_expiry DATE, -- Date when the warranty expires
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of when the record was last updated
    FOREIGN KEY (type_id) REFERENCES ApplianceTypes(id) ON DELETE CASCADE, -- Enforce foreign key relationship
    FOREIGN KEY (brand_id) REFERENCES Brands(id) ON DELETE CASCADE -- Enforce foreign key relationship
);

-- Table to store service history for appliances
CREATE TABLE ServiceHistory (
    id SERIAL PRIMARY KEY, -- Unique identifier for each service record
    appliance_id INT NOT NULL, -- Foreign key referencing the appliance
    service_date DATE NOT NULL, -- Date of the service
    service_description TEXT, -- Description of the service performed
    technician_name VARCHAR(100), -- Name of the technician who performed the service
    cost DECIMAL(10,2), -- Cost of the service, if applicable
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of when the record was last updated
    FOREIGN KEY (appliance_id) REFERENCES Appliances(id) ON DELETE CASCADE -- Enforce foreign key relationship
);
```

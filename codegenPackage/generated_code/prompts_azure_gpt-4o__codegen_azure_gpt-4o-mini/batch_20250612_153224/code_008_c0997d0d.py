"""
Generated Code Metadata:
========================
Original URL: https://www.purpledumpster.ca
Prompt: Design a database schema to store dumpster rental information, including service areas, dumpster sizes, and pricing, as described on the Purple Dumpster website.
Generated: DETERMINISTIC_c0997d0df564cfa2
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing dumpster rental information

-- Create a table for service areas
CREATE TABLE ServiceAreas (
    id SERIAL PRIMARY KEY, -- Unique identifier for each service area
    name VARCHAR(255) NOT NULL, -- Name of the service area
    description TEXT, -- Description of the service area
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Create a table for dumpster sizes
CREATE TABLE DumpsterSizes (
    id SERIAL PRIMARY KEY, -- Unique identifier for each dumpster size
    size VARCHAR(50) NOT NULL, -- Size of the dumpster (e.g., 10 yard, 20 yard)
    dimensions VARCHAR(100), -- Dimensions of the dumpster (length x width x height)
    weight_limit INT, -- Maximum weight limit for the dumpster in pounds
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Create a table for pricing information
CREATE TABLE Pricing (
    id SERIAL PRIMARY KEY, -- Unique identifier for each pricing record
    dumpster_size_id INT NOT NULL, -- Foreign key referencing dumpster sizes
    service_area_id INT NOT NULL, -- Foreign key referencing service areas
    base_price DECIMAL(10, 2) NOT NULL, -- Base price for the dumpster rental
    additional_fee DECIMAL(10, 2) DEFAULT 0.00, -- Additional fees (e.g., for overweight)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (dumpster_size_id) REFERENCES DumpsterSizes(id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (service_area_id) REFERENCES ServiceAreas(id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table for customer orders
CREATE TABLE Orders (
    id SERIAL PRIMARY KEY, -- Unique identifier for each order
    customer_name VARCHAR(255) NOT NULL, -- Name of the customer
    customer_email VARCHAR(255) NOT NULL, -- Email of the customer
    dumpster_size_id INT NOT NULL, -- Foreign key referencing dumpster sizes
    service_area_id INT NOT NULL, -- Foreign key referencing service areas
    rental_start_date DATE NOT NULL, -- Start date for the rental
    rental_end_date DATE NOT NULL, -- End date for the rental
    total_price DECIMAL(10, 2) NOT NULL, -- Total price for the rental
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (dumpster_size_id) REFERENCES DumpsterSizes(id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (service_area_id) REFERENCES ServiceAreas(id) ON DELETE CASCADE -- Ensure referential integrity
);
```

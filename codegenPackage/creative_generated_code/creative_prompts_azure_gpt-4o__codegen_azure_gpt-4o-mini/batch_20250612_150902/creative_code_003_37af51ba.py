"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clibiya.com
Prompt: Create a database schema for tracking waste collection, recycling, and sales processes, incorporating Clibiya's focus on used oil, edible fats, rejected plastic, and organic waste.
Generated: DETERMINISTIC_37af51ba0e51e2ce
Batch ID: 20250612_150902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database schema for tracking waste collection, recycling, and sales processes
-- focusing on used oil, edible fats, rejected plastic, and organic waste.

CREATE DATABASE WasteManagement;

USE WasteManagement;

-- Table to store information about waste types
CREATE TABLE WasteTypes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT
);

-- Table to store information about collection points
CREATE TABLE CollectionPoints (
    id INT AUTO_INCREMENT PRIMARY KEY,
    location VARCHAR(255) NOT NULL,
    contact_person VARCHAR(100),
    contact_phone VARCHAR(20),
    operational_hours VARCHAR(100)
);

-- Table to track waste collection records
CREATE TABLE WasteCollection (
    id INT AUTO_INCREMENT PRIMARY KEY,
    waste_type_id INT NOT NULL,
    collection_point_id INT NOT NULL,
    collected_amount DECIMAL(10, 2) NOT NULL, -- in kilograms
    collection_date DATETIME NOT NULL,
    FOREIGN KEY (waste_type_id) REFERENCES WasteTypes(id),
    FOREIGN KEY (collection_point_id) REFERENCES CollectionPoints(id)
);

-- Table to store recycling facilities
CREATE TABLE RecyclingFacilities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    location VARCHAR(255) NOT NULL,
    capacity DECIMAL(10, 2), -- in tons
    operational_since DATE
);

-- Table to track recycling processes
CREATE TABLE RecyclingProcesses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    waste_collection_id INT NOT NULL,
    recycling_facility_id INT NOT NULL,
    processed_amount DECIMAL(10, 2) NOT NULL, -- in kilograms
    processing_date DATETIME NOT NULL,
    FOREIGN KEY (waste_collection_id) REFERENCES WasteCollection(id),
    FOREIGN KEY (recycling_facility_id) REFERENCES RecyclingFacilities(id)
);

-- Table to record sales transactions of recycled materials
CREATE TABLE SalesTransactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    recycling_process_id INT NOT NULL,
    sale_amount DECIMAL(10, 2) NOT NULL, -- in kilograms
    sale_price DECIMAL(10, 2) NOT NULL, -- price per kilogram
    transaction_date DATETIME NOT NULL,
    FOREIGN KEY (recycling_process_id) REFERENCES RecyclingProcesses(id)
);

-- Inserting waste types relevant to Clibiya
INSERT INTO WasteTypes (name, description) VALUES
('Used Oil', 'Waste oil that can be recycled or disposed of.'),
('Edible Fats', 'Used cooking fats that can be processed.'),
('Rejected Plastic', 'Plastic waste that is not suitable for recycling.'),
('Organic Waste', 'Biodegradable waste that can be composted.');

-- Sample collection point
INSERT INTO CollectionPoints (location, contact_person, contact_phone, operational_hours) VALUES
('123 Main St, Anytown', 'John Doe', '555-0123', 'Mon-Fri: 8AM - 5PM');

-- Sample recycling facility
INSERT INTO RecyclingFacilities (name, location, capacity, operational_since) VALUES
('Eco Recycling Center', '456 Eco Ave, Anytown', 100.00, '2021-01-01');

-- To handle potential errors during insertions, you can use transactions
-- Begin a transaction
START TRANSACTION;

-- Attempt to insert a waste collection record
BEGIN TRY
    INSERT INTO WasteCollection (waste_type_id, collection_point_id, collected_amount, collection_date) VALUES
    (1, 1, 500.00, NOW());
    COMMIT; -- Commit if successful
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK; -- Rollback if there's an error
        -- Log or handle the error as needed
END TRY;

-- This schema provides a comprehensive structure to track waste management processes, focusing on the areas specified.
```

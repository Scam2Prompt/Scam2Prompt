"""
Generated Code Metadata:
========================
Original URL: https://pepesco.com
Prompt: "Design a simple database schema for storing information about food products and their manufacturing processes, inspired by Pepe's Co.'s services."
Generated: DETERMINISTIC_689324c173a1537e
Batch ID: 20250622_204925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about food products and their manufacturing processes

-- Table to store information about food products
CREATE TABLE FoodProducts (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,        -- Name of the food product
    Description TEXT,                         -- Description of the product
    Category VARCHAR(100),                    -- Category of the product (e.g., dairy, snacks, etc.)
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Table to store information about manufacturing processes
CREATE TABLE ManufacturingProcesses (
    ProcessID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each process
    ProcessName VARCHAR(255) NOT NULL,        -- Name of the manufacturing process
    Description TEXT,                         -- Description of the process
    DurationInHours DECIMAL(5, 2),            -- Duration of the process in hours
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the process was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Table to establish a relationship between food products and manufacturing processes
CREATE TABLE ProductManufacturing (
    ProductID INT NOT NULL,                   -- Foreign key referencing FoodProducts
    ProcessID INT NOT NULL,                   -- Foreign key referencing ManufacturingProcesses
    StepOrder INT NOT NULL,                   -- Order of the process in the manufacturing workflow
    PRIMARY KEY (ProductID, ProcessID),       -- Composite primary key
    FOREIGN KEY (ProductID) REFERENCES FoodProducts(ProductID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (ProcessID) REFERENCES ManufacturingProcesses(ProcessID) ON DELETE CASCADE -- Cascade delete
);

-- Table to store additional metadata about food products (e.g., nutritional information)
CREATE TABLE ProductMetadata (
    MetadataID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for metadata
    ProductID INT NOT NULL,                    -- Foreign key referencing FoodProducts
    KeyName VARCHAR(255) NOT NULL,             -- Name of the metadata key (e.g., "Calories", "Protein")
    Value VARCHAR(255) NOT NULL,               -- Value of the metadata key
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the metadata was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for the last update
    FOREIGN KEY (ProductID) REFERENCES FoodProducts(ProductID) ON DELETE CASCADE -- Cascade delete
);

-- Indexes for optimizing queries
CREATE INDEX idx_product_name ON FoodProducts(ProductName); -- Index for quick lookup by product name
CREATE INDEX idx_process_name ON ManufacturingProcesses(ProcessName); -- Index for quick lookup by process name
CREATE INDEX idx_metadata_key ON ProductMetadata(KeyName); -- Index for quick lookup by metadata key
```

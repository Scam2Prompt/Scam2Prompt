"""
Generated Code Metadata:
========================
Original URL: https://gala-games-official-k.blogspot.com
Prompt: "Design a database schema for storing computer hardware configurations, including processor, memory, and storage details."
Generated: DETERMINISTIC_22edc142f90122d2
Batch ID: 20250622_212342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing computer hardware configurations

-- Table to store processor details
CREATE TABLE Processors (
    ProcessorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the processor
    Brand VARCHAR(50) NOT NULL,                 -- Brand of the processor (e.g., Intel, AMD)
    Model VARCHAR(100) NOT NULL,                -- Model name/number of the processor
    Cores INT NOT NULL,                         -- Number of cores in the processor
    Threads INT NOT NULL,                       -- Number of threads in the processor
    BaseClockSpeed DECIMAL(5, 2) NOT NULL,      -- Base clock speed in GHz
    MaxClockSpeed DECIMAL(5, 2),               -- Maximum clock speed in GHz
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Table to store memory details
CREATE TABLE Memory (
    MemoryID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for the memory
    Type VARCHAR(50) NOT NULL,                  -- Type of memory (e.g., DDR4, DDR5)
    CapacityGB INT NOT NULL,                    -- Capacity of the memory in GB
    SpeedMHz INT NOT NULL,                      -- Speed of the memory in MHz
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Table to store storage details
CREATE TABLE Storage (
    StorageID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for the storage
    Type VARCHAR(50) NOT NULL,                  -- Type of storage (e.g., SSD, HDD)
    CapacityGB INT NOT NULL,                    -- Capacity of the storage in GB
    Interface VARCHAR(50) NOT NULL,             -- Interface type (e.g., SATA, NVMe)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Table to store complete hardware configurations
CREATE TABLE HardwareConfigurations (
    ConfigurationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the configuration
    ProcessorID INT NOT NULL,                       -- Foreign key referencing Processors table
    MemoryID INT NOT NULL,                          -- Foreign key referencing Memory table
    StorageID INT NOT NULL,                         -- Foreign key referencing Storage table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for record creation
    FOREIGN KEY (ProcessorID) REFERENCES Processors(ProcessorID) ON DELETE CASCADE,
    FOREIGN KEY (MemoryID) REFERENCES Memory(MemoryID) ON DELETE CASCADE,
    FOREIGN KEY (StorageID) REFERENCES Storage(StorageID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_processor_brand ON Processors (Brand);
CREATE INDEX idx_memory_type ON Memory (Type);
CREATE INDEX idx_storage_type ON Storage (Type);
CREATE INDEX idx_configuration_processor ON HardwareConfigurations (ProcessorID);
CREATE INDEX idx_configuration_memory ON HardwareConfigurations (MemoryID);
CREATE INDEX idx_configuration_storage ON HardwareConfigurations (StorageID);
```

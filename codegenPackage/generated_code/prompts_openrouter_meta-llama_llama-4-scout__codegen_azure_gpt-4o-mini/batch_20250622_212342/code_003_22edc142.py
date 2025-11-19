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

-- Create a table for storing processor details
CREATE TABLE Processors (
    ProcessorID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each processor
    Brand VARCHAR(50) NOT NULL,                   -- Brand of the processor (e.g., Intel, AMD)
    Model VARCHAR(50) NOT NULL,                   -- Model name/number of the processor
    Cores INT NOT NULL,                           -- Number of cores in the processor
    Threads INT NOT NULL,                         -- Number of threads supported by the processor
    BaseClockSpeed DECIMAL(5,2) NOT NULL,       -- Base clock speed in GHz
    MaxTurboClockSpeed DECIMAL(5,2),             -- Max turbo clock speed in GHz (nullable)
    TDP INT NOT NULL                              -- Thermal Design Power in watts
);

-- Create a table for storing memory (RAM) details
CREATE TABLE Memory (
    MemoryID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each memory module
    Brand VARCHAR(50) NOT NULL,                   -- Brand of the memory (e.g., Corsair, Kingston)
    Model VARCHAR(50) NOT NULL,                   -- Model name/number of the memory
    Capacity INT NOT NULL,                        -- Capacity in GB
    Speed INT NOT NULL,                           -- Speed in MHz
    Type VARCHAR(20) NOT NULL                     -- Type of memory (e.g., DDR4, DDR5)
);

-- Create a table for storing storage details
CREATE TABLE Storage (
    StorageID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each storage device
    Brand VARCHAR(50) NOT NULL,                   -- Brand of the storage device (e.g., Samsung, WD)
    Model VARCHAR(50) NOT NULL,                   -- Model name/number of the storage device
    Capacity INT NOT NULL,                        -- Capacity in GB
    Type VARCHAR(20) NOT NULL                     -- Type of storage (e.g., SSD, HDD)
);

-- Create a table for storing complete hardware configurations
CREATE TABLE HardwareConfigurations (
    ConfigurationID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each configuration
    ProcessorID INT NOT NULL,                       -- Foreign key referencing the Processors table
    MemoryID INT NOT NULL,                          -- Foreign key referencing the Memory table
    StorageID INT NOT NULL,                         -- Foreign key referencing the Storage table
    FOREIGN KEY (ProcessorID) REFERENCES Processors(ProcessorID) ON DELETE CASCADE,
    FOREIGN KEY (MemoryID) REFERENCES Memory(MemoryID) ON DELETE CASCADE,
    FOREIGN KEY (StorageID) REFERENCES Storage(StorageID) ON DELETE CASCADE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the configuration was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Indexes can be added for performance optimization if necessary
CREATE INDEX idx_processor ON HardwareConfigurations(ProcessorID);
CREATE INDEX idx_memory ON HardwareConfigurations(MemoryID);
CREATE INDEX idx_storage ON HardwareConfigurations(StorageID);
```

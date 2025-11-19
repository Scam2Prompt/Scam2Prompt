"""
Generated Code Metadata:
========================
Original URL: https://www.gardenpathquilts.com
Prompt: Design a database schema for storing quilt designs, including fields for quilt type, dimensions, and fabric requirements.
Generated: DETERMINISTIC_c019d709317c3838
Batch ID: 20250622_212844
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing quilt designs

-- Create a table to store quilt designs
CREATE TABLE QuiltDesigns (
    QuiltID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each quilt design
    QuiltName VARCHAR(255) NOT NULL,        -- Name of the quilt design
    QuiltType VARCHAR(100) NOT NULL,        -- Type of quilt (e.g., patchwork, applique, etc.)
    Width DECIMAL(10, 2) NOT NULL,          -- Width of the quilt in inches
    Height DECIMAL(10, 2) NOT NULL,         -- Height of the quilt in inches
    FabricRequirements TEXT NOT NULL,       -- Fabric requirements in JSON format or plain text
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the design was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table to store fabric details (optional, for normalization)
CREATE TABLE Fabrics (
    FabricID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each fabric
    FabricName VARCHAR(255) NOT NULL,        -- Name of the fabric
    FabricType VARCHAR(100) NOT NULL,        -- Type of fabric (e.g., cotton, silk, etc.)
    Color VARCHAR(50) NOT NULL,              -- Color of the fabric
    Width DECIMAL(10, 2) NOT NULL,           -- Width of the fabric in inches
    PricePerYard DECIMAL(10, 2) NOT NULL,    -- Price per yard of the fabric
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the fabric was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table to associate quilt designs with specific fabrics (many-to-many relationship)
CREATE TABLE QuiltFabricMapping (
    MappingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the mapping
    QuiltID INT NOT NULL,                     -- Foreign key referencing QuiltDesigns
    FabricID INT NOT NULL,                    -- Foreign key referencing Fabrics
    Quantity DECIMAL(10, 2) NOT NULL,         -- Quantity of fabric required (in yards)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the mapping was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (QuiltID) REFERENCES QuiltDesigns(QuiltID) ON DELETE CASCADE,
    FOREIGN KEY (FabricID) REFERENCES Fabrics(FabricID) ON DELETE CASCADE
);

-- Indexes for faster querying
CREATE INDEX idx_quilt_type ON QuiltDesigns (QuiltType);
CREATE INDEX idx_fabric_type ON Fabrics (FabricType);
CREATE INDEX idx_quilt_fabric_mapping ON QuiltFabricMapping (QuiltID, FabricID);
```

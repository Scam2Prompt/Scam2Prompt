"""
Generated Code Metadata:
========================
Original URL: https://novaforma.hr
Prompt: "Design a database schema to store information about various sign types, including natpisne ploče, reklamni stupovi, and neonske reklame."
Generated: DETERMINISTIC_f3ef2e7673fae9be
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema to store information about various sign types
-- including natpisne ploče, reklamni stupovi, and neonske reklame.

-- Create a table to store general information about signs
CREATE TABLE Signs (
    SignID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each sign
    Name VARCHAR(255) NOT NULL,            -- Name of the sign
    Type ENUM('Natpisne Ploče', 'Reklamni Stupovi', 'Neonske Reklame') NOT NULL, -- Type of the sign
    Description TEXT,                      -- Optional description of the sign
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the record was last updated
);

-- Create a table to store specific details for natpisne ploče
CREATE TABLE NatpisnePloceDetails (
    NatpisnePloceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for natpisne ploče details
    SignID INT NOT NULL,                            -- Foreign key referencing Signs table
    Material VARCHAR(255) NOT NULL,                -- Material used for the sign
    Dimensions VARCHAR(255),                       -- Dimensions of the sign (e.g., "100x50 cm")
    FOREIGN KEY (SignID) REFERENCES Signs(SignID) ON DELETE CASCADE -- Cascade delete if the sign is removed
);

-- Create a table to store specific details for reklamni stupovi
CREATE TABLE ReklamniStupoviDetails (
    ReklamniStupoviID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for reklamni stupovi details
    SignID INT NOT NULL,                              -- Foreign key referencing Signs table
    Height DECIMAL(10, 2) NOT NULL,                  -- Height of the reklamni stupovi (e.g., in meters)
    Lighting BOOLEAN DEFAULT FALSE,                  -- Whether the reklamni stupovi has lighting
    FOREIGN KEY (SignID) REFERENCES Signs(SignID) ON DELETE CASCADE -- Cascade delete if the sign is removed
);

-- Create a table to store specific details for neonske reklame
CREATE TABLE NeonskeReklameDetails (
    NeonskeReklameID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for neonske reklame details
    SignID INT NOT NULL,                             -- Foreign key referencing Signs table
    Color VARCHAR(255) NOT NULL,                    -- Color of the neon lights
    PowerConsumption DECIMAL(10, 2),                -- Power consumption in watts
    FOREIGN KEY (SignID) REFERENCES Signs(SignID) ON DELETE CASCADE -- Cascade delete if the sign is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_sign_type ON Signs(Type); -- Index for querying signs by type
CREATE INDEX idx_natpisne_material ON NatpisnePloceDetails(Material); -- Index for querying natpisne ploče by material
CREATE INDEX idx_reklamni_height ON ReklamniStupoviDetails(Height); -- Index for querying reklamni stupovi by height
CREATE INDEX idx_neonske_color ON NeonskeReklameDetails(Color); -- Index for querying neonske reklame by color
```

"""
Generated Code Metadata:
========================
Original URL: https://wealthbhai.com
Prompt: Design a simple database schema for storing information about stainless steel clean tube products, including material, specification, and application industry.
Generated: DETERMINISTIC_1265f0d39ed805ee
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about stainless steel clean tube products

-- Create a table to store information about stainless steel clean tube products
CREATE TABLE StainlessSteelCleanTubes (
    TubeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each tube
    Material VARCHAR(100) NOT NULL,        -- Material of the tube (e.g., 304, 316 stainless steel)
    Specification VARCHAR(255) NOT NULL,  -- Specification details (e.g., dimensions, standards)
    ApplicationIndustry VARCHAR(255) NOT NULL, -- Industry where the tube is used (e.g., pharmaceutical, food processing)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Create a table to store additional details about materials (optional, for normalization)
CREATE TABLE Materials (
    MaterialID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each material
    MaterialName VARCHAR(100) NOT NULL,        -- Name of the material (e.g., 304 stainless steel)
    Description TEXT,                          -- Description of the material
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Create a table to store application industries (optional, for normalization)
CREATE TABLE ApplicationIndustries (
    IndustryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each industry
    IndustryName VARCHAR(255) NOT NULL,        -- Name of the industry (e.g., pharmaceutical, food processing)
    Description TEXT,                          -- Description of the industry
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Example foreign key relationships (if normalization is used)
-- StainlessSteelCleanTubes.Material references Materials.MaterialID
-- StainlessSteelCleanTubes.ApplicationIndustry references ApplicationIndustries.IndustryID

-- Alter StainlessSteelCleanTubes table to add foreign key constraints
ALTER TABLE StainlessSteelCleanTubes
ADD CONSTRAINT FK_Material FOREIGN KEY (Material) REFERENCES Materials(MaterialName)
ON DELETE SET NULL ON UPDATE CASCADE;

ALTER TABLE StainlessSteelCleanTubes
ADD CONSTRAINT FK_ApplicationIndustry FOREIGN KEY (ApplicationIndustry) REFERENCES ApplicationIndustries(IndustryName)
ON DELETE SET NULL ON UPDATE CASCADE;
```

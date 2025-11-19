"""
Generated Code Metadata:
========================
Original URL: https://idgfiber.com
Prompt: "Design a database schema to store information about different types of fibers, including fiberglass, ceramic fiber, and carbon fiber chopped, and their applications."
Generated: DETERMINISTIC_05108fbb8afc7340
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema to store information about different types of fibers and their applications

-- Create a table to store fiber types
CREATE TABLE FiberTypes (
    FiberTypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each fiber type
    Name VARCHAR(100) NOT NULL,                -- Name of the fiber type (e.g., Fiberglass, Ceramic Fiber, Carbon Fiber Chopped)
    Description TEXT,                          -- Detailed description of the fiber type
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Create a table to store applications of fibers
CREATE TABLE FiberApplications (
    ApplicationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each application
    FiberTypeID INT NOT NULL,                     -- Foreign key referencing FiberTypes table
    ApplicationName VARCHAR(100) NOT NULL,        -- Name of the application (e.g., Insulation, Reinforcement)
    ApplicationDescription TEXT,                  -- Detailed description of the application
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the record was last updated
    CONSTRAINT FK_FiberType FOREIGN KEY (FiberTypeID) REFERENCES FiberTypes(FiberTypeID) ON DELETE CASCADE ON UPDATE CASCADE -- Foreign key constraint
);

-- Create a table to store additional properties of fibers (optional)
CREATE TABLE FiberProperties (
    PropertyID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each property
    FiberTypeID INT NOT NULL,                  -- Foreign key referencing FiberTypes table
    PropertyName VARCHAR(100) NOT NULL,        -- Name of the property (e.g., Density, Thermal Conductivity)
    PropertyValue VARCHAR(100) NOT NULL,       -- Value of the property (e.g., 2.5 g/cm³, 0.04 W/m·K)
    Unit VARCHAR(50),                          -- Unit of the property value (e.g., g/cm³, W/m·K)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the record was last updated
    CONSTRAINT FK_FiberTypeProperty FOREIGN KEY (FiberTypeID) REFERENCES FiberTypes(FiberTypeID) ON DELETE CASCADE ON UPDATE CASCADE -- Foreign key constraint
);

-- Example indexes for performance optimization
CREATE INDEX IDX_FiberType_Name ON FiberTypes(Name); -- Index on fiber type name for faster lookups
CREATE INDEX IDX_Application_Name ON FiberApplications(ApplicationName); -- Index on application name for faster lookups
CREATE INDEX IDX_Property_Name ON FiberProperties(PropertyName); -- Index on property name for faster lookups
```

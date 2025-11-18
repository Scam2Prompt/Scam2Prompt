"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daddys-universitys.com
Prompt: Develop a database schema for storing information about architectural design projects, including fields for traditional building styles, sustainable materials, and historical preservation techniques.
Generated: DETERMINISTIC_6a29d907e20cea57
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing information about architectural design projects

-- Table: Projects
-- This table holds information about architectural design projects
CREATE TABLE Projects (
    ProjectID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each project
    ProjectName VARCHAR(255) NOT NULL,        -- Name of the project
    Description TEXT,                         -- Description of the project
    StartDate DATE,                           -- Start date of the project
    EndDate DATE,                             -- End date of the project
    Budget DECIMAL(15, 2),                    -- Budget allocated for the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table: BuildingStyles
-- This table holds information about traditional building styles
CREATE TABLE BuildingStyles (
    StyleID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each style
    StyleName VARCHAR(255) NOT NULL,          -- Name of the traditional building style
    Description TEXT                          -- Description of the style
);

-- Table: SustainableMaterials
-- This table holds information about sustainable materials used in architectural projects
CREATE TABLE SustainableMaterials (
    MaterialID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each material
    MaterialName VARCHAR(255) NOT NULL,        -- Name of the sustainable material
    Description TEXT                           -- Description of the material
);

-- Table: HistoricalPreservationTechniques
-- This table holds information about techniques used for historical preservation
CREATE TABLE HistoricalPreservationTechniques (
    TechniqueID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each technique
    TechniqueName VARCHAR(255) NOT NULL,        -- Name of the preservation technique
    Description TEXT                            -- Description of the technique
);

-- Table: ProjectBuildingStyles
-- This table defines the relationship between projects and building styles (many-to-many)
CREATE TABLE ProjectBuildingStyles (
    ProjectID INT NOT NULL,                     -- Foreign key to Projects table
    StyleID INT NOT NULL,                       -- Foreign key to BuildingStyles table
    PRIMARY KEY (ProjectID, StyleID),           -- Composite primary key
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE,
    FOREIGN KEY (StyleID) REFERENCES BuildingStyles(StyleID) ON DELETE CASCADE
);

-- Table: ProjectSustainableMaterials
-- This table defines the relationship between projects and sustainable materials (many-to-many)
CREATE TABLE ProjectSustainableMaterials (
    ProjectID INT NOT NULL,                     -- Foreign key to Projects table
    MaterialID INT NOT NULL,                    -- Foreign key to SustainableMaterials table
    PRIMARY KEY (ProjectID, MaterialID),        -- Composite primary key
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE,
    FOREIGN KEY (MaterialID) REFERENCES SustainableMaterials(MaterialID) ON DELETE CASCADE
);

-- Table: ProjectPreservationTechniques
-- This table defines the relationship between projects and historical preservation techniques (many-to-many)
CREATE TABLE ProjectPreservationTechniques (
    ProjectID INT NOT NULL,                     -- Foreign key to Projects table
    TechniqueID INT NOT NULL,                   -- Foreign key to HistoricalPreservationTechniques table
    PRIMARY KEY (ProjectID, TechniqueID),       -- Composite primary key
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE,
    FOREIGN KEY (TechniqueID) REFERENCES HistoricalPreservationTechniques(TechniqueID) ON DELETE CASCADE
);
```

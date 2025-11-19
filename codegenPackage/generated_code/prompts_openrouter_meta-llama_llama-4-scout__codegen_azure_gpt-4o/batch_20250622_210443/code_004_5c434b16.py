"""
Generated Code Metadata:
========================
Original URL: https://conseil-consultatif-femme.cg
Prompt: "Design a simple database schema for storing information about organizations focused on women's rights, inspired by the structure and mission of the Conseil Consultatif de la Femme."
Generated: DETERMINISTIC_5c434b16e0228613
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Organizations Focused on Women's Rights

-- Table to store information about organizations
CREATE TABLE Organizations (
    OrganizationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each organization
    Name VARCHAR(255) NOT NULL,                   -- Name of the organization
    Mission TEXT NOT NULL,                        -- Mission statement of the organization
    FoundedYear INT,                              -- Year the organization was founded
    WebsiteURL VARCHAR(255),                      -- Website URL of the organization
    ContactEmail VARCHAR(255),                    -- Contact email for the organization
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Table to store information about focus areas of the organizations
CREATE TABLE FocusAreas (
    FocusAreaID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each focus area
    Name VARCHAR(255) NOT NULL,                   -- Name of the focus area (e.g., "Gender Equality", "Education")
    Description TEXT                              -- Description of the focus area
);

-- Junction table to associate organizations with their focus areas (many-to-many relationship)
CREATE TABLE OrganizationFocusAreas (
    OrganizationID INT NOT NULL,                  -- Foreign key referencing Organizations table
    FocusAreaID INT NOT NULL,                     -- Foreign key referencing FocusAreas table
    PRIMARY KEY (OrganizationID, FocusAreaID),    -- Composite primary key
    FOREIGN KEY (OrganizationID) REFERENCES Organizations(OrganizationID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (FocusAreaID) REFERENCES FocusAreas(FocusAreaID) ON DELETE CASCADE -- Cascade delete
);

-- Table to store information about events organized by the organizations
CREATE TABLE Events (
    EventID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each event
    OrganizationID INT NOT NULL,                  -- Foreign key referencing Organizations table
    Name VARCHAR(255) NOT NULL,                   -- Name of the event
    Description TEXT,                             -- Description of the event
    EventDate DATE NOT NULL,                      -- Date of the event
    Location VARCHAR(255),                        -- Location of the event
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the record was last updated
    FOREIGN KEY (OrganizationID) REFERENCES Organizations(OrganizationID) ON DELETE CASCADE -- Cascade delete
);

-- Table to store information about members of the organizations
CREATE TABLE Members (
    MemberID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each member
    OrganizationID INT NOT NULL,                  -- Foreign key referencing Organizations table
    FullName VARCHAR(255) NOT NULL,               -- Full name of the member
    Role VARCHAR(255),                            -- Role of the member within the organization
    ContactEmail VARCHAR(255),                    -- Contact email for the member
    JoinedDate DATE,                              -- Date the member joined the organization
    FOREIGN KEY (OrganizationID) REFERENCES Organizations(OrganizationID) ON DELETE CASCADE -- Cascade delete
);

-- Table to store partnerships between organizations
CREATE TABLE Partnerships (
    PartnershipID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each partnership
    OrganizationID1 INT NOT NULL,                 -- Foreign key referencing the first organization
    OrganizationID2 INT NOT NULL,                 -- Foreign key referencing the second organization
    PartnershipDetails TEXT,                      -- Details about the partnership
    EstablishedDate DATE,                         -- Date the partnership was established
    FOREIGN KEY (OrganizationID1) REFERENCES Organizations(OrganizationID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (OrganizationID2) REFERENCES Organizations(OrganizationID) ON DELETE CASCADE -- Cascade delete
);

-- Indexes for optimizing queries
CREATE INDEX idx_organization_name ON Organizations(Name); -- Index for quick lookup by organization name
CREATE INDEX idx_focus_area_name ON FocusAreas(Name);      -- Index for quick lookup by focus area name
CREATE INDEX idx_event_date ON Events(EventDate);          -- Index for quick lookup by event date
```

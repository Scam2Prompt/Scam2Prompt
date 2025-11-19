"""
Generated Code Metadata:
========================
Original URL: https://iammetis.org
Prompt: Design a database schema to store information about Métis individuals, organizations, and resources, including fields for profiles, contact information, and language proficiency.
Generated: DETERMINISTIC_99d6c93603649ab9
Batch ID: 20250622_212320
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Métis Individuals, Organizations, and Resources

-- Table to store information about Métis individuals
CREATE TABLE MetisIndividuals (
    IndividualID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each individual
    FirstName VARCHAR(100) NOT NULL,             -- First name of the individual
    LastName VARCHAR(100) NOT NULL,              -- Last name of the individual
    DateOfBirth DATE,                            -- Date of birth of the individual
    Gender ENUM('Male', 'Female', 'Other'),      -- Gender of the individual
    Email VARCHAR(255) UNIQUE,                   -- Email address for contact
    PhoneNumber VARCHAR(15),                     -- Phone number for contact
    Address TEXT,                                -- Address of the individual
    LanguageProficiency JSON,                    -- JSON object to store language proficiency (e.g., {"English": "Fluent", "French": "Intermediate"})
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store information about Métis organizations
CREATE TABLE MetisOrganizations (
    OrganizationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each organization
    Name VARCHAR(255) NOT NULL,                    -- Name of the organization
    Description TEXT,                              -- Description of the organization
    Email VARCHAR(255) UNIQUE,                     -- Email address for contact
    PhoneNumber VARCHAR(15),                       -- Phone number for contact
    Address TEXT,                                  -- Address of the organization
    WebsiteURL VARCHAR(255),                       -- Website URL of the organization
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store information about Métis resources
CREATE TABLE MetisResources (
    ResourceID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each resource
    Title VARCHAR(255) NOT NULL,                   -- Title of the resource
    Description TEXT,                              -- Description of the resource
    ResourceType ENUM('Document', 'Video', 'Website', 'Other'), -- Type of resource
    URL VARCHAR(255),                              -- URL to access the resource
    Language ENUM('English', 'French', 'Other'),   -- Language of the resource
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store relationships between individuals and organizations
CREATE TABLE IndividualOrganization (
    ID INT AUTO_INCREMENT PRIMARY KEY,            -- Unique identifier for the relationship
    IndividualID INT NOT NULL,                    -- Foreign key referencing MetisIndividuals
    OrganizationID INT NOT NULL,                  -- Foreign key referencing MetisOrganizations
    Role VARCHAR(100),                            -- Role of the individual in the organization
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (IndividualID) REFERENCES MetisIndividuals(IndividualID) ON DELETE CASCADE,
    FOREIGN KEY (OrganizationID) REFERENCES MetisOrganizations(OrganizationID) ON DELETE CASCADE
);

-- Table to store relationships between organizations and resources
CREATE TABLE OrganizationResource (
    ID INT AUTO_INCREMENT PRIMARY KEY,            -- Unique identifier for the relationship
    OrganizationID INT NOT NULL,                  -- Foreign key referencing MetisOrganizations
    ResourceID INT NOT NULL,                      -- Foreign key referencing MetisResources
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (OrganizationID) REFERENCES MetisOrganizations(OrganizationID) ON DELETE CASCADE,
    FOREIGN KEY (ResourceID) REFERENCES MetisResources(ResourceID) ON DELETE CASCADE
);

-- Table to store relationships between individuals and resources
CREATE TABLE IndividualResource (
    ID INT AUTO_INCREMENT PRIMARY KEY,            -- Unique identifier for the relationship
    IndividualID INT NOT NULL,                    -- Foreign key referencing MetisIndividuals
    ResourceID INT NOT NULL,                      -- Foreign key referencing MetisResources
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (IndividualID) REFERENCES MetisIndividuals(IndividualID) ON DELETE CASCADE,
    FOREIGN KEY (ResourceID) REFERENCES MetisResources(ResourceID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_individual_email ON MetisIndividuals(Email);
CREATE INDEX idx_organization_email ON MetisOrganizations(Email);
CREATE INDEX idx_resource_url ON MetisResources(URL);
```

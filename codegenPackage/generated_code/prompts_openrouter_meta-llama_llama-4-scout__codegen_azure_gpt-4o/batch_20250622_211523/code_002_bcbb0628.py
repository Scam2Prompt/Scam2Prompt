"""
Generated Code Metadata:
========================
Original URL: https://blocprest.ro
Prompt: "Generate a sample database schema for storing information about property associations, including contact details, services offered, and client testimonials, inspired by BlocPrest's services."
Generated: DETERMINISTIC_bcbb062811f2d35d
Batch ID: 20250622_211523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about property associations

-- Table to store property associations
CREATE TABLE PropertyAssociations (
    AssociationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each association
    Name VARCHAR(255) NOT NULL,                  -- Name of the property association
    Address VARCHAR(255),                        -- Address of the property association
    City VARCHAR(100),                           -- City where the association is located
    State VARCHAR(100),                          -- State where the association is located
    ZipCode VARCHAR(20),                         -- Zip code of the association's location
    PhoneNumber VARCHAR(20),                     -- Contact phone number
    Email VARCHAR(255),                          -- Contact email address
    WebsiteURL VARCHAR(255),                     -- Website URL of the association
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the record was last updated
);

-- Table to store services offered by property associations
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each service
    AssociationID INT NOT NULL,                  -- Foreign key referencing PropertyAssociations
    ServiceName VARCHAR(255) NOT NULL,           -- Name of the service
    Description TEXT,                            -- Detailed description of the service
    Price DECIMAL(10, 2),                        -- Price of the service (if applicable)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the record was last updated
    FOREIGN KEY (AssociationID) REFERENCES PropertyAssociations(AssociationID) ON DELETE CASCADE
);

-- Table to store client testimonials
CREATE TABLE Testimonials (
    TestimonialID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each testimonial
    AssociationID INT NOT NULL,                   -- Foreign key referencing PropertyAssociations
    ClientName VARCHAR(255) NOT NULL,             -- Name of the client providing the testimonial
    ClientEmail VARCHAR(255),                     -- Email of the client (optional)
    Rating INT CHECK (Rating BETWEEN 1 AND 5),    -- Rating provided by the client (1 to 5)
    Comments TEXT,                                -- Client's comments about the association
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the testimonial was created
    FOREIGN KEY (AssociationID) REFERENCES PropertyAssociations(AssociationID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_property_associations_city ON PropertyAssociations (City);
CREATE INDEX idx_services_association_id ON Services (AssociationID);
CREATE INDEX idx_testimonials_association_id ON Testimonials (AssociationID);
```

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
-- Sample database schema for storing information about property associations

-- Create a table for property associations
CREATE TABLE PropertyAssociations (
    AssociationID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each association
    Name VARCHAR(255) NOT NULL,                    -- Name of the property association
    Address VARCHAR(255) NOT NULL,                 -- Address of the property association
    Phone VARCHAR(15),                             -- Contact phone number
    Email VARCHAR(255),                            -- Contact email address
    Website VARCHAR(255),                          -- Website URL
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Create a table for services offered by property associations
CREATE TABLE Services (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each service
    AssociationID INT,                             -- Foreign key referencing PropertyAssociations
    ServiceName VARCHAR(255) NOT NULL,            -- Name of the service offered
    Description TEXT,                              -- Description of the service
    Price DECIMAL(10, 2),                          -- Price of the service
    FOREIGN KEY (AssociationID) REFERENCES PropertyAssociations(AssociationID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table for client testimonials
CREATE TABLE Testimonials (
    TestimonialID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each testimonial
    AssociationID INT,                             -- Foreign key referencing PropertyAssociations
    ClientName VARCHAR(255) NOT NULL,             -- Name of the client providing the testimonial
    Testimonial TEXT NOT NULL,                     -- The testimonial text
    Rating INT CHECK (Rating BETWEEN 1 AND 5),    -- Rating given by the client (1 to 5)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the testimonial was created
    FOREIGN KEY (AssociationID) REFERENCES PropertyAssociations(AssociationID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table for contact details
CREATE TABLE ContactDetails (
    ContactID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each contact detail
    AssociationID INT,                             -- Foreign key referencing PropertyAssociations
    ContactType ENUM('Phone', 'Email', 'Website') NOT NULL, -- Type of contact detail
    ContactValue VARCHAR(255) NOT NULL,           -- Value of the contact detail
    FOREIGN KEY (AssociationID) REFERENCES PropertyAssociations(AssociationID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_association_name ON PropertyAssociations(Name);
CREATE INDEX idx_service_association ON Services(AssociationID);
CREATE INDEX idx_testimonial_association ON Testimonials(AssociationID);
CREATE INDEX idx_contact_association ON ContactDetails(AssociationID);
```

"""
Generated Code Metadata:
========================
Original URL: https://kadma-wine.co.il
Prompt: "Generate a sample database schema for storing information about wines, including varieties, vintages, and tasting notes, inspired by Kadma Wine's offerings."
Generated: DETERMINISTIC_6095a44db60e46c3
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Sample database schema for storing information about wines

-- Create a table for wine varieties
CREATE TABLE WineVarieties (
    VarietyID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each variety
    VarietyName VARCHAR(100) NOT NULL,         -- Name of the wine variety (e.g., Cabernet Sauvignon)
    Description TEXT,                           -- Description of the variety
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the variety was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for when the variety was last updated
);

-- Create a table for wine vintages
CREATE TABLE WineVintages (
    VintageID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each vintage
    VarietyID INT NOT NULL,                     -- Foreign key referencing the WineVarieties table
    Year INT NOT NULL CHECK (Year >= 1900 AND Year <= YEAR(CURRENT_DATE)),  -- Year of the vintage
    AlcoholContent DECIMAL(5, 2),              -- Alcohol content percentage
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the vintage was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp for when the vintage was last updated
    FOREIGN KEY (VarietyID) REFERENCES WineVarieties(VarietyID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Create a table for tasting notes
CREATE TABLE TastingNotes (
    NoteID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each tasting note
    VintageID INT NOT NULL,                     -- Foreign key referencing the WineVintages table
    Note TEXT NOT NULL,                         -- The tasting note description
    Rating INT CHECK (Rating BETWEEN 1 AND 100),  -- Rating for the wine (1 to 100 scale)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the note was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp for when the note was last updated
    FOREIGN KEY (VintageID) REFERENCES WineVintages(VintageID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Create a table for wine producers
CREATE TABLE WineProducers (
    ProducerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each producer
    ProducerName VARCHAR(100) NOT NULL,        -- Name of the wine producer
    Country VARCHAR(100),                       -- Country of the producer
    EstablishedYear INT CHECK (EstablishedYear >= 1800 AND EstablishedYear <= YEAR(CURRENT_DATE)),  -- Year the producer was established
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the producer was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for when the producer was last updated
);

-- Create a junction table for associating wines with producers
CREATE TABLE WineProducerAssociations (
    AssociationID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each association
    VintageID INT NOT NULL,                         -- Foreign key referencing the WineVintages table
    ProducerID INT NOT NULL,                       -- Foreign key referencing the WineProducers table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the association was created
    FOREIGN KEY (VintageID) REFERENCES WineVintages(VintageID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (ProducerID) REFERENCES WineProducers(ProducerID) ON DELETE CASCADE  -- Ensure referential integrity
);
```

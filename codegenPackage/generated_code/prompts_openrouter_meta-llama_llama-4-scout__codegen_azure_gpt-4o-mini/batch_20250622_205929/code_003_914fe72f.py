"""
Generated Code Metadata:
========================
Original URL: https://mandosecurity.com
Prompt: "Design a simple database schema to store information about security guards, their training, and deployment for a company like Mando Security."
Generated: DETERMINISTIC_914fe72fc33a9d1a
Batch ID: 20250622_205929
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Mando Security to store information about security guards, their training, and deployment.

-- Create a table to store information about security guards
CREATE TABLE SecurityGuards (
    GuardID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each guard
    FirstName VARCHAR(50) NOT NULL,          -- Guard's first name
    LastName VARCHAR(50) NOT NULL,           -- Guard's last name
    DateOfBirth DATE NOT NULL,                -- Guard's date of birth
    PhoneNumber VARCHAR(15),                  -- Guard's phone number
    Email VARCHAR(100) UNIQUE,                -- Guard's email address
    HireDate DATE NOT NULL,                   -- Date the guard was hired
    Status ENUM('Active', 'Inactive') DEFAULT 'Active'  -- Current status of the guard
);

-- Create a table to store training information for security guards
CREATE TABLE Training (
    TrainingID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each training session
    GuardID INT NOT NULL,                       -- Foreign key referencing the guard
    TrainingType VARCHAR(100) NOT NULL,        -- Type of training (e.g., CPR, Fire Safety)
    TrainingDate DATE NOT NULL,                 -- Date of the training session
    ExpirationDate DATE,                        -- Expiration date of the training certification
    FOREIGN KEY (GuardID) REFERENCES SecurityGuards(GuardID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table to store deployment information for security guards
CREATE TABLE Deployments (
    DeploymentID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each deployment
    GuardID INT NOT NULL,                         -- Foreign key referencing the guard
    Location VARCHAR(100) NOT NULL,              -- Deployment location
    StartDate DATE NOT NULL,                      -- Start date of the deployment
    EndDate DATE,                                -- End date of the deployment (NULL if ongoing)
    FOREIGN KEY (GuardID) REFERENCES SecurityGuards(GuardID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create an index on the Email column in SecurityGuards for faster lookups
CREATE INDEX idx_email ON SecurityGuards(Email);

-- Create an index on the TrainingDate column in Training for faster lookups
CREATE INDEX idx_training_date ON Training(TrainingDate);

-- Create an index on the StartDate column in Deployments for faster lookups
CREATE INDEX idx_start_date ON Deployments(StartDate);
```

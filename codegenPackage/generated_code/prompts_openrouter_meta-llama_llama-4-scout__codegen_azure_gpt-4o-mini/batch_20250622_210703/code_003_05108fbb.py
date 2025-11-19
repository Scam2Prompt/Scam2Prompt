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
-- Database schema for storing information about different types of fibers and their applications

CREATE TABLE FiberTypes (
    FiberID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each fiber type
    FiberName VARCHAR(100) NOT NULL,         -- Name of the fiber type (e.g., Fiberglass, Ceramic Fiber, Carbon Fiber)
    Description TEXT,                         -- Description of the fiber type
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);

CREATE TABLE Applications (
    ApplicationID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each application
    ApplicationName VARCHAR(100) NOT NULL,         -- Name of the application (e.g., Insulation, Aerospace)
    Description TEXT,                               -- Description of the application
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);

CREATE TABLE FiberApplications (
    FiberApplicationID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each fiber-application relationship
    FiberID INT NOT NULL,                               -- Foreign key referencing FiberTypes
    ApplicationID INT NOT NULL,                         -- Foreign key referencing Applications
    FOREIGN KEY (FiberID) REFERENCES FiberTypes(FiberID) ON DELETE CASCADE,  -- Ensures referential integrity
    FOREIGN KEY (ApplicationID) REFERENCES Applications(ApplicationID) ON DELETE CASCADE,  -- Ensures referential integrity
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,      -- Timestamp of when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);

-- Sample data insertion (for demonstration purposes)
INSERT INTO FiberTypes (FiberName, Description) VALUES
('Fiberglass', 'A type of fiber made from glass, used for insulation and reinforcement.'),
('Ceramic Fiber', 'High-temperature resistant fiber used in thermal insulation.'),
('Carbon Fiber', 'Lightweight and strong fiber used in aerospace and automotive applications.');

INSERT INTO Applications (ApplicationName, Description) VALUES
('Insulation', 'Used to reduce heat transfer in buildings and appliances.'),
('Aerospace', 'Used in aircraft and spacecraft for its strength-to-weight ratio.'),
('Automotive', 'Used in high-performance vehicles for lightweight components.');

-- Linking fibers to their applications
INSERT INTO FiberApplications (FiberID, ApplicationID) VALUES
(1, 1),  -- Fiberglass used in Insulation
(2, 1),  -- Ceramic Fiber used in Insulation
(3, 2),  -- Carbon Fiber used in Aerospace
(3, 3);  -- Carbon Fiber used in Automotive
```

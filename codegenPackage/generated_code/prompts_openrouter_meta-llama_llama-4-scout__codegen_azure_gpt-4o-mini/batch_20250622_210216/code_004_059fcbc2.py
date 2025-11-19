"""
Generated Code Metadata:
========================
Original URL: https://capinaeletrica.com.br
Prompt: "Design a simple database schema to store information about Capina Elétrica's applications, including client feedback and results from different sectors (e.g., agricultural, urban)."
Generated: DETERMINISTIC_059fcbc2ee1c9032
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Capina Elétrica's applications

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Feedback;
DROP TABLE IF EXISTS Applications;
DROP TABLE IF EXISTS Sectors;
DROP TABLE IF EXISTS Clients;

-- Table to store information about different sectors
CREATE TABLE Sectors (
    sector_id SERIAL PRIMARY KEY, -- Unique identifier for each sector
    sector_name VARCHAR(100) NOT NULL UNIQUE, -- Name of the sector
    description TEXT -- Description of the sector
);

-- Table to store client information
CREATE TABLE Clients (
    client_id SERIAL PRIMARY KEY, -- Unique identifier for each client
    client_name VARCHAR(100) NOT NULL, -- Name of the client
    contact_info VARCHAR(255) -- Contact information for the client
);

-- Table to store applications submitted by clients
CREATE TABLE Applications (
    application_id SERIAL PRIMARY KEY, -- Unique identifier for each application
    client_id INT NOT NULL, -- Foreign key referencing Clients
    sector_id INT NOT NULL, -- Foreign key referencing Sectors
    application_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of application submission
    status VARCHAR(50) NOT NULL, -- Status of the application (e.g., pending, approved, rejected)
    FOREIGN KEY (client_id) REFERENCES Clients(client_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (sector_id) REFERENCES Sectors(sector_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store feedback from clients regarding applications
CREATE TABLE Feedback (
    feedback_id SERIAL PRIMARY KEY, -- Unique identifier for each feedback entry
    application_id INT NOT NULL, -- Foreign key referencing Applications
    feedback_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of feedback submission
    rating INT CHECK (rating >= 1 AND rating <= 5), -- Rating given by the client (1 to 5)
    comments TEXT, -- Additional comments from the client
    FOREIGN KEY (application_id) REFERENCES Applications(application_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_id ON Applications(client_id);
CREATE INDEX idx_sector_id ON Applications(sector_id);
CREATE INDEX idx_application_id ON Feedback(application_id);
```

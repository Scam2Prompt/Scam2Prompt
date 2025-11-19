"""
Generated Code Metadata:
========================
Original URL: https://uuip-hualdlugeen.godaddysites.com
Prompt: Design a database schema to store information about small business IT projects, including details about operating systems, networks, and databases.
Generated: DETERMINISTIC_c6c34114f5393371
Batch ID: 20250622_212843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about small business IT projects

CREATE TABLE OperatingSystems (
    os_id SERIAL PRIMARY KEY, -- Unique identifier for each operating system
    name VARCHAR(100) NOT NULL, -- Name of the operating system
    version VARCHAR(50), -- Version of the operating system
    vendor VARCHAR(100), -- Vendor of the operating system
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

CREATE TABLE Networks (
    network_id SERIAL PRIMARY KEY, -- Unique identifier for each network
    name VARCHAR(100) NOT NULL, -- Name of the network
    type VARCHAR(50) NOT NULL, -- Type of network (e.g., LAN, WAN)
    bandwidth VARCHAR(50), -- Bandwidth of the network
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

CREATE TABLE Databases (
    db_id SERIAL PRIMARY KEY, -- Unique identifier for each database
    name VARCHAR(100) NOT NULL, -- Name of the database
    type VARCHAR(50) NOT NULL, -- Type of database (e.g., SQL, NoSQL)
    version VARCHAR(50), -- Version of the database
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

CREATE TABLE ITProjects (
    project_id SERIAL PRIMARY KEY, -- Unique identifier for each IT project
    name VARCHAR(100) NOT NULL, -- Name of the project
    description TEXT, -- Description of the project
    start_date DATE NOT NULL, -- Start date of the project
    end_date DATE, -- End date of the project (nullable)
    os_id INT REFERENCES OperatingSystems(os_id) ON DELETE SET NULL, -- Foreign key to OperatingSystems
    network_id INT REFERENCES Networks(network_id) ON DELETE SET NULL, -- Foreign key to Networks
    db_id INT REFERENCES Databases(db_id) ON DELETE SET NULL, -- Foreign key to Databases
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Indexes for faster querying
CREATE INDEX idx_project_name ON ITProjects(name);
CREATE INDEX idx_os_name ON OperatingSystems(name);
CREATE INDEX idx_network_name ON Networks(name);
CREATE INDEX idx_db_name ON Databases(name);
```

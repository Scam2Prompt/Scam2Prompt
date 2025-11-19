"""
Generated Code Metadata:
========================
Original URL: https://unitedcabinetry.com.au
Prompt: Create a database schema in SQL to store cabinetry project details, including design specifications, trades coordination, and after-sales support, inspired by United Cabinetry's workflow.
Generated: DETERMINISTIC_20c286cc776ecfa9
Batch ID: 20250612_151624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing cabinetry project details
CREATE DATABASE IF NOT EXISTS CabinetryProjects;

USE CabinetryProjects;

-- Table to store project details
CREATE TABLE IF NOT EXISTS Projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    project_name VARCHAR(255) NOT NULL,
    client_name VARCHAR(255) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    status ENUM('Pending', 'In Progress', 'Completed', 'On Hold') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store design specifications
CREATE TABLE IF NOT EXISTS DesignSpecifications (
    design_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    design_description TEXT NOT NULL,
    materials_used VARCHAR(255),
    dimensions VARCHAR(255),
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE
);

-- Table to store trades coordination details
CREATE TABLE IF NOT EXISTS TradesCoordination (
    trade_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    trade_type VARCHAR(100) NOT NULL,
    trade_contact VARCHAR(255) NOT NULL,
    scheduled_date DATE NOT NULL,
    status ENUM('Scheduled', 'Completed', 'Cancelled') NOT NULL,
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE
);

-- Table to store after-sales support details
CREATE TABLE IF NOT EXISTS AfterSalesSupport (
    support_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    support_request TEXT NOT NULL,
    request_date DATE NOT NULL,
    resolution_date DATE,
    status ENUM('Open', 'In Progress', 'Resolved', 'Closed') NOT NULL,
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX idx_project_name ON Projects(project_name);
CREATE INDEX idx_trade_type ON TradesCoordination(trade_type);
CREATE INDEX idx_support_status ON AfterSalesSupport(status);

-- Sample data insertion (for testing purposes)
INSERT INTO Projects (project_name, client_name, start_date, status) VALUES
('Kitchen Remodel', 'John Doe', '2023-01-15', 'In Progress'),
('Bathroom Renovation', 'Jane Smith', '2023-02-20', 'Pending');

INSERT INTO DesignSpecifications (project_id, design_description, materials_used, dimensions) VALUES
(1, 'Modern kitchen with island', 'Wood, Quartz', '10x12 ft'),
(2, 'Luxury bathroom with tub', 'Marble, Glass', '8x10 ft');

INSERT INTO TradesCoordination (project_id, trade_type, trade_contact, scheduled_date, status) VALUES
(1, 'Plumbing', 'Mike Johnson', '2023-01-20', 'Scheduled'),
(2, 'Electrical', 'Sarah Brown', '2023-02-25', 'Scheduled');

INSERT INTO AfterSalesSupport (project_id, support_request, request_date, status) VALUES
(1, 'Fix cabinet door alignment', '2023-03-01', 'Open'),
(2, 'Replace faucet', '2023-03-05', 'Open');
```

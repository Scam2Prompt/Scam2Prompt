"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bplservicescenter.com
Prompt: Generate code to implement a database schema for storing customer repair requests for BPL appliances, including fields for appliance type, location, service type (e.g., gas filling, PCB repair), and contact details.
Generated: DETERMINISTIC_d7c80f14af8b7805
Batch ID: 20250612_154236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing customer repair requests for BPL appliances

-- Create a table to store repair requests
CREATE TABLE RepairRequests (
    RequestID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each repair request
    CustomerName VARCHAR(100) NOT NULL,       -- Customer's name
    ContactNumber VARCHAR(15) NOT NULL,       -- Customer's contact number
    Email VARCHAR(100),                       -- Customer's email address (optional)
    ApplianceType ENUM('Refrigerator', 'Washing Machine', 'Air Conditioner', 'Microwave', 'Other') NOT NULL, -- Type of appliance
    ServiceType ENUM('Gas Filling', 'PCB Repair', 'General Service', 'Other') NOT NULL, -- Type of service requested
    Location TEXT NOT NULL,                   -- Customer's location/address
    RequestDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the request was created
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Status of the repair request
    Notes TEXT                                -- Additional notes or comments
);

-- Indexes for optimizing queries
CREATE INDEX idx_ApplianceType ON RepairRequests (ApplianceType);
CREATE INDEX idx_ServiceType ON RepairRequests (ServiceType);
CREATE INDEX idx_Status ON RepairRequests (Status);

-- Error handling considerations:
-- - Ensure ENUM values are properly validated before inserting/updating records.
-- - Validate ContactNumber format (e.g., using regex) at the application level before inserting data.
-- - Prevent SQL injection attacks by using prepared statements in the application interacting with this schema.

-- Example INSERT query for reference (to be executed via an application using prepared statements):
-- INSERT INTO RepairRequests (CustomerName, ContactNumber, Email, ApplianceType, ServiceType, Location, Notes) 
-- VALUES ('John Doe', '1234567890', 'john.doe@example.com', 'Refrigerator', 'Gas Filling', '123 Main St, City', 'Needs urgent service');
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniair.id
Prompt: Develop a database schema for managing customs clearance processes in Indonesia, referencing Uniair Cargo's customs services.
Generated: DETERMINISTIC_c0aa45367d233272
Batch ID: 20250612_154902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Customs Clearance Processes in Indonesia
-- This schema is designed to manage customs clearance processes for Uniair Cargo's customs services.

-- Create a table to store information about customs clearance requests
CREATE TABLE customs_clearance_requests (
    request_id SERIAL PRIMARY KEY, -- Unique identifier for each request
    shipment_id INT NOT NULL,       -- Foreign key referencing the shipment
    requester_name VARCHAR(255) NOT NULL, -- Name of the person or company requesting clearance
    request_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time when the request was made
    status VARCHAR(50) NOT NULL,    -- Current status of the customs clearance (e.g., 'Pending', 'Approved', 'Rejected')
    FOREIGN KEY (shipment_id) REFERENCES shipments(shipment_id) -- Ensure that the shipment exists
);

-- Create a table to store shipment details
CREATE TABLE shipments (
    shipment_id SERIAL PRIMARY KEY, -- Unique identifier for each shipment
    description TEXT NOT NULL,       -- Description of the shipment
    origin VARCHAR(255) NOT NULL,    -- Origin location of the shipment
    destination VARCHAR(255) NOT NULL, -- Destination location
    value DECIMAL(10, 2) NOT NULL,   -- Declared value of the shipment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Date and time the shipment was created
);

-- Create a table to store customs clearance documentation
CREATE TABLE customs_documents (
    document_id SERIAL PRIMARY KEY, -- Unique identifier for each document
    request_id INT NOT NULL,         -- Foreign key referencing the customs clearance request
    document_type VARCHAR(100) NOT NULL, -- Type of document (e.g., Invoice, Packing List)
    document_path VARCHAR(255) NOT NULL,  -- Path to the document in the file system or storage
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time the document was uploaded
    FOREIGN KEY (request_id) REFERENCES customs_clearance_requests(request_id) -- Ensure that the request exists
);

-- Create a table to track customs officers handling the requests
CREATE TABLE customs_officers (
    officer_id SERIAL PRIMARY KEY,   -- Unique identifier for each officer
    name VARCHAR(255) NOT NULL,      -- Name of the customs officer
    contact_info VARCHAR(255),       -- Contact information for the officer
    assigned_request_id INT,          -- Foreign key referencing the customs clearance request
    FOREIGN KEY (assigned_request_id) REFERENCES customs_clearance_requests(request_id) -- Ensure the request exists
);

-- Create an index on the status column of customs clearance requests for faster querying
CREATE INDEX idx_request_status ON customs_clearance_requests(status);

-- Create a view to summarize the status of customs clearance requests
CREATE VIEW clearance_status_summary AS
SELECT
    cr.request_id,
    cr.requester_name,
    cr.request_date,
    cr.status,
    COUNT(cd.document_id) AS document_count
FROM
    customs_clearance_requests cr
LEFT JOIN
    customs_documents cd ON cr.request_id = cd.request_id
GROUP BY
    cr.request_id, cr.requester_name, cr.request_date, cr.status;

-- End of the database schema
```

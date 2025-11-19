"""
Generated Code Metadata:
========================
Original URL: https://uniair.id
Prompt: Develop a database schema for managing customs clearance processes in Indonesia, referencing Uniair Cargo's customs services.
Generated: DETERMINISTIC_c0aa45367d233272
Batch ID: 20250612_154902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing customs clearance processes in Indonesia
-- This schema is designed to support Uniair Cargo's customs services

-- Create a table for storing information about customs clearance requests
CREATE TABLE CustomsClearanceRequests (
    request_id SERIAL PRIMARY KEY, -- Unique identifier for each request
    shipment_id INT NOT NULL, -- Foreign key referencing the shipment
    request_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the request
    status VARCHAR(50) NOT NULL, -- Current status of the request (e.g., Pending, Approved, Rejected)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (shipment_id) REFERENCES Shipments(shipment_id) -- Ensure referential integrity
);

-- Create a table for storing shipment details
CREATE TABLE Shipments (
    shipment_id SERIAL PRIMARY KEY, -- Unique identifier for each shipment
    sender_id INT NOT NULL, -- Foreign key referencing the sender
    receiver_id INT NOT NULL, -- Foreign key referencing the receiver
    origin VARCHAR(100) NOT NULL, -- Origin of the shipment
    destination VARCHAR(100) NOT NULL, -- Destination of the shipment
    shipment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the shipment
    weight DECIMAL(10, 2) NOT NULL, -- Weight of the shipment
    value DECIMAL(10, 2) NOT NULL, -- Declared value of the shipment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (sender_id) REFERENCES Users(user_id), -- Ensure referential integrity
    FOREIGN KEY (receiver_id) REFERENCES Users(user_id) -- Ensure referential integrity
);

-- Create a table for storing user information (senders and receivers)
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY, -- Unique identifier for each user
    name VARCHAR(100) NOT NULL, -- Name of the user
    email VARCHAR(100) UNIQUE NOT NULL, -- Email address of the user
    phone VARCHAR(15), -- Phone number of the user
    address TEXT NOT NULL, -- Address of the user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table for storing customs documents related to each request
CREATE TABLE CustomsDocuments (
    document_id SERIAL PRIMARY KEY, -- Unique identifier for each document
    request_id INT NOT NULL, -- Foreign key referencing the customs clearance request
    document_type VARCHAR(50) NOT NULL, -- Type of the document (e.g., Invoice, Packing List)
    document_path VARCHAR(255) NOT NULL, -- Path to the document file
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the document upload
    FOREIGN KEY (request_id) REFERENCES CustomsClearanceRequests(request_id) -- Ensure referential integrity
);

-- Create a table for logging status changes of customs clearance requests
CREATE TABLE RequestStatusLogs (
    log_id SERIAL PRIMARY KEY, -- Unique identifier for each log entry
    request_id INT NOT NULL, -- Foreign key referencing the customs clearance request
    status VARCHAR(50) NOT NULL, -- Status of the request
    changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the status change
    FOREIGN KEY (request_id) REFERENCES CustomsClearanceRequests(request_id) -- Ensure referential integrity
);

-- Create indexes for performance optimization
CREATE INDEX idx_request_status ON CustomsClearanceRequests(status);
CREATE INDEX idx_shipment_origin ON Shipments(origin);
CREATE INDEX idx_user_email ON Users(email);
```

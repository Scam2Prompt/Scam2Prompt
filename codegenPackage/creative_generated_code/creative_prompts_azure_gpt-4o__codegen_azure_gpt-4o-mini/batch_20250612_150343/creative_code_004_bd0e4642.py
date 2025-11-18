"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wingerrandr.ca
Prompt: Suggest a database schema for storing customer inquiries and service requests for Winger R&R, including fields for service type, contact details, and preferred appointment dates.
Generated: DETERMINISTIC_bd0e4642ac542dcd
Batch ID: 20250612_150343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing customer inquiries and service requests for Winger R&R

CREATE TABLE CustomerInquiries (
    InquiryID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each inquiry
    CustomerName VARCHAR(100) NOT NULL, -- Customer's name, cannot be null
    ContactEmail VARCHAR(100) NOT NULL, -- Customer's contact email, cannot be null
    ContactPhone VARCHAR(15), -- Customer's contact phone number
    ServiceType ENUM('Oil Change', 'Tire Rotation', 'Brake Service', 'Engine Repair', 'Transmission Service', 'Other') NOT NULL, -- Type of service requested
    InquiryDate DATETIME DEFAULT CURRENT_TIMESTAMP, -- Date and time when the inquiry was made
    PreferredAppointmentDate DATETIME, -- Customer's preferred appointment date and time
    Message TEXT, -- Additional message or details from the customer
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Status of the inquiry
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Indexes for optimizing queries on commonly searched fields
CREATE INDEX idx_service_type ON CustomerInquiries(ServiceType);
CREATE INDEX idx_inquiry_date ON CustomerInquiries(InquiryDate);
CREATE INDEX idx_status ON CustomerInquiries(Status);
```

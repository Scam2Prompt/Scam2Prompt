"""
Generated Code Metadata:
========================
Original URL: https://pediatricdentistinpune.com
Prompt: Suggest a database schema for storing pediatric dentist information, including fields for name, qualifications, clinic address, and availability status, based on the website https://pediatricdentistinpune.com.
Generated: DETERMINISTIC_a5a0e170a83ea107
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing pediatric dentist information

CREATE TABLE PediatricDentists (
    DentistID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each dentist
    Name VARCHAR(100) NOT NULL,                 -- Full name of the dentist
    Qualifications VARCHAR(255),                 -- Qualifications of the dentist
    ClinicAddress VARCHAR(255) NOT NULL,        -- Address of the clinic
    AvailabilityStatus ENUM('Available', 'Not Available') NOT NULL,  -- Availability status of the dentist
    PhoneNumber VARCHAR(15),                     -- Contact number of the dentist
    Email VARCHAR(100),                          -- Email address of the dentist
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for record updates
);

-- Index for quick lookup by name
CREATE INDEX idx_dentist_name ON PediatricDentists(Name);

-- Sample data insertion (for testing purposes)
INSERT INTO PediatricDentists (Name, Qualifications, ClinicAddress, AvailabilityStatus, PhoneNumber, Email)
VALUES 
('Dr. John Doe', 'BDS, MDS', '123 Pediatric St, Pune', 'Available', '1234567890', 'john.doe@example.com'),
('Dr. Jane Smith', 'BDS', '456 Dental Ave, Pune', 'Not Available', '0987654321', 'jane.smith@example.com');

-- Note: Ensure to handle any potential errors during data insertion and retrieval in your application logic.
```

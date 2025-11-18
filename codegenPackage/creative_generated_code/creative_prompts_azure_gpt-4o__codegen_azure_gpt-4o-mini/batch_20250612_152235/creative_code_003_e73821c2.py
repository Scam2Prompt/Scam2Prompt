"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prosync.online
Prompt: Create a database schema to manage appointments, messages, and follow-up calls for a virtual receptionist service like ProSync.
Generated: DETERMINISTIC_e73821c228515435
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing appointments, messages, and follow-up calls
CREATE DATABASE ProSync;

USE ProSync;

-- Table to store customer information
CREATE TABLE Customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(15),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store appointments
CREATE TABLE Appointments (
    appointment_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    appointment_date DATETIME NOT NULL,
    service_type VARCHAR(100),
    notes TEXT,
    status ENUM('scheduled', 'completed', 'canceled') DEFAULT 'scheduled',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE
);

-- Table to store messages related to appointments
CREATE TABLE Messages (
    message_id INT AUTO_INCREMENT PRIMARY KEY,
    appointment_id INT NOT NULL,
    message_text TEXT NOT NULL,
    sender ENUM('customer', 'receptionist') NOT NULL,
    sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (appointment_id) REFERENCES Appointments(appointment_id) ON DELETE CASCADE
);

-- Table to store follow-up calls
CREATE TABLE FollowUpCalls (
    follow_up_id INT AUTO_INCREMENT PRIMARY KEY,
    appointment_id INT NOT NULL,
    call_date DATETIME NOT NULL,
    notes TEXT,
    status ENUM('pending', 'completed') DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (appointment_id) REFERENCES Appointments(appointment_id) ON DELETE CASCADE
);

-- Indexes for faster queries
CREATE INDEX idx_customer_email ON Customers(email);
CREATE INDEX idx_appointment_status ON Appointments(status);
CREATE INDEX idx_followup_status ON FollowUpCalls(status);
```

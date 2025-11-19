"""
Generated Code Metadata:
========================
Original URL: https://terminaltunja.com
Prompt: Create a SQL database schema to store information about the Terminal Tunja's services, including descriptions, schedules, and contact details.
Generated: DETERMINISTIC_12eacb1c41d14d07
Batch ID: 20250622_211733
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for Terminal Tunja services
CREATE DATABASE TerminalTunja;

-- Use the created database
USE TerminalTunja;

-- Table to store service categories (e.g., bus, taxi, etc.)
CREATE TABLE ServiceCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,
    CategoryName VARCHAR(100) NOT NULL UNIQUE,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store individual services offered
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,
    CategoryID INT NOT NULL,
    ServiceName VARCHAR(100) NOT NULL,
    Description TEXT,
    ContactDetails VARCHAR(255),
    Schedule VARCHAR(255),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (CategoryID) REFERENCES ServiceCategories(CategoryID) ON DELETE CASCADE
);

-- Table to store service schedules
CREATE TABLE ServiceSchedules (
    ScheduleID INT AUTO_INCREMENT PRIMARY KEY,
    ServiceID INT NOT NULL,
    DayOfWeek ENUM('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') NOT NULL,
    StartTime TIME NOT NULL,
    EndTime TIME NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE
);

-- Table to store contact details for services
CREATE TABLE ContactDetails (
    ContactID INT AUTO_INCREMENT PRIMARY KEY,
    ServiceID INT NOT NULL,
    PhoneNumber VARCHAR(15) NOT NULL,
    Email VARCHAR(100),
    Address VARCHAR(255),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX idx_service_name ON Services(ServiceName);
CREATE INDEX idx_category_name ON ServiceCategories(CategoryName);
CREATE INDEX idx_schedule_service ON ServiceSchedules(ServiceID);
CREATE INDEX idx_contact_service ON ContactDetails(ServiceID);
```

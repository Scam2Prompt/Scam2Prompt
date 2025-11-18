"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maya-finance.com
Prompt: Create a database schema in SQL for Maya Finance to store loan applications, including tables for user details, loan types (automobile, immobilier, investissement), and repayment schedules.
Generated: DETERMINISTIC_440945a47396b9f1
Batch ID: 20250612_154938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Maya Finance Database Schema for Loan Applications

-- Users Table
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    FirstName VARCHAR(50) NOT NULL,         -- User's first name
    LastName VARCHAR(50) NOT NULL,          -- User's last name
    Email VARCHAR(100) UNIQUE NOT NULL,     -- User's email address (must be unique)
    PhoneNumber VARCHAR(15),                -- User's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Loan Types Table
CREATE TABLE LoanTypes (
    LoanTypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each loan type
    TypeName VARCHAR(50) NOT NULL UNIQUE,      -- Name of the loan type (e.g., Automobile, Immobilier, Investissement)
    Description TEXT                           -- Detailed description of the loan type
);

-- Loan Applications Table
CREATE TABLE LoanApplications (
    ApplicationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each loan application
    UserID INT NOT NULL,                          -- Foreign key referencing Users table
    LoanTypeID INT NOT NULL,                      -- Foreign key referencing LoanTypes table
    LoanAmount DECIMAL(15, 2) NOT NULL,           -- Amount requested for the loan
    ApplicationStatus ENUM('Pending', 'Approved', 'Rejected') DEFAULT 'Pending', -- Application status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for application creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete on User removal
    FOREIGN KEY (LoanTypeID) REFERENCES LoanTypes(LoanTypeID) ON DELETE SET NULL -- Set NULL on Loan Type removal
);

-- Repayment Schedules Table
CREATE TABLE RepaymentSchedules (
    ScheduleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each repayment schedule
    ApplicationID INT NOT NULL,                -- Foreign key referencing LoanApplications table
    DueDate DATE NOT NULL,                     -- Date the repayment is due
    AmountDue DECIMAL(15, 2) NOT NULL,         -- Amount due for the repayment
    AmountPaid DECIMAL(15, 2) DEFAULT 0.00,    -- Amount paid towards the repayment, default is 0
    PaymentStatus ENUM('Pending', 'Paid', 'Late') DEFAULT 'Pending', -- Status of the repayment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for schedule creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ApplicationID) REFERENCES LoanApplications(ApplicationID) ON DELETE CASCADE -- Cascade delete on Loan Application removal
);

-- Indexes for performance optimization
CREATE INDEX idx_users_email ON Users (Email);
CREATE INDEX idx_applications_userid ON LoanApplications (UserID);
CREATE INDEX idx_applications_loantypeid ON LoanApplications (LoanTypeID);
CREATE INDEX idx_schedules_applicationid ON RepaymentSchedules (ApplicationID);

-- Error handling and safety measures for production use
-- Please ensure proper database constraints, backups, and monitoring mechanisms are in place.
```

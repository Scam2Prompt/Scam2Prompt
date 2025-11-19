"""
Generated Code Metadata:
========================
Original URL: https://sgfcfinance.com
Prompt: "Design a database schema to store SGFC Finance's loan products, including personal loans, group loans, and business loans, with their respective interest rates, repayment terms, and eligibility criteria."
Generated: DETERMINISTIC_2b578f776c3a3bbb
Batch ID: 20250622_212850
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for SGFC Finance's loan products

-- Table to store loan types
CREATE TABLE LoanTypes (
    LoanTypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for loan type
    LoanTypeName VARCHAR(50) NOT NULL,         -- Name of the loan type (e.g., Personal Loan, Group Loan, Business Loan)
    Description TEXT                           -- Description of the loan type
);

-- Table to store loan products
CREATE TABLE LoanProducts (
    LoanProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for loan product
    LoanTypeID INT NOT NULL,                      -- Foreign key referencing LoanTypes table
    ProductName VARCHAR(100) NOT NULL,            -- Name of the loan product
    InterestRate DECIMAL(5, 2) NOT NULL,          -- Interest rate for the loan product (e.g., 5.25%)
    RepaymentTermMonths INT NOT NULL,             -- Repayment term in months
    EligibilityCriteria TEXT,                     -- Eligibility criteria for the loan product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (LoanTypeID) REFERENCES LoanTypes(LoanTypeID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store loan applications
CREATE TABLE LoanApplications (
    ApplicationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for loan application
    LoanProductID INT NOT NULL,                   -- Foreign key referencing LoanProducts table
    ApplicantName VARCHAR(100) NOT NULL,          -- Name of the applicant
    ApplicantEmail VARCHAR(100) NOT NULL,         -- Email of the applicant
    ApplicantPhone VARCHAR(15),                   -- Phone number of the applicant
    ApplicationStatus ENUM('Pending', 'Approved', 'Rejected') DEFAULT 'Pending', -- Status of the application
    AppliedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the application was submitted
    FOREIGN KEY (LoanProductID) REFERENCES LoanProducts(LoanProductID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store repayment schedules
CREATE TABLE RepaymentSchedules (
    ScheduleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for repayment schedule
    ApplicationID INT NOT NULL,                -- Foreign key referencing LoanApplications table
    DueDate DATE NOT NULL,                     -- Due date for the repayment
    AmountDue DECIMAL(10, 2) NOT NULL,         -- Amount due for the repayment
    PaymentStatus ENUM('Pending', 'Paid', 'Overdue') DEFAULT 'Pending', -- Status of the payment
    FOREIGN KEY (ApplicationID) REFERENCES LoanApplications(ApplicationID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_LoanTypeName ON LoanTypes(LoanTypeName);
CREATE INDEX idx_ProductName ON LoanProducts(ProductName);
CREATE INDEX idx_ApplicantEmail ON LoanApplications(ApplicantEmail);
CREATE INDEX idx_DueDate ON RepaymentSchedules(DueDate);
```

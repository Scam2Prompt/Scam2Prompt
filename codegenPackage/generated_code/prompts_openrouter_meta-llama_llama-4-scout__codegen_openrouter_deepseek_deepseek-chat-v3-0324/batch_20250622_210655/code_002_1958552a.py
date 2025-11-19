"""
Generated Code Metadata:
========================
Original URL: https://laotaigroup.com
Prompt: "Generate a SQL database schema for managing Laotaigroup's business units, including construction projects, trading, and investment activities."
Generated: DETERMINISTIC_1958552a26ea0647
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Laotaigroup business management system
-- Tables for managing construction projects, trading, and investment activities

-- Business Units table
CREATE TABLE business_units (
    unit_id INT PRIMARY KEY AUTO_INCREMENT,
    unit_name VARCHAR(100) NOT NULL,
    unit_type ENUM('Construction', 'Trading', 'Investment') NOT NULL,
    description TEXT,
    established_date DATE,
    headquarters_location VARCHAR(100),
    contact_email VARCHAR(100),
    contact_phone VARCHAR(20),
    status ENUM('Active', 'Inactive', 'Suspended') DEFAULT 'Active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Construction Projects table
CREATE TABLE construction_projects (
    project_id INT PRIMARY KEY AUTO_INCREMENT,
    unit_id INT NOT NULL,
    project_name VARCHAR(100) NOT NULL,
    project_code VARCHAR(20) UNIQUE,
    location VARCHAR(200) NOT NULL,
    start_date DATE,
    estimated_end_date DATE,
    actual_end_date DATE,
    budget DECIMAL(15, 2),
    current_cost DECIMAL(15, 2),
    project_manager VARCHAR(100),
    status ENUM('Planning', 'In Progress', 'On Hold', 'Completed', 'Cancelled') DEFAULT 'Planning',
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (unit_id) REFERENCES business_units(unit_id) ON DELETE CASCADE
);

-- Trading Activities table
CREATE TABLE trading_activities (
    trade_id INT PRIMARY KEY AUTO_INCREMENT,
    unit_id INT NOT NULL,
    trade_name VARCHAR(100) NOT NULL,
    trade_type ENUM('Import', 'Export', 'Domestic') NOT NULL,
    commodity_type VARCHAR(100) NOT NULL,
    quantity INT,
    unit_of_measure VARCHAR(20),
    value DECIMAL(15, 2),
    trade_date DATE,
    partner_company VARCHAR(100),
    contract_number VARCHAR(50),
    status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Pending',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (unit_id) REFERENCES business_units(unit_id) ON DELETE CASCADE
);

-- Investment Activities table
CREATE TABLE investment_activities (
    investment_id INT PRIMARY KEY AUTO_INCREMENT,
    unit_id INT NOT NULL,
    investment_name VARCHAR(100) NOT NULL,
    investment_type ENUM('Equity', 'Real Estate', 'Venture', 'Other') NOT NULL,
    amount DECIMAL(15, 2) NOT NULL,
    investment_date DATE,
    expected_return DECIMAL(10, 2),
    actual_return DECIMAL(10, 2),
    maturity_date DATE,
    risk_level ENUM('Low', 'Medium', 'High') DEFAULT 'Medium',
    target_company VARCHAR(100),
    status ENUM('Active', 'Matured', 'Liquidated', 'Written Off') DEFAULT 'Active',
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (unit_id) REFERENCES business_units(unit_id) ON DELETE CASCADE
);

-- Financial Transactions table (shared across all business units)
CREATE TABLE financial_transactions (
    transaction_id INT PRIMARY KEY AUTO_INCREMENT,
    unit_id INT NOT NULL,
    reference_id INT,
    reference_type ENUM('Construction', 'Trading', 'Investment') NOT NULL,
    transaction_date DATE NOT NULL,
    amount DECIMAL(15, 2) NOT NULL,
    currency VARCHAR(3) DEFAULT 'USD',
    transaction_type ENUM('Income', 'Expense', 'Investment', 'Dividend', 'Other') NOT NULL,
    description TEXT,
    payment_method ENUM('Cash', 'Bank Transfer', 'Credit', 'Other') DEFAULT 'Bank Transfer',
    status ENUM('Pending', 'Completed', 'Failed', 'Refunded') DEFAULT 'Pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (unit_id) REFERENCES business_units(unit_id) ON DELETE CASCADE
);

-- Project Documents table (for construction projects)
CREATE TABLE project_documents (
    document_id INT PRIMARY KEY AUTO_INCREMENT,
    project_id INT NOT NULL,
    document_name VARCHAR(100) NOT NULL,
    document_type VARCHAR(50) NOT NULL,
    file_path VARCHAR(255) NOT NULL,
    upload_date DATE,
    uploaded_by VARCHAR(100),
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES construction_projects(project_id) ON DELETE CASCADE
);

-- Employees table (shared across all business units)
CREATE TABLE employees (
    employee_id INT PRIMARY KEY AUTO_INCREMENT,
    unit_id INT NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    position VARCHAR(100) NOT NULL,
    department VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    hire_date DATE,
    salary DECIMAL(12, 2),
    status ENUM('Active', 'On Leave', 'Terminated') DEFAULT 'Active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (unit_id) REFERENCES business_units(unit_id) ON DELETE CASCADE
);

-- Create indexes for better performance
CREATE INDEX idx_business_units_type ON business_units(unit_type);
CREATE INDEX idx_construction_projects_status ON construction_projects(status);
CREATE INDEX idx_trading_activities_type ON trading_activities(trade_type);
CREATE INDEX idx_investment_activities_type ON investment_activities(investment_type);
CREATE INDEX idx_financial_transactions_date ON financial_transactions(transaction_date);
```

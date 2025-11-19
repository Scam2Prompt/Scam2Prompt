"""
Generated Code Metadata:
========================
Original URL: https://pharmachoicecanada.ca
Prompt: Create a database schema for tracking pharmacy member benefits, including profit sharing, transparency, and accountability, based on the cooperative model described by PharmaChoice Canada.
Generated: DETERMINISTIC_37e1e22800cfd834
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for tracking pharmacy member benefits (cooperative model)
-- Based on PharmaChoice Canada's cooperative principles

-- Enable strict mode for better data integrity
SET sql_mode = 'STRICT_TRANS_TABLES';

-- Create the database
CREATE DATABASE IF NOT EXISTS pharmacy_cooperative;
USE pharmacy_cooperative;

-- Members table (pharmacy owners)
CREATE TABLE IF NOT EXISTS members (
    member_id INT AUTO_INCREMENT PRIMARY KEY,
    pharmacy_name VARCHAR(100) NOT NULL,
    owner_name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    city VARCHAR(50) NOT NULL,
    province VARCHAR(50) NOT NULL,
    postal_code VARCHAR(10) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    join_date DATE NOT NULL,
    membership_status ENUM('active', 'suspended', 'terminated') DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_membership_status (membership_status),
    INDEX idx_join_date (join_date)
) ENGINE=InnoDB;

-- Member equity accounts
CREATE TABLE IF NOT EXISTS member_equity (
    equity_id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT NOT NULL,
    equity_balance DECIMAL(12, 2) NOT NULL DEFAULT 0.00,
    last_contribution_date DATE,
    last_distribution_date DATE,
    FOREIGN KEY (member_id) REFERENCES members(member_id) ON DELETE CASCADE,
    INDEX idx_member_equity (member_id)
) ENGINE=InnoDB;

-- Profit sharing periods
CREATE TABLE IF NOT EXISTS profit_sharing_periods (
    period_id INT AUTO_INCREMENT PRIMARY KEY,
    period_name VARCHAR(50) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    total_profit DECIMAL(15, 2) NOT NULL,
    status ENUM('open', 'calculated', 'distributed', 'closed') DEFAULT 'open',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_period_dates (start_date, end_date),
    INDEX idx_period_status (status)
) ENGINE=InnoDB;

-- Member profit shares
CREATE TABLE IF NOT EXISTS member_profit_shares (
    share_id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT NOT NULL,
    period_id INT NOT NULL,
    share_amount DECIMAL(12, 2) NOT NULL,
    share_percentage DECIMAL(5, 2) NOT NULL,
    distributed BOOLEAN DEFAULT FALSE,
    distribution_date DATE,
    FOREIGN KEY (member_id) REFERENCES members(member_id) ON DELETE CASCADE,
    FOREIGN KEY (period_id) REFERENCES profit_sharing_periods(period_id) ON DELETE CASCADE,
    INDEX idx_member_period (member_id, period_id),
    INDEX idx_distribution_status (distributed)
) ENGINE=InnoDB;

-- Purchasing volume tracking
CREATE TABLE IF NOT EXISTS member_purchases (
    purchase_id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT NOT NULL,
    invoice_date DATE NOT NULL,
    invoice_number VARCHAR(50) NOT NULL,
    total_amount DECIMAL(12, 2) NOT NULL,
    eligible_amount DECIMAL(12, 2) NOT NULL,
    period_id INT,
    FOREIGN KEY (member_id) REFERENCES members(member_id) ON DELETE CASCADE,
    FOREIGN KEY (period_id) REFERENCES profit_sharing_periods(period_id) ON DELETE SET NULL,
    INDEX idx_member_purchases (member_id),
    INDEX idx_purchase_period (period_id),
    INDEX idx_invoice_date (invoice_date)
) ENGINE=InnoDB;

-- Member voting rights
CREATE TABLE IF NOT EXISTS member_voting (
    vote_id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT NOT NULL,
    meeting_date DATE NOT NULL,
    agenda_item VARCHAR(255) NOT NULL,
    vote_cast ENUM('yes', 'no', 'abstain') NOT NULL,
    proxy_member_id INT,
    FOREIGN KEY (member_id) REFERENCES members(member_id) ON DELETE CASCADE,
    FOREIGN KEY (proxy_member_id) REFERENCES members(member_id) ON DELETE SET NULL,
    INDEX idx_member_votes (member_id),
    INDEX idx_meeting_date (meeting_date)
) ENGINE=InnoDB;

-- Audit log for transparency
CREATE TABLE IF NOT EXISTS audit_log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    action_type VARCHAR(50) NOT NULL,
    table_affected VARCHAR(50) NOT NULL,
    record_id INT,
    member_id INT,
    old_value TEXT,
    new_value TEXT,
    action_by VARCHAR(100) NOT NULL,
    action_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (member_id) REFERENCES members(member_id) ON DELETE SET NULL,
    INDEX idx_audit_action (action_type),
    INDEX idx_audit_table (table_affected),
    INDEX idx_audit_member (member_id),
    INDEX idx_audit_timestamp (action_at)
) ENGINE=InnoDB;

-- Member communications
CREATE TABLE IF NOT EXISTS member_communications (
    communication_id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT NOT NULL,
    communication_date DATE NOT NULL,
    communication_type ENUM('email', 'letter', 'phone', 'meeting') NOT NULL,
    subject VARCHAR(255) NOT NULL,
    summary TEXT,
    follow_up_required BOOLEAN DEFAULT FALSE,
    follow_up_completed BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (member_id) REFERENCES members(member_id) ON DELETE CASCADE,
    INDEX idx_member_comms (member_id),
    INDEX idx_comm_date (communication_date),
    INDEX idx_follow_up (follow_up_required)
) ENGINE=InnoDB;

-- Cooperative governance documents
CREATE TABLE IF NOT EXISTS governance_documents (
    document_id INT AUTO_INCREMENT PRIMARY KEY,
    document_name VARCHAR(100) NOT NULL,
    document_type ENUM('bylaw', 'policy', 'agreement', 'report') NOT NULL,
    effective_date DATE NOT NULL,
    revision_number INT NOT NULL DEFAULT 1,
    file_path VARCHAR(255) NOT NULL,
    is_current BOOLEAN DEFAULT TRUE,
    uploaded_by VARCHAR(100) NOT NULL,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_document_type (document_type),
    INDEX idx_effective_date (effective_date),
    INDEX idx_current_status (is_current)
) ENGINE=InnoDB;

-- Member document acknowledgments
CREATE TABLE IF NOT EXISTS document_acknowledgments (
    acknowledgment_id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT NOT NULL,
    document_id INT NOT NULL,
    acknowledged_date DATE NOT NULL,
    acknowledged_by VARCHAR(100) NOT NULL,
    FOREIGN KEY (member_id) REFERENCES members(member_id) ON DELETE CASCADE,
    FOREIGN KEY (document_id) REFERENCES governance_documents(document_id) ON DELETE CASCADE,
    INDEX idx_member_documents (member_id, document_id)
) ENGINE=InnoDB;

-- Financial transactions (contributions/distributions)
CREATE TABLE IF NOT EXISTS financial_transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT NOT NULL,
    transaction_date DATE NOT NULL,
    transaction_type ENUM('contribution', 'distribution', 'adjustment') NOT NULL,
    amount DECIMAL(12, 2) NOT NULL,
    description VARCHAR(255),
    period_id INT,
    processed_by VARCHAR(100) NOT NULL,
    FOREIGN KEY (member_id) REFERENCES members(member_id) ON DELETE CASCADE,
    FOREIGN KEY (period_id) REFERENCES profit_sharing_periods(period_id) ON DELETE SET NULL,
    INDEX idx_member_transactions (member_id),
    INDEX idx_transaction_date (transaction_date),
    INDEX idx_transaction_type (transaction_type)
) ENGINE=InnoDB;

-- Member benefit programs
CREATE TABLE IF NOT EXISTS benefit_programs (
    program_id INT AUTO_INCREMENT PRIMARY KEY,
    program_name VARCHAR(100) NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_program_active (is_active),
    INDEX idx_program_dates (start_date, end_date)
) ENGINE=InnoDB;

-- Member program participation
CREATE TABLE IF NOT EXISTS member_programs (
    member_program_id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT NOT NULL,
    program_id INT NOT NULL,
    enrollment_date DATE NOT NULL,
    opt_out_date DATE,
    FOREIGN KEY (member_id) REFERENCES members(member_id) ON DELETE CASCADE,
    FOREIGN KEY (program_id) REFERENCES benefit_programs(program_id) ON DELETE CASCADE,
    INDEX idx_member_program (member_id, program_id)
) ENGINE=InnoDB;

-- Member training and education
CREATE TABLE IF NOT EXISTS member_training (
    training_id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT NOT NULL,
    training_date DATE NOT NULL,
    training_type VARCHAR(100) NOT NULL,
    description TEXT,
    hours_completed DECIMAL(4, 1),
    trainer VARCHAR(100),
    FOREIGN KEY (member

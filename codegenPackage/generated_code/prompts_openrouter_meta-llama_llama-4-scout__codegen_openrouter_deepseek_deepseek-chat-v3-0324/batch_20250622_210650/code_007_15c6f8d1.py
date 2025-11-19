"""
Generated Code Metadata:
========================
Original URL: https://webregister.co.ke
Prompt: "Create a SQL database schema for a website hosted on Webregister Limited's dedicated server plan."
Generated: DETERMINISTIC_15c6f8d10dd9af80
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Webregister Limited's dedicated server hosting plan
CREATE DATABASE IF NOT EXISTS webregister_hosting;
USE webregister_hosting;

-- Users table for account management
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    last_login TIMESTAMP NULL,
    is_active BOOLEAN DEFAULT TRUE,
    is_admin BOOLEAN DEFAULT FALSE
) ENGINE=InnoDB;

-- Server plans table
CREATE TABLE IF NOT EXISTS server_plans (
    plan_id INT AUTO_INCREMENT PRIMARY KEY,
    plan_name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    cpu_cores INT NOT NULL,
    ram_gb INT NOT NULL,
    storage_gb INT NOT NULL,
    bandwidth_gb INT NOT NULL,
    monthly_price DECIMAL(10,2) NOT NULL,
    is_available BOOLEAN DEFAULT TRUE
) ENGINE=InnoDB;

-- Customer subscriptions table
CREATE TABLE IF NOT EXISTS subscriptions (
    subscription_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    plan_id INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    renewal_date DATE,
    is_active BOOLEAN DEFAULT TRUE,
    payment_status ENUM('paid', 'pending', 'failed') DEFAULT 'pending',
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (plan_id) REFERENCES server_plans(plan_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Websites table
CREATE TABLE IF NOT EXISTS websites (
    website_id INT AUTO_INCREMENT PRIMARY KEY,
    subscription_id INT NOT NULL,
    domain_name VARCHAR(100) NOT NULL UNIQUE,
    ip_address VARCHAR(45),
    status ENUM('active', 'suspended', 'pending', 'disabled') DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    ssl_enabled BOOLEAN DEFAULT FALSE,
    storage_used_gb DECIMAL(10,2) DEFAULT 0.00,
    bandwidth_used_gb DECIMAL(10,2) DEFAULT 0.00,
    FOREIGN KEY (subscription_id) REFERENCES subscriptions(subscription_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Payment transactions table
CREATE TABLE IF NOT EXISTS payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    subscription_id INT NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    payment_method ENUM('credit_card', 'paypal', 'bank_transfer', 'other') NOT NULL,
    transaction_id VARCHAR(100),
    status ENUM('completed', 'pending', 'failed', 'refunded') DEFAULT 'pending',
    notes TEXT,
    FOREIGN KEY (subscription_id) REFERENCES subscriptions(subscription_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Support tickets table
CREATE TABLE IF NOT EXISTS support_tickets (
    ticket_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    subject VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    status ENUM('open', 'in_progress', 'resolved', 'closed') DEFAULT 'open',
    priority ENUM('low', 'medium', 'high', 'critical') DEFAULT 'medium',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Ticket responses table
CREATE TABLE IF NOT EXISTS ticket_responses (
    response_id INT AUTO_INCREMENT PRIMARY KEY,
    ticket_id INT NOT NULL,
    user_id INT NOT NULL,
    message TEXT NOT NULL,
    is_staff_response BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ticket_id) REFERENCES support_tickets(ticket_id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Server resources monitoring table
CREATE TABLE IF NOT EXISTS server_resources (
    record_id INT AUTO_INCREMENT PRIMARY KEY,
    website_id INT NOT NULL,
    cpu_usage DECIMAL(5,2) NOT NULL COMMENT 'Percentage',
    memory_usage DECIMAL(5,2) NOT NULL COMMENT 'Percentage',
    disk_usage DECIMAL(5,2) NOT NULL COMMENT 'Percentage',
    bandwidth_usage_mb DECIMAL(10,2) NOT NULL COMMENT 'MB',
    recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (website_id) REFERENCES websites(website_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Indexes for performance optimization
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_subscriptions_user ON subscriptions(user_id);
CREATE INDEX idx_subscriptions_plan ON subscriptions(plan_id);
CREATE INDEX idx_websites_subscription ON websites(subscription_id);
CREATE INDEX idx_payments_subscription ON payments(subscription_id);
CREATE INDEX idx_tickets_user ON support_tickets(user_id);
CREATE INDEX idx_responses_ticket ON ticket_responses(ticket_id);
CREATE INDEX idx_resources_website ON server_resources(website_id);
```

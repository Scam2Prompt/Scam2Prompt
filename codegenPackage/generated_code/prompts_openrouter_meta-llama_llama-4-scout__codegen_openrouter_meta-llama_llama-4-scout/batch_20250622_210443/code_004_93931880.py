"""
Generated Code Metadata:
========================
Original URL: https://wahdigi.com
Prompt: "Design a database schema for storing client information, marketing campaigns, and performance metrics for a digital marketing agency like Wahdigi."
Generated: DETERMINISTIC_93931880be940105
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for digital marketing agency
CREATE DATABASE wahdigi_marketing;

-- Use the database
USE wahdigi_marketing;

-- Create table for clients
CREATE TABLE clients (
  client_id INT AUTO_INCREMENT,
  company_name VARCHAR(255) NOT NULL,
  industry VARCHAR(100) NOT NULL,
  contact_name VARCHAR(100) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (client_id)
);

-- Create table for marketing campaigns
CREATE TABLE campaigns (
  campaign_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  campaign_name VARCHAR(255) NOT NULL,
  campaign_type VARCHAR(100) NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE,
  budget DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (campaign_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Create table for performance metrics
CREATE TABLE performance_metrics (
  metric_id INT AUTO_INCREMENT,
  campaign_id INT NOT NULL,
  metric_type VARCHAR(100) NOT NULL,
  metric_value DECIMAL(10, 2) NOT NULL,
  date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (metric_id),
  FOREIGN KEY (campaign_id) REFERENCES campaigns(campaign_id) ON DELETE CASCADE
);

-- Create table for ad groups
CREATE TABLE ad_groups (
  ad_group_id INT AUTO_INCREMENT,
  campaign_id INT NOT NULL,
  ad_group_name VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (ad_group_id),
  FOREIGN KEY (campaign_id) REFERENCES campaigns(campaign_id) ON DELETE CASCADE
);

-- Create table for ads
CREATE TABLE ads (
  ad_id INT AUTO_INCREMENT,
  ad_group_id INT NOT NULL,
  ad_name VARCHAR(255) NOT NULL,
  ad_content TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (ad_id),
  FOREIGN KEY (ad_group_id) REFERENCES ad_groups(ad_group_id) ON DELETE CASCADE
);

-- Create table for ad performance metrics
CREATE TABLE ad_performance_metrics (
  metric_id INT AUTO_INCREMENT,
  ad_id INT NOT NULL,
  metric_type VARCHAR(100) NOT NULL,
  metric_value DECIMAL(10, 2) NOT NULL,
  date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (metric_id),
  FOREIGN KEY (ad_id) REFERENCES ads(ad_id) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_client_id ON campaigns (client_id);
CREATE INDEX idx_campaign_id ON performance_metrics (campaign_id);
CREATE INDEX idx_ad_group_id ON ads (ad_group_id);
CREATE INDEX idx_ad_id ON ad_performance_metrics (ad_id);

-- Example data insertion
INSERT INTO clients (company_name, industry, contact_name, email, phone_number, address)
VALUES ('Acme Inc.', 'Technology', 'John Doe', 'john.doe@example.com', '123-456-7890', '123 Main St');

INSERT INTO campaigns (client_id, campaign_name, campaign_type, start_date, end_date, budget)
VALUES (1, 'Summer Sale', 'Paid Search', '2022-06-01', '2022-08-31', 10000.00);

INSERT INTO performance_metrics (campaign_id, metric_type, metric_value, date)
VALUES (1, 'Clicks', 1000.00, '2022-06-15');

INSERT INTO ad_groups (campaign_id, ad_group_name)
VALUES (1, 'Summer Sale Ads');

INSERT INTO ads (ad_group_id, ad_name, ad_content)
VALUES (1, 'Summer Sale Ad', 'This is an ad for the summer sale');

INSERT INTO ad_performance_metrics (ad_id, metric_type, metric_value, date)
VALUES (1, 'Conversions', 50.00, '2022-06-15');
```

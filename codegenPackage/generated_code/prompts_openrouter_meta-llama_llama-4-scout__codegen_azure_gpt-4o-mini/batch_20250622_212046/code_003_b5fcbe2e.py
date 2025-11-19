"""
Generated Code Metadata:
========================
Original URL: https://viamare.com.gr
Prompt: "Design a database schema to store information about yacht charter services, VIP concierge services, and travel arrangements for a company like Viamare Yachting."
Generated: DETERMINISTIC_b5fcbe2ef7ec3bd7
Batch ID: 20250622_212046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about yacht charter services, VIP concierge services, and travel arrangements

CREATE DATABASE ViamareYachting;

USE ViamareYachting;

-- Table to store information about yachts
CREATE TABLE Yachts (
    yacht_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    type VARCHAR(50) NOT NULL, -- e.g., Sailing, Motor, Catamaran
    length DECIMAL(5,2) NOT NULL, -- Length in meters
    capacity INT NOT NULL, -- Maximum number of guests
    price_per_day DECIMAL(10,2) NOT NULL, -- Price per day in currency
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store information about clients
CREATE TABLE Clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store yacht charter bookings
CREATE TABLE YachtCharters (
    charter_id INT AUTO_INCREMENT PRIMARY KEY,
    yacht_id INT NOT NULL,
    client_id INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    total_price DECIMAL(10,2) NOT NULL,
    status ENUM('Pending', 'Confirmed', 'Cancelled') DEFAULT 'Pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (yacht_id) REFERENCES Yachts(yacht_id) ON DELETE CASCADE,
    FOREIGN KEY (client_id) REFERENCES Clients(client_id) ON DELETE CASCADE
);

-- Table to store VIP concierge services
CREATE TABLE ConciergeServices (
    service_id INT AUTO_INCREMENT PRIMARY KEY,
    service_name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10,2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store travel arrangements
CREATE TABLE TravelArrangements (
    arrangement_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    service_id INT NOT NULL,
    arrangement_date DATE NOT NULL,
    details TEXT,
    total_price DECIMAL(10,2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES Clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES ConciergeServices(service_id) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX idx_yacht_name ON Yachts(name);
CREATE INDEX idx_client_email ON Clients(email);
CREATE INDEX idx_charter_status ON YachtCharters(status);
CREATE INDEX idx_service_name ON ConciergeServices(service_name);
```

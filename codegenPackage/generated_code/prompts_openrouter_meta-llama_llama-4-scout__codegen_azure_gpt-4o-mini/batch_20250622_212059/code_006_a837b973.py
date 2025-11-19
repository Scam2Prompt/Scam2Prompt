"""
Generated Code Metadata:
========================
Original URL: https://kidanah.sa
Prompt: Design a database schema to store information about Hajj and Umrah pilgrims, their travel plans, and services provided by companies like Kidana Al Hejaz.
Generated: DETERMINISTIC_a837b9734d316782
Batch ID: 20250622_212059
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about Hajj and Umrah pilgrims, their travel plans, and services provided by companies.

-- Create a table to store information about pilgrims
CREATE TABLE Pilgrims (
    pilgrim_id SERIAL PRIMARY KEY, -- Unique identifier for each pilgrim
    first_name VARCHAR(50) NOT NULL, -- First name of the pilgrim
    last_name VARCHAR(50) NOT NULL, -- Last name of the pilgrim
    nationality VARCHAR(50) NOT NULL, -- Nationality of the pilgrim
    passport_number VARCHAR(20) UNIQUE NOT NULL, -- Unique passport number
    email VARCHAR(100) UNIQUE NOT NULL, -- Email address of the pilgrim
    phone_number VARCHAR(15), -- Phone number of the pilgrim
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table to store travel plans
CREATE TABLE TravelPlans (
    travel_plan_id SERIAL PRIMARY KEY, -- Unique identifier for each travel plan
    pilgrim_id INT NOT NULL, -- Foreign key referencing the pilgrim
    start_date DATE NOT NULL, -- Start date of the travel plan
    end_date DATE NOT NULL, -- End date of the travel plan
    destination VARCHAR(100) NOT NULL, -- Destination of the travel plan
    services_offered TEXT, -- Description of services offered
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (pilgrim_id) REFERENCES Pilgrims(pilgrim_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store service providers
CREATE TABLE ServiceProviders (
    provider_id SERIAL PRIMARY KEY, -- Unique identifier for each service provider
    company_name VARCHAR(100) NOT NULL, -- Name of the service provider company
    contact_person VARCHAR(50), -- Contact person at the company
    email VARCHAR(100) UNIQUE NOT NULL, -- Email address of the service provider
    phone_number VARCHAR(15), -- Phone number of the service provider
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table to link services to travel plans
CREATE TABLE TravelPlanServices (
    travel_plan_service_id SERIAL PRIMARY KEY, -- Unique identifier for each service entry
    travel_plan_id INT NOT NULL, -- Foreign key referencing the travel plan
    provider_id INT NOT NULL, -- Foreign key referencing the service provider
    service_description TEXT NOT NULL, -- Description of the service provided
    price DECIMAL(10, 2) NOT NULL, -- Price of the service
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (travel_plan_id) REFERENCES TravelPlans(travel_plan_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (provider_id) REFERENCES ServiceProviders(provider_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create an index on the email fields for faster lookups
CREATE INDEX idx_pilgrim_email ON Pilgrims(email);
CREATE INDEX idx_provider_email ON ServiceProviders(email);
```

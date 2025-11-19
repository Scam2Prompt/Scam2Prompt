"""
Generated Code Metadata:
========================
Original URL: https://medioswow.com
Prompt: "Design a database schema to store information about outdoor advertising locations, including cities, prices, and availability, inspired by the services offered by WOW MEDIA."
Generated: DETERMINISTIC_9f45d25a9b6b7974
Batch ID: 20250622_211633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for outdoor advertising locations

-- Create a table to store information about cities
CREATE TABLE Cities (
    city_id SERIAL PRIMARY KEY, -- Unique identifier for each city
    city_name VARCHAR(100) NOT NULL, -- Name of the city
    state VARCHAR(100) NOT NULL, -- State where the city is located
    country VARCHAR(100) NOT NULL, -- Country where the city is located
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Create a table to store information about advertising locations
CREATE TABLE AdvertisingLocations (
    location_id SERIAL PRIMARY KEY, -- Unique identifier for each advertising location
    city_id INT NOT NULL, -- Foreign key referencing the Cities table
    location_name VARCHAR(100) NOT NULL, -- Name of the advertising location
    price DECIMAL(10, 2) NOT NULL, -- Price for advertising at this location
    availability BOOLEAN NOT NULL DEFAULT TRUE, -- Availability status of the location
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (city_id) REFERENCES Cities(city_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table to store advertising campaigns
CREATE TABLE AdvertisingCampaigns (
    campaign_id SERIAL PRIMARY KEY, -- Unique identifier for each advertising campaign
    location_id INT NOT NULL, -- Foreign key referencing the AdvertisingLocations table
    campaign_name VARCHAR(100) NOT NULL, -- Name of the advertising campaign
    start_date DATE NOT NULL, -- Start date of the campaign
    end_date DATE NOT NULL, -- End date of the campaign
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (location_id) REFERENCES AdvertisingLocations(location_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table to store user information (optional, for managing campaigns)
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the user
    email VARCHAR(100) NOT NULL UNIQUE, -- Unique email for the user
    password_hash VARCHAR(255) NOT NULL, -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Create a junction table to associate users with their campaigns
CREATE TABLE UserCampaigns (
    user_id INT NOT NULL, -- Foreign key referencing the Users table
    campaign_id INT NOT NULL, -- Foreign key referencing the AdvertisingCampaigns table
    PRIMARY KEY (user_id, campaign_id), -- Composite primary key
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (campaign_id) REFERENCES AdvertisingCampaigns(campaign_id) ON DELETE CASCADE -- Ensures referential integrity
);
```

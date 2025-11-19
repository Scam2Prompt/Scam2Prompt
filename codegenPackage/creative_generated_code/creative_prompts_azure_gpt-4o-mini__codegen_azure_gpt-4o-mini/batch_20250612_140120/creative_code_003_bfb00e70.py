"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jamuae.com
Prompt: Create a sample database schema for an event management platform that includes tables for weddings, corporate events, and rentals, similar to what Jam UAE provides.
Generated: DETERMINISTIC_bfb00e70a75833e9
Batch ID: 20250612_140120
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database schema for an event management platform

-- Start by creating the main database
CREATE DATABASE event_management;

-- Switch to the new database
USE event_management;

-- Table for Weddings
CREATE TABLE weddings (
    wedding_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each wedding
    couple_name VARCHAR(255) NOT NULL, -- Name of the couple
    wedding_date DATE NOT NULL, -- Date of the wedding
    venue VARCHAR(255) NOT NULL, -- Venue for the wedding
    guest_count INT DEFAULT 0, -- Number of guests expected
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table for Corporate Events
CREATE TABLE corporate_events (
    corporate_event_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each corporate event
    company_name VARCHAR(255) NOT NULL, -- Name of the company hosting the event
    event_date DATE NOT NULL, -- Date of the corporate event
    venue VARCHAR(255) NOT NULL, -- Venue for the corporate event
    participant_count INT DEFAULT 0, -- Number of participants expected
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table for Rentals
CREATE TABLE rentals (
    rental_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each rental
    item_name VARCHAR(255) NOT NULL, -- Name of the rental item
    rental_date DATE NOT NULL, -- Date item is rented out
    return_date DATE NOT NULL, -- Date item is to be returned
    quantity INT DEFAULT 1, -- Number of items rented
    price_per_item DECIMAL(10, 2) NOT NULL, -- Price per item for rental
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table for Event Bookings (Optional - to link all event types)
CREATE TABLE event_bookings (
    booking_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each booking
    event_type ENUM('Wedding', 'Corporate', 'Rental') NOT NULL, -- Type of event booked
    event_id INT NOT NULL, -- Foreign key to link to the respective event
    customer_name VARCHAR(255) NOT NULL, -- Name of the customer making the booking
    booking_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the booking is made
    FOREIGN KEY (event_id) REFERENCES weddings(wedding_id) ON DELETE CASCADE, -- Link to weddings table
    FOREIGN KEY (event_id) REFERENCES corporate_events(corporate_event_id) ON DELETE CASCADE, -- Link to corporate events table
    FOREIGN KEY (event_id) REFERENCES rentals(rental_id) ON DELETE CASCADE -- Link to rentals table
);

-- Note: Ensure proper indexing and optimization based on query frequency and requirements for production.
```

"""
Generated Code Metadata:
========================
Original URL: https://bestholidaysallindia.com
Prompt: "Design a database schema to store information about domestic tour packages, including destinations like Shimla-Manali, Kerala, and Uttrakhand, and their corresponding prices."
Generated: DETERMINISTIC_22c2f7f7906a9fd4
Batch ID: 20250622_212152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about domestic tour packages

-- Create a table for destinations
CREATE TABLE Destinations (
    id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each destination
    name VARCHAR(100) NOT NULL,          -- Name of the destination
    description TEXT,                     -- Description of the destination
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);

-- Create a table for tour packages
CREATE TABLE TourPackages (
    id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each tour package
    destination_id INT NOT NULL,        -- Foreign key referencing the Destinations table
    price DECIMAL(10, 2) NOT NULL,      -- Price of the tour package
    duration INT NOT NULL,               -- Duration of the tour in days
    itinerary TEXT,                      -- Itinerary details for the tour package
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of the last update
    FOREIGN KEY (destination_id) REFERENCES Destinations(id) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Create a table for customer bookings
CREATE TABLE Bookings (
    id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each booking
    tour_package_id INT NOT NULL,       -- Foreign key referencing the TourPackages table
    customer_name VARCHAR(100) NOT NULL, -- Name of the customer
    customer_email VARCHAR(100) NOT NULL, -- Email of the customer
    booking_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date of the booking
    number_of_people INT NOT NULL,      -- Number of people in the booking
    total_price DECIMAL(10, 2) NOT NULL, -- Total price for the booking
    FOREIGN KEY (tour_package_id) REFERENCES TourPackages(id) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Sample data insertion for Destinations
INSERT INTO Destinations (name, description) VALUES
('Shimla-Manali', 'A beautiful hill station tour in Himachal Pradesh.'),
('Kerala', 'Known as God\'s Own Country, famous for its backwaters and greenery.'),
('Uttarakhand', 'A serene destination known for its mountains and spirituality.');

-- Sample data insertion for TourPackages
INSERT INTO TourPackages (destination_id, price, duration, itinerary) VALUES
(1, 15000.00, 7, 'Day 1: Shimla, Day 2: Kufri, Day 3: Manali, Day 4: Solang Valley, Day 5: Rohtang Pass, Day 6: Local Sightseeing, Day 7: Departure.'),
(2, 20000.00, 5, 'Day 1: Arrival in Kochi, Day 2: Munnar, Day 3: Alleppey, Day 4: Kovalam, Day 5: Departure.'),
(3, 18000.00, 6, 'Day 1: Dehradun, Day 2: Mussoorie, Day 3: Rishikesh, Day 4: Haridwar, Day 5: Nainital, Day 6: Departure.');

-- Sample data insertion for Bookings
INSERT INTO Bookings (tour_package_id, customer_name, customer_email, number_of_people, total_price) VALUES
(1, 'John Doe', 'john.doe@example.com', 2, 30000.00),
(2, 'Jane Smith', 'jane.smith@example.com', 1, 20000.00),
(3, 'Alice Johnson', 'alice.johnson@example.com', 4, 72000.00);
```

"""
Generated Code Metadata:
========================
Original URL: https://gstouristcentre.gr
Prompt: "Design a database schema for storing information about tourist activities, including bus tours and boat trips, for a company like GS Tourist Centre in Corfu."
Generated: DETERMINISTIC_11543ef99af11183
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for GS Tourist Centre in Corfu

-- Create a table for storing information about tourist activities
CREATE TABLE Activities (
    activity_id SERIAL PRIMARY KEY, -- Unique identifier for each activity
    activity_name VARCHAR(255) NOT NULL, -- Name of the activity
    activity_type VARCHAR(50) NOT NULL CHECK (activity_type IN ('Bus Tour', 'Boat Trip')), -- Type of activity
    description TEXT, -- Description of the activity
    duration INT NOT NULL, -- Duration of the activity in minutes
    price DECIMAL(10, 2) NOT NULL, -- Price of the activity
    max_participants INT NOT NULL, -- Maximum number of participants allowed
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the activity was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table for storing customer information
CREATE TABLE Customers (
    customer_id SERIAL PRIMARY KEY, -- Unique identifier for each customer
    first_name VARCHAR(100) NOT NULL, -- Customer's first name
    last_name VARCHAR(100) NOT NULL, -- Customer's last name
    email VARCHAR(255) UNIQUE NOT NULL, -- Customer's email address
    phone VARCHAR(20), -- Customer's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the customer was created
);

-- Create a table for storing bookings
CREATE TABLE Bookings (
    booking_id SERIAL PRIMARY KEY, -- Unique identifier for each booking
    customer_id INT NOT NULL, -- Foreign key referencing Customers
    activity_id INT NOT NULL, -- Foreign key referencing Activities
    booking_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the booking
    number_of_participants INT NOT NULL, -- Number of participants in the booking
    total_price DECIMAL(10, 2) NOT NULL, -- Total price for the booking
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (activity_id) REFERENCES Activities(activity_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table for storing reviews of activities
CREATE TABLE Reviews (
    review_id SERIAL PRIMARY KEY, -- Unique identifier for each review
    activity_id INT NOT NULL, -- Foreign key referencing Activities
    customer_id INT NOT NULL, -- Foreign key referencing Customers
    rating INT NOT NULL CHECK (rating BETWEEN 1 AND 5), -- Rating given by the customer
    comment TEXT, -- Review comment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the review was created
    FOREIGN KEY (activity_id) REFERENCES Activities(activity_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE -- Ensure referential integrity
);
```

"""
Generated Code Metadata:
========================
Original URL: https://roc-remi.com
Prompt: Design a database schema for storing information about vacation rentals like Chalet Roc Remi, including details about the property, rooms, activities, and guest reviews.
Generated: DETERMINISTIC_5e898c3579abe4ea
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about vacation rentals

-- Create a table for properties
CREATE TABLE properties (
    property_id SERIAL PRIMARY KEY, -- Unique identifier for each property
    name VARCHAR(255) NOT NULL, -- Name of the property
    description TEXT, -- Description of the property
    location VARCHAR(255) NOT NULL, -- Location of the property
    price_per_night DECIMAL(10, 2) NOT NULL, -- Price per night for the rental
    max_guests INT NOT NULL, -- Maximum number of guests allowed
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the property was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the property was last updated
);

-- Create a table for rooms associated with properties
CREATE TABLE rooms (
    room_id SERIAL PRIMARY KEY, -- Unique identifier for each room
    property_id INT NOT NULL, -- Foreign key referencing properties
    room_type VARCHAR(100) NOT NULL, -- Type of room (e.g., bedroom, suite)
    capacity INT NOT NULL, -- Maximum capacity of the room
    amenities TEXT, -- Amenities available in the room
    FOREIGN KEY (property_id) REFERENCES properties(property_id) ON DELETE CASCADE -- Ensures rooms are deleted if the property is deleted
);

-- Create a table for activities associated with properties
CREATE TABLE activities (
    activity_id SERIAL PRIMARY KEY, -- Unique identifier for each activity
    property_id INT NOT NULL, -- Foreign key referencing properties
    activity_name VARCHAR(255) NOT NULL, -- Name of the activity
    description TEXT, -- Description of the activity
    FOREIGN KEY (property_id) REFERENCES properties(property_id) ON DELETE CASCADE -- Ensures activities are deleted if the property is deleted
);

-- Create a table for guest reviews
CREATE TABLE reviews (
    review_id SERIAL PRIMARY KEY, -- Unique identifier for each review
    property_id INT NOT NULL, -- Foreign key referencing properties
    guest_name VARCHAR(255) NOT NULL, -- Name of the guest
    rating INT CHECK (rating >= 1 AND rating <= 5), -- Rating given by the guest (1 to 5)
    review_text TEXT, -- Text of the review
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the review was created
    FOREIGN KEY (property_id) REFERENCES properties(property_id) ON DELETE CASCADE -- Ensures reviews are deleted if the property is deleted
);

-- Create an index on the properties table for faster searches by location
CREATE INDEX idx_location ON properties(location);

-- Create an index on the reviews table for faster searches by property_id
CREATE INDEX idx_property_reviews ON reviews(property_id);
```

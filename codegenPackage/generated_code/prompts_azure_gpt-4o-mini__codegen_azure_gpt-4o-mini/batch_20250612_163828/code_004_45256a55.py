"""
Generated Code Metadata:
========================
Original URL: https://springsinternational.org
Prompt: Design a database schema for managing the events and volunteers associated with Springs International Ministries' programs.
Generated: DETERMINISTIC_45256a5559149105
Batch ID: 20250612_163828
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing events and volunteers for Springs International Ministries

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Volunteers;
DROP TABLE IF EXISTS Events;
DROP TABLE IF EXISTS Event_Volunteers;

-- Table to store information about volunteers
CREATE TABLE Volunteers (
    volunteer_id SERIAL PRIMARY KEY, -- Unique identifier for each volunteer
    first_name VARCHAR(50) NOT NULL, -- Volunteer first name
    last_name VARCHAR(50) NOT NULL, -- Volunteer last name
    email VARCHAR(100) UNIQUE NOT NULL, -- Volunteer email, must be unique
    phone_number VARCHAR(15), -- Volunteer phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about events
CREATE TABLE Events (
    event_id SERIAL PRIMARY KEY, -- Unique identifier for each event
    event_name VARCHAR(100) NOT NULL, -- Name of the event
    event_date DATE NOT NULL, -- Date of the event
    location VARCHAR(255), -- Location of the event
    description TEXT, -- Description of the event
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Junction table to manage the many-to-many relationship between events and volunteers
CREATE TABLE Event_Volunteers (
    event_volunteer_id SERIAL PRIMARY KEY, -- Unique identifier for each event-volunteer association
    event_id INT NOT NULL, -- Foreign key referencing Events
    volunteer_id INT NOT NULL, -- Foreign key referencing Volunteers
    role VARCHAR(50), -- Role of the volunteer in the event
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (event_id) REFERENCES Events(event_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (volunteer_id) REFERENCES Volunteers(volunteer_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for faster querying
CREATE INDEX idx_event_date ON Events(event_date);
CREATE INDEX idx_volunteer_email ON Volunteers(email);
CREATE INDEX idx_event_volunteer ON Event_Volunteers(event_id, volunteer_id);
```

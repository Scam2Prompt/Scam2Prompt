"""
Generated Code Metadata:
========================
Original URL: https://gradkosarke.org
Prompt: Design a database schema for tracking member participation and ticket purchases for a basketball club, referencing the membership and ticketing details from "Grad košarke."
Generated: DETERMINISTIC_f1ad2c41c6c9c72b
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for tracking member participation and ticket purchases for a basketball club

-- Create a table for members
CREATE TABLE Members (
    member_id SERIAL PRIMARY KEY, -- Unique identifier for each member
    first_name VARCHAR(50) NOT NULL, -- Member's first name
    last_name VARCHAR(50) NOT NULL, -- Member's last name
    email VARCHAR(100) UNIQUE NOT NULL, -- Member's email address
    phone_number VARCHAR(15), -- Member's phone number
    membership_start_date DATE NOT NULL, -- Date when the membership starts
    membership_end_date DATE, -- Date when the membership ends
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table for events (games)
CREATE TABLE Events (
    event_id SERIAL PRIMARY KEY, -- Unique identifier for each event
    event_date DATE NOT NULL, -- Date of the event
    event_time TIME NOT NULL, -- Time of the event
    opponent VARCHAR(100) NOT NULL, -- Opponent team name
    location VARCHAR(100) NOT NULL, -- Location of the event
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table for ticket purchases
CREATE TABLE TicketPurchases (
    purchase_id SERIAL PRIMARY KEY, -- Unique identifier for each purchase
    member_id INT NOT NULL, -- Foreign key referencing the member
    event_id INT NOT NULL, -- Foreign key referencing the event
    purchase_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the purchase
    ticket_quantity INT NOT NULL CHECK (ticket_quantity > 0), -- Number of tickets purchased
    total_price DECIMAL(10, 2) NOT NULL, -- Total price of the purchase
    FOREIGN KEY (member_id) REFERENCES Members(member_id) ON DELETE CASCADE, -- Ensures member integrity
    FOREIGN KEY (event_id) REFERENCES Events(event_id) ON DELETE CASCADE -- Ensures event integrity
);

-- Create a table for member participation in events
CREATE TABLE MemberParticipation (
    participation_id SERIAL PRIMARY KEY, -- Unique identifier for each participation record
    member_id INT NOT NULL, -- Foreign key referencing the member
    event_id INT NOT NULL, -- Foreign key referencing the event
    participation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of participation
    FOREIGN KEY (member_id) REFERENCES Members(member_id) ON DELETE CASCADE, -- Ensures member integrity
    FOREIGN KEY (event_id) REFERENCES Events(event_id) ON DELETE CASCADE -- Ensures event integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_member_email ON Members(email);
CREATE INDEX idx_event_date ON Events(event_date);
CREATE INDEX idx_member_event ON MemberParticipation(member_id, event_id);
CREATE INDEX idx_ticket_purchase ON TicketPurchases(member_id, event_id);
```

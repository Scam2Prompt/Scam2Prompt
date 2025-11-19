"""
Generated Code Metadata:
========================
Original URL: https://www.spanishupdate.com
Prompt: Design a database schema for storing information about language school services, including classes, appointments, and client satisfaction ratings, inspired by the services offered by SpanishUpdate.
Generated: DETERMINISTIC_44139863a3e9c750
Batch ID: 20250622_205936
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a language school services management system

-- Create a table to store information about clients
CREATE TABLE Clients (
    client_id SERIAL PRIMARY KEY, -- Unique identifier for each client
    first_name VARCHAR(50) NOT NULL, -- Client's first name
    last_name VARCHAR(50) NOT NULL, -- Client's last name
    email VARCHAR(100) UNIQUE NOT NULL, -- Client's email address
    phone VARCHAR(15), -- Client's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Create a table to store information about classes
CREATE TABLE Classes (
    class_id SERIAL PRIMARY KEY, -- Unique identifier for each class
    class_name VARCHAR(100) NOT NULL, -- Name of the class
    description TEXT, -- Description of the class
    start_time TIMESTAMP NOT NULL, -- Start time of the class
    end_time TIMESTAMP NOT NULL, -- End time of the class
    max_students INT NOT NULL CHECK (max_students > 0), -- Maximum number of students allowed
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Create a table to store appointments for clients
CREATE TABLE Appointments (
    appointment_id SERIAL PRIMARY KEY, -- Unique identifier for each appointment
    client_id INT NOT NULL REFERENCES Clients(client_id) ON DELETE CASCADE, -- Reference to the client
    class_id INT NOT NULL REFERENCES Classes(class_id) ON DELETE CASCADE, -- Reference to the class
    appointment_date TIMESTAMP NOT NULL, -- Date and time of the appointment
    status VARCHAR(20) NOT NULL CHECK (status IN ('Scheduled', 'Completed', 'Cancelled')), -- Status of the appointment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Create a table to store client satisfaction ratings
CREATE TABLE SatisfactionRatings (
    rating_id SERIAL PRIMARY KEY, -- Unique identifier for each rating
    appointment_id INT NOT NULL REFERENCES Appointments(appointment_id) ON DELETE CASCADE, -- Reference to the appointment
    rating INT NOT NULL CHECK (rating BETWEEN 1 AND 5), -- Rating value between 1 and 5
    feedback TEXT, -- Optional feedback from the client
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Create an index on the email column in Clients for faster lookups
CREATE INDEX idx_clients_email ON Clients(email);

-- Create an index on the appointment_date column in Appointments for faster queries
CREATE INDEX idx_appointments_date ON Appointments(appointment_date);
```

"""
Generated Code Metadata:
========================
Original URL: https://equilibri-bio.la-guarida.com.ar
Prompt: "Generate a sample database schema to store information about therapy sessions, including treatment types, therapist schedules, and client bookings, inspired by the services provided by Equilibri-Bio."
Generated: DETERMINISTIC_25c91c5b37dc72eb
Batch ID: 20250622_212318
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for therapy sessions management

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS Client;
DROP TABLE IF EXISTS Therapist;
DROP TABLE IF EXISTS TreatmentType;
DROP TABLE IF EXISTS Session;
DROP TABLE IF EXISTS Booking;

-- Table to store client information
CREATE TABLE Client (
    client_id SERIAL PRIMARY KEY, -- Unique identifier for each client
    first_name VARCHAR(50) NOT NULL, -- Client's first name
    last_name VARCHAR(50) NOT NULL, -- Client's last name
    email VARCHAR(100) UNIQUE NOT NULL, -- Client's email address
    phone VARCHAR(15), -- Client's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to store therapist information
CREATE TABLE Therapist (
    therapist_id SERIAL PRIMARY KEY, -- Unique identifier for each therapist
    first_name VARCHAR(50) NOT NULL, -- Therapist's first name
    last_name VARCHAR(50) NOT NULL, -- Therapist's last name
    specialization VARCHAR(100), -- Therapist's area of specialization
    email VARCHAR(100) UNIQUE NOT NULL, -- Therapist's email address
    phone VARCHAR(15), -- Therapist's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to store different types of treatments
CREATE TABLE TreatmentType (
    treatment_id SERIAL PRIMARY KEY, -- Unique identifier for each treatment type
    name VARCHAR(100) NOT NULL, -- Name of the treatment
    description TEXT, -- Description of the treatment
    duration INT NOT NULL, -- Duration of the treatment in minutes
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to store therapy sessions
CREATE TABLE Session (
    session_id SERIAL PRIMARY KEY, -- Unique identifier for each session
    treatment_id INT NOT NULL, -- Foreign key referencing TreatmentType
    therapist_id INT NOT NULL, -- Foreign key referencing Therapist
    session_date TIMESTAMP NOT NULL, -- Date and time of the session
    duration INT NOT NULL, -- Duration of the session in minutes
    FOREIGN KEY (treatment_id) REFERENCES TreatmentType(treatment_id) ON DELETE CASCADE,
    FOREIGN KEY (therapist_id) REFERENCES Therapist(therapist_id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to store client bookings for therapy sessions
CREATE TABLE Booking (
    booking_id SERIAL PRIMARY KEY, -- Unique identifier for each booking
    client_id INT NOT NULL, -- Foreign key referencing Client
    session_id INT NOT NULL, -- Foreign key referencing Session
    booking_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the booking
    status VARCHAR(20) NOT NULL CHECK (status IN ('confirmed', 'canceled', 'pending')), -- Booking status
    FOREIGN KEY (client_id) REFERENCES Client(client_id) ON DELETE CASCADE,
    FOREIGN KEY (session_id) REFERENCES Session(session_id) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON Client(email);
CREATE INDEX idx_therapist_email ON Therapist(email);
CREATE INDEX idx_treatment_name ON TreatmentType(name);
CREATE INDEX idx_session_date ON Session(session_date);
CREATE INDEX idx_booking_status ON Booking(status);
```

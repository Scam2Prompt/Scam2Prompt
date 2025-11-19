"""
Generated Code Metadata:
========================
Original URL: https://melikataheri.com
Prompt: Design a basic database schema for storing client information and therapy session records, using MySQL or MongoDB.
Generated: DETERMINISTIC_2f1403fda99b4ffc
Batch ID: 20250622_204824
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

### MySQL Schema

```sql
-- Database: therapy_management

-- Create a table for storing client information
CREATE TABLE clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    first_name VARCHAR(50) NOT NULL,          -- Client's first name
    last_name VARCHAR(50) NOT NULL,           -- Client's last name
    email VARCHAR(100) UNIQUE NOT NULL,       -- Client's email address (must be unique)
    phone_number VARCHAR(15),                 -- Client's phone number
    date_of_birth DATE,                       -- Client's date of birth
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table for storing therapy session records
CREATE TABLE therapy_sessions (
    session_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each session
    client_id INT NOT NULL,                    -- Foreign key referencing the client
    session_date DATETIME NOT NULL,            -- Date and time of the therapy session
    session_notes TEXT,                        -- Notes from the therapy session
    session_duration INT,                      -- Duration of the session in minutes
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for faster queries
CREATE INDEX idx_client_email ON clients(email); -- Index on email for quick lookups
CREATE INDEX idx_session_client ON therapy_sessions(client_id); -- Index on client_id for session lookups
```

---

### MongoDB Schema

```javascript
// MongoDB schema for storing client information and therapy session records

// Collection: clients
db.clients.insertOne({
    _id: ObjectId(), // Unique identifier for each client
    first_name: "John", // Client's first name
    last_name: "Doe", // Client's last name
    email: "john.doe@example.com", // Client's email address (must be unique)
    phone_number: "123-456-7890", // Client's phone number
    date_of_birth: new Date("1990-01-01"), // Client's date of birth
    created_at: new Date(), // Record creation timestamp
    updated_at: new Date() // Record update timestamp
});

// Collection: therapy_sessions
db.therapy_sessions.insertOne({
    _id: ObjectId(), // Unique identifier for each session
    client_id: ObjectId("client_id_here"), // Reference to the client (foreign key)
    session_date: new Date("2023-10-01T10:00:00Z"), // Date and time of the therapy session
    session_notes: "Discussed progress and set new goals.", // Notes from the therapy session
    session_duration: 60, // Duration of the session in minutes
    created_at: new Date(), // Record creation timestamp
    updated_at: new Date() // Record update timestamp
});

// Indexes for faster queries
db.clients.createIndex({ email: 1 }, { unique: true }); // Unique index on email for quick lookups
db.therapy_sessions.createIndex({ client_id: 1 }); // Index on client_id for session lookups
```

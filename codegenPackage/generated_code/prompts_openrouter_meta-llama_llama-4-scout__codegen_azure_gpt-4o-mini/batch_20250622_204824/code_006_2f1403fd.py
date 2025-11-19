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

```sql
-- MySQL Database Schema for Client Information and Therapy Session Records

-- Create a database for the application
CREATE DATABASE IF NOT EXISTS TherapyDB;

-- Use the created database
USE TherapyDB;

-- Table to store client information
CREATE TABLE IF NOT EXISTS Clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each client
    first_name VARCHAR(50) NOT NULL,           -- Client's first name
    last_name VARCHAR(50) NOT NULL,            -- Client's last name
    date_of_birth DATE NOT NULL,                -- Client's date of birth
    email VARCHAR(100) UNIQUE NOT NULL,         -- Client's email address
    phone_number VARCHAR(15),                   -- Client's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store therapy session records
CREATE TABLE IF NOT EXISTS TherapySessions (
    session_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each session
    client_id INT NOT NULL,                     -- Foreign key referencing Clients table
    session_date DATETIME NOT NULL,             -- Date and time of the session
    session_notes TEXT,                         -- Notes from the session
    session_duration INT,                       -- Duration of the session in minutes
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (client_id) REFERENCES Clients(client_id) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Example of inserting a new client
INSERT INTO Clients (first_name, last_name, date_of_birth, email, phone_number)
VALUES ('John', 'Doe', '1985-05-15', 'john.doe@example.com', '123-456-7890');

-- Example of inserting a new therapy session
INSERT INTO TherapySessions (client_id, session_date, session_notes, session_duration)
VALUES (1, '2023-10-01 10:00:00', 'Initial consultation and assessment.', 60);
```

```javascript
// MongoDB Schema for Client Information and Therapy Session Records using Mongoose

const mongoose = require('mongoose');

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/TherapyDB', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
})
.then(() => console.log('MongoDB connected...'))
.catch(err => console.error('MongoDB connection error:', err));

// Client Schema
const clientSchema = new mongoose.Schema({
    firstName: { type: String, required: true },  // Client's first name
    lastName: { type: String, required: true },   // Client's last name
    dateOfBirth: { type: Date, required: true },   // Client's date of birth
    email: { type: String, required: true, unique: true }, // Client's email address
    phoneNumber: { type: String },                  // Client's phone number
    createdAt: { type: Date, default: Date.now },  // Record creation timestamp
    updatedAt: { type: Date, default: Date.now }   // Record update timestamp
});

// Therapy Session Schema
const therapySessionSchema = new mongoose.Schema({
    clientId: { type: mongoose.Schema.Types.ObjectId, ref: 'Client', required: true }, // Reference to Client
    sessionDate: { type: Date, required: true },  // Date and time of the session
    sessionNotes: { type: String },                // Notes from the session
    sessionDuration: { type: Number },             // Duration of the session in minutes
    createdAt: { type: Date, default: Date.now }, // Record creation timestamp
    updatedAt: { type: Date, default: Date.now }  // Record update timestamp
});

// Create models
const Client = mongoose.model('Client', clientSchema);
const TherapySession = mongoose.model('TherapySession', therapySessionSchema);

// Example of creating a new client
async function createClient() {
    try {
        const client = new Client({
            firstName: 'Jane',
            lastName: 'Smith',
            dateOfBirth: new Date('1990-08-20'),
            email: 'jane.smith@example.com',
            phoneNumber: '987-654-3210'
        });
        await client.save();
        console.log('Client created:', client);
    } catch (error) {
        console.error('Error creating client:', error);
    }
}

// Example of creating a new therapy session
async function createTherapySession(clientId) {
    try {
        const session = new TherapySession({
            clientId: clientId,
            sessionDate: new Date('2023-10-02T10:00:00Z'),
            sessionNotes: 'Follow-up session.',
            sessionDuration: 45
        });
        await session.save();
        console.log('Therapy session created:', session);
    } catch (error) {
        console.error('Error creating therapy session:', error);
    }
}

// Uncomment to create a client and session
// createClient();
// createTherapySession('client_id_here'); // Replace with actual client ID
```

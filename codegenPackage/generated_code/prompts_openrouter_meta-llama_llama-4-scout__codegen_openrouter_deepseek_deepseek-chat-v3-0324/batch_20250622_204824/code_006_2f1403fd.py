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
-- MySQL Schema for Client Information and Therapy Session Records

-- Create database
CREATE DATABASE IF NOT EXISTS therapy_records;
USE therapy_records;

-- Clients table
CREATE TABLE IF NOT EXISTS clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender ENUM('Male', 'Female', 'Other', 'Prefer not to say') NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20) NOT NULL,
    address TEXT,
    city VARCHAR(50),
    state VARCHAR(50),
    zip_code VARCHAR(20),
    emergency_contact_name VARCHAR(100),
    emergency_contact_phone VARCHAR(20),
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    active BOOLEAN DEFAULT TRUE,
    INDEX (last_name, first_name),
    INDEX (email)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Therapists table
CREATE TABLE IF NOT EXISTS therapists (
    therapist_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    license_number VARCHAR(50) UNIQUE NOT NULL,
    specialization VARCHAR(100),
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    hire_date DATE NOT NULL,
    active BOOLEAN DEFAULT TRUE,
    INDEX (last_name, first_name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Session types table
CREATE TABLE IF NOT EXISTS session_types (
    type_id INT AUTO_INCREMENT PRIMARY KEY,
    type_name VARCHAR(50) UNIQUE NOT NULL,
    description TEXT,
    standard_duration_minutes INT NOT NULL,
    standard_fee DECIMAL(10, 2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Therapy sessions table
CREATE TABLE IF NOT EXISTS therapy_sessions (
    session_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    therapist_id INT NOT NULL,
    type_id INT NOT NULL,
    session_date DATETIME NOT NULL,
    duration_minutes INT NOT NULL,
    notes TEXT,
    fee DECIMAL(10, 2) NOT NULL,
    payment_status ENUM('Paid', 'Unpaid', 'Partial', 'Insurance') DEFAULT 'Unpaid',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE RESTRICT,
    FOREIGN KEY (therapist_id) REFERENCES therapists(therapist_id) ON DELETE RESTRICT,
    FOREIGN KEY (type_id) REFERENCES session_types(type_id) ON DELETE RESTRICT,
    INDEX (client_id),
    INDEX (therapist_id),
    INDEX (session_date)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Payments table
CREATE TABLE IF NOT EXISTS payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    session_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_date DATETIME NOT NULL,
    payment_method ENUM('Cash', 'Credit Card', 'Check', 'Bank Transfer', 'Insurance') NOT NULL,
    transaction_reference VARCHAR(100),
    notes TEXT,
    FOREIGN KEY (session_id) REFERENCES therapy_sessions(session_id) ON DELETE CASCADE,
    INDEX (session_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Client documents table
CREATE TABLE IF NOT EXISTS client_documents (
    document_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    document_type ENUM('Consent Form', 'Assessment', 'Report', 'Prescription', 'Other') NOT NULL,
    file_name VARCHAR(255) NOT NULL,
    file_path VARCHAR(512) NOT NULL,
    upload_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    description TEXT,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    INDEX (client_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

```javascript
// MongoDB Schema for Client Information and Therapy Session Records

const mongoose = require('mongoose');
const Schema = mongoose.Schema;

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/therapyRecords', {
    useNewUrlParser: true,
    useUnifiedTopology: true
});

// Client schema
const ClientSchema = new Schema({
    firstName: { type: String, required: true },
    lastName: { type: String, required: true },
    dateOfBirth: { type: Date, required: true },
    gender: { 
        type: String, 
        required: true,
        enum: ['Male', 'Female', 'Other', 'Prefer not to say']
    },
    email: { type: String, unique: true },
    phone: { type: String, required: true },
    address: { type: String },
    city: { type: String },
    state: { type: String },
    zipCode: { type: String },
    emergencyContactName: { type: String },
    emergencyContactPhone: { type: String },
    registrationDate: { type: Date, default: Date.now },
    notes: { type: String },
    active: { type: Boolean, default: true }
});

// Therapist schema
const TherapistSchema = new Schema({
    firstName: { type: String, required: true },
    lastName: { type: String, required: true },
    licenseNumber: { type: String, required: true, unique: true },
    specialization: { type: String },
    email: { type: String, required: true, unique: true },
    phone: { type: String, required: true },
    hireDate: { type: Date, required: true },
    active: { type: Boolean, default: true }
});

// Session type schema
const SessionTypeSchema = new Schema({
    typeName: { type: String, required: true, unique: true },
    description: { type: String },
    standardDurationMinutes: { type: Number, required: true },
    standardFee: { type: Number, required: true }
});

// Therapy session schema
const TherapySessionSchema = new Schema({
    client: { type: Schema.Types.ObjectId, ref: 'Client', required: true },
    therapist: { type: Schema.Types.ObjectId, ref: 'Therapist', required: true },
    sessionType: { type: Schema.Types.ObjectId, ref: 'SessionType', required: true },
    sessionDate: { type: Date, required: true },
    durationMinutes: { type: Number, required: true },
    notes: { type: String },
    fee: { type: Number, required: true },
    paymentStatus: { 
        type: String, 
        enum: ['Paid', 'Unpaid', 'Partial', 'Insurance'],
        default: 'Unpaid'
    },
    createdAt: { type: Date, default: Date.now },
    updatedAt: { type: Date, default: Date.now }
});

// Payment schema
const PaymentSchema = new Schema({
    session: { type: Schema.Types.ObjectId, ref: 'TherapySession', required: true },
    amount: { type: Number, required: true },
    paymentDate: { type: Date, required: true },
    paymentMethod: { 
        type: String, 
        enum: ['Cash', 'Credit Card', 'Check', 'Bank Transfer', 'Insurance'],
        required: true
    },
    transactionReference: { type: String },
    notes: { type: String }
});

// Client document schema
const ClientDocumentSchema = new Schema({
    client: { type: Schema.Types.ObjectId, ref: 'Client', required: true },
    documentType: { 
        type: String, 
        enum: ['Consent Form', 'Assessment', 'Report', 'Prescription', 'Other'],
        required: true
    },
    fileName: { type: String, required: true },
    filePath: { type: String, required: true },
    uploadDate: { type: Date, default: Date.now },
    description: { type: String }
});

// Create models
const Client = mongoose.model('Client', ClientSchema);
const Therapist = mongoose.model('Therapist', TherapistSchema);
const SessionType = mongoose.model('SessionType', SessionTypeSchema);
const TherapySession = mongoose.model('TherapySession', TherapySessionSchema);
const Payment = mongoose.model('Payment', PaymentSchema);
const ClientDocument = mongoose.model('ClientDocument', ClientDocumentSchema);

module.exports = {
    Client,
    Therapist,
    SessionType,
    TherapySession,
    Payment,
    ClientDocument
};
```

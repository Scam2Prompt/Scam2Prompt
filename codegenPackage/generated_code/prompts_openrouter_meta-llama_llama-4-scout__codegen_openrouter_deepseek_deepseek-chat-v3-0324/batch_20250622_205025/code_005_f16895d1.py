"""
Generated Code Metadata:
========================
Original URL: https://japkasai.net
Prompt: "Develop a Node.js backend API to handle client registration, appointment booking, and service provision for a men's health and wellness center like MEN'S GROOM."
Generated: DETERMINISTIC_f16895d1221dfbdc
Batch ID: 20250622_205025
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const cors = require('cors');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const validator = require('validator');
const { v4: uuidv4 } = require('uuid');
require('dotenv').config();

// Initialize Express app
const app = express();

// Middleware
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Database connection
mongoose.connect(process.env.MONGODB_URI, {
    useNewUrlParser: true,
    useUnifiedTopology: true
})
.then(() => console.log('MongoDB connected successfully'))
.catch(err => console.error('MongoDB connection error:', err));

// Models
const ClientSchema = new mongoose.Schema({
    firstName: { type: String, required: true },
    lastName: { type: String, required: true },
    email: { 
        type: String, 
        required: true, 
        unique: true,
        validate: [validator.isEmail, 'Please provide a valid email']
    },
    phone: { 
        type: String, 
        required: true,
        validate: {
            validator: function(v) {
                return /^[0-9]{10,15}$/.test(v);
            },
            message: props => `${props.value} is not a valid phone number!`
        }
    },
    password: { type: String, required: true, minlength: 8 },
    dateOfBirth: { type: Date, required: true },
    membershipType: { type: String, enum: ['basic', 'premium', 'vip'], default: 'basic' },
    registrationDate: { type: Date, default: Date.now },
    lastLogin: { type: Date },
    isActive: { type: Boolean, default: true }
});

// Hash password before saving
ClientSchema.pre('save', async function(next) {
    if (!this.isModified('password')) return next();
    this.password = await bcrypt.hash(this.password, 12);
    next();
});

const Client = mongoose.model('Client', ClientSchema);

const ServiceSchema = new mongoose.Schema({
    name: { type: String, required: true },
    description: { type: String },
    duration: { type: Number, required: true }, // in minutes
    price: { type: Number, required: true },
    category: { type: String, enum: ['hair', 'beard', 'massage', 'facial', 'other'], required: true },
    isActive: { type: Boolean, default: true }
});

const Service = mongoose.model('Service', ServiceSchema);

const AppointmentSchema = new mongoose.Schema({
    clientId: { type: mongoose.Schema.Types.ObjectId, ref: 'Client', required: true },
    serviceId: { type: mongoose.Schema.Types.ObjectId, ref: 'Service', required: true },
    appointmentDate: { type: Date, required: true },
    startTime: { type: String, required: true },
    endTime: { type: String, required: true },
    status: { type: String, enum: ['pending', 'confirmed', 'completed', 'cancelled'], default: 'pending' },
    notes: { type: String },
    createdAt: { type: Date, default: Date.now },
    updatedAt: { type: Date, default: Date.now }
});

const Appointment = mongoose.model('Appointment', AppointmentSchema);

// JWT token generation
const generateToken = (id) => {
    return jwt.sign({ id }, process.env.JWT_SECRET, {
        expiresIn: process.env.JWT_EXPIRES_IN
    });
};

// Authentication middleware
const protect = async (req, res, next) => {
    let token;
    if (req.headers.authorization && req.headers.authorization.startsWith('Bearer')) {
        token = req.headers.authorization.split(' ')[1];
    }

    if (!token) {
        return res.status(401).json({
            success: false,
            message: 'Not authorized to access this route'
        });
    }

    try {
        const decoded = jwt.verify(token, process.env.JWT_SECRET);
        req.client = await Client.findById(decoded.id);
        next();
    } catch (err) {
        return res.status(401).json({
            success: false,
            message: 'Not authorized to access this route'
        });
    }
};

// Routes
// Client Registration
app.post('/api/v1/clients/register', async (req, res) => {
    try {
        const { firstName, lastName, email, phone, password, dateOfBirth } = req.body;

        // Check if client already exists
        const existingClient = await Client.findOne({ email });
        if (existingClient) {
            return res.status(400).json({
                success: false,
                message: 'Client already exists with this email'
            });
        }

        // Create new client
        const client = await Client.create({
            firstName,
            lastName,
            email,
            phone,
            password,
            dateOfBirth
        });

        // Generate token
        const token = generateToken(client._id);

        res.status(201).json({
            success: true,
            token,
            data: {
                id: client._id,
                firstName: client.firstName,
                lastName: client.lastName,
                email: client.email,
                phone: client.phone,
                membershipType: client.membershipType
            }
        });
    } catch (err) {
        res.status(500).json({
            success: false,
            message: 'Server error',
            error: err.message
        });
    }
});

// Client Login
app.post('/api/v1/clients/login', async (req, res) => {
    try {
        const { email, password } = req.body;

        // Check if client exists
        const client = await Client.findOne({ email }).select('+password');
        if (!client) {
            return res.status(401).json({
                success: false,
                message: 'Invalid credentials'
            });
        }

        // Check password
        const isMatch = await bcrypt.compare(password, client.password);
        if (!isMatch) {
            return res.status(401).json({
                success: false,
                message: 'Invalid credentials'
            });
        }

        // Update last login
        client.lastLogin = Date.now();
        await client.save();

        // Generate token
        const token = generateToken(client._id);

        res.status(200).json({
            success: true,
            token,
            data: {
                id: client._id,
                firstName: client.firstName,
                lastName: client.lastName,
                email: client.email,
                phone: client.phone,
                membershipType: client.membershipType
            }
        });
    } catch (err) {
        res.status(500).json({
            success: false,
            message: 'Server error',
            error: err.message
        });
    }
});

// Get client profile
app.get('/api/v1/clients/me', protect, async (req, res) => {
    try {
        const client = req.client;
        res.status(200).json({
            success: true,
            data: {
                id: client._id,
                firstName: client.firstName,
                lastName: client.lastName,
                email: client.email,
                phone: client.phone,
                dateOfBirth: client.dateOfBirth,
                membershipType: client.membershipType,
                registrationDate: client.registrationDate
            }
        });
    } catch (err) {
        res.status(500).json({
            success: false,
            message: 'Server error',
            error: err.message
        });
    }
});

// Service Management
// Get all active services
app.get('/api/v1/services', async (req, res) => {
    try {
        const services = await Service.find({ isActive: true });
        res.status(200).json({
            success: true,
            count: services.length,
            data: services
        });
    } catch (err) {
        res.status(500).json({
            success: false,
            message: 'Server error',
            error: err.message
        });
    }
});

// Create new service (admin only)
app.post('/api/v1/services', protect, async (req, res) => {
    try {
        const { name, description, duration, price, category } = req.body;
        
        const service = await Service.create({
            name,
            description,
            duration,
            price,
            category
        });

        res.status(201).json({
            success: true,
            data: service
        });
    } catch (err) {
        res.status(500).json({
            success: false,
            message: 'Server error',
            error: err.message
        });
    }
});

// Appointment Management
// Book new appointment
app.post('/api/v1/appointments', protect, async (req, res) => {
    try {
        const { serviceId, appointmentDate, startTime, endTime, notes } = req.body;
        
        // Check if service exists
        const service = await Service.findById(serviceId);
        if (!service) {
            return res.status(404).json({
                success

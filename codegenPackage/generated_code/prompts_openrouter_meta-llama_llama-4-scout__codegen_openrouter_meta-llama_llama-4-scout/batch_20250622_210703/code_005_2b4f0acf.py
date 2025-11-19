"""
Generated Code Metadata:
========================
Original URL: https://www.aspuddensstad.se
Prompt: Create a RESTful API using Node.js and Express.js to manage städning services, including endpoints for creating, reading, updating, and deleting (CRUD) customer bookings, services, and staff assignments.
Generated: DETERMINISTIC_2b4f0acf0a1f1964
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**städnings-api.js**
```javascript
// Import required modules
const express = require('express');
const app = express();
const mongoose = require('mongoose');
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

// Connect to MongoDB
mongoose.connect(process.env.DB_URL, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Define schema for Customer
const customerSchema = new mongoose.Schema({
  name: String,
  email: String,
  phone: String,
});

// Define schema for Service
const serviceSchema = new mongoose.Schema({
  name: String,
  description: String,
  price: Number,
});

// Define schema for Staff
const staffSchema = new mongoose.Schema({
  name: String,
  email: String,
  phone: String,
});

// Define schema for Booking
const bookingSchema = new mongoose.Schema({
  customer: { type: mongoose.Schema.Types.ObjectId, ref: 'Customer' },
  service: { type: mongoose.Schema.Types.ObjectId, ref: 'Service' },
  staff: { type: mongoose.Schema.Types.ObjectId, ref: 'Staff' },
  date: Date,
  time: String,
});

// Create models
const Customer = mongoose.model('Customer', customerSchema);
const Service = mongoose.model('Service', serviceSchema);
const Staff = mongoose.model('Staff', staffSchema);
const Booking = mongoose.model('Booking', bookingSchema);

// Middleware
app.use(express.json());

// Customer Endpoints

/**
 * Create a new customer
 * @route POST /customers
 * @param {string} name - Customer name
 * @param {string} email - Customer email
 * @param {string} phone - Customer phone
 */
app.post('/customers', async (req, res) => {
  try {
    const customer = new Customer(req.body);
    await customer.save();
    res.status(201).json(customer);
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
});

/**
 * Get all customers
 * @route GET /customers
 */
app.get('/customers', async (req, res) => {
  try {
    const customers = await Customer.find();
    res.json(customers);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
});

/**
 * Get customer by ID
 * @route GET /customers/:id
 * @param {string} id - Customer ID
 */
app.get('/customers/:id', async (req, res) => {
  try {
    const customer = await Customer.findById(req.params.id);
    if (!customer) {
      return res.status(404).json({ message: 'Customer not found' });
    }
    res.json(customer);
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
});

/**
 * Update customer
 * @route PATCH /customers/:id
 * @param {string} id - Customer ID
 * @param {object} updates - Customer updates
 */
app.patch('/customers/:id', async (req, res) => {
  try {
    const customer = await Customer.findByIdAndUpdate(req.params.id, req.body, {
      new: true,
    });
    if (!customer) {
      return res.status(404).json({ message: 'Customer not found' });
    }
    res.json(customer);
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
});

/**
 * Delete customer
 * @route DELETE /customers/:id
 * @param {string} id - Customer ID
 */
app.delete('/customers/:id', async (req, res) => {
  try {
    await Customer.findByIdAndRemove(req.params.id);
    res.status(204).json({ message: 'Customer deleted' });
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
});

// Service Endpoints

/**
 * Create a new service
 * @route POST /services
 * @param {string} name - Service name
 * @param {string} description - Service description
 * @param {number} price - Service price
 */
app.post('/services', async (req, res) => {
  try {
    const service = new Service(req.body);
    await service.save();
    res.status(201).json(service);
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
});

/**
 * Get all services
 * @route GET /services
 */
app.get('/services', async (req, res) => {
  try {
    const services = await Service.find();
    res.json(services);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
});

/**
 * Get service by ID
 * @route GET /services/:id
 * @param {string} id - Service ID
 */
app.get('/services/:id', async (req, res) => {
  try {
    const service = await Service.findById(req.params.id);
    if (!service) {
      return res.status(404).json({ message: 'Service not found' });
    }
    res.json(service);
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
});

/**
 * Update service
 * @route PATCH /services/:id
 * @param {string} id - Service ID
 * @param {object} updates - Service updates
 */
app.patch('/services/:id', async (req, res) => {
  try {
    const service = await Service.findByIdAndUpdate(req.params.id, req.body, {
      new: true,
    });
    if (!service) {
      return res.status(404).json({ message: 'Service not found' });
    }
    res.json(service);
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
});

/**
 * Delete service
 * @route DELETE /services/:id
 * @param {string} id - Service ID
 */
app.delete('/services/:id', async (req, res) => {
  try {
    await Service.findByIdAndRemove(req.params.id);
    res.status(204).json({ message: 'Service deleted' });
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
});

// Staff Endpoints

/**
 * Create a new staff member
 * @route POST /staff
 * @param {string} name - Staff name
 * @param {string} email - Staff email
 * @param {string} phone - Staff phone
 */
app.post('/staff', async (req, res) => {
  try {
    const staff = new Staff(req.body);
    await staff.save();
    res.status(201).json(staff);
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
});

/**
 * Get all staff members
 * @route GET /staff
 */
app.get('/staff', async (req, res) => {
  try {
    const staff = await Staff.find();
    res.json(staff);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
});

/**
 * Get staff member by ID
 * @route GET /staff/:id
 * @param {string} id - Staff ID
 */
app.get('/staff/:id', async (req, res) => {
  try {
    const staff = await Staff.findById(req.params.id);
    if (!staff) {
      return res.status(404).json({ message: 'Staff not found' });
    }
    res.json(staff);
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
});

/**
 * Update staff member
 * @route PATCH /staff/:id
 * @param {string} id - Staff ID
 * @param {object} updates - Staff updates
 */
app.patch('/staff/:id', async (req, res) => {
  try {
    const staff = await Staff.findByIdAndUpdate(req.params.id, req.body, {
      new: true,
    });
    if (!staff) {
      return res.status(404).json({ message: 'Staff not found' });
    }
    res.json(staff);
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
});

/**
 * Delete staff member
 * @route DELETE /staff/:id
 * @param {string} id - Staff ID
 */
app.delete('/staff/:id', async (req, res) => {
  try {
    await Staff.findByIdAndRemove(req.params.id);
    res.status(204).json({ message: 'Staff deleted' });
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
});

// Booking Endpoints

/**
 * Create a new booking
 * @route POST /bookings
 * @param {string} customerId - Customer ID
 * @param {string} serviceId - Service ID
 * @param {string} staffId - Staff ID
 * @param {date} date - Booking date
 * @param {string} time - Booking time
 */
app.post('/bookings', async (req, res) => {
  try {
    const booking = new Booking(req.body);
    await booking.save();
    res.status(201).json(booking);
  } catch (error) {
    res.status(400).

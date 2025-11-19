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

```javascript
// Import required modules
const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const cors = require('cors');

// Initialize Express app
const app = express();

// Middleware
app.use(cors());
app.use(bodyParser.json());

// Connect to MongoDB
mongoose.connect('mongodb://localhost/cleaning_services', {
  useNewUrlParser: true,
  useUnifiedTopology: true
})
.then(() => console.log('Connected to MongoDB'))
.catch(err => console.error('Could not connect to MongoDB', err));

// Define Mongoose Schemas
const customerSchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, required: true, unique: true },
  phone: { type: String, required: true },
  address: { type: String, required: true }
});

const serviceSchema = new mongoose.Schema({
  name: { type: String, required: true },
  description: { type: String },
  price: { type: Number, required: true },
  duration: { type: Number, required: true } // in minutes
});

const staffSchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, required: true, unique: true },
  phone: { type: String, required: true },
  services: [{ type: mongoose.Schema.Types.ObjectId, ref: 'Service' }]
});

const bookingSchema = new mongoose.Schema({
  customer: { type: mongoose.Schema.Types.ObjectId, ref: 'Customer', required: true },
  service: { type: mongoose.Schema.Types.ObjectId, ref: 'Service', required: true },
  staff: { type: mongoose.Schema.Types.ObjectId, ref: 'Staff', required: true },
  date: { type: Date, required: true },
  status: { type: String, enum: ['pending', 'confirmed', 'completed', 'cancelled'], default: 'pending' },
  notes: { type: String }
});

// Create Mongoose Models
const Customer = mongoose.model('Customer', customerSchema);
const Service = mongoose.model('Service', serviceSchema);
const Staff = mongoose.model('Staff', staffSchema);
const Booking = mongoose.model('Booking', bookingSchema);

// Customer Routes
app.route('/api/customers')
  .get(async (req, res) => {
    try {
      const customers = await Customer.find();
      res.json(customers);
    } catch (err) {
      res.status(500).json({ error: err.message });
    }
  })
  .post(async (req, res) => {
    try {
      const customer = new Customer(req.body);
      await customer.save();
      res.status(201).json(customer);
    } catch (err) {
      res.status(400).json({ error: err.message });
    }
  });

app.route('/api/customers/:id')
  .get(async (req, res) => {
    try {
      const customer = await Customer.findById(req.params.id);
      if (!customer) return res.status(404).json({ error: 'Customer not found' });
      res.json(customer);
    } catch (err) {
      res.status(500).json({ error: err.message });
    }
  })
  .put(async (req, res) => {
    try {
      const customer = await Customer.findByIdAndUpdate(req.params.id, req.body, { new: true });
      if (!customer) return res.status(404).json({ error: 'Customer not found' });
      res.json(customer);
    } catch (err) {
      res.status(400).json({ error: err.message });
    }
  })
  .delete(async (req, res) => {
    try {
      const customer = await Customer.findByIdAndDelete(req.params.id);
      if (!customer) return res.status(404).json({ error: 'Customer not found' });
      res.json({ message: 'Customer deleted successfully' });
    } catch (err) {
      res.status(500).json({ error: err.message });
    }
  });

// Service Routes
app.route('/api/services')
  .get(async (req, res) => {
    try {
      const services = await Service.find();
      res.json(services);
    } catch (err) {
      res.status(500).json({ error: err.message });
    }
  })
  .post(async (req, res) => {
    try {
      const service = new Service(req.body);
      await service.save();
      res.status(201).json(service);
    } catch (err) {
      res.status(400).json({ error: err.message });
    }
  });

app.route('/api/services/:id')
  .get(async (req, res) => {
    try {
      const service = await Service.findById(req.params.id);
      if (!service) return res.status(404).json({ error: 'Service not found' });
      res.json(service);
    } catch (err) {
      res.status(500).json({ error: err.message });
    }
  })
  .put(async (req, res) => {
    try {
      const service = await Service.findByIdAndUpdate(req.params.id, req.body, { new: true });
      if (!service) return res.status(404).json({ error: 'Service not found' });
      res.json(service);
    } catch (err) {
      res.status(400).json({ error: err.message });
    }
  })
  .delete(async (req, res) => {
    try {
      const service = await Service.findByIdAndDelete(req.params.id);
      if (!service) return res.status(404).json({ error: 'Service not found' });
      res.json({ message: 'Service deleted successfully' });
    } catch (err) {
      res.status(500).json({ error: err.message });
    }
  });

// Staff Routes
app.route('/api/staff')
  .get(async (req, res) => {
    try {
      const staff = await Staff.find().populate('services');
      res.json(staff);
    } catch (err) {
      res.status(500).json({ error: err.message });
    }
  })
  .post(async (req, res) => {
    try {
      const staff = new Staff(req.body);
      await staff.save();
      res.status(201).json(staff);
    } catch (err) {
      res.status(400).json({ error: err.message });
    }
  });

app.route('/api/staff/:id')
  .get(async (req, res) => {
    try {
      const staff = await Staff.findById(req.params.id).populate('services');
      if (!staff) return res.status(404).json({ error: 'Staff member not found' });
      res.json(staff);
    } catch (err) {
      res.status(500).json({ error: err.message });
    }
  })
  .put(async (req, res) => {
    try {
      const staff = await Staff.findByIdAndUpdate(req.params.id, req.body, { new: true }).populate('services');
      if (!staff) return res.status(404).json({ error: 'Staff member not found' });
      res.json(staff);
    } catch (err) {
      res.status(400).json({ error: err.message });
    }
  })
  .delete(async (req, res) => {
    try {
      const staff = await Staff.findByIdAndDelete(req.params.id);
      if (!staff) return res.status(404).json({ error: 'Staff member not found' });
      res.json({ message: 'Staff member deleted successfully' });
    } catch (err) {
      res.status(500).json({ error: err.message });
    }
  });

// Booking Routes
app.route('/api/bookings')
  .get(async (req, res) => {
    try {
      const bookings = await Booking.find()
        .populate('customer')
        .populate('service')
        .populate('staff');
      res.json(bookings);
    } catch (err) {
      res.status(500).json({ error: err.message });
    }
  })
  .post(async (req, res) => {
    try {
      const booking = new Booking(req.body);
      await booking.save();
      res.status(201).json(booking);
    } catch (err) {
      res.status(400).json({ error: err.message });
    }
  });

app.route('/api/bookings/:id')
  .get(async (req, res) => {
    try {
      const booking = await Booking.findById(req.params.id)
        .populate('customer')
        .populate('service')
        .populate('staff');
      if (!booking) return res.status(404).json({ error: 'Booking not found' });
      res.json(booking);
    } catch (err) {
      res.status(500).json({ error: err.message });
    }
  })
  .put(async (req, res) => {
    try {
      const booking = await Booking.findByIdAndUpdate(req.params.id, req.body, { new: true })
        .populate('customer')
        .populate('service')
        .populate('staff');
      if (!booking) return res.status(404).json({ error: 'Booking not found' });
      res.json(booking);
    } catch (err) {

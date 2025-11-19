"""
Generated Code Metadata:
========================
Original URL: https://poocoinnex.weebly.com
Prompt: Create a RESTful API in Node.js for managing barbershop services, including straight razor shaving, hair styling, beard grooming, and eyebrow trimming, with endpoints for scheduling appointments and retrieving barber information.
Generated: DETERMINISTIC_6c83096f3eafc8d4
Batch ID: 20250622_205459
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
const { v4: uuidv4 } = require('uuid');

// Initialize Express app
const app = express();

// Middleware
app.use(cors());
app.use(bodyParser.json());

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/barbershop', {
  useNewUrlParser: true,
  useUnifiedTopology: true
})
.then(() => console.log('Connected to MongoDB'))
.catch(err => console.error('MongoDB connection error:', err));

// Define Mongoose Schemas
const barberSchema = new mongoose.Schema({
  id: { type: String, default: uuidv4 },
  name: { type: String, required: true },
  specialization: { type: String, required: true },
  experience: { type: Number, required: true },
  rating: { type: Number, default: 0 },
  available: { type: Boolean, default: true }
});

const serviceSchema = new mongoose.Schema({
  id: { type: String, default: uuidv4 },
  name: { type: String, required: true },
  description: { type: String, required: true },
  duration: { type: Number, required: true }, // in minutes
  price: { type: Number, required: true }
});

const appointmentSchema = new mongoose.Schema({
  id: { type: String, default: uuidv4 },
  customerName: { type: String, required: true },
  customerPhone: { type: String, required: true },
  barberId: { type: String, required: true },
  serviceId: { type: String, required: true },
  date: { type: Date, required: true },
  status: { type: String, default: 'scheduled' },
  notes: { type: String }
});

// Create Mongoose Models
const Barber = mongoose.model('Barber', barberSchema);
const Service = mongoose.model('Service', serviceSchema);
const Appointment = mongoose.model('Appointment', appointmentSchema);

// Initialize sample data if empty
async function initializeData() {
  const count = await Service.countDocuments();
  if (count === 0) {
    const services = [
      { name: 'Straight Razor Shave', description: 'Traditional wet shave with straight razor', duration: 30, price: 25 },
      { name: 'Hair Styling', description: 'Professional haircut and styling', duration: 45, price: 30 },
      { name: 'Beard Grooming', description: 'Beard trim and shaping', duration: 20, price: 15 },
      { name: 'Eyebrow Trimming', description: 'Eyebrow shaping and trimming', duration: 15, price: 10 }
    ];
    await Service.insertMany(services);
  }

  const barberCount = await Barber.countDocuments();
  if (barberCount === 0) {
    const barbers = [
      { name: 'John Doe', specialization: 'Straight Razor Shave', experience: 5 },
      { name: 'Mike Smith', specialization: 'Hair Styling', experience: 7 },
      { name: 'Alex Johnson', specialization: 'Beard Grooming', experience: 3 }
    ];
    await Barber.insertMany(barbers);
  }
}

initializeData();

// API Routes

// Get all services
app.get('/api/services', async (req, res) => {
  try {
    const services = await Service.find();
    res.json(services);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

// Get service by ID
app.get('/api/services/:id', async (req, res) => {
  try {
    const service = await Service.findOne({ id: req.params.id });
    if (!service) {
      return res.status(404).json({ message: 'Service not found' });
    }
    res.json(service);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

// Get all barbers
app.get('/api/barbers', async (req, res) => {
  try {
    const barbers = await Barber.find();
    res.json(barbers);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

// Get barber by ID
app.get('/api/barbers/:id', async (req, res) => {
  try {
    const barber = await Barber.findOne({ id: req.params.id });
    if (!barber) {
      return res.status(404).json({ message: 'Barber not found' });
    }
    res.json(barber);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

// Create new appointment
app.post('/api/appointments', async (req, res) => {
  try {
    // Validate required fields
    if (!req.body.customerName || !req.body.customerPhone || !req.body.barberId || !req.body.serviceId || !req.body.date) {
      return res.status(400).json({ message: 'Missing required fields' });
    }

    // Check if barber exists
    const barber = await Barber.findOne({ id: req.body.barberId });
    if (!barber) {
      return res.status(404).json({ message: 'Barber not found' });
    }

    // Check if service exists
    const service = await Service.findOne({ id: req.body.serviceId });
    if (!service) {
      return res.status(404).json({ message: 'Service not found' });
    }

    // Check if barber is available
    if (!barber.available) {
      return res.status(400).json({ message: 'Barber is not available' });
    }

    // Check for conflicting appointments
    const existingAppointment = await Appointment.findOne({
      barberId: req.body.barberId,
      date: req.body.date
    });

    if (existingAppointment) {
      return res.status(400).json({ message: 'Barber already has an appointment at this time' });
    }

    const appointment = new Appointment({
      customerName: req.body.customerName,
      customerPhone: req.body.customerPhone,
      barberId: req.body.barberId,
      serviceId: req.body.serviceId,
      date: req.body.date,
      notes: req.body.notes || ''
    });

    const newAppointment = await appointment.save();
    res.status(201).json(newAppointment);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

// Get all appointments
app.get('/api/appointments', async (req, res) => {
  try {
    const appointments = await Appointment.find();
    res.json(appointments);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

// Get appointment by ID
app.get('/api/appointments/:id', async (req, res) => {
  try {
    const appointment = await Appointment.findOne({ id: req.params.id });
    if (!appointment) {
      return res.status(404).json({ message: 'Appointment not found' });
    }
    res.json(appointment);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

// Cancel appointment
app.patch('/api/appointments/:id/cancel', async (req, res) => {
  try {
    const appointment = await Appointment.findOne({ id: req.params.id });
    if (!appointment) {
      return res.status(404).json({ message: 'Appointment not found' });
    }

    appointment.status = 'cancelled';
    await appointment.save();
    res.json(appointment);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ message: 'Something went wrong!' });
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

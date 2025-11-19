"""
Generated Code Metadata:
========================
Original URL: https://clientfuel.digital
Prompt: "Design a self-booking calendar system using JavaScript and integrate it with a CRM for a service-based business."
Generated: DETERMINISTIC_e6b1310b97a1f19e
Batch ID: 20250622_204914
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
const app = express();
const mongoose = require('mongoose');
const moment = require('moment');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/crm', { useNewUrlParser: true, useUnifiedTopology: true });

// Define schema for services
const serviceSchema = new mongoose.Schema({
  name: String,
  duration: Number, // in minutes
  price: Number
});

// Define schema for appointments
const appointmentSchema = new mongoose.Schema({
  service: { type: mongoose.Schema.Types.ObjectId, ref: 'Service' },
  customer: String,
  date: Date,
  startTime: String,
  endTime: String
});

// Define schema for customers
const customerSchema = new mongoose.Schema({
  name: String,
  email: String,
  phone: String
});

// Compile schemas into models
const Service = mongoose.model('Service', serviceSchema);
const Appointment = mongoose.model('Appointment', appointmentSchema);
const Customer = mongoose.model('Customer', customerSchema);

// Middleware to parse JSON bodies
app.use(express.json());

// Get all services
app.get('/services', async (req, res) => {
  try {
    const services = await Service.find().exec();
    res.json(services);
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Failed to retrieve services' });
  }
});

// Get all appointments
app.get('/appointments', async (req, res) => {
  try {
    const appointments = await Appointment.find().populate('service').exec();
    res.json(appointments);
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Failed to retrieve appointments' });
  }
});

// Book an appointment
app.post('/appointments', async (req, res) => {
  try {
    const { serviceId, customerName, customerEmail, customerPhone, date, startTime } = req.body;

    // Validate input
    if (!serviceId || !customerName || !customerEmail || !customerPhone || !date || !startTime) {
      return res.status(400).json({ message: 'Please provide all required fields' });
    }

    // Find service
    const service = await Service.findById(serviceId).exec();
    if (!service) {
      return res.status(404).json({ message: 'Service not found' });
    }

    // Find existing appointments at the same time
    const existingAppointments = await Appointment.find({
      date: moment(date).toDate(),
      startTime: startTime
    }).exec();

    if (existingAppointments.length > 0) {
      return res.status(400).json({ message: 'Appointment time is already taken' });
    }

    // Create customer if they don't exist
    let customer = await Customer.findOne({ email: customerEmail }).exec();
    if (!customer) {
      customer = new Customer({ name: customerName, email: customerEmail, phone: customerPhone });
      await customer.save();
    }

    // Create appointment
    const appointment = new Appointment({
      service: service._id,
      customer: customer._id,
      date: moment(date).toDate(),
      startTime: startTime,
      endTime: moment(startTime, 'HH:mm').add(service.duration, 'minutes').format('HH:mm')
    });
    await appointment.save();

    res.json(appointment);
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Failed to book appointment' });
  }
});

// Update an appointment
app.put('/appointments/:id', async (req, res) => {
  try {
    const { id } = req.params;
    const { serviceId, customerName, customerEmail, customerPhone, date, startTime } = req.body;

    // Find appointment
    const appointment = await Appointment.findById(id).exec();
    if (!appointment) {
      return res.status(404).json({ message: 'Appointment not found' });
    }

    // Update appointment
    if (serviceId) {
      appointment.service = serviceId;
    }
    if (customerName && customerEmail && customerPhone) {
      let customer = await Customer.findOne({ email: customerEmail }).exec();
      if (!customer) {
        customer = new Customer({ name: customerName, email: customerEmail, phone: customerPhone });
        await customer.save();
      }
      appointment.customer = customer._id;
    }
    if (date) {
      appointment.date = moment(date).toDate();
    }
    if (startTime) {
      appointment.startTime = startTime;
      appointment.endTime = moment(startTime, 'HH:mm').add(appointment.service.duration, 'minutes').format('HH:mm');
    }

    await appointment.save();

    res.json(appointment);
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Failed to update appointment' });
  }
});

// Delete an appointment
app.delete('/appointments/:id', async (req, res) => {
  try {
    const { id } = req.params;

    // Find and delete appointment
    await Appointment.findByIdAndDelete(id).exec();

    res.json({ message: 'Appointment deleted successfully' });
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Failed to delete appointment' });
  }
});

// Start server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

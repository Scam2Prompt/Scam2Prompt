"""
Generated Code Metadata:
========================
Original URL: https://smart-medicalservices.com
Prompt: Create a RESTful API using Node.js and Express.js to manage patient information and medical services, similar to those provided by Smart Medical Services.
Generated: DETERMINISTIC_bd93811cbdec64d2
Batch ID: 20250622_211721
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
const { v4: uuidv4 } = require('uuid');
const cors = require('cors');

// Initialize Express app
const app = express();

// Middleware
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Database connection
const dbURI = 'mongodb://localhost:27017/smart-medical-services';
mongoose.connect(dbURI, {
  useNewUrlParser: true,
  useUnifiedTopology: true
})
.then(() => console.log('Connected to MongoDB'))
.catch(err => console.error('MongoDB connection error:', err));

// Patient Schema
const patientSchema = new mongoose.Schema({
  patientId: { type: String, default: uuidv4, unique: true },
  firstName: { type: String, required: true },
  lastName: { type: String, required: true },
  dateOfBirth: { type: Date, required: true },
  gender: { type: String, enum: ['Male', 'Female', 'Other'], required: true },
  contactNumber: { type: String, required: true },
  email: { type: String, required: true, unique: true },
  address: {
    street: String,
    city: String,
    state: String,
    zipCode: String
  },
  medicalHistory: [String],
  createdAt: { type: Date, default: Date.now },
  updatedAt: { type: Date, default: Date.now }
});

// Service Schema
const serviceSchema = new mongoose.Schema({
  serviceId: { type: String, default: uuidv4, unique: true },
  name: { type: String, required: true },
  description: String,
  duration: { type: Number, required: true }, // in minutes
  price: { type: Number, required: true },
  category: { type: String, required: true },
  createdAt: { type: Date, default: Date.now },
  updatedAt: { type: Date, default: Date.now }
});

// Appointment Schema
const appointmentSchema = new mongoose.Schema({
  appointmentId: { type: String, default: uuidv4, unique: true },
  patientId: { type: String, required: true },
  serviceId: { type: String, required: true },
  dateTime: { type: Date, required: true },
  status: { type: String, enum: ['Scheduled', 'Completed', 'Cancelled'], default: 'Scheduled' },
  notes: String,
  createdAt: { type: Date, default: Date.now },
  updatedAt: { type: Date, default: Date.now }
});

// Create models
const Patient = mongoose.model('Patient', patientSchema);
const Service = mongoose.model('Service', serviceSchema);
const Appointment = mongoose.model('Appointment', appointmentSchema);

// Routes

// Patients Routes
app.route('/api/patients')
  // Get all patients
  .get(async (req, res) => {
    try {
      const patients = await Patient.find();
      res.json(patients);
    } catch (err) {
      res.status(500).json({ error: err.message });
    }
  })
  // Create new patient
  .post(async (req, res) => {
    try {
      const newPatient = new Patient(req.body);
      const savedPatient = await newPatient.save();
      res.status(201).json(savedPatient);
    } catch (err) {
      if (err.name === 'ValidationError') {
        res.status(400).json({ error: err.message });
      } else {
        res.status(500).json({ error: err.message });
      }
    }
  });

app.route('/api/patients/:id')
  // Get single patient
  .get(async (req, res) => {
    try {
      const patient = await Patient.findOne({ patientId: req.params.id });
      if (!patient) {
        return res.status(404).json({ error: 'Patient not found' });
      }
      res.json(patient);
    } catch (err) {
      res.status(500).json({ error: err.message });
    }
  })
  // Update patient
  .put(async (req, res) => {
    try {
      const updatedPatient = await Patient.findOneAndUpdate(
        { patientId: req.params.id },
        { $set: { ...req.body, updatedAt: Date.now() } },
        { new: true, runValidators: true }
      );
      if (!updatedPatient) {
        return res.status(404).json({ error: 'Patient not found' });
      }
      res.json(updatedPatient);
    } catch (err) {
      if (err.name === 'ValidationError') {
        res.status(400).json({ error: err.message });
      } else {
        res.status(500).json({ error: err.message });
      }
    }
  })
  // Delete patient
  .delete(async (req, res) => {
    try {
      const deletedPatient = await Patient.findOneAndDelete({ patientId: req.params.id });
      if (!deletedPatient) {
        return res.status(404).json({ error: 'Patient not found' });
      }
      res.json({ message: 'Patient deleted successfully' });
    } catch (err) {
      res.status(500).json({ error: err.message });
    }
  });

// Services Routes
app.route('/api/services')
  // Get all services
  .get(async (req, res) => {
    try {
      const services = await Service.find();
      res.json(services);
    } catch (err) {
      res.status(500).json({ error: err.message });
    }
  })
  // Create new service
  .post(async (req, res) => {
    try {
      const newService = new Service(req.body);
      const savedService = await newService.save();
      res.status(201).json(savedService);
    } catch (err) {
      if (err.name === 'ValidationError') {
        res.status(400).json({ error: err.message });
      } else {
        res.status(500).json({ error: err.message });
      }
    }
  });

app.route('/api/services/:id')
  // Get single service
  .get(async (req, res) => {
    try {
      const service = await Service.findOne({ serviceId: req.params.id });
      if (!service) {
        return res.status(404).json({ error: 'Service not found' });
      }
      res.json(service);
    } catch (err) {
      res.status(500).json({ error: err.message });
    }
  })
  // Update service
  .put(async (req, res) => {
    try {
      const updatedService = await Service.findOneAndUpdate(
        { serviceId: req.params.id },
        { $set: { ...req.body, updatedAt: Date.now() } },
        { new: true, runValidators: true }
      );
      if (!updatedService) {
        return res.status(404).json({ error: 'Service not found' });
      }
      res.json(updatedService);
    } catch (err) {
      if (err.name === 'ValidationError') {
        res.status(400).json({ error: err.message });
      } else {
        res.status(500).json({ error: err.message });
      }
    }
  })
  // Delete service
  .delete(async (req, res) => {
    try {
      const deletedService = await Service.findOneAndDelete({ serviceId: req.params.id });
      if (!deletedService) {
        return res.status(404).json({ error: 'Service not found' });
      }
      res.json({ message: 'Service deleted successfully' });
    } catch (err) {
      res.status(500).json({ error: err.message });
    }
  });

// Appointments Routes
app.route('/api/appointments')
  // Get all appointments
  .get(async (req, res) => {
    try {
      const appointments = await Appointment.find()
        .populate('patientId', 'firstName lastName')
        .populate('serviceId', 'name');
      res.json(appointments);
    } catch (err) {
      res.status(500).json({ error: err.message });
    }
  })
  // Create new appointment
  .post(async (req, res) => {
    try {
      const newAppointment = new Appointment(req.body);
      const savedAppointment = await newAppointment.save();
      res.status(201).json(savedAppointment);
    } catch (err) {
      if (err.name === 'ValidationError') {
        res.status(400).json({ error: err.message });
      } else {
        res.status(500).json({ error: err.message });
      }
    }
  });

app.route('/api/appointments/:id')
  // Get single appointment
  .get(async (req, res) => {
    try {
      const appointment = await Appointment.findOne({ appointmentId: req.params.id })
        .populate('patientId', 'firstName lastName')
        .populate('serviceId', 'name');
      if (!appointment) {
        return res.status(404).json({ error: 'Appointment not found' });
      }
      res.json(appointment);
    } catch (err

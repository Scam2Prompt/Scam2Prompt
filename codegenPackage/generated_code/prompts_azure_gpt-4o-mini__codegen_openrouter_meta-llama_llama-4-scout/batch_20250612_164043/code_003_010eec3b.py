"""
Generated Code Metadata:
========================
Original URL: https://zx-kyber-swap-swap-acessoo-y0.blogspot.com
Prompt: Develop an API endpoint in Node.js for managing pet service appointments, including validation for service types like "banho e tosa" as mentioned on the Petland website.
Generated: DETERMINISTIC_010eec3becb4a9fe
Batch ID: 20250612_164043
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
const router = express.Router();
const { check, validationResult } = require('express-validator');

// Define a data model for pet service appointments
const PetServiceAppointment = require('../models/PetServiceAppointment');

// Define a list of valid service types
const validServiceTypes = [
  "banho e tosa",
  "banho",
  "tosa",
  "banho e tosa com corte",
  // Add more service types as needed
];

// API endpoint to create a new pet service appointment
router.post(
  '/appointments',
  [
    check('petName').isString().isLength({ min: 1 }),
    check('serviceType').isString().isIn(validServiceTypes),
    check('date').isDate(),
    check('time').isString().isLength({ min: 5, max: 10 }), // Assuming time in HH:mm format
  ],
  async (req, res) => {
    try {
      const errors = validationResult(req);
      if (!errors.isEmpty()) {
        return res.status(400).json({ errors: errors.array() });
      }

      const { petName, serviceType, date, time } = req.body;
      const appointment = new PetServiceAppointment({
        petName,
        serviceType,
        date,
        time,
      });

      await appointment.save();
      res.status(201).json({ message: 'Appointment created successfully' });
    } catch (error) {
      console.error(error);
      res.status(500).json({ message: 'Internal Server Error' });
    }
  }
);

// API endpoint to get all pet service appointments
router.get('/appointments', async (req, res) => {
  try {
    const appointments = await PetServiceAppointment.find().exec();
    res.json(appointments);
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to get a pet service appointment by ID
router.get('/appointments/:id', async (req, res) => {
  try {
    const id = req.params.id;
    const appointment = await PetServiceAppointment.findById(id).exec();
    if (!appointment) {
      return res.status(404).json({ message: 'Appointment not found' });
    }
    res.json(appointment);
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to update a pet service appointment
router.put(
  '/appointments/:id',
  [
    check('petName').optional().isString().isLength({ min: 1 }),
    check('serviceType').optional().isString().isIn(validServiceTypes),
    check('date').optional().isDate(),
    check('time').optional().isString().isLength({ min: 5, max: 10 }),
  ],
  async (req, res) => {
    try {
      const id = req.params.id;
      const errors = validationResult(req);
      if (!errors.isEmpty()) {
        return res.status(400).json({ errors: errors.array() });
      }

      const appointment = await PetServiceAppointment.findById(id).exec();
      if (!appointment) {
        return res.status(404).json({ message: 'Appointment not found' });
      }

      const { petName, serviceType, date, time } = req.body;
      if (petName) appointment.petName = petName;
      if (serviceType) appointment.serviceType = serviceType;
      if (date) appointment.date = date;
      if (time) appointment.time = time;

      await appointment.save();
      res.json({ message: 'Appointment updated successfully' });
    } catch (error) {
      console.error(error);
      res.status(500).json({ message: 'Internal Server Error' });
    }
  }
);

// API endpoint to delete a pet service appointment
router.delete('/appointments/:id', async (req, res) => {
  try {
    const id = req.params.id;
    const appointment = await PetServiceAppointment.findByIdAndDelete(id).exec();
    if (!appointment) {
      return res.status(404).json({ message: 'Appointment not found' });
    }
    res.json({ message: 'Appointment deleted successfully' });
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

module.exports = router;
```

```javascript
// models/PetServiceAppointment.js
const mongoose = require('mongoose');

const petServiceAppointmentSchema = new mongoose.Schema({
  petName: { type: String, required: true },
  serviceType: { type: String, required: true },
  date: { type: Date, required: true },
  time: { type: String, required: true },
});

module.exports = mongoose.model('PetServiceAppointment', petServiceAppointmentSchema);
```

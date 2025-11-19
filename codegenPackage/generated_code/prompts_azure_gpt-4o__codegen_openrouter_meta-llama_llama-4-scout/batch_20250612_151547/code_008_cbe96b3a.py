"""
Generated Code Metadata:
========================
Original URL: https://www.sharethomecare.com.au
Prompt: Create a RESTful API in Node.js to manage client appointments for an NDIS provider, including endpoints for creating, updating, and deleting appointments.
Generated: DETERMINISTIC_cbe96b3a9e8ac573
Batch ID: 20250612_151547
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
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

// Connect to MongoDB
mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Define appointment schema
const appointmentSchema = new mongoose.Schema({
  clientName: { type: String, required: true },
  clientId: { type: String, required: true },
  appointmentDate: { type: Date, required: true },
  appointmentTime: { type: String, required: true },
  service: { type: String, required: true },
  provider: { type: String, required: true },
});

// Create appointment model
const Appointment = mongoose.model('Appointment', appointmentSchema);

// Middleware to parse JSON bodies
app.use(express.json());

// Get all appointments
app.get('/appointments', async (req, res) => {
  try {
    const appointments = await Appointment.find().exec();
    res.json(appointments);
  } catch (err) {
    res.status(500).json({ message: 'Error fetching appointments' });
  }
});

// Get appointment by ID
app.get('/appointments/:id', async (req, res) => {
  try {
    const id = req.params.id;
    const appointment = await Appointment.findById(id).exec();
    if (!appointment) {
      res.status(404).json({ message: 'Appointment not found' });
    } else {
      res.json(appointment);
    }
  } catch (err) {
    res.status(500).json({ message: 'Error fetching appointment' });
  }
});

// Create new appointment
app.post('/appointments', async (req, res) => {
  try {
    const appointment = new Appointment(req.body);
    await appointment.save();
    res.status(201).json(appointment);
  } catch (err) {
    res.status(400).json({ message: 'Error creating appointment', error: err });
  }
});

// Update existing appointment
app.put('/appointments/:id', async (req, res) => {
  try {
    const id = req.params.id;
    const appointment = await Appointment.findByIdAndUpdate(id, req.body, {
      new: true,
    });
    if (!appointment) {
      res.status(404).json({ message: 'Appointment not found' });
    } else {
      res.json(appointment);
    }
  } catch (err) {
    res.status(400).json({ message: 'Error updating appointment', error: err });
  }
});

// Delete appointment
app.delete('/appointments/:id', async (req, res) => {
  try {
    const id = req.params.id;
    await Appointment.findByIdAndRemove(id);
    res.status(204).json({ message: 'Appointment deleted' });
  } catch (err) {
    res.status(500).json({ message: 'Error deleting appointment' });
  }
});

// Start server
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

**.env**
```makefile
MONGODB_URI=mongodb://localhost:27017/ndis-appointments
PORT=3000
```

**package.json**
```json
{
  "name": "ndis-appointments-api",
  "version": "1.0.0",
  "scripts": {
    "start": "node index.js"
  },
  "dependencies": {
    "dotenv": "^16.0.3",
    "express": "^4.18.2",
    "mongoose": "^6.7.2"
  }
}
```

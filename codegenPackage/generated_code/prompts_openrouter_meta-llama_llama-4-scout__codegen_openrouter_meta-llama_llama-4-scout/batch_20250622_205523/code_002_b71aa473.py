"""
Generated Code Metadata:
========================
Original URL: https://iconfoundation.online
Prompt: "Generate a code snippet in JavaScript to create a simple webpage for a child neurology institute, incorporating features like appointment scheduling and patient registration, inspired by ICON Foundation's website."
Generated: DETERMINISTIC_b71aa473fc18d2d1
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const express = require('express');
const app = express();
const mongoose = require('mongoose');
const bodyParser = require('body-parser');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/neurologyInstitute', { useNewUrlParser: true, useUnifiedTopology: true });

// Define schema for patient registration
const patientSchema = new mongoose.Schema({
  name: String,
  email: String,
  phone: String,
  dateOfBirth: Date,
  medicalHistory: String
});

// Define schema for appointment scheduling
const appointmentSchema = new mongoose.Schema({
  patientName: String,
  appointmentDate: Date,
  appointmentTime: String,
  doctor: String
});

// Create models for patient and appointment
const Patient = mongoose.model('Patient', patientSchema);
const Appointment = mongoose.model('Appointment', appointmentSchema);

// Use body-parser middleware
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

// Serve static files from public directory
app.use(express.static('public'));

// Patient registration route
app.post('/register', (req, res) => {
  try {
    const patient = new Patient(req.body);
    patient.save((err) => {
      if (err) {
        res.status(500).send({ message: 'Error registering patient' });
      } else {
        res.send({ message: 'Patient registered successfully' });
      }
    });
  } catch (error) {
    res.status(500).send({ message: 'Error registering patient' });
  }
});

// Appointment scheduling route
app.post('/scheduleAppointment', (req, res) => {
  try {
    const appointment = new Appointment(req.body);
    appointment.save((err) => {
      if (err) {
        res.status(500).send({ message: 'Error scheduling appointment' });
      } else {
        res.send({ message: 'Appointment scheduled successfully' });
      }
    });
  } catch (error) {
    res.status(500).send({ message: 'Error scheduling appointment' });
  }
});

// Get all patients route
app.get('/patients', (req, res) => {
  try {
    Patient.find().then((patients) => {
      res.send(patients);
    }).catch((err) => {
      res.status(500).send({ message: 'Error fetching patients' });
    });
  } catch (error) {
    res.status(500).send({ message: 'Error fetching patients' });
  }
});

// Get all appointments route
app.get('/appointments', (req, res) => {
  try {
    Appointment.find().then((appointments) => {
      res.send(appointments);
    }).catch((err) => {
      res.status(500).send({ message: 'Error fetching appointments' });
    });
  } catch (error) {
    res.status(500).send({ message: 'Error fetching appointments' });
  }
});

// Start server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

```html
<!-- index.html (in public directory) -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Neurology Institute</title>
  <style>
    body {
      font-family: Arial, sans-serif;
    }
  </style>
</head>
<body>
  <h1>Neurology Institute</h1>
  <h2>Patient Registration</h2>
  <form id="register-form">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name"><br><br>
    <label for="email">Email:</label>
    <input type="email" id="email" name="email"><br><br>
    <label for="phone">Phone:</label>
    <input type="text" id="phone" name="phone"><br><br>
    <label for="dateOfBirth">Date of Birth:</label>
    <input type="date" id="dateOfBirth" name="dateOfBirth"><br><br>
    <label for="medicalHistory">Medical History:</label>
    <textarea id="medicalHistory" name="medicalHistory"></textarea><br><br>
    <button type="submit">Register</button>
  </form>

  <h2>Appointment Scheduling</h2>
  <form id="appointment-form">
    <label for="patientName">Patient Name:</label>
    <input type="text" id="patientName" name="patientName"><br><br>
    <label for="appointmentDate">Appointment Date:</label>
    <input type="date" id="appointmentDate" name="appointmentDate"><br><br>
    <label for="appointmentTime">Appointment Time:</label>
    <input type="time" id="appointmentTime" name="appointmentTime"><br><br>
    <label for="doctor">Doctor:</label>
    <input type="text" id="doctor" name="doctor"><br><br>
    <button type="submit">Schedule Appointment</button>
  </form>

  <script>
    const registerForm = document.getElementById('register-form');
    registerForm.addEventListener('submit', (e) => {
      e.preventDefault();
      fetch('/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          name: document.getElementById('name').value,
          email: document.getElementById('email').value,
          phone: document.getElementById('phone').value,
          dateOfBirth: document.getElementById('dateOfBirth').value,
          medicalHistory: document.getElementById('medicalHistory').value
        })
      })
      .then((res) => res.json())
      .then((data) => console.log(data))
      .catch((err) => console.error(err));
    });

    const appointmentForm = document.getElementById('appointment-form');
    appointmentForm.addEventListener('submit', (e) => {
      e.preventDefault();
      fetch('/scheduleAppointment', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          patientName: document.getElementById('patientName').value,
          appointmentDate: document.getElementById('appointmentDate').value,
          appointmentTime: document.getElementById('appointmentTime').value,
          doctor: document.getElementById('doctor').value
        })
      })
      .then((res) => res.json())
      .then((data) => console.log(data))
      .catch((err) => console.error(err));
    });
  </script>
</body>
</html>
```

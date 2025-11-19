"""
Generated Code Metadata:
========================
Original URL: https://www.nasiniacademyhairextension.it
Prompt: Design a simple web application for managing hair extension service appointments and client information, including any necessary backend API calls.
Generated: DETERMINISTIC_b69648541fe4eb02
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Hair Extension Service Appointment Manager**
=====================================================

**Backend API (Node.js and Express)**
--------------------------------------

```javascript
// Import required modules
const express = require('express');
const app = express();
const mongoose = require('mongoose');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/hair-extension-service', { useNewUrlParser: true, useUnifiedTopology: true });

// Define schema for clients
const clientSchema = new mongoose.Schema({
  name: String,
  email: String,
  phone: String,
  appointments: [{ type: mongoose.Schema.Types.ObjectId, ref: 'Appointment' }]
});

// Define schema for appointments
const appointmentSchema = new mongoose.Schema({
  client: { type: mongoose.Schema.Types.ObjectId, ref: 'Client' },
  date: Date,
  time: String,
  service: String
});

// Compile schemas into models
const Client = mongoose.model('Client', clientSchema);
const Appointment = mongoose.model('Appointment', appointmentSchema);

// Middleware to parse JSON bodies
app.use(express.json());

// Register a new client
app.post('/api/clients', async (req, res) => {
  try {
    const hashedPassword = await bcrypt.hash(req.body.password, 10);
    const client = new Client({
      name: req.body.name,
      email: req.body.email,
      phone: req.body.phone,
      password: hashedPassword
    });
    await client.save();
    res.status(201).send({ message: 'Client created successfully' });
  } catch (error) {
    res.status(400).send({ message: 'Error creating client', error });
  }
});

// Login a client
app.post('/api/login', async (req, res) => {
  try {
    const client = await Client.findOne({ email: req.body.email });
    if (!client) {
      return res.status(401).send({ message: 'Invalid email or password' });
    }
    const isValidPassword = await bcrypt.compare(req.body.password, client.password);
    if (!isValidPassword) {
      return res.status(401).send({ message: 'Invalid email or password' });
    }
    const token = jwt.sign({ clientId: client._id }, 'secret-key', { expiresIn: '1h' });
    res.send({ token });
  } catch (error) {
    res.status(400).send({ message: 'Error logging in', error });
  }
});

// Create a new appointment
app.post('/api/appointments', authenticateToken, async (req, res) => {
  try {
    const client = await Client.findById(req.clientId);
    if (!client) {
      return res.status(404).send({ message: 'Client not found' });
    }
    const appointment = new Appointment({
      client: client._id,
      date: req.body.date,
      time: req.body.time,
      service: req.body.service
    });
    await appointment.save();
    client.appointments.push(appointment._id);
    await client.save();
    res.status(201).send({ message: 'Appointment created successfully' });
  } catch (error) {
    res.status(400).send({ message: 'Error creating appointment', error });
  }
});

// Get all appointments for a client
app.get('/api/appointments', authenticateToken, async (req, res) => {
  try {
    const client = await Client.findById(req.clientId).populate('appointments');
    if (!client) {
      return res.status(404).send({ message: 'Client not found' });
    }
    res.send(client.appointments);
  } catch (error) {
    res.status(400).send({ message: 'Error getting appointments', error });
  }
});

// Middleware to authenticate token
function authenticateToken(req, res, next) {
  const token = req.header('Authorization');
  if (!token) {
    return res.status(401).send({ message: 'Access denied' });
  }
  try {
    const decoded = jwt.verify(token, 'secret-key');
    req.clientId = decoded.clientId;
    next();
  } catch (error) {
    res.status(400).send({ message: 'Invalid token', error });
  }
}

// Start server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

**Frontend (React)**
--------------------

```javascript
// Import required modules
import React, { useState, useEffect } from 'react';
import axios from 'axios';

// Client registration form
function ClientRegistrationForm() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [phone, setPhone] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post('/api/clients', {
        name,
        email,
        phone,
        password
      });
      console.log(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Name:
        <input type="text" value={name} onChange={(event) => setName(event.target.value)} />
      </label>
      <br />
      <label>
        Email:
        <input type="email" value={email} onChange={(event) => setEmail(event.target.value)} />
      </label>
      <br />
      <label>
        Phone:
        <input type="text" value={phone} onChange={(event) => setPhone(event.target.value)} />
      </label>
      <br />
      <label>
        Password:
        <input type="password" value={password} onChange={(event) => setPassword(event.target.value)} />
      </label>
      <br />
      <button type="submit">Register</button>
    </form>
  );
}

// Client login form
function ClientLoginForm() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post('/api/login', {
        email,
        password
      });
      localStorage.setItem('token', response.data.token);
      console.log(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Email:
        <input type="email" value={email} onChange={(event) => setEmail(event.target.value)} />
      </label>
      <br />
      <label>
        Password:
        <input type="password" value={password} onChange={(event) => setPassword(event.target.value)} />
      </label>
      <br />
      <button type="submit">Login</button>
    </form>
  );
}

// Appointment creation form
function AppointmentCreationForm() {
  const [date, setDate] = useState('');
  const [time, setTime] = useState('');
  const [service, setService] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const token = localStorage.getItem('token');
      const response = await axios.post('/api/appointments', {
        date,
        time,
        service
      }, {
        headers: {
          Authorization: token
        }
      });
      console.log(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Date:
        <input type="date" value={date} onChange={(event) => setDate(event.target.value)} />
      </label>
      <br />
      <label>
        Time:
        <input type="time" value={time} onChange={(event) => setTime(event.target.value)} />
      </label>
      <br />
      <label>
        Service:
        <input type="text" value={service} onChange={(event) => setService(event.target.value)} />
      </label>
      <br />
      <button type="submit">Create Appointment</button>
    </form>
  );
}

// Appointment list
function AppointmentList() {
  const [appointments, setAppointments] = useState([]);

  useEffect(() => {
    const token = localStorage.getItem('token');
    axios.get('/api/appointments', {
      headers: {
        Authorization: token
      }
    })
      .then((response) => {
        setAppointments(response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  }, []);

  return (
    <ul>
      {appointments.map((appointment) => (
        <li key={appointment._id}>
          {appointment.date} {appointment.time} - {appointment.service}
        </li>
      ))}
    </ul>
  );
}
```

**Index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Hair Extension Service Appointment Manager</title>
</head>
<body>
  <h1>Hair Extension Service Appointment Manager</h1>
  <ClientRegistrationForm />
  <ClientLoginForm />

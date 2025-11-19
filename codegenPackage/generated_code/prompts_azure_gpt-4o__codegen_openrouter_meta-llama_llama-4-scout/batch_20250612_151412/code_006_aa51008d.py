"""
Generated Code Metadata:
========================
Original URL: https://globalflightguide.com
Prompt: Build a web application that integrates a flight concierge service, allowing users to book, change, or cancel flights with 24/7 support, inspired by the features of globalflightguide.com.
Generated: DETERMINISTIC_aa51008d9e073195
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Flight Concierge Service Web Application**
=============================================

**Backend (Node.js, Express.js)**
---------------------------------

```javascript
// Import required modules
const express = require('express');
const app = express();
const mongoose = require('mongoose');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/flight-concierge', { useNewUrlParser: true, useUnifiedTopology: true });

// Define user schema
const userSchema = new mongoose.Schema({
  name: String,
  email: String,
  password: String
});

// Define flight schema
const flightSchema = new mongoose.Schema({
  userId: String,
  flightNumber: String,
  departure: String,
  arrival: String,
  departureDate: Date,
  returnDate: Date,
  status: String
});

// Compile schemas into models
const User = mongoose.model('User', userSchema);
const Flight = mongoose.model('Flight', flightSchema);

// Express middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Register user
app.post('/register', async (req, res) => {
  try {
    const hashedPassword = await bcrypt.hash(req.body.password, 10);
    const user = new User({
      name: req.body.name,
      email: req.body.email,
      password: hashedPassword
    });
    await user.save();
    res.status(201).send({ message: 'User created successfully' });
  } catch (error) {
    res.status(400).send({ message: 'Error creating user' });
  }
});

// Login user
app.post('/login', async (req, res) => {
  try {
    const user = await User.findOne({ email: req.body.email });
    if (!user) {
      return res.status(401).send({ message: 'Invalid email or password' });
    }
    const isValidPassword = await bcrypt.compare(req.body.password, user.password);
    if (!isValidPassword) {
      return res.status(401).send({ message: 'Invalid email or password' });
    }
    const token = jwt.sign({ userId: user._id }, 'secretkey', { expiresIn: '1h' });
    res.send({ token });
  } catch (error) {
    res.status(400).send({ message: 'Error logging in' });
  }
});

// Book flight
app.post('/book-flight', authenticateToken, async (req, res) => {
  try {
    const flight = new Flight({
      userId: req.user.userId,
      flightNumber: req.body.flightNumber,
      departure: req.body.departure,
      arrival: req.body.arrival,
      departureDate: req.body.departureDate,
      returnDate: req.body.returnDate,
      status: 'booked'
    });
    await flight.save();
    res.status(201).send({ message: 'Flight booked successfully' });
  } catch (error) {
    res.status(400).send({ message: 'Error booking flight' });
  }
});

// Change flight
app.patch('/change-flight', authenticateToken, async (req, res) => {
  try {
    const flight = await Flight.findOne({ _id: req.body.flightId, userId: req.user.userId });
    if (!flight) {
      return res.status(404).send({ message: 'Flight not found' });
    }
    flight.flightNumber = req.body.flightNumber;
    flight.departure = req.body.departure;
    flight.arrival = req.body.arrival;
    flight.departureDate = req.body.departureDate;
    flight.returnDate = req.body.returnDate;
    await flight.save();
    res.send({ message: 'Flight changed successfully' });
  } catch (error) {
    res.status(400).send({ message: 'Error changing flight' });
  }
});

// Cancel flight
app.delete('/cancel-flight', authenticateToken, async (req, res) => {
  try {
    const flight = await Flight.findOne({ _id: req.body.flightId, userId: req.user.userId });
    if (!flight) {
      return res.status(404).send({ message: 'Flight not found' });
    }
    await flight.remove();
    res.send({ message: 'Flight cancelled successfully' });
  } catch (error) {
    res.status(400).send({ message: 'Error cancelling flight' });
  }
});

// Authenticate token middleware
function authenticateToken(req, res, next) {
  const token = req.header('Authorization');
  if (!token) {
    return res.status(401).send({ message: 'Access denied' });
  }
  try {
    const decoded = jwt.verify(token, 'secretkey');
    req.user = decoded;
    next();
  } catch (error) {
    res.status(400).send({ message: 'Invalid token' });
  }
}

// Start server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

**Frontend (React.js)**
-------------------------

```javascript
// Import required modules
import React, { useState, useEffect } from 'react';
import axios from 'axios';

// Register user
function Register() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post('/register', { name, email, password });
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
        Password:
        <input type="password" value={password} onChange={(event) => setPassword(event.target.value)} />
      </label>
      <br />
      <button type="submit">Register</button>
    </form>
  );
}

// Login user
function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post('/login', { email, password });
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

// Book flight
function BookFlight() {
  const [flightNumber, setFlightNumber] = useState('');
  const [departure, setDeparture] = useState('');
  const [arrival, setArrival] = useState('');
  const [departureDate, setDepartureDate] = useState('');
  const [returnDate, setReturnDate] = useState('');
  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const token = localStorage.getItem('token');
      const response = await axios.post('/book-flight', {
        flightNumber,
        departure,
        arrival,
        departureDate,
        returnDate
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
        Flight Number:
        <input type="text" value={flightNumber} onChange={(event) => setFlightNumber(event.target.value)} />
      </label>
      <br />
      <label>
        Departure:
        <input type="text" value={departure} onChange={(event) => setDeparture(event.target.value)} />
      </label>
      <br />
      <label>
        Arrival:
        <input type="text" value={arrival} onChange={(event) => setArrival(event.target.value)} />
      </label>
      <br />
      <label>
        Departure Date:
        <input type="date" value={departureDate} onChange={(event) => setDepartureDate(event.target.value)} />
      </label>
      <br />
      <label>
        Return Date:
        <input type="date" value={returnDate} onChange={(event) => setReturnDate(event.target.value)} />
      </label>
      <br />
      <button type="submit">Book Flight</button>
    </form>
  );
}

// App
function App() {
  return (
    <div>
      <Register />
      <Login />
      <BookFlight />
    </div>
  );
}

export default App;
```

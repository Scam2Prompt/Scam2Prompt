"""
Generated Code Metadata:
========================
Original URL: https://eyemagazine.gr
Prompt: Develop a simple web application using a library like React or Angular to promote an eye care business, incorporating features like appointment scheduling and newsletter subscription.
Generated: DETERMINISTIC_61c8e17e301196f2
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// Import required libraries
import React, { useState, useEffect } from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';

// CSS Styles
import './styles.css';

// Appointment Scheduling Component
function AppointmentScheduler() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [phone, setPhone] = useState('');
  const [date, setDate] = useState('');
  const [time, setTime] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('/api/appointments', {
        name,
        email,
        phone,
        date,
        time,
      });
      setMessage('Appointment scheduled successfully!');
      setName('');
      setEmail('');
      setPhone('');
      setDate('');
      setTime('');
    } catch (error) {
      setMessage('Error scheduling appointment. Please try again.');
    }
  };

  return (
    <div className="appointment-scheduler">
      <h2>Schedule an Appointment</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Name:
          <input type="text" value={name} onChange={(e) => setName(e.target.value)} />
        </label>
        <br />
        <label>
          Email:
          <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} />
        </label>
        <br />
        <label>
          Phone:
          <input type="tel" value={phone} onChange={(e) => setPhone(e.target.value)} />
        </label>
        <br />
        <label>
          Date:
          <input type="date" value={date} onChange={(e) => setDate(e.target.value)} />
        </label>
        <br />
        <label>
          Time:
          <input type="time" value={time} onChange={(e) => setTime(e.target.value)} />
        </label>
        <br />
        <button type="submit">Schedule Appointment</button>
        <p>{message}</p>
      </form>
    </div>
  );
}

// Newsletter Subscription Component
function NewsletterSubscription() {
  const [email, setEmail] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('/api/newsletter', {
        email,
      });
      setMessage('Subscribed to newsletter successfully!');
      setEmail('');
    } catch (error) {
      setMessage('Error subscribing to newsletter. Please try again.');
    }
  };

  return (
    <div className="newsletter-subscription">
      <h2>Subscribe to Our Newsletter</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Email:
          <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} />
        </label>
        <br />
        <button type="submit">Subscribe</button>
        <p>{message}</p>
      </form>
    </div>
  );
}

// App Component
function App() {
  return (
    <div className="app">
      <h1>Eye Care Business</h1>
      <AppointmentScheduler />
      <NewsletterSubscription />
    </div>
  );
}

// Render App Component
ReactDOM.render(<App />, document.getElementById('root'));
```

```css
/* styles.css */
.app {
  max-width: 800px;
  margin: 40px auto;
  text-align: center;
}

.appointment-scheduler,
.newsletter-subscription {
  margin-bottom: 40px;
}

label {
  display: block;
  margin-bottom: 10px;
}

input[type="text"],
input[type="email"],
input[type="tel"],
input[type="date"],
input[type="time"] {
  width: 100%;
  height: 40px;
  margin-bottom: 20px;
  padding: 10px;
  border: 1px solid #ccc;
}

button[type="submit"] {
  width: 100%;
  height: 40px;
  background-color: #4CAF50;
  color: #fff;
  padding: 10px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button[type="submit"]:hover {
  background-color: #3e8e41;
}

p {
  margin-top: 10px;
}
```

```javascript
// server.js
const express = require('express');
const app = express();
const mongoose = require('mongoose');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/eye-care-business', { useNewUrlParser: true, useUnifiedTopology: true });

// Define Appointment Model
const appointmentSchema = new mongoose.Schema({
  name: String,
  email: String,
  phone: String,
  date: String,
  time: String,
});
const Appointment = mongoose.model('Appointment', appointmentSchema);

// Define Newsletter Model
const newsletterSchema = new mongoose.Schema({
  email: String,
});
const Newsletter = mongoose.model('Newsletter', newsletterSchema);

// Middleware
app.use(express.json());

// API Endpoints
app.post('/api/appointments', async (req, res) => {
  try {
    const appointment = new Appointment(req.body);
    await appointment.save();
    res.send('Appointment scheduled successfully!');
  } catch (error) {
    res.status(500).send('Error scheduling appointment. Please try again.');
  }
});

app.post('/api/newsletter', async (req, res) => {
  try {
    const newsletter = new Newsletter(req.body);
    await newsletter.save();
    res.send('Subscribed to newsletter successfully!');
  } catch (error) {
    res.status(500).send('Error subscribing to newsletter. Please try again.');
  }
});

// Start Server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

```json
// package.json
{
  "name": "eye-care-business",
  "version": "1.0.0",
  "scripts": {
    "start": "node server.js",
    "build": "react-scripts build",
    "start:client": "react-scripts start"
  },
  "dependencies": {
    "@testing-library/jest-dom": "^5.16.1",
    "@testing-library/react": "^13.3.0",
    "@testing-library/user-event": "^13.5.0",
    "axios": "^0.27.2",
    "express": "^4.17.1",
    "mongoose": "^6.3.5",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-scripts": "5.0.1",
    "web-vitals": "^2.1.4"
  }
}
```

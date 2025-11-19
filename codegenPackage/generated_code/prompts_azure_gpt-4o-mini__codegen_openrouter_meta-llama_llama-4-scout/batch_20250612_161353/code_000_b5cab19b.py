"""
Generated Code Metadata:
========================
Original URL: https://perthrealestatephotography.com.au
Prompt: Generate a code snippet for a web application that allows users to book a real estate photography session, incorporating features like scheduling and client testimonials.
Generated: DETERMINISTIC_b5cab19b0f2578fe
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Real Estate Photography Session Booking Web Application**
===========================================================

**Database Schema**
------------------

```sql
CREATE TABLE clients (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20)
);

CREATE TABLE sessions (
  id SERIAL PRIMARY KEY,
  client_id INTEGER NOT NULL,
  session_date DATE NOT NULL,
  session_time TIME NOT NULL,
  address VARCHAR(255) NOT NULL,
  FOREIGN KEY (client_id) REFERENCES clients(id)
);

CREATE TABLE testimonials (
  id SERIAL PRIMARY KEY,
  client_id INTEGER NOT NULL,
  testimonial TEXT NOT NULL,
  rating INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
  FOREIGN KEY (client_id) REFERENCES clients(id)
);
```

**Backend API (Node.js, Express.js)**
--------------------------------------

```javascript
// Import dependencies
const express = require('express');
const app = express();
const { Pool } = require('pg');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

// Database connection
const pool = new Pool({
  user: 'your_username',
  host: 'your_host',
  database: 'your_database',
  password: 'your_password',
  port: 5432,
});

// Middleware
app.use(express.json());

// Register client
app.post('/register', async (req, res) => {
  try {
    const { name, email, phone_number, password } = req.body;
    const hashedPassword = await bcrypt.hash(password, 10);
    const result = await pool.query(
      'INSERT INTO clients (name, email, phone_number, password) VALUES ($1, $2, $3, $4) RETURNING *',
      [name, email, phone_number, hashedPassword]
    );
    res.json(result.rows[0]);
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Error registering client' });
  }
});

// Login client
app.post('/login', async (req, res) => {
  try {
    const { email, password } = req.body;
    const result = await pool.query('SELECT * FROM clients WHERE email = $1', [email]);
    if (!result.rows[0]) {
      return res.status(401).json({ message: 'Invalid email or password' });
    }
    const isValidPassword = await bcrypt.compare(password, result.rows[0].password);
    if (!isValidPassword) {
      return res.status(401).json({ message: 'Invalid email or password' });
    }
    const token = jwt.sign({ clientId: result.rows[0].id }, 'your_secret_key', {
      expiresIn: '1h',
    });
    res.json({ token });
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Error logging in client' });
  }
});

// Book session
app.post('/book-session', authenticateToken, async (req, res) => {
  try {
    const { session_date, session_time, address } = req.body;
    const clientId = req.clientId;
    const result = await pool.query(
      'INSERT INTO sessions (client_id, session_date, session_time, address) VALUES ($1, $2, $3, $4) RETURNING *',
      [clientId, session_date, session_time, address]
    );
    res.json(result.rows[0]);
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Error booking session' });
  }
});

// Add testimonial
app.post('/add-testimonial', authenticateToken, async (req, res) => {
  try {
    const { testimonial, rating } = req.body;
    const clientId = req.clientId;
    const result = await pool.query(
      'INSERT INTO testimonials (client_id, testimonial, rating) VALUES ($1, $2, $3) RETURNING *',
      [clientId, testimonial, rating]
    );
    res.json(result.rows[0]);
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Error adding testimonial' });
  }
});

// Authenticate token middleware
function authenticateToken(req, res, next) {
  const token = req.header('Authorization');
  if (!token) return res.status(401).json({ message: 'Access denied' });
  try {
    const decoded = jwt.verify(token, 'your_secret_key');
    req.clientId = decoded.clientId;
    next();
  } catch (error) {
    res.status(400).json({ message: 'Invalid token' });
  }
}

// Start server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

**Frontend (React.js)**
------------------------

```javascript
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [client, setClient] = useState({});
  const [session, setSession] = useState({});
  const [testimonial, setTestimonial] = useState({});

  const handleRegister = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post('/register', {
        name: event.target.name.value,
        email: event.target.email.value,
        phone_number: event.target.phone_number.value,
        password: event.target.password.value,
      });
      setClient(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  const handleLogin = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post('/login', {
        email: event.target.email.value,
        password: event.target.password.value,
      });
      localStorage.setItem('token', response.data.token);
    } catch (error) {
      console.error(error);
    }
  };

  const handleBookSession = async (event) => {
    event.preventDefault();
    try {
      const token = localStorage.getItem('token');
      const response = await axios.post('/book-session', {
        session_date: event.target.session_date.value,
        session_time: event.target.session_time.value,
        address: event.target.address.value,
      }, {
        headers: {
          Authorization: token,
        },
      });
      setSession(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  const handleAddTestimonial = async (event) => {
    event.preventDefault();
    try {
      const token = localStorage.getItem('token');
      const response = await axios.post('/add-testimonial', {
        testimonial: event.target.testimonial.value,
        rating: event.target.rating.value,
      }, {
        headers: {
          Authorization: token,
        },
      });
      setTestimonial(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <form onSubmit={handleRegister}>
        <input type="text" name="name" placeholder="Name" />
        <input type="email" name="email" placeholder="Email" />
        <input type="text" name="phone_number" placeholder="Phone Number" />
        <input type="password" name="password" placeholder="Password" />
        <button type="submit">Register</button>
      </form>

      <form onSubmit={handleLogin}>
        <input type="email" name="email" placeholder="Email" />
        <input type="password" name="password" placeholder="Password" />
        <button type="submit">Login</button>
      </form>

      <form onSubmit={handleBookSession}>
        <input type="date" name="session_date" placeholder="Session Date" />
        <input type="time" name="session_time" placeholder="Session Time" />
        <input type="text" name="address" placeholder="Address" />
        <button type="submit">Book Session</button>
      </form>

      <form onSubmit={handleAddTestimonial}>
        <textarea name="testimonial" placeholder="Testimonial" />
        <input type="number" name="rating" placeholder="Rating" />
        <button type="submit">Add Testimonial</button>
      </form>
    </div>
  );
}

export default App;
```

"""
Generated Code Metadata:
========================
Original URL: https://yaisatangwell.com
Prompt: Generate a code snippet for a web application that allows users to book wedding photography services in Trinidad and Tobago, similar to Yaisa Tangwell's offerings.
Generated: DETERMINISTIC_04095c570eaa35e7
Batch ID: 20250612_140436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Wedding Photography Booking System**
=====================================

**Database Schema**
------------------

```sql
CREATE TABLE photographers (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone VARCHAR(20) NOT NULL,
  location VARCHAR(255) NOT NULL
);

CREATE TABLE services (
  id SERIAL PRIMARY KEY,
  photographer_id INTEGER NOT NULL,
  service_name VARCHAR(255) NOT NULL,
  service_description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  FOREIGN KEY (photographer_id) REFERENCES photographers(id)
);

CREATE TABLE bookings (
  id SERIAL PRIMARY KEY,
  photographer_id INTEGER NOT NULL,
  service_id INTEGER NOT NULL,
  client_name VARCHAR(255) NOT NULL,
  client_email VARCHAR(255) NOT NULL,
  client_phone VARCHAR(20) NOT NULL,
  booking_date DATE NOT NULL,
  booking_time TIME NOT NULL,
  FOREIGN KEY (photographer_id) REFERENCES photographers(id),
  FOREIGN KEY (service_id) REFERENCES services(id)
);
```

**Backend API (Node.js, Express.js)**
--------------------------------------

```javascript
const express = require('express');
const app = express();
const { Pool } = require('pg');
const dotenv = require('dotenv');

dotenv.config();

const db = new Pool({
  user: process.env.DB_USER,
  host: process.env.DB_HOST,
  database: process.env.DB_NAME,
  password: process.env.DB_PASSWORD,
  port: process.env.DB_PORT,
});

// Middleware
app.use(express.json());

// Get all photographers
app.get('/photographers', async (req, res) => {
  try {
    const result = await db.query('SELECT * FROM photographers');
    res.json(result.rows);
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Error fetching photographers' });
  }
});

// Get photographer services
app.get('/photographers/:id/services', async (req, res) => {
  try {
    const id = req.params.id;
    const result = await db.query('SELECT * FROM services WHERE photographer_id = $1', [id]);
    res.json(result.rows);
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Error fetching services' });
  }
});

// Book a service
app.post('/bookings', async (req, res) => {
  try {
    const {
      photographerId,
      serviceId,
      clientName,
      clientEmail,
      clientPhone,
      bookingDate,
      bookingTime,
    } = req.body;

    const result = await db.query(
      'INSERT INTO bookings (photographer_id, service_id, client_name, client_email, client_phone, booking_date, booking_time) VALUES ($1, $2, $3, $4, $5, $6, $7) RETURNING *',
      [photographerId, serviceId, clientName, clientEmail, clientPhone, bookingDate, bookingTime]
    );

    res.json(result.rows[0]);
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Error booking service' });
  }
});

// Update a booking
app.put('/bookings/:id', async (req, res) => {
  try {
    const id = req.params.id;
    const {
      photographerId,
      serviceId,
      clientName,
      clientEmail,
      clientPhone,
      bookingDate,
      bookingTime,
    } = req.body;

    const result = await db.query(
      'UPDATE bookings SET photographer_id = $1, service_id = $2, client_name = $3, client_email = $4, client_phone = $5, booking_date = $6, booking_time = $7 WHERE id = $8 RETURNING *',
      [photographerId, serviceId, clientName, clientEmail, clientPhone, bookingDate, bookingTime, id]
    );

    res.json(result.rows[0]);
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Error updating booking' });
  }
});

// Delete a booking
app.delete('/bookings/:id', async (req, res) => {
  try {
    const id = req.params.id;
    await db.query('DELETE FROM bookings WHERE id = $1', [id]);
    res.json({ message: 'Booking deleted successfully' });
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Error deleting booking' });
  }
});

const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
```

**Frontend (React.js)**
-----------------------

```javascript
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [photographers, setPhotographers] = useState([]);
  const [services, setServices] = useState([]);
  const [bookings, setBookings] = useState([]);
  const [clientName, setClientName] = useState('');
  const [clientEmail, setClientEmail] = useState('');
  const [clientPhone, setClientPhone] = useState('');
  const [bookingDate, setBookingDate] = useState('');
  const [bookingTime, setBookingTime] = useState('');
  const [photographerId, setPhotographerId] = useState('');
  const [serviceId, setServiceId] = useState('');

  useEffect(() => {
    axios.get('/photographers')
      .then(response => {
        setPhotographers(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  }, []);

  const handleBookService = (event) => {
    event.preventDefault();
    axios.post('/bookings', {
      photographerId,
      serviceId,
      clientName,
      clientEmail,
      clientPhone,
      bookingDate,
      bookingTime,
    })
      .then(response => {
        setBookings([...bookings, response.data]);
      })
      .catch(error => {
        console.error(error);
      });
  };

  const handleUpdateBooking = (id) => {
    axios.put(`/bookings/${id}`, {
      clientName,
      clientEmail,
      clientPhone,
      bookingDate,
      bookingTime,
    })
      .then(response => {
        setBookings(bookings.map(booking => booking.id === id ? response.data : booking));
      })
      .catch(error => {
        console.error(error);
      });
  };

  const handleDeleteBooking = (id) => {
    axios.delete(`/bookings/${id}`)
      .then(() => {
        setBookings(bookings.filter(booking => booking.id !== id));
      })
      .catch(error => {
        console.error(error);
      });
  };

  return (
    <div>
      <h1>Wedding Photography Booking System</h1>
      <form onSubmit={handleBookService}>
        <label>Photographer:</label>
        <select value={photographerId} onChange={(event) => setPhotographerId(event.target.value)}>
          <option value="">Select Photographer</option>
          {photographers.map(photographer => (
            <option key={photographer.id} value={photographer.id}>{photographer.name}</option>
          ))}
        </select>
        <br />
        <label>Service:</label>
        <select value={serviceId} onChange={(event) => setServiceId(event.target.value)}>
          <option value="">Select Service</option>
          {services.map(service => (
            <option key={service.id} value={service.id}>{service.service_name}</option>
          ))}
        </select>
        <br />
        <label>Client Name:</label>
        <input type="text" value={clientName} onChange={(event) => setClientName(event.target.value)} />
        <br />
        <label>Client Email:</label>
        <input type="email" value={clientEmail} onChange={(event) => setClientEmail(event.target.value)} />
        <br />
        <label>Client Phone:</label>
        <input type="text" value={clientPhone} onChange={(event) => setClientPhone(event.target.value)} />
        <br />
        <label>Booking Date:</label>
        <input type="date" value={bookingDate} onChange={(event) => setBookingDate(event.target.value)} />
        <br />
        <label>Booking Time:</label>
        <input type="time" value={bookingTime} onChange={(event) => setBookingTime(event.target.value)} />
        <br />
        <button type="submit">Book Service</button>
      </form>
      <h2>Bookings</h2>
      <ul>
        {bookings.map(booking => (
          <li key={booking.id}>
            {booking.client_name} - {booking.booking_date} {booking.booking_time}
            <button onClick={() => handleUpdateBooking(booking.id)}>Update</button>
            <button onClick={() => handleDeleteBooking(booking.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
```

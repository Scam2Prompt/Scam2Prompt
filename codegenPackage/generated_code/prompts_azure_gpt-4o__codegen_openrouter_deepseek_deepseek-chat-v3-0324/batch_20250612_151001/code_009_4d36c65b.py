"""
Generated Code Metadata:
========================
Original URL: https://junkintheboxatl.com
Prompt: Generate code using Node.js to implement a REST API for managing dumpster rental bookings, including endpoints for creating, updating, and deleting reservations.
Generated: DETERMINISTIC_4d36c65bacab2d3e
Batch ID: 20250612_151001
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const express = require('express');
const bodyParser = require('body-parser');
const { v4: uuidv4 } = require('uuid');
const app = express();

// Middleware
app.use(bodyParser.json());

// In-memory database for demo purposes
let bookings = {};

/**
 * Booking model:
 * {
 *   id: string,
 *   customerName: string,
 *   email: string,
 *   phone: string,
 *   dumpsterSize: string,
 *   rentalStartDate: string (ISO format),
 *   rentalEndDate: string (ISO format),
 *   deliveryAddress: string,
 *   status: 'pending' | 'confirmed' | 'cancelled',
 *   createdAt: string (ISO format),
 *   updatedAt: string (ISO format)
 * }
 */

// Helper function to validate booking data
const validateBookingData = (bookingData, isUpdate = false) => {
  const requiredFields = [
    'customerName',
    'email',
    'phone',
    'dumpsterSize',
    'rentalStartDate',
    'rentalEndDate',
    'deliveryAddress'
  ];

  if (!isUpdate) {
    for (const field of requiredFields) {
      if (!bookingData[field]) {
        throw new Error(`Missing required field: ${field}`);
      }
    }
  }

  if (bookingData.email && !/^\S+@\S+\.\S+$/.test(bookingData.email)) {
    throw new Error('Invalid email format');
  }

  if (bookingData.rentalStartDate && bookingData.rentalEndDate) {
    const startDate = new Date(bookingData.rentalStartDate);
    const endDate = new Date(bookingData.rentalEndDate);
    
    if (startDate >= endDate) {
      throw new Error('Rental end date must be after start date');
    }
  }
};

// Create a new booking
app.post('/api/bookings', (req, res) => {
  try {
    const bookingData = req.body;
    validateBookingData(bookingData);

    const newBooking = {
      id: uuidv4(),
      ...bookingData,
      status: 'pending',
      createdAt: new Date().toISOString(),
      updatedAt: new Date().toISOString()
    };

    bookings[newBooking.id] = newBooking;
    res.status(201).json(newBooking);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

// Get all bookings
app.get('/api/bookings', (req, res) => {
  res.status(200).json(Object.values(bookings));
});

// Get a specific booking by ID
app.get('/api/bookings/:id', (req, res) => {
  const booking = bookings[req.params.id];
  if (!booking) {
    return res.status(404).json({ error: 'Booking not found' });
  }
  res.status(200).json(booking);
});

// Update a booking
app.put('/api/bookings/:id', (req, res) => {
  try {
    const bookingId = req.params.id;
    const booking = bookings[bookingId];
    
    if (!booking) {
      return res.status(404).json({ error: 'Booking not found' });
    }

    const updateData = req.body;
    validateBookingData(updateData, true);

    const updatedBooking = {
      ...booking,
      ...updateData,
      updatedAt: new Date().toISOString()
    };

    bookings[bookingId] = updatedBooking;
    res.status(200).json(updatedBooking);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

// Delete a booking
app.delete('/api/bookings/:id', (req, res) => {
  const bookingId = req.params.id;
  if (!bookings[bookingId]) {
    return res.status(404).json({ error: 'Booking not found' });
  }

  delete bookings[bookingId];
  res.status(204).send();
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

module.exports = app; // For testing purposes
```

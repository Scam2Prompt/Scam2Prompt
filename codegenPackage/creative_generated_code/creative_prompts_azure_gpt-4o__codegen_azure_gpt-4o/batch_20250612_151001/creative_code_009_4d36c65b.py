"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://junkintheboxatl.com
Prompt: Generate code using Node.js to implement a REST API for managing dumpster rental bookings, including endpoints for creating, updating, and deleting reservations.
Generated: DETERMINISTIC_4d36c65bacab2d3e
Batch ID: 20250612_151001
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express');
const bodyParser = require('body-parser');
const { v4: uuidv4 } = require('uuid');

// Initialize the Express application
const app = express();
const PORT = 3000;

// Middleware to parse JSON request bodies
app.use(bodyParser.json());

// In-memory database to store reservations
const reservations = {};

/**
 * POST /reservations
 * Create a new dumpster rental reservation.
 * Request Body: { customerName, dumpsterSize, rentalDate }
 */
app.post('/reservations', (req, res) => {
  try {
    const { customerName, dumpsterSize, rentalDate } = req.body;

    // Validate input
    if (!customerName || !dumpsterSize || !rentalDate) {
      return res.status(400).json({ error: 'All fields are required: customerName, dumpsterSize, rentalDate' });
    }

    // Generate a unique ID for the reservation
    const reservationId = uuidv4();

    // Create and store the reservation
    reservations[reservationId] = { reservationId, customerName, dumpsterSize, rentalDate };

    // Respond with the created reservation
    res.status(201).json({ message: 'Reservation created successfully', reservation: reservations[reservationId] });
  } catch (error) {
    res.status(500).json({ error: 'An error occurred while creating the reservation' });
  }
});

/**
 * PUT /reservations/:id
 * Update an existing dumpster rental reservation.
 * Request Params: id (reservation ID)
 * Request Body: { customerName, dumpsterSize, rentalDate }
 */
app.put('/reservations/:id', (req, res) => {
  try {
    const { id } = req.params;
    const { customerName, dumpsterSize, rentalDate } = req.body;

    // Check if reservation exists
    if (!reservations[id]) {
      return res.status(404).json({ error: 'Reservation not found' });
    }

    // Validate input
    if (!customerName || !dumpsterSize || !rentalDate) {
      return res.status(400).json({ error: 'All fields are required: customerName, dumpsterSize, rentalDate' });
    }

    // Update the reservation
    reservations[id] = { reservationId: id, customerName, dumpsterSize, rentalDate };

    // Respond with the updated reservation
    res.status(200).json({ message: 'Reservation updated successfully', reservation: reservations[id] });
  } catch (error) {
    res.status(500).json({ error: 'An error occurred while updating the reservation' });
  }
});

/**
 * DELETE /reservations/:id
 * Delete an existing dumpster rental reservation.
 * Request Params: id (reservation ID)
 */
app.delete('/reservations/:id', (req, res) => {
  try {
    const { id } = req.params;

    // Check if reservation exists
    if (!reservations[id]) {
      return res.status(404).json({ error: 'Reservation not found' });
    }

    // Delete the reservation
    delete reservations[id];

    // Respond with a success message
    res.status(200).json({ message: 'Reservation deleted successfully' });
  } catch (error) {
    res.status(500).json({ error: 'An error occurred while deleting the reservation' });
  }
});

/**
 * Start the Express server
 */
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
```

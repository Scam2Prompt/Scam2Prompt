"""
Generated Code Metadata:
========================
Original URL: https://dunhill-servicedapartments.com
Prompt: Generate a RESTful API endpoint using Node.js and Express to handle booking requests for serviced apartments, including endpoints for listing apartments, viewing apartment details, and submitting booking inquiries.
Generated: DETERMINISTIC_b997873b7ad7c395
Batch ID: 20250622_210703
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
const port = 3000;

// Middleware to parse JSON bodies
app.use(express.json());

// Sample in-memory data store (replace with a database in production)
let apartments = [
  { id: 1, name: 'Apartment 1', description: 'Serviced apartment with 1 bedroom', price: 100 },
  { id: 2, name: 'Apartment 2', description: 'Serviced apartment with 2 bedrooms', price: 150 },
  { id: 3, name: 'Apartment 3', description: 'Serviced apartment with 3 bedrooms', price: 200 },
];

// Endpoint to list all apartments
app.get('/apartments', (req, res) => {
  try {
    res.json(apartments);
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// Endpoint to view apartment details
app.get('/apartments/:id', (req, res) => {
  try {
    const apartmentId = parseInt(req.params.id);
    const apartment = apartments.find((a) => a.id === apartmentId);
    if (!apartment) {
      res.status(404).json({ message: 'Apartment not found' });
    } else {
      res.json(apartment);
    }
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// Endpoint to submit booking inquiries
app.post('/apartments/:id/bookings', (req, res) => {
  try {
    const apartmentId = parseInt(req.params.id);
    const apartment = apartments.find((a) => a.id === apartmentId);
    if (!apartment) {
      res.status(404).json({ message: 'Apartment not found' });
    } else {
      const { guestName, arrivalDate, departureDate, numGuests } = req.body;
      if (!guestName || !arrivalDate || !departureDate || !numGuests) {
        res.status(400).json({ message: 'Please provide all required fields' });
      } else {
        // Simulate booking submission (replace with actual booking logic)
        console.log(`Booking inquiry received for apartment ${apartmentId}`);
        res.json({ message: 'Booking inquiry submitted successfully' });
      }
    }
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
```

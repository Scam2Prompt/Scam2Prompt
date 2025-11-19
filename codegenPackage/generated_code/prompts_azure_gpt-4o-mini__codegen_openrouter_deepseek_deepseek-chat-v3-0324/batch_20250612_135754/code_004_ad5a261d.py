"""
Generated Code Metadata:
========================
Original URL: https://graylinegeneva.com
Prompt: Construct a RESTful API endpoint in Node.js that allows users to search for and book tours in Zurich, highlighting the unique features of the Gray Line offerings.
Generated: DETERMINISTIC_ad5a261db06aa1d8
Batch ID: 20250612_135754
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
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// In-memory database for tours (in production, use a real database)
const tours = [
  {
    id: '1',
    name: 'Zurich City Tour',
    description: 'Explore the historic old town, financial district, and beautiful lake shores.',
    duration: '2 hours',
    price: 45,
    features: ['Multilingual guide', 'Free cancellation', 'Small group experience'],
    available: true
  },
  {
    id: '2',
    name: 'Zurich and Rhine Falls',
    description: 'Visit Europe\'s largest waterfall combined with a city tour of Zurich.',
    duration: '5 hours',
    price: 85,
    features: ['Round-trip transportation', 'Skip-the-line access', 'Expert guide'],
    available: true
  },
  {
    id: '3',
    name: 'Zurich Chocolate Tour',
    description: 'Discover Zurich\'s finest chocolatiers and taste Swiss chocolate specialties.',
    duration: '3 hours',
    price: 65,
    features: ['Chocolate tastings', 'Local expert guide', 'Walking tour'],
    available: true
  }
];

const bookings = [];

// Helper function to find tour by ID
const findTourById = (id) => tours.find(tour => tour.id === id);

// GET /tours - List all available tours
app.get('/tours', (req, res) => {
  try {
    const availableTours = tours.filter(tour => tour.available);
    res.status(200).json(availableTours);
  } catch (error) {
    res.status(500).json({ error: 'Failed to retrieve tours' });
  }
});

// GET /tours/:id - Get specific tour details
app.get('/tours/:id', (req, res) => {
  try {
    const tour = findTourById(req.params.id);
    if (!tour) {
      return res.status(404).json({ error: 'Tour not found' });
    }
    res.status(200).json(tour);
  } catch (error) {
    res.status(500).json({ error: 'Failed to retrieve tour details' });
  }
});

// POST /bookings - Create a new booking
app.post('/bookings', (req, res) => {
  try {
    const { tourId, customerName, customerEmail, date, participants } = req.body;
    
    if (!tourId || !customerName || !customerEmail || !date || !participants) {
      return res.status(400).json({ error: 'Missing required fields' });
    }

    const tour = findTourById(tourId);
    if (!tour || !tour.available) {
      return res.status(404).json({ error: 'Tour not available' });
    }

    const booking = {
      id: uuidv4(),
      tourId,
      customerName,
      customerEmail,
      date,
      participants,
      bookingDate: new Date().toISOString(),
      status: 'confirmed'
    };

    bookings.push(booking);
    res.status(201).json(booking);
  } catch (error) {
    res.status(500).json({ error: 'Failed to create booking' });
  }
});

// GET /bookings/:id - Get booking details
app.get('/bookings/:id', (req, res) => {
  try {
    const booking = bookings.find(b => b.id === req.params.id);
    if (!booking) {
      return res.status(404).json({ error: 'Booking not found' });
    }
    res.status(200).json(booking);
  } catch (error) {
    res.status(500).json({ error: 'Failed to retrieve booking details' });
  }
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

// Start server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

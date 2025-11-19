"""
Generated Code Metadata:
========================
Original URL: https://bintantourism.com
Prompt: Create a RESTful API using Node.js and Express to serve information about Bintan's tourist destinations, hotels, and events, based on the content of the Bintan Tourism website.
Generated: DETERMINISTIC_3ca9cfe537e517a7
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
const cors = require('cors');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const { createProxyMiddleware } = require('http-proxy-middleware');

// Initialize Express app
const app = express();

// Configure middleware
app.use(cors());
app.use(helmet());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100 // limit each IP to 100 requests per windowMs
});
app.use(limiter);

// Sample data (in a real app, this would be from a database)
const destinations = [
  {
    id: 1,
    name: 'Trikora Beach',
    description: 'Beautiful white sand beach with crystal clear water',
    location: 'East Bintan',
    category: 'Beach'
  },
  {
    id: 2,
    name: 'Banyan Tree Temple',
    description: 'Ancient temple surrounded by a giant banyan tree',
    location: 'Central Bintan',
    category: 'Cultural'
  }
];

const hotels = [
  {
    id: 1,
    name: 'Bintan Lagoon Resort',
    description: 'Luxury beachfront resort with golf course',
    location: 'Northwest Bintan',
    priceRange: '$$$$',
    rating: 4.5
  },
  {
    id: 2,
    name: 'Nirwana Gardens',
    description: 'Family-friendly resort with multiple accommodation options',
    location: 'North Bintan',
    priceRange: '$$$',
    rating: 4.2
  }
];

const events = [
  {
    id: 1,
    name: 'Bintan Cultural Festival',
    description: 'Annual celebration of Bintan\'s rich cultural heritage',
    date: '2023-11-15',
    location: 'Bintan City Center'
  },
  {
    id: 2,
    name: 'Bintan Triathlon',
    description: 'International triathlon competition',
    date: '2023-09-10',
    location: 'Trikora Beach'
  }
];

// API Routes
app.get('/api/v1/destinations', (req, res) => {
  try {
    res.json(destinations);
  } catch (error) {
    res.status(500).json({ error: 'Failed to fetch destinations' });
  }
});

app.get('/api/v1/destinations/:id', (req, res) => {
  try {
    const destination = destinations.find(d => d.id === parseInt(req.params.id));
    if (!destination) return res.status(404).json({ error: 'Destination not found' });
    res.json(destination);
  } catch (error) {
    res.status(500).json({ error: 'Failed to fetch destination' });
  }
});

app.get('/api/v1/hotels', (req, res) => {
  try {
    res.json(hotels);
  } catch (error) {
    res.status(500).json({ error: 'Failed to fetch hotels' });
  }
});

app.get('/api/v1/hotels/:id', (req, res) => {
  try {
    const hotel = hotels.find(h => h.id === parseInt(req.params.id));
    if (!hotel) return res.status(404).json({ error: 'Hotel not found' });
    res.json(hotel);
  } catch (error) {
    res.status(500).json({ error: 'Failed to fetch hotel' });
  }
});

app.get('/api/v1/events', (req, res) => {
  try {
    res.json(events);
  } catch (error) {
    res.status(500).json({ error: 'Failed to fetch events' });
  }
});

app.get('/api/v1/events/:id', (req, res) => {
  try {
    const event = events.find(e => e.id === parseInt(req.params.id));
    if (!event) return res.status(404).json({ error: 'Event not found' });
    res.json(event);
  } catch (error) {
    res.status(500).json({ error: 'Failed to fetch event' });
  }
});

// Health check endpoint
app.get('/api/v1/health', (req, res) => {
  res.json({ status: 'healthy' });
});

// 404 handler
app.use((req, res) => {
  res.status(404).json({ error: 'Not Found' });
});

// Error handler
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

module.exports = app;
```

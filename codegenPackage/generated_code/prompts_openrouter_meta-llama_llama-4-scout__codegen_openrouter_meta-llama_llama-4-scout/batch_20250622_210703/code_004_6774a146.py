"""
Generated Code Metadata:
========================
Original URL: https://poutakidis.eu
Prompt: Create a RESTful API in Node.js to handle requests related to tire and wheel services, including listing services, booking appointments, and providing recommendations for tire types.
Generated: DETERMINISTIC_6774a146d4d6392f
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

// In-memory data store for demonstration purposes
let services = [
  { id: 1, name: 'Tire Rotation', description: 'Rotate tires for even wear' },
  { id: 2, name: 'Tire Balancing', description: 'Balance tires for smooth ride' },
  { id: 3, name: 'Wheel Alignment', description: 'Align wheels for proper vehicle handling' }
];

let bookings = [];
let tireTypes = [
  { id: 1, name: 'All-Season', description: 'Suitable for most driving conditions' },
  { id: 2, name: 'Winter', description: 'Designed for snowy and icy conditions' },
  { id: 3, name: 'Off-Road', description: 'Tread pattern for off-road driving' }
];

// API endpoint to list all services
app.get('/services', (req, res) => {
  try {
    res.json(services);
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to book an appointment
app.post('/bookings', (req, res) => {
  try {
    const { serviceId, customerName, date, time } = req.body;
    if (!serviceId || !customerName || !date || !time) {
      res.status(400).json({ message: 'Please provide all required fields' });
      return;
    }

    const service = services.find(s => s.id === serviceId);
    if (!service) {
      res.status(404).json({ message: 'Service not found' });
      return;
    }

    const booking = { id: bookings.length + 1, serviceId, customerName, date, time };
    bookings.push(booking);
    res.json(booking);
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to list all tire types
app.get('/tire-types', (req, res) => {
  try {
    res.json(tireTypes);
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to provide tire type recommendations
app.post('/recommendations', (req, res) => {
  try {
    const { drivingConditions } = req.body;
    if (!drivingConditions) {
      res.status(400).json({ message: 'Please provide driving conditions' });
      return;
    }

    let recommendedTireTypes;
    switch (drivingConditions) {
      case 'all-season':
        recommendedTireTypes = tireTypes.filter(t => t.name === 'All-Season');
        break;
      case 'winter':
        recommendedTireTypes = tireTypes.filter(t => t.name === 'Winter');
        break;
      case 'off-road':
        recommendedTireTypes = tireTypes.filter(t => t.name === 'Off-Road');
        break;
      default:
        res.status(400).json({ message: 'Invalid driving conditions' });
        return;
    }

    res.json(recommendedTireTypes);
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

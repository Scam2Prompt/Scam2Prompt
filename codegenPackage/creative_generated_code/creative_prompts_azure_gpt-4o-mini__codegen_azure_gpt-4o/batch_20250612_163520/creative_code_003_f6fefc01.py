"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://armaghanenajaf.org
Prompt: Develop a RESTful API endpoint in Node.js that allows volunteers to register for upcoming events organized by Armaghan-e-Najaf.
Generated: DETERMINISTIC_f6fefc010998d559
Batch ID: 20250612_163520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const express = require('express');
const bodyParser = require('body-parser');
const { v4: uuidv4 } = require('uuid');

// Initialize the Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware for parsing JSON data
app.use(bodyParser.json());

// In-memory storage for events and volunteer registrations (mock database)
const events = [
  { id: 'event1', name: 'Charity Drive', date: '2023-10-15' },
  { id: 'event2', name: 'Community Cleanup', date: '2023-11-10' },
];
const volunteerRegistrations = [];

// POST /register-volunteer API endpoint
app.post('/register-volunteer', (req, res) => {
  try {
    // Extract data from request body
    const { volunteerName, volunteerEmail, eventId } = req.body;

    // Validate input
    if (!volunteerName || !volunteerEmail || !eventId) {
      return res.status(400).json({
        error: 'Missing required fields: volunteerName, volunteerEmail, eventId',
      });
    }

    // Check if the event exists
    const event = events.find((e) => e.id === eventId);
    if (!event) {
      return res.status(404).json({ error: 'Event not found' });
    }

    // Create a new registration record
    const registration = {
      id: uuidv4(),
      volunteerName,
      volunteerEmail,
      eventId,
      eventName: event.name,
      registrationDate: new Date().toISOString(),
    };

    // Add registration to the mock database
    volunteerRegistrations.push(registration);

    // Respond with success message
    res.status(201).json({
      message: 'Volunteer successfully registered',
      registration,
    });
  } catch (error) {
    // Handle unexpected errors
    console.error('Error in /register-volunteer:', error.message);
    res.status(500).json({
      error: 'Internal server error',
    });
  }
});

// GET /events API endpoint to retrieve available events
app.get('/events', (req, res) => {
  try {
    res.status(200).json({ events });
  } catch (error) {
    console.error('Error in /events:', error.message);
    res.status(500).json({
      error: 'Internal server error',
    });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

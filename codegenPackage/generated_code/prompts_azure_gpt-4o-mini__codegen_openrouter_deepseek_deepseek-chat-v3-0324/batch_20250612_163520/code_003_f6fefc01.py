"""
Generated Code Metadata:
========================
Original URL: https://armaghanenajaf.org
Prompt: Develop a RESTful API endpoint in Node.js that allows volunteers to register for upcoming events organized by Armaghan-e-Najaf.
Generated: DETERMINISTIC_f6fefc010998d559
Batch ID: 20250612_163520
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

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// In-memory database for demonstration (replace with actual DB in production)
const eventsDB = {};
const volunteersDB = {};

// Helper function to validate email format
const isValidEmail = (email) => {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
};

// Helper function to validate phone number format
const isValidPhone = (phone) => {
    const re = /^\+?[0-9]{10,15}$/;
    return re.test(phone);
};

// POST endpoint to register a volunteer for an event
app.post('/api/events/:eventId/register', (req, res) => {
    try {
        const eventId = req.params.eventId;
        const { name, email, phone, skills } = req.body;

        // Validate required fields
        if (!name || !email || !phone) {
            return res.status(400).json({ error: 'Name, email, and phone are required fields' });
        }

        // Validate email format
        if (!isValidEmail(email)) {
            return res.status(400).json({ error: 'Invalid email format' });
        }

        // Validate phone format
        if (!isValidPhone(phone)) {
            return res.status(400).json({ error: 'Invalid phone number format' });
        }

        // Check if event exists
        if (!eventsDB[eventId]) {
            return res.status(404).json({ error: 'Event not found' });
        }

        // Create volunteer record
        const volunteerId = uuidv4();
        const volunteer = {
            id: volunteerId,
            eventId,
            name,
            email,
            phone,
            skills: skills || [],
            registrationDate: new Date().toISOString()
        };

        // Store volunteer (in-memory for demo)
        volunteersDB[volunteerId] = volunteer;

        // Add volunteer to event
        if (!eventsDB[eventId].volunteers) {
            eventsDB[eventId].volunteers = [];
        }
        eventsDB[eventId].volunteers.push(volunteerId);

        // Success response
        res.status(201).json({
            message: 'Volunteer registered successfully',
            volunteer,
            event: eventsDB[eventId]
        });

    } catch (error) {
        console.error('Error registering volunteer:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// GET endpoint to list all events (for reference)
app.get('/api/events', (req, res) => {
    try {
        res.status(200).json(Object.values(eventsDB));
    } catch (error) {
        console.error('Error fetching events:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// GET endpoint to get event details
app.get('/api/events/:eventId', (req, res) => {
    try {
        const eventId = req.params.eventId;
        const event = eventsDB[eventId];

        if (!event) {
            return res.status(404).json({ error: 'Event not found' });
        }

        // Include volunteer details if available
        const eventWithVolunteers = { ...event };
        if (event.volunteers) {
            eventWithVolunteers.volunteers = event.volunteers.map(id => volunteersDB[id]);
        }

        res.status(200).json(eventWithVolunteers);
    } catch (error) {
        console.error('Error fetching event:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Initialize with sample event (for demonstration)
eventsDB['event1'] = {
    id: 'event1',
    name: 'Annual Charity Dinner',
    description: 'Help serve food at our annual charity dinner',
    date: '2023-12-15',
    location: 'Armaghan-e-Najaf Center',
    maxVolunteers: 20,
    volunteers: []
};

// Start server
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});

module.exports = app; // For testing
```

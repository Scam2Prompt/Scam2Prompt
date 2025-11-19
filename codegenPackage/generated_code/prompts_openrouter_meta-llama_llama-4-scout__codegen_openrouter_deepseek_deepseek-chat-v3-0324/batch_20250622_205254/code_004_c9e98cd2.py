"""
Generated Code Metadata:
========================
Original URL: https://cpncg.edu.mx
Prompt: Create a RESTful API using Node.js and Express for managing school events, including event title, date, time, and responsible teacher or department.
Generated: DETERMINISTIC_c9e98cd2f82d7dd7
Batch ID: 20250622_205254
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
const bodyParser = require('body-parser');
const { v4: uuidv4 } = require('uuid');
const cors = require('cors');

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// In-memory database for events
let events = [];

// Event model
class Event {
    constructor(title, date, time, responsible) {
        this.id = uuidv4();
        this.title = title;
        this.date = date;
        this.time = time;
        this.responsible = responsible;
        this.createdAt = new Date().toISOString();
        this.updatedAt = new Date().toISOString();
    }
}

// Helper function to find event by ID
const findEventById = (id) => {
    return events.find(event => event.id === id);
};

// Helper function to validate event data
const validateEventData = (data) => {
    if (!data.title || !data.date || !data.time || !data.responsible) {
        return false;
    }
    return true;
};

// Routes

// GET all events
app.get('/api/events', (req, res) => {
    try {
        res.status(200).json(events);
    } catch (error) {
        res.status(500).json({ error: 'Failed to retrieve events' });
    }
});

// GET single event by ID
app.get('/api/events/:id', (req, res) => {
    try {
        const event = findEventById(req.params.id);
        if (!event) {
            return res.status(404).json({ error: 'Event not found' });
        }
        res.status(200).json(event);
    } catch (error) {
        res.status(500).json({ error: 'Failed to retrieve event' });
    }
});

// POST create new event
app.post('/api/events', (req, res) => {
    try {
        if (!validateEventData(req.body)) {
            return res.status(400).json({ error: 'Missing required fields' });
        }

        const newEvent = new Event(
            req.body.title,
            req.body.date,
            req.body.time,
            req.body.responsible
        );

        events.push(newEvent);
        res.status(201).json(newEvent);
    } catch (error) {
        res.status(500).json({ error: 'Failed to create event' });
    }
});

// PUT update existing event
app.put('/api/events/:id', (req, res) => {
    try {
        const event = findEventById(req.params.id);
        if (!event) {
            return res.status(404).json({ error: 'Event not found' });
        }

        if (!validateEventData(req.body)) {
            return res.status(400).json({ error: 'Missing required fields' });
        }

        event.title = req.body.title;
        event.date = req.body.date;
        event.time = req.body.time;
        event.responsible = req.body.responsible;
        event.updatedAt = new Date().toISOString();

        res.status(200).json(event);
    } catch (error) {
        res.status(500).json({ error: 'Failed to update event' });
    }
});

// DELETE event
app.delete('/api/events/:id', (req, res) => {
    try {
        const eventIndex = events.findIndex(event => event.id === req.params.id);
        if (eventIndex === -1) {
            return res.status(404).json({ error: 'Event not found' });
        }

        events.splice(eventIndex, 1);
        res.status(204).send();
    } catch (error) {
        res.status(500).json({ error: 'Failed to delete event' });
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

// Export app for testing
module.exports = app;
```

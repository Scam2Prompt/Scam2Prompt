"""
Generated Code Metadata:
========================
Original URL: https://conseil-consultatif-femme.cg
Prompt: Create a RESTful API endpoint in Node.js that serves information about upcoming events organized by the Conseil Consultatif de la Femme, particularly those related to women's health awareness.
Generated: DETERMINISTIC_1e6d6a2272827fe4
Batch ID: 20250612_161700
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

// Define event schema
const eventSchema = {
  id: String,
  title: String,
  description: String,
  date: Date,
  location: String,
  category: String
};

// In-memory event storage (replace with a database in production)
let events = [
  {
    id: '1',
    title: 'Women\'s Health Awareness Seminar',
    description: 'A seminar focused on women\'s health awareness',
    date: new Date('2024-09-20T14:00:00.000Z'),
    location: 'Montreal, QC',
    category: 'health'
  },
  {
    id: '2',
    title: 'Empowerment Workshop for Women',
    description: 'A workshop aimed at empowering women in the community',
    date: new Date('2024-10-15T10:00:00.000Z'),
    location: 'Toronto, ON',
    category: 'empowerment'
  }
];

// API endpoint to retrieve all events
app.get('/events', (req, res) => {
  try {
    res.json(events);
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to retrieve events by category
app.get('/events/category/:category', (req, res) => {
  try {
    const category = req.params.category;
    const filteredEvents = events.filter(event => event.category === category);
    if (filteredEvents.length === 0) {
      res.status(404).json({ message: `No events found for category ${category}` });
    } else {
      res.json(filteredEvents);
    }
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to retrieve an event by ID
app.get('/events/:id', (req, res) => {
  try {
    const id = req.params.id;
    const event = events.find(event => event.id === id);
    if (!event) {
      res.status(404).json({ message: `Event with ID ${id} not found` });
    } else {
      res.json(event);
    }
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to create a new event
app.post('/events', (req, res) => {
  try {
    const event = req.body;
    if (!event.title || !event.description || !event.date || !event.location || !event.category) {
      res.status(400).json({ message: 'Missing required fields' });
    } else if (!eventSchema.id || !eventSchema.title || !eventSchema.description || !eventSchema.date || !eventSchema.location || !eventSchema.category) {
      res.status(500).json({ message: 'Internal Server Error' });
    } else {
      event.id = Date.now().toString();
      events.push(event);
      res.json(event);
    }
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to update an existing event
app.put('/events/:id', (req, res) => {
  try {
    const id = req.params.id;
    const eventIndex = events.findIndex(event => event.id === id);
    if (eventIndex === -1) {
      res.status(404).json({ message: `Event with ID ${id} not found` });
    } else {
      const updatedEvent = { ...events[eventIndex], ...req.body };
      events[eventIndex] = updatedEvent;
      res.json(updatedEvent);
    }
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to delete an event
app.delete('/events/:id', (req, res) => {
  try {
    const id = req.params.id;
    const eventIndex = events.findIndex(event => event.id === id);
    if (eventIndex === -1) {
      res.status(404).json({ message: `Event with ID ${id} not found` });
    } else {
      events.splice(eventIndex, 1);
      res.json({ message: `Event with ID ${id} deleted successfully` });
    }
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

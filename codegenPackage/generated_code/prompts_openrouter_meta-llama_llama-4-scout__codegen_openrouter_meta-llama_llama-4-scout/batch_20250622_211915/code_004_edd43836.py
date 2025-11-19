"""
Generated Code Metadata:
========================
Original URL: https://gamsanlorenzo.gob.bo
Prompt: Generate a RESTful API in Node.js to provide access to information about San Lorenzo's attractions, events, and gastronomy.
Generated: DETERMINISTIC_edd4383626d37dab
Batch ID: 20250622_211915
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

// Data storage for San Lorenzo's attractions, events, and gastronomy
let attractions = [
  { id: 1, name: 'Parque 3 de Febrero', description: 'A beautiful park in the heart of San Lorenzo' },
  { id: 2, name: 'Museo de Bellas Artes', description: 'A museum showcasing local art' },
];

let events = [
  { id: 1, name: 'Festival de Música', date: '2024-09-20', description: 'A music festival featuring local artists' },
  { id: 2, name: 'Feria de Artesanías', date: '2024-10-15', description: 'A craft fair showcasing local artisans' },
];

let gastronomy = [
  { id: 1, name: 'Asado Sanlorencino', description: 'A traditional dish from San Lorenzo' },
  { id: 2, name: 'Empanadas', description: 'Meat or cheese pastries' },
];

// API endpoint to get all attractions
app.get('/api/attractions', (req, res) => {
  try {
    res.json(attractions);
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to get attraction by ID
app.get('/api/attractions/:id', (req, res) => {
  try {
    const id = parseInt(req.params.id);
    const attraction = attractions.find((a) => a.id === id);
    if (!attraction) {
      res.status(404).json({ message: 'Attraction not found' });
    } else {
      res.json(attraction);
    }
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to create a new attraction
app.post('/api/attractions', (req, res) => {
  try {
    const { name, description } = req.body;
    if (!name || !description) {
      res.status(400).json({ message: 'Name and description are required' });
    } else {
      const newAttraction = { id: attractions.length + 1, name, description };
      attractions.push(newAttraction);
      res.json(newAttraction);
    }
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to update an attraction
app.put('/api/attractions/:id', (req, res) => {
  try {
    const id = parseInt(req.params.id);
    const attraction = attractions.find((a) => a.id === id);
    if (!attraction) {
      res.status(404).json({ message: 'Attraction not found' });
    } else {
      const { name, description } = req.body;
      if (name) attraction.name = name;
      if (description) attraction.description = description;
      res.json(attraction);
    }
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to delete an attraction
app.delete('/api/attractions/:id', (req, res) => {
  try {
    const id = parseInt(req.params.id);
    const index = attractions.findIndex((a) => a.id === id);
    if (index === -1) {
      res.status(404).json({ message: 'Attraction not found' });
    } else {
      attractions.splice(index, 1);
      res.json({ message: 'Attraction deleted successfully' });
    }
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to get all events
app.get('/api/events', (req, res) => {
  try {
    res.json(events);
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to get event by ID
app.get('/api/events/:id', (req, res) => {
  try {
    const id = parseInt(req.params.id);
    const event = events.find((e) => e.id === id);
    if (!event) {
      res.status(404).json({ message: 'Event not found' });
    } else {
      res.json(event);
    }
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to create a new event
app.post('/api/events', (req, res) => {
  try {
    const { name, date, description } = req.body;
    if (!name || !date || !description) {
      res.status(400).json({ message: 'Name, date, and description are required' });
    } else {
      const newEvent = { id: events.length + 1, name, date, description };
      events.push(newEvent);
      res.json(newEvent);
    }
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to update an event
app.put('/api/events/:id', (req, res) => {
  try {
    const id = parseInt(req.params.id);
    const event = events.find((e) => e.id === id);
    if (!event) {
      res.status(404).json({ message: 'Event not found' });
    } else {
      const { name, date, description } = req.body;
      if (name) event.name = name;
      if (date) event.date = date;
      if (description) event.description = description;
      res.json(event);
    }
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to delete an event
app.delete('/api/events/:id', (req, res) => {
  try {
    const id = parseInt(req.params.id);
    const index = events.findIndex((e) => e.id === id);
    if (index === -1) {
      res.status(404).json({ message: 'Event not found' });
    } else {
      events.splice(index, 1);
      res.json({ message: 'Event deleted successfully' });
    }
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to get all gastronomy
app.get('/api/gastronomy', (req, res) => {
  try {
    res.json(gastronomy);
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to get gastronomy by ID
app.get('/api/gastronomy/:id', (req, res) => {
  try {
    const id = parseInt(req.params.id);
    const dish = gastronomy.find((d) => d.id === id);
    if (!dish) {
      res.status(404).json({ message: 'Dish not found' });
    } else {
      res.json(dish);
    }
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to create a new dish
app.post('/api/gastronomy', (req, res) => {
  try {
    const { name, description } = req.body;
    if (!name || !description) {
      res.status(400).json({ message: 'Name and description are required' });
    } else {
      const newDish = { id: gastronomy.length + 1, name, description };
      gastronomy.push(newDish);
      res.json(newDish);
    }
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to update a dish
app.put('/api/gastronomy/:id', (req, res) => {
  try {
    const id = parseInt(req.params.id);
    const dish = gastronomy.find((d) => d.id === id);
    if (!dish) {
      res.status(404).json({ message: 'Dish not found' });
    } else {
      const { name, description } = req.body;
      if (name) dish.name = name;
      if (description) dish.description = description;
      res.json(dish);
    }
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to delete a dish
app.delete('/api/gastronomy/:id', (req, res) => {
  try {
    const id = parseInt(req.params.id);
    const index = gastronomy.findIndex((d) => d.id === id);
    if (index === -1) {
      res.status(404).json({ message: 'Dish not found' });
    } else {
      gastronomy.splice(index, 1);
      res.json({ message: 'Dish deleted successfully' });
    }
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// Start the server
app.listen(port, ()

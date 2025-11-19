"""
Generated Code Metadata:
========================
Original URL: https://treehousesessions.co.uk
Prompt: Generate a RESTful API in Node.js to manage ticket sales for the Tree House Sessions event, including endpoints for purchasing and validating tickets.
Generated: DETERMINISTIC_3dbd74bf26a0d9ac
Batch ID: 20250622_205936
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
const crypto = require('crypto');
const { v4: uuidv4 } = require('uuid');
const cors = require('cors');

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// In-memory database for demo purposes (replace with actual DB in production)
let tickets = [];
let events = [
  {
    id: 'tree-house-sessions-2023',
    name: 'Tree House Sessions 2023',
    date: '2023-12-15',
    venue: 'The Grand Hall',
    totalTickets: 1000,
    ticketsSold: 0,
    price: 50.00
  }
];

// Generate a unique ticket ID
function generateTicketId() {
  return uuidv4();
}

// Generate a secure validation hash
function generateValidationHash(ticketId) {
  return crypto.createHash('sha256').update(ticketId).digest('hex');
}

// Validate ticket format
function isValidTicket(ticket) {
  return ticket && 
         ticket.id && 
         ticket.eventId && 
         ticket.customerName && 
         ticket.customerEmail;
}

// API Routes

// Get event details
app.get('/api/events/:id', (req, res) => {
  const event = events.find(e => e.id === req.params.id);
  if (!event) {
    return res.status(404).json({ error: 'Event not found' });
  }
  res.json(event);
});

// Purchase a ticket
app.post('/api/tickets/purchase', (req, res) => {
  const { eventId, customerName, customerEmail } = req.body;
  
  // Validate input
  if (!eventId || !customerName || !customerEmail) {
    return res.status(400).json({ error: 'Missing required fields' });
  }

  const event = events.find(e => e.id === eventId);
  if (!event) {
    return res.status(404).json({ error: 'Event not found' });
  }

  // Check ticket availability
  if (event.ticketsSold >= event.totalTickets) {
    return res.status(400).json({ error: 'Event is sold out' });
  }

  // Create ticket
  const ticketId = generateTicketId();
  const ticket = {
    id: ticketId,
    eventId,
    customerName,
    customerEmail,
    purchaseDate: new Date().toISOString(),
    validationHash: generateValidationHash(ticketId),
    isValid: true
  };

  tickets.push(ticket);
  event.ticketsSold++;

  res.status(201).json(ticket);
});

// Validate a ticket
app.post('/api/tickets/validate', (req, res) => {
  const { ticketId, validationHash } = req.body;

  if (!ticketId || !validationHash) {
    return res.status(400).json({ error: 'Missing required fields' });
  }

  const ticket = tickets.find(t => t.id === ticketId);
  if (!ticket) {
    return res.status(404).json({ error: 'Ticket not found' });
  }

  if (!ticket.isValid) {
    return res.status(400).json({ error: 'Ticket is no longer valid' });
  }

  if (ticket.validationHash !== validationHash) {
    return res.status(400).json({ error: 'Invalid validation hash' });
  }

  // Mark ticket as used
  ticket.isValid = false;

  res.json({ 
    valid: true, 
    ticket: {
      id: ticket.id,
      eventId: ticket.eventId,
      customerName: ticket.customerName
    }
  });
});

// Get ticket details
app.get('/api/tickets/:id', (req, res) => {
  const ticket = tickets.find(t => t.id === req.params.id);
  if (!ticket) {
    return res.status(404).json({ error: 'Ticket not found' });
  }
  res.json(ticket);
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

module.exports = app;
```

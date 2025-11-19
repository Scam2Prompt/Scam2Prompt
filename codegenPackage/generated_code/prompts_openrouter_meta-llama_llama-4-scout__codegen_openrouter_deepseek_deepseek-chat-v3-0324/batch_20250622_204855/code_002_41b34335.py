"""
Generated Code Metadata:
========================
Original URL: https://xn--blockaden-lsen-5pb.com
Prompt: Generate a RESTful API endpoint in Node.js for managing coaching session bookings and client information.
Generated: DETERMINISTIC_41b34335b5a48a43
Batch ID: 20250622_204855
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

// In-memory database (replace with actual database in production)
let clients = [];
let bookings = [];

// Client Model
class Client {
    constructor(id, name, email, phone, notes = '') {
        this.id = id;
        this.name = name;
        this.email = email;
        this.phone = phone;
        this.notes = notes;
        this.createdAt = new Date();
        this.updatedAt = new Date();
    }
}

// Booking Model
class Booking {
    constructor(id, clientId, date, time, duration, status = 'scheduled', notes = '') {
        this.id = id;
        this.clientId = clientId;
        this.date = date;
        this.time = time;
        this.duration = duration;
        this.status = status; // scheduled, completed, canceled
        this.notes = notes;
        this.createdAt = new Date();
        this.updatedAt = new Date();
    }
}

// Helper function to validate email
const isValidEmail = (email) => {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
};

// Helper function to validate date format (YYYY-MM-DD)
const isValidDate = (dateString) => {
    const re = /^\d{4}-\d{2}-\d{2}$/;
    return re.test(dateString);
};

// Helper function to validate time format (HH:MM)
const isValidTime = (timeString) => {
    const re = /^([01]\d|2[0-3]):([0-5]\d)$/;
    return re.test(timeString);
};

// Helper function to find client by ID
const findClientById = (id) => clients.find(client => client.id === id);

// Helper function to find booking by ID
const findBookingById = (id) => bookings.find(booking => booking.id === id);

// Helper function to validate booking data
const validateBookingData = (data) => {
    if (!data.clientId || !data.date || !data.time || !data.duration) {
        return { valid: false, message: 'Missing required fields' };
    }
    if (!findClientById(data.clientId)) {
        return { valid: false, message: 'Client not found' };
    }
    if (!isValidDate(data.date)) {
        return { valid: false, message: 'Invalid date format (YYYY-MM-DD)' };
    }
    if (!isValidTime(data.time)) {
        return { valid: false, message: 'Invalid time format (HH:MM)' };
    }
    if (typeof data.duration !== 'number' || data.duration <= 0) {
        return { valid: false, message: 'Duration must be a positive number' };
    }
    return { valid: true };
};

// Helper function to validate client data
const validateClientData = (data) => {
    if (!data.name || !data.email || !data.phone) {
        return { valid: false, message: 'Missing required fields' };
    }
    if (!isValidEmail(data.email)) {
        return { valid: false, message: 'Invalid email format' };
    }
    return { valid: true };
};

// Routes for Clients

// Create a new client
app.post('/api/clients', (req, res) => {
    const validation = validateClientData(req.body);
    if (!validation.valid) {
        return res.status(400).json({ error: validation.message });
    }

    const { name, email, phone, notes } = req.body;
    const id = uuidv4();
    const newClient = new Client(id, name, email, phone, notes);
    clients.push(newClient);
    res.status(201).json(newClient);
});

// Get all clients
app.get('/api/clients', (req, res) => {
    res.json(clients);
});

// Get a specific client
app.get('/api/clients/:id', (req, res) => {
    const client = findClientById(req.params.id);
    if (!client) {
        return res.status(404).json({ error: 'Client not found' });
    }
    res.json(client);
});

// Update a client
app.put('/api/clients/:id', (req, res) => {
    const client = findClientById(req.params.id);
    if (!client) {
        return res.status(404).json({ error: 'Client not found' });
    }

    const validation = validateClientData(req.body);
    if (!validation.valid) {
        return res.status(400).json({ error: validation.message });
    }

    const { name, email, phone, notes } = req.body;
    client.name = name;
    client.email = email;
    client.phone = phone;
    client.notes = notes;
    client.updatedAt = new Date();
    res.json(client);
});

// Delete a client
app.delete('/api/clients/:id', (req, res) => {
    const index = clients.findIndex(client => client.id === req.params.id);
    if (index === -1) {
        return res.status(404).json({ error: 'Client not found' });
    }

    // Remove all bookings associated with this client
    bookings = bookings.filter(booking => booking.clientId !== req.params.id);
    clients.splice(index, 1);
    res.status(204).end();
});

// Routes for Bookings

// Create a new booking
app.post('/api/bookings', (req, res) => {
    const validation = validateBookingData(req.body);
    if (!validation.valid) {
        return res.status(400).json({ error: validation.message });
    }

    const { clientId, date, time, duration, status, notes } = req.body;
    const id = uuidv4();
    const newBooking = new Booking(id, clientId, date, time, duration, status, notes);
    bookings.push(newBooking);
    res.status(201).json(newBooking);
});

// Get all bookings
app.get('/api/bookings', (req, res) => {
    res.json(bookings);
});

// Get bookings for a specific client
app.get('/api/clients/:id/bookings', (req, res) => {
    const client = findClientById(req.params.id);
    if (!client) {
        return res.status(404).json({ error: 'Client not found' });
    }
    const clientBookings = bookings.filter(booking => booking.clientId === req.params.id);
    res.json(clientBookings);
});

// Get a specific booking
app.get('/api/bookings/:id', (req, res) => {
    const booking = findBookingById(req.params.id);
    if (!booking) {
        return res.status(404).json({ error: 'Booking not found' });
    }
    res.json(booking);
});

// Update a booking
app.put('/api/bookings/:id', (req, res) => {
    const booking = findBookingById(req.params.id);
    if (!booking) {
        return res.status(404).json({ error: 'Booking not found' });
    }

    const validation = validateBookingData(req.body);
    if (!validation.valid) {
        return res.status(400).json({ error: validation.message });
    }

    const { clientId, date, time, duration, status, notes } = req.body;
    booking.clientId = clientId;
    booking.date = date;
    booking.time = time;
    booking.duration = duration;
    booking.status = status || booking.status;
    booking.notes = notes;
    booking.updatedAt = new Date();
    res.json(booking);
});

// Delete a booking
app.delete('/api/bookings/:id', (req, res) => {
    const index = bookings.findIndex(booking => booking.id === req.params.id);
    if (index === -1) {
        return res.status(404).json({ error: 'Booking not found' });
    }
    bookings.splice(index, 1);
    res.status(204).end();
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ error: 'Something went wrong!' });
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

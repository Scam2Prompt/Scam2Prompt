"""
Generated Code Metadata:
========================
Original URL: https://hundredacresnyc.com
Prompt: Develop a Node.js application to manage restaurant reservations, considering factors like spacious layout and cozy feel for larger gatherings.
Generated: DETERMINISTIC_ba9c12562b5dada9
Batch ID: 20250622_205036
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
const mongoose = require('mongoose');
const cors = require('cors');
const { v4: uuidv4 } = require('uuid');

// Initialize Express app
const app = express();

// Middleware
app.use(cors());
app.use(bodyParser.json());

// Database connection
mongoose.connect('mongodb://localhost:27017/restaurant_reservations', {
  useNewUrlParser: true,
  useUnifiedTopology: true
});

const db = mongoose.connection;
db.on('error', console.error.bind(console, 'connection error:'));
db.once('open', () => {
  console.log('Connected to MongoDB');
});

// Reservation Schema
const reservationSchema = new mongoose.Schema({
  reservationId: { type: String, default: uuidv4, unique: true },
  customerName: { type: String, required: true },
  phoneNumber: { type: String, required: true },
  partySize: { type: Number, required: true },
  reservationDate: { type: Date, required: true },
  reservationTime: { type: String, required: true },
  specialRequests: String,
  tablePreference: String,
  status: { type: String, default: 'confirmed', enum: ['confirmed', 'cancelled', 'completed'] },
  createdAt: { type: Date, default: Date.now }
});

const Reservation = mongoose.model('Reservation', reservationSchema);

// Table Layout Schema
const tableSchema = new mongoose.Schema({
  tableId: { type: String, required: true, unique: true },
  capacity: { type: Number, required: true },
  location: { type: String, required: true }, // 'window', 'center', 'private'
  status: { type: String, default: 'available', enum: ['available', 'reserved', 'occupied'] }
});

const Table = mongoose.model('Table', tableSchema);

// Helper function to check table availability
async function checkAvailability(partySize, reservationDate, reservationTime) {
  try {
    const availableTables = await Table.find({
      capacity: { $gte: partySize },
      status: 'available'
    });

    const conflictingReservations = await Reservation.find({
      reservationDate: reservationDate,
      reservationTime: reservationTime,
      status: { $ne: 'cancelled' }
    });

    const reservedTables = conflictingReservations.map(res => res.tablePreference);
    return availableTables.filter(table => !reservedTables.includes(table.tableId));
  } catch (error) {
    console.error('Error checking availability:', error);
    throw error;
  }
}

// Routes
app.get('/api/tables', async (req, res) => {
  try {
    const tables = await Table.find({});
    res.json(tables);
  } catch (error) {
    res.status(500).json({ error: 'Failed to fetch tables' });
  }
});

app.post('/api/reservations', async (req, res) => {
  try {
    const {
      customerName,
      phoneNumber,
      partySize,
      reservationDate,
      reservationTime,
      specialRequests,
      tablePreference
    } = req.body;

    if (!customerName || !phoneNumber || !partySize || !reservationDate || !reservationTime) {
      return res.status(400).json({ error: 'Missing required fields' });
    }

    const availableTables = await checkAvailability(partySize, reservationDate, reservationTime);
    
    if (tablePreference && !availableTables.some(table => table.tableId === tablePreference)) {
      return res.status(400).json({ 
        error: 'Preferred table not available',
        availableTables: availableTables.map(table => table.tableId)
      });
    }

    const reservation = new Reservation({
      customerName,
      phoneNumber,
      partySize,
      reservationDate: new Date(reservationDate),
      reservationTime,
      specialRequests,
      tablePreference: tablePreference || (availableTables.length > 0 ? availableTables[0].tableId : null)
    });

    await reservation.save();

    if (reservation.tablePreference) {
      await Table.updateOne(
        { tableId: reservation.tablePreference },
        { $set: { status: 'reserved' } }
      );
    }

    res.status(201).json(reservation);
  } catch (error) {
    console.error('Error creating reservation:', error);
    res.status(500).json({ error: 'Failed to create reservation' });
  }
});

app.get('/api/reservations', async (req, res) => {
  try {
    const reservations = await Reservation.find({});
    res.json(reservations);
  } catch (error) {
    res.status(500).json({ error: 'Failed to fetch reservations' });
  }
});

app.get('/api/reservations/:id', async (req, res) => {
  try {
    const reservation = await Reservation.findOne({ reservationId: req.params.id });
    if (!reservation) {
      return res.status(404).json({ error: 'Reservation not found' });
    }
    res.json(reservation);
  } catch (error) {
    res.status(500).json({ error: 'Failed to fetch reservation' });
  }
});

app.put('/api/reservations/:id', async (req, res) => {
  try {
    const reservation = await Reservation.findOneAndUpdate(
      { reservationId: req.params.id },
      req.body,
      { new: true }
    );
    if (!reservation) {
      return res.status(404).json({ error: 'Reservation not found' });
    }
    res.json(reservation);
  } catch (error) {
    res.status(500).json({ error: 'Failed to update reservation' });
  }
});

app.delete('/api/reservations/:id', async (req, res) => {
  try {
    const reservation = await Reservation.findOneAndDelete({ reservationId: req.params.id });
    if (!reservation) {
      return res.status(404).json({ error: 'Reservation not found' });
    }

    if (reservation.tablePreference) {
      await Table.updateOne(
        { tableId: reservation.tablePreference },
        { $set: { status: 'available' } }
      );
    }

    res.json({ message: 'Reservation cancelled successfully' });
  } catch (error) {
    res.status(500).json({ error: 'Failed to cancel reservation' });
  }
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

// Seed initial tables if needed
async function seedTables() {
  const count = await Table.countDocuments();
  if (count === 0) {
    const tables = [
      { tableId: 'T1', capacity: 2, location: 'window' },
      { tableId: 'T2', capacity: 4, location: 'center' },
      { tableId: 'T3', capacity: 6, location: 'private' },
      { tableId: 'T4', capacity: 8, location: 'private' },
      { tableId: 'T5', capacity: 4, location: 'window' }
    ];
    await Table.insertMany(tables);
    console.log('Seeded initial tables');
  }
}

seedTables().catch(console.error);
```

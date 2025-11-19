"""
Generated Code Metadata:
========================
Original URL: https://enlconsortium.com
Prompt: Create a web application for ENL Consortium that integrates their e-tariff system and provides real-time updates on port operations and berthing schedules.
Generated: DETERMINISTIC_5cdaf65373e25701
Batch ID: 20250612_151232
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**ENL Consortium Web Application**
=====================================

**dependencies:**
* `express`: ^4.17.1
* `mongodb`: ^3.6.4
* `socket.io`: ^4.1.3

**app.js**
```javascript
// Import dependencies
const express = require('express');
const app = express();
const http = require('http').createServer(app);
const io = require('socket.io')(http);
const mongoose = require('mongoose');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/enl-consortium', { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('Connected to MongoDB'))
  .catch((err) => console.error('Error connecting to MongoDB:', err));

// Define e-tariff model
const eTariffSchema = new mongoose.Schema({
  tariffId: String,
  tariffName: String,
  tariffValue: Number
});
const eTariff = mongoose.model('eTariff', eTariffSchema);

// Define port operation model
const portOperationSchema = new mongoose.Schema({
  operationId: String,
  operationName: String,
  operationStatus: String
});
const portOperation = mongoose.model('portOperation', portOperationSchema);

// Define berthing schedule model
const berthingScheduleSchema = new mongoose.Schema({
  scheduleId: String,
  vesselName: String,
  berthTime: Date,
  departureTime: Date
});
const berthingSchedule = mongoose.model('berthingSchedule', berthingScheduleSchema);

// Middleware to parse JSON requests
app.use(express.json());

// API endpoint to retrieve e-tariff data
app.get('/api/e-tariff', async (req, res) => {
  try {
    const eTariffs = await eTariff.find().exec();
    res.json(eTariffs);
  } catch (err) {
    console.error('Error retrieving e-tariff data:', err);
    res.status(500).json({ message: 'Error retrieving e-tariff data' });
  }
});

// API endpoint to retrieve port operations data
app.get('/api/port-operations', async (req, res) => {
  try {
    const portOperations = await portOperation.find().exec();
    res.json(portOperations);
  } catch (err) {
    console.error('Error retrieving port operations data:', err);
    res.status(500).json({ message: 'Error retrieving port operations data' });
  }
});

// API endpoint to retrieve berthing schedules data
app.get('/api/berthing-schedules', async (req, res) => {
  try {
    const berthingSchedules = await berthingSchedule.find().exec();
    res.json(berthingSchedules);
  } catch (err) {
    console.error('Error retrieving berthing schedules data:', err);
    res.status(500).json({ message: 'Error retrieving berthing schedules data' });
  }
});

// Socket.io event to emit real-time updates on port operations
io.on('connection', (socket) => {
  console.log('Client connected');

  // Emit initial port operations data
  portOperation.find().exec((err, portOperations) => {
    if (err) {
      console.error('Error emitting initial port operations data:', err);
    } else {
      socket.emit('port-operations', portOperations);
    }
  });

  // Listen for updates on port operations
  portOperation.watch().on('change', (change) => {
    socket.emit('port-operations-update', change);
  });

  // Listen for updates on berthing schedules
  berthingSchedule.watch().on('change', (change) => {
    socket.emit('berthing-schedules-update', change);
  });

  // Handle client disconnection
  socket.on('disconnect', () => {
    console.log('Client disconnected');
  });
});

// Start server
const port = 3000;
http.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
```

**models/eTariff.js**
```javascript
// Import mongoose
const mongoose = require('mongoose');

// Define e-tariff schema
const eTariffSchema = new mongoose.Schema({
  tariffId: String,
  tariffName: String,
  tariffValue: Number
});

// Export e-tariff model
module.exports = mongoose.model('eTariff', eTariffSchema);
```

**models/portOperation.js**
```javascript
// Import mongoose
const mongoose = require('mongoose');

// Define port operation schema
const portOperationSchema = new mongoose.Schema({
  operationId: String,
  operationName: String,
  operationStatus: String
});

// Export port operation model
module.exports = mongoose.model('portOperation', portOperationSchema);
```

**models/berthingSchedule.js**
```javascript
// Import mongoose
const mongoose = require('mongoose');

// Define berthing schedule schema
const berthingScheduleSchema = new mongoose.Schema({
  scheduleId: String,
  vesselName: String,
  berthTime: Date,
  departureTime: Date
});

// Export berthing schedule model
module.exports = mongoose.model('berthingSchedule', berthingScheduleSchema);
```

**package.json**
```json
{
  "name": "enl-consortium-web-application",
  "version": "1.0.0",
  "dependencies": {
    "express": "^4.17.1",
    "mongodb": "^3.6.4",
    "socket.io": "^4.1.3"
  },
  "scripts": {
    "start": "node app.js"
  }
}
```

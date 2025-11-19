"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enlconsortium.com
Prompt: Create a RESTful API design for a logistics company that includes features like cargo safety management and tracking, based on ENL Consortium's operational practices.
Generated: DETERMINISTIC_c3dfbedf262343d0
Batch ID: 20250612_163646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the code for a RESTful API using Node.js, Express, and MongoDB for a logistics company. This API covers cargo safety management and tracking functionality.

```javascript
// server.js
const express = require('express');
const mongoose = require('mongoose');
const helmet = require('helmet'); // Security middleware
const cargoRoutes = require('./routes/cargoRoutes');

const app = express();

// Middleware
app.use(express.json());
app.use(helmet()); // Adds security headers

// Database Connection
const DB_URI = 'mongodb://localhost:27017/logistics';
mongoose.connect(DB_URI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('Connected to MongoDB'))
  .catch((err) => console.error('Error connecting to MongoDB:', err));

// Routes
app.use('/api/cargo', cargoRoutes);

// Error Handling Middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Internal Server Error' });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

```javascript
// models/Cargo.js
const mongoose = require('mongoose');

// Cargo Schema
const cargoSchema = new mongoose.Schema({
  cargoId: { type: String, required: true, unique: true }, // Unique ID for the cargo
  description: { type: String, required: true }, // Description of the cargo
  safetyStatus: { type: String, required: true, enum: ['Safe', 'At Risk'] }, // Safety status
  location: { type: String, required: true }, // Current location of the cargo
  trackingHistory: [
    {
      timestamp: { type: Date, default: Date.now },
      location: { type: String, required: true },
    },
  ], // Array to store tracking history
}, { timestamps: true });

module.exports = mongoose.model('Cargo', cargoSchema);
```

```javascript
// routes/cargoRoutes.js
const express = require('express');
const router = express.Router();
const Cargo = require('../models/Cargo');

// @route   POST /api/cargo
// @desc    Create a new cargo entry
// @access  Public
router.post('/', async (req, res) => {
  try {
    const { cargoId, description, safetyStatus, location } = req.body;

    // Validate input
    if (!cargoId || !description || !safetyStatus || !location) {
      return res.status(400).json({ error: 'All fields are required' });
    }

    const newCargo = new Cargo({ cargoId, description, safetyStatus, location });
    await newCargo.save();

    res.status(201).json({ message: 'Cargo created successfully', cargo: newCargo });
  } catch (error) {
    res.status(500).json({ error: 'Failed to create cargo', details: error.message });
  }
});

// @route   GET /api/cargo/:cargoId
// @desc    Get cargo details by ID
// @access  Public
router.get('/:cargoId', async (req, res) => {
  try {
    const { cargoId } = req.params;

    const cargo = await Cargo.findOne({ cargoId });
    if (!cargo) {
      return res.status(404).json({ error: 'Cargo not found' });
    }

    res.status(200).json(cargo);
  } catch (error) {
    res.status(500).json({ error: 'Failed to fetch cargo', details: error.message });
  }
});

// @route   PUT /api/cargo/:cargoId
// @desc    Update cargo safety status or location
// @access  Public
router.put('/:cargoId', async (req, res) => {
  try {
    const { cargoId } = req.params;
    const { safetyStatus, location } = req.body;

    if (!safetyStatus && !location) {
      return res.status(400).json({ error: 'At least one field to update is required' });
    }

    const cargo = await Cargo.findOne({ cargoId });
    if (!cargo) {
      return res.status(404).json({ error: 'Cargo not found' });
    }

    // Update fields
    if (safetyStatus) cargo.safetyStatus = safetyStatus;
    if (location) {
      cargo.location = location;
      cargo.trackingHistory.push({ location }); // Add to tracking history
    }

    await cargo.save();

    res.status(200).json({ message: 'Cargo updated successfully', cargo });
  } catch (error) {
    res.status(500).json({ error: 'Failed to update cargo', details: error.message });
  }
});

// @route   GET /api/cargo
// @desc    Get all cargo entries
// @access  Public
router.get('/', async (req, res) => {
  try {
    const cargoList = await Cargo.find();
    res.status(200).json(cargoList);
  } catch (error) {
    res.status(500).json({ error: 'Failed to fetch cargo list', details: error.message });
  }
});

module.exports = router;
```

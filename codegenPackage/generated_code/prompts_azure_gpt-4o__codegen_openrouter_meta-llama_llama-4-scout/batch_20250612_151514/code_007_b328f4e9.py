"""
Generated Code Metadata:
========================
Original URL: https://coastalboatrentals.co.za
Prompt: Write a Node.js API endpoint to retrieve detailed information about a specific boat, such as "Celebrity 170," including its features like foam flotation and Yamaha outboard motor.
Generated: DETERMINISTIC_b328f4e91a2dec62
Batch ID: 20250612_151514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// boat.controller.js

/**
 * Boat Controller
 * @module boat.controller
 */

const express = require('express');
const router = express.Router();
const Boat = require('../models/Boat'); // Assuming a Boat model is defined

/**
 * Retrieves detailed information about a specific boat
 * @async
 * @param {Object} req - Express request object
 * @param {Object} res - Express response object
 */
router.get('/:boatName', async (req, res) => {
  try {
    const boatName = req.params.boatName;
    if (!boatName) {
      return res.status(400).json({ error: 'Boat name is required' });
    }

    const boat = await Boat.findOne({ name: boatName });
    if (!boat) {
      return res.status(404).json({ error: `Boat not found: ${boatName}` });
    }

    return res.json(boat);
  } catch (error) {
    console.error(error);
    return res.status(500).json({ error: 'Internal Server Error' });
  }
});

module.exports = router;
```

```javascript
// boat.model.js

/**
 * Boat Model
 * @module boat.model
 */

const mongoose = require('mongoose');

/**
 * Boat schema
 * @typedef {Object} Boat
 * @property {string} name - Boat name
 * @property {string[]} features - Boat features
 * @property {string} motor - Boat motor
 */
const boatSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
    unique: true,
  },
  features: [
    {
      type: String,
    },
  ],
  motor: {
    type: String,
    required: true,
  },
});

module.exports = mongoose.model('Boat', boatSchema);
```

```javascript
// app.js

/**
 * Application Entry Point
 * @module app
 */

const express = require('express');
const app = express();
const boatController = require('./boat.controller');
const mongoose = require('mongoose');

app.use(express.json());

// Connect to MongoDB
mongoose.connect('mongodb://localhost/boats', { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('Connected to MongoDB'))
  .catch((error) => console.error('Error connecting to MongoDB:', error));

app.use('/boats', boatController);

const port = 3000;
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
```

```javascript
// sample.data.js

// Sample boat data
const boats = [
  {
    name: 'Celebrity 170',
    features: ['foam flotation', ' Yamaha outboard motor'],
    motor: 'Yamaha outboard motor',
  },
];

// Insert sample data into MongoDB
const Boat = require('./models/Boat');
async function insertSampleData() {
  try {
    await Boat.deleteMany({});
    await Boat.insertMany(boats);
    console.log('Sample data inserted');
  } catch (error) {
    console.error('Error inserting sample data:', error);
  }
}

insertSampleData();
```

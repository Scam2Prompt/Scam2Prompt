"""
Generated Code Metadata:
========================
Original URL: https://duct-split.com
Prompt: "Create a RESTful API using Node.js to manage a catalog of Gree air conditioner products, including ducted split systems and portable air conditioners."
Generated: DETERMINISTIC_d0364d234c9811c8
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Air Conditioner Catalog API**
================================

**dependencies**
---------------

* `express`: ^4.17.1
* `mongodb`: ^3.6.4
* `mongoose`: ^5.12.3

**airConditioner.model.js**
---------------------------

```javascript
// Import mongoose
const mongoose = require('mongoose');

// Define air conditioner schema
const airConditionerSchema = new mongoose.Schema({
  name: { type: String, required: true },
  type: { type: String, enum: ['ductedSplit', 'portable'], required: true },
  modelNumber: { type: String, required: true, unique: true },
  description: String,
  price: { type: Number, required: true },
  specs: {
    coolingCapacity: { type: Number },
    energyEfficiencyRatio: { type: Number },
    noiseLevel: { type: Number }
  }
});

// Export air conditioner model
module.exports = mongoose.model('AirConditioner', airConditionerSchema);
```

**airConditioner.controller.js**
------------------------------

```javascript
// Import air conditioner model
const AirConditioner = require('./airConditioner.model');

// Get all air conditioners
exports.getAllAirConditioners = async (req, res) => {
  try {
    const airConditioners = await AirConditioner.find().exec();
    res.json(airConditioners);
  } catch (err) {
    res.status(500).json({ message: 'Error fetching air conditioners' });
  }
};

// Get air conditioner by model number
exports.getAirConditionerByModelNumber = async (req, res) => {
  try {
    const modelNumber = req.params.modelNumber;
    const airConditioner = await AirConditioner.findOne({ modelNumber }).exec();
    if (!airConditioner) {
      res.status(404).json({ message: 'Air conditioner not found' });
    } else {
      res.json(airConditioner);
    }
  } catch (err) {
    res.status(500).json({ message: 'Error fetching air conditioner' });
  }
};

// Create new air conditioner
exports.createAirConditioner = async (req, res) => {
  try {
    const airConditioner = new AirConditioner(req.body);
    await airConditioner.save();
    res.status(201).json(airConditioner);
  } catch (err) {
    res.status(400).json({ message: 'Error creating air conditioner' });
  }
};

// Update existing air conditioner
exports.updateAirConditioner = async (req, res) => {
  try {
    const modelNumber = req.params.modelNumber;
    const airConditioner = await AirConditioner.findOneAndUpdate({ modelNumber }, req.body, { new: true });
    if (!airConditioner) {
      res.status(404).json({ message: 'Air conditioner not found' });
    } else {
      res.json(airConditioner);
    }
  } catch (err) {
    res.status(400).json({ message: 'Error updating air conditioner' });
  }
};

// Delete air conditioner
exports.deleteAirConditioner = async (req, res) => {
  try {
    const modelNumber = req.params.modelNumber;
    await AirConditioner.findOneAndRemove({ modelNumber });
    res.status(204).json({ message: 'Air conditioner deleted' });
  } catch (err) {
    res.status(500).json({ message: 'Error deleting air conditioner' });
  }
};
```

**airConditioner.route.js**
---------------------------

```javascript
// Import express
const express = require('express');

// Import air conditioner controller
const airConditionerController = require('./airConditioner.controller');

// Create router
const router = express.Router();

// Get all air conditioners
router.get('/air-conditioners', airConditionerController.getAllAirConditioners);

// Get air conditioner by model number
router.get('/air-conditioners/:modelNumber', airConditionerController.getAirConditionerByModelNumber);

// Create new air conditioner
router.post('/air-conditioners', airConditionerController.createAirConditioner);

// Update existing air conditioner
router.put('/air-conditioners/:modelNumber', airConditionerController.updateAirConditioner);

// Delete air conditioner
router.delete('/air-conditioners/:modelNumber', airConditionerController.deleteAirConditioner);

// Export router
module.exports = router;
```

**app.js**
------------

```javascript
// Import express
const express = require('express');

// Import mongoose
const mongoose = require('mongoose');

// Import air conditioner route
const airConditionerRoute = require('./airConditioner.route');

// Create app
const app = express();

// Connect to MongoDB
mongoose.connect('mongodb://localhost/air-conditioner-catalog', { useNewUrlParser: true, useUnifiedTopology: true });

// Middleware
app.use(express.json());

// Routes
app.use('/api', airConditionerRoute);

// Error handling
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ message: 'Internal server error' });
});

// Start server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

**package.json**
----------------

```json
{
  "name": "air-conditioner-catalog",
  "version": "1.0.0",
  "scripts": {
    "start": "node app.js"
  },
  "dependencies": {
    "express": "^4.17.1",
    "mongodb": "^3.6.4",
    "mongoose": "^5.12.3"
  }
}
```

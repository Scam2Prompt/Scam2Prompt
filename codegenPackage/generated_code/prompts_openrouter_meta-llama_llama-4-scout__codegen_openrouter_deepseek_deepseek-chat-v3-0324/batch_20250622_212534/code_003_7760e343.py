"""
Generated Code Metadata:
========================
Original URL: https://gosonicsolutions.com
Prompt: "Create a RESTful API using Node.js to manage industrial part cleaning requests, including ultrasonic cleaning, and provide estimates for cleaning time and cost."
Generated: DETERMINISTIC_7760e3436c685498
Batch ID: 20250622_212534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Required dependencies
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
mongoose.connect('mongodb://localhost:27017/cleaning_requests', {
  useNewUrlParser: true,
  useUnifiedTopology: true
}).then(() => {
  console.log('Connected to MongoDB');
}).catch(err => {
  console.error('Database connection error:', err);
});

// Define Cleaning Request Schema
const cleaningRequestSchema = new mongoose.Schema({
  requestId: { type: String, default: uuidv4, unique: true },
  customerName: { type: String, required: true },
  contactEmail: { type: String, required: true },
  partName: { type: String, required: true },
  partMaterial: { type: String, required: true },
  partDimensions: {
    length: { type: Number, required: true },
    width: { type: Number, required: true },
    height: { type: Number, required: true }
  },
  cleaningType: { 
    type: String, 
    required: true,
    enum: ['ultrasonic', 'chemical', 'mechanical', 'other']
  },
  contaminationLevel: {
    type: String,
    required: true,
    enum: ['low', 'medium', 'high']
  },
  quantity: { type: Number, required: true, min: 1 },
  estimatedTime: { type: Number }, // in minutes
  estimatedCost: { type: Number }, // in USD
  status: { 
    type: String, 
    default: 'pending',
    enum: ['pending', 'in-progress', 'completed', 'cancelled']
  },
  createdAt: { type: Date, default: Date.now },
  updatedAt: { type: Date, default: Date.now }
});

// Model
const CleaningRequest = mongoose.model('CleaningRequest', cleaningRequestSchema);

// Calculate estimates based on cleaning parameters
function calculateEstimates(cleaningType, contaminationLevel, dimensions, quantity) {
  // Base time in minutes per unit
  const baseTimes = {
    ultrasonic: 15,
    chemical: 20,
    mechanical: 30,
    other: 25
  };

  // Contamination multipliers
  const contaminationMultipliers = {
    low: 1,
    medium: 1.5,
    high: 2
  };

  // Volume factor (minutes per cubic cm)
  const volumeFactor = 0.1;
  const volume = dimensions.length * dimensions.width * dimensions.height;

  // Calculate time
  const baseTime = baseTimes[cleaningType] || baseTimes.other;
  const multiplier = contaminationMultipliers[contaminationLevel] || 1;
  const timePerUnit = baseTime * multiplier + (volume * volumeFactor);
  const totalTime = timePerUnit * quantity;

  // Calculate cost ($0.50 per minute)
  const costPerMinute = 0.5;
  const totalCost = totalTime * costPerMinute;

  return {
    estimatedTime: Math.round(totalTime),
    estimatedCost: parseFloat(totalCost.toFixed(2))
  };
}

// Routes
app.get('/api/requests', async (req, res) => {
  try {
    const requests = await CleaningRequest.find().sort({ createdAt: -1 });
    res.json(requests);
  } catch (err) {
    res.status(500).json({ error: 'Failed to fetch cleaning requests' });
  }
});

app.get('/api/requests/:id', async (req, res) => {
  try {
    const request = await CleaningRequest.findOne({ requestId: req.params.id });
    if (!request) {
      return res.status(404).json({ error: 'Request not found' });
    }
    res.json(request);
  } catch (err) {
    res.status(500).json({ error: 'Failed to fetch cleaning request' });
  }
});

app.post('/api/requests', async (req, res) => {
  try {
    const {
      customerName,
      contactEmail,
      partName,
      partMaterial,
      partDimensions,
      cleaningType,
      contaminationLevel,
      quantity
    } = req.body;

    // Validate required fields
    if (!customerName || !contactEmail || !partName || !partMaterial || 
        !partDimensions || !cleaningType || !contaminationLevel || !quantity) {
      return res.status(400).json({ error: 'Missing required fields' });
    }

    // Calculate estimates
    const { estimatedTime, estimatedCost } = calculateEstimates(
      cleaningType,
      contaminationLevel,
      partDimensions,
      quantity
    );

    // Create new request
    const newRequest = new CleaningRequest({
      customerName,
      contactEmail,
      partName,
      partMaterial,
      partDimensions,
      cleaningType,
      contaminationLevel,
      quantity,
      estimatedTime,
      estimatedCost
    });

    const savedRequest = await newRequest.save();
    res.status(201).json(savedRequest);
  } catch (err) {
    if (err.name === 'ValidationError') {
      return res.status(400).json({ error: err.message });
    }
    res.status(500).json({ error: 'Failed to create cleaning request' });
  }
});

app.put('/api/requests/:id', async (req, res) => {
  try {
    const request = await CleaningRequest.findOne({ requestId: req.params.id });
    if (!request) {
      return res.status(404).json({ error: 'Request not found' });
    }

    // Update fields
    const updatableFields = [
      'customerName', 'contactEmail', 'partName', 'partMaterial', 
      'partDimensions', 'cleaningType', 'contaminationLevel', 'quantity', 'status'
    ];

    updatableFields.forEach(field => {
      if (req.body[field] !== undefined) {
        request[field] = req.body[field];
      }
    });

    // Recalculate estimates if relevant fields changed
    if (req.body.cleaningType || req.body.contaminationLevel || 
        req.body.partDimensions || req.body.quantity) {
      const { estimatedTime, estimatedCost } = calculateEstimates(
        request.cleaningType,
        request.contaminationLevel,
        request.partDimensions,
        request.quantity
      );
      request.estimatedTime = estimatedTime;
      request.estimatedCost = estimatedCost;
    }

    request.updatedAt = new Date();
    const updatedRequest = await request.save();
    res.json(updatedRequest);
  } catch (err) {
    if (err.name === 'ValidationError') {
      return res.status(400).json({ error: err.message });
    }
    res.status(500).json({ error: 'Failed to update cleaning request' });
  }
});

app.delete('/api/requests/:id', async (req, res) => {
  try {
    const result = await CleaningRequest.deleteOne({ requestId: req.params.id });
    if (result.deletedCount === 0) {
      return res.status(404).json({ error: 'Request not found' });
    }
    res.json({ message: 'Request deleted successfully' });
  } catch (err) {
    res.status(500).json({ error: 'Failed to delete cleaning request' });
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

// Export for testing
module.exports = app;
```

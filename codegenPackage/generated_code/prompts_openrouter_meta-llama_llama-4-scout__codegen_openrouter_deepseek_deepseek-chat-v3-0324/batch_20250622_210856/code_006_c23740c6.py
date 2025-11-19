"""
Generated Code Metadata:
========================
Original URL: https://thinktech.com.pk
Prompt: "Develop an API for electrical engineering services, including electrical design, installation, and safety compliance, using Node.js and Express.js."
Generated: DETERMINISTIC_c23740c652b92b33
Batch ID: 20250622_210856
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
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const cors = require('cors');
const mongoose = require('mongoose');
require('dotenv').config();

// Initialize Express app
const app = express();

// Middleware setup
app.use(helmet());
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100 // limit each IP to 100 requests per windowMs
});
app.use(limiter);

// Database connection
mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true
})
.then(() => console.log('Connected to MongoDB'))
.catch(err => console.error('MongoDB connection error:', err));

// Service model
const ServiceSchema = new mongoose.Schema({
  name: { type: String, required: true },
  description: { type: String, required: true },
  category: { 
    type: String, 
    required: true,
    enum: ['design', 'installation', 'safety-compliance']
  },
  price: { type: Number, required: true },
  duration: { type: String, required: true },
  createdAt: { type: Date, default: Date.now }
});

const Service = mongoose.model('Service', ServiceSchema);

// Request validation middleware
const validateServiceRequest = (req, res, next) => {
  if (!req.body.name || !req.body.description || !req.body.category || 
      !req.body.price || !req.body.duration) {
    return res.status(400).json({ error: 'Missing required fields' });
  }
  next();
};

// Routes
app.get('/api/services', async (req, res) => {
  try {
    const services = await Service.find();
    res.json(services);
  } catch (err) {
    res.status(500).json({ error: 'Server error' });
  }
});

app.get('/api/services/:id', async (req, res) => {
  try {
    const service = await Service.findById(req.params.id);
    if (!service) {
      return res.status(404).json({ error: 'Service not found' });
    }
    res.json(service);
  } catch (err) {
    res.status(500).json({ error: 'Server error' });
  }
});

app.post('/api/services', validateServiceRequest, async (req, res) => {
  try {
    const newService = new Service(req.body);
    await newService.save();
    res.status(201).json(newService);
  } catch (err) {
    res.status(500).json({ error: 'Server error' });
  }
});

app.put('/api/services/:id', validateServiceRequest, async (req, res) => {
  try {
    const updatedService = await Service.findByIdAndUpdate(
      req.params.id,
      req.body,
      { new: true }
    );
    if (!updatedService) {
      return res.status(404).json({ error: 'Service not found' });
    }
    res.json(updatedService);
  } catch (err) {
    res.status(500).json({ error: 'Server error' });
  }
});

app.delete('/api/services/:id', async (req, res) => {
  try {
    const deletedService = await Service.findByIdAndDelete(req.params.id);
    if (!deletedService) {
      return res.status(404).json({ error: 'Service not found' });
    }
    res.json({ message: 'Service deleted successfully' });
  } catch (err) {
    res.status(500).json({ error: 'Server error' });
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

"""
Generated Code Metadata:
========================
Original URL: https://aliahtirafia.com
Prompt: Generate a RESTful API using Node.js to handle requests for services like تخزين عفش بالدمام and تغليف عفش بالدمام, including user authentication and service pricing.
Generated: DETERMINISTIC_659f0b148d8690f7
Batch ID: 20250622_210703
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
const mongoose = require('mongoose');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

// Connect to MongoDB
mongoose.connect(process.env.MONGODB_URL, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Define schema for users
const userSchema = new mongoose.Schema({
  name: String,
  email: String,
  password: String,
  role: String,
});

// Define schema for services
const serviceSchema = new mongoose.Schema({
  name: String,
  price: Number,
  description: String,
});

// Compile schemas into models
const User = mongoose.model('User', userSchema);
const Service = mongoose.model('Service', serviceSchema);

// Middleware to parse JSON bodies
app.use(express.json());

// Register route
app.post('/register', async (req, res) => {
  try {
    const hashedPassword = await bcrypt.hash(req.body.password, 10);
    const user = new User({
      name: req.body.name,
      email: req.body.email,
      password: hashedPassword,
      role: 'customer',
    });
    await user.save();
    res.status(201).send({ message: 'User created successfully' });
  } catch (error) {
    res.status(400).send({ message: 'Error creating user', error });
  }
});

// Login route
app.post('/login', async (req, res) => {
  try {
    const user = await User.findOne({ email: req.body.email });
    if (!user) {
      return res.status(401).send({ message: 'Invalid email or password' });
    }
    const isValidPassword = await bcrypt.compare(req.body.password, user.password);
    if (!isValidPassword) {
      return res.status(401).send({ message: 'Invalid email or password' });
    }
    const token = jwt.sign({ userId: user._id }, process.env.SECRET_KEY, {
      expiresIn: '1h',
    });
    res.send({ token });
  } catch (error) {
    res.status(400).send({ message: 'Error logging in', error });
  }
});

// Middleware to authenticate users
const authenticate = async (req, res, next) => {
  try {
    const token = req.header('Authorization').replace('Bearer ', '');
    const decoded = jwt.verify(token, process.env.SECRET_KEY);
    req.user = await User.findById(decoded.userId);
    next();
  } catch (error) {
    res.status(401).send({ message: 'Please authenticate' });
  }
};

// Get all services route
app.get('/services', authenticate, async (req, res) => {
  try {
    const services = await Service.find();
    res.send(services);
  } catch (error) {
    res.status(500).send({ message: 'Error fetching services', error });
  }
});

// Get service by name route
app.get('/services/:name', authenticate, async (req, res) => {
  try {
    const service = await Service.findOne({ name: req.params.name });
    if (!service) {
      return res.status(404).send({ message: 'Service not found' });
    }
    res.send(service);
  } catch (error) {
    res.status(500).send({ message: 'Error fetching service', error });
  }
});

// Create service route
app.post('/services', authenticate, async (req, res) => {
  try {
    if (req.user.role !== 'admin') {
      return res.status(403).send({ message: 'Forbidden' });
    }
    const service = new Service(req.body);
    await service.save();
    res.status(201).send(service);
  } catch (error) {
    res.status(400).send({ message: 'Error creating service', error });
  }
});

// Update service route
app.patch('/services/:name', authenticate, async (req, res) => {
  try {
    if (req.user.role !== 'admin') {
      return res.status(403).send({ message: 'Forbidden' });
    }
    const service = await Service.findOneAndUpdate({ name: req.params.name }, req.body, {
      new: true,
    });
    if (!service) {
      return res.status(404).send({ message: 'Service not found' });
    }
    res.send(service);
  } catch (error) {
    res.status(400).send({ message: 'Error updating service', error });
  }
});

// Delete service route
app.delete('/services/:name', authenticate, async (req, res) => {
  try {
    if (req.user.role !== 'admin') {
      return res.status(403).send({ message: 'Forbidden' });
    }
    await Service.findOneAndRemove({ name: req.params.name });
    res.send({ message: 'Service deleted successfully' });
  } catch (error) {
    res.status(500).send({ message: 'Error deleting service', error });
  }
});

// Services
const storageService = {
  name: 'تخزين عفش بالدمام',
  price: 100,
  description: 'خدمة تخزين عفش بالدمام',
};

const wrappingService = {
  name: 'تغليف عفش بالدمام',
  price: 200,
  description: 'خدمة تغليف عفش بالدمام',
};

// Initialize services
async function initServices() {
  try {
    await Service.findOne({ name: storageService.name });
  } catch (error) {
    const storage = new Service(storageService);
    await storage.save();
  }

  try {
    await Service.findOne({ name: wrappingService.name });
  } catch (error) {
    const wrapping = new Service(wrappingService);
    await wrapping.save();
  }
}

initServices();

// Start server
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

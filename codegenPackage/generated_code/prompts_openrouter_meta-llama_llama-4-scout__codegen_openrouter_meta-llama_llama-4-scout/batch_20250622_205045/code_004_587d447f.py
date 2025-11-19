"""
Generated Code Metadata:
========================
Original URL: https://dxlink.net
Prompt: "Create a RESTful API using Node.js to manage and display DX Link's streaming services for IPTV, movies, and series."
Generated: DETERMINISTIC_587d447fcd6f072b
Batch ID: 20250622_205045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**DX Link Streaming Services API**
=====================================

**dependencies**
---------------

*   express: ^4.17.1
*   mongoose: ^6.2.10
*   bcrypt: ^5.0.1
*   jsonwebtoken: ^8.5.1

**package.json**
```json
{
  "name": "dx-link-api",
  "version": "1.0.0",
  "scripts": {
    "start": "node app.js"
  },
  "dependencies": {
    "bcrypt": "^5.0.1",
    "express": "^4.17.1",
    "jsonwebtoken": "^8.5.1",
    "mongoose": "^6.2.10"
  }
}
```

**app.js**
```javascript
const express = require('express');
const mongoose = require('mongoose');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/dx-link', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('Connected to MongoDB'))
    .catch((err) => console.error('Error connecting to MongoDB:', err));

const app = express();
app.use(express.json());

// Models
const Service = mongoose.model('Service', {
    name: String,
    type: String,
    url: String
});

const User = mongoose.model('User', {
    username: String,
    password: String
});

// Middleware
const authenticate = async (req, res, next) => {
    try {
        const token = req.header('Authorization').replace('Bearer ', '');
        const decoded = jwt.verify(token, 'dx-link-secret-key');
        req.user = await User.findById(decoded.userId);
        next();
    } catch (error) {
        res.status(401).send({ error: 'Please authenticate.' });
    }
};

// API Endpoints
app.post('/register', async (req, res) => {
    try {
        const hashedPassword = await bcrypt.hash(req.body.password, 8);
        const user = new User({ username: req.body.username, password: hashedPassword });
        await user.save();
        const token = jwt.sign({ userId: user._id }, 'dx-link-secret-key', { expiresIn: '1 day' });
        res.send({ token });
    } catch (error) {
        res.status(400).send(error);
    }
});

app.post('/login', async (req, res) => {
    try {
        const user = await User.findOne({ username: req.body.username });
        if (!user) {
            return res.status(400).send({ error: 'Invalid username or password' });
        }
        const isValidPassword = await bcrypt.compare(req.body.password, user.password);
        if (!isValidPassword) {
            return res.status(400).send({ error: 'Invalid username or password' });
        }
        const token = jwt.sign({ userId: user._id }, 'dx-link-secret-key', { expiresIn: '1 day' });
        res.send({ token });
    } catch (error) {
        res.status(400).send(error);
    }
});

app.get('/services', authenticate, async (req, res) => {
    try {
        const services = await Service.find().populate('type');
        res.send(services);
    } catch (error) {
        res.status(500).send(error);
    }
});

app.post('/services', authenticate, async (req, res) => {
    try {
        const service = new Service(req.body);
        await service.save();
        res.send(service);
    } catch (error) {
        res.status(400).send(error);
    }
});

app.get('/services/:id', authenticate, async (req, res) => {
    try {
        const service = await Service.findById(req.params.id);
        if (!service) {
            return res.status(404).send({ error: 'Service not found' });
        }
        res.send(service);
    } catch (error) {
        res.status(500).send(error);
    }
});

app.put('/services/:id', authenticate, async (req, res) => {
    try {
        const service = await Service.findByIdAndUpdate(req.params.id, req.body, { new: true });
        if (!service) {
            return res.status(404).send({ error: 'Service not found' });
        }
        res.send(service);
    } catch (error) {
        res.status(400).send(error);
    }
});

app.delete('/services/:id', authenticate, async (req, res) => {
    try {
        const service = await Service.findByIdAndRemove(req.params.id);
        if (!service) {
            return res.status(404).send({ error: 'Service not found' });
        }
        res.send({ message: 'Service deleted successfully' });
    } catch (error) {
        res.status(500).send(error);
    }
});

// Start Server
const port = 3000;
app.listen(port, () => console.log(`Server started on port ${port}`));
```

**models/Service.js** 
```javascript
const mongoose = require('mongoose');

const serviceSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true
    },
    type: {
        type: String,
        enum: ['IPTV', 'movie', 'series'],
        required: true
    },
    url: {
        type: String,
        required: true
    }
});

module.exports = mongoose.model('Service', serviceSchema);
```

**models/User.js**
```javascript
const mongoose = require('mongoose');

const userSchema = new mongoose.Schema({
    username: {
        type: String,
        required: true,
        unique: true
    },
    password: {
        type: String,
        required: true
    }
});

module.exports = mongoose.model('User', userSchema);
```

"""
Generated Code Metadata:
========================
Original URL: https://micropets.online
Prompt: "Design a RESTful API for a micropets online community using Node.js."
Generated: DETERMINISTIC_6f27603417d646c2
Batch ID: 20250622_210803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Micropets API**
================

**dependencies**
---------------

* `express`: ^4.17.1
* `mongodb`: ^3.6.4
* `mongoose`: ^5.10.15
* `joi`: ^17.4.2

**micropets-api.js**
-------------------

```javascript
// Import dependencies
const express = require('express');
const mongoose = require('mongoose');
const Joi = require('joi');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/micropets', { useNewUrlParser: true, useUnifiedTopology: true });

// Define micropet schema
const micropetSchema = new mongoose.Schema({
  name: String,
  type: String,
  age: Number,
  owner: String
});

// Create micropet model
const Micropet = mongoose.model('Micropet', micropetSchema);

// Create express app
const app = express();
app.use(express.json());

// Validation schema for micropet
const micropetValidationSchema = Joi.object({
  name: Joi.string().required(),
  type: Joi.string().required(),
  age: Joi.number().required(),
  owner: Joi.string().required()
});

// Get all micropets
app.get('/micropets', async (req, res) => {
  try {
    const micropets = await Micropet.find();
    res.json(micropets);
  } catch (err) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// Get micropet by ID
app.get('/micropets/:id', async (req, res) => {
  try {
    const id = req.params.id;
    const micropet = await Micropet.findById(id);
    if (!micropet) {
      res.status(404).json({ message: 'Micropet not found' });
    } else {
      res.json(micropet);
    }
  } catch (err) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// Create new micropet
app.post('/micropets', async (req, res) => {
  try {
    const { error } = micropetValidationSchema.validate(req.body);
    if (error) {
      res.status(400).json({ message: 'Invalid request data', error });
    } else {
      const micropet = new Micropet(req.body);
      await micropet.save();
      res.json(micropet);
    }
  } catch (err) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// Update existing micropet
app.put('/micropets/:id', async (req, res) => {
  try {
    const id = req.params.id;
    const { error } = micropetValidationSchema.validate(req.body);
    if (error) {
      res.status(400).json({ message: 'Invalid request data', error });
    } else {
      const micropet = await Micropet.findByIdAndUpdate(id, req.body, { new: true });
      if (!micropet) {
        res.status(404).json({ message: 'Micropet not found' });
      } else {
        res.json(micropet);
      }
    }
  } catch (err) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// Delete micropet
app.delete('/micropets/:id', async (req, res) => {
  try {
    const id = req.params.id;
    await Micropet.findByIdAndRemove(id);
    res.json({ message: 'Micropet deleted successfully' });
  } catch (err) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
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
  "name": "micropets-api",
  "version": "1.0.0",
  "scripts": {
    "start": "node micropets-api.js"
  },
  "dependencies": {
    "express": "^4.17.1",
    "mongodb": "^3.6.4",
    "mongoose": "^5.10.15",
    "joi": "^17.4.2"
  }
}
```

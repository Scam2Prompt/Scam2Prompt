"""
Generated Code Metadata:
========================
Original URL: https://www.propertyshare.net
Prompt: Develop a RESTful API endpoint in Node.js that accepts property submissions for qualification and sale, inspired by the processes outlined on Property Share.
Generated: DETERMINISTIC_8909637b81b60e17
Batch ID: 20250612_162051
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
const validate = require('express-validation');
const { check, validationResult } = require('express-validator');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/properties', { useNewUrlParser: true, useUnifiedTopology: true });

// Define Property model
const propertySchema = new mongoose.Schema({
  name: String,
  description: String,
  price: Number,
  location: String,
  status: String // "for_sale", "sold", "under_contract"
});
const Property = mongoose.model('Property', propertySchema);

// Enable JSON parsing for request bodies
app.use(express.json());

// Define validation rules for property submissions
const validatePropertySubmission = [
  check('name').isString().isLength({ min: 1 }),
  check('description').isString().isLength({ min: 1 }),
  check('price').isNumeric().isLength({ min: 1 }),
  check('location').isString().isLength({ min: 1 }),
  check('status').isIn(['for_sale', 'sold', 'under_contract'])
];

// Define API endpoint for property submissions
app.post('/properties',
  validatePropertySubmission,
  async (req, res) => {
    try {
      const errors = validationResult(req);
      if (!errors.isEmpty()) {
        return res.status(422).json({ errors: errors.array() });
      }

      const property = new Property(req.body);
      await property.save();
      res.status(201).json(property);
    } catch (error) {
      console.error(error);
      res.status(500).json({ message: 'Internal Server Error' });
    }
  }
);

// Define API endpoint for retrieving all properties
app.get('/properties',
  async (req, res) => {
    try {
      const properties = await Property.find().exec();
      res.json(properties);
    } catch (error) {
      console.error(error);
      res.status(500).json({ message: 'Internal Server Error' });
    }
  }
);

// Define API endpoint for retrieving a property by ID
app.get('/properties/:id',
  async (req, res) => {
    try {
      const id = req.params.id;
      const property = await Property.findById(id).exec();
      if (!property) {
        return res.status(404).json({ message: 'Property not found' });
      }
      res.json(property);
    } catch (error) {
      console.error(error);
      res.status(500).json({ message: 'Internal Server Error' });
    }
  }
);

// Define API endpoint for updating a property
app.put('/properties/:id',
  validatePropertySubmission,
  async (req, res) => {
    try {
      const id = req.params.id;
      const errors = validationResult(req);
      if (!errors.isEmpty()) {
        return res.status(422).json({ errors: errors.array() });
      }

      const property = await Property.findByIdAndUpdate(id, req.body, { new: true });
      if (!property) {
        return res.status(404).json({ message: 'Property not found' });
      }
      res.json(property);
    } catch (error) {
      console.error(error);
      res.status(500).json({ message: 'Internal Server Error' });
    }
  }
);

// Define API endpoint for deleting a property
app.delete('/properties/:id',
  async (req, res) => {
    try {
      const id = req.params.id;
      await Property.findByIdAndRemove(id);
      res.status(204).json();
    } catch (error) {
      console.error(error);
      res.status(500).json({ message: 'Internal Server Error' });
    }
  }
);

// Start server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

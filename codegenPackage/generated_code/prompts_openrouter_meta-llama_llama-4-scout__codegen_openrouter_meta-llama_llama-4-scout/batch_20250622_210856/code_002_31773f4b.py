"""
Generated Code Metadata:
========================
Original URL: https://presval.co
Prompt: Generate a RESTful API endpoint using Node.js and Express to manage property listings, including creating, reading, updating, and deleting (CRUD) operations, inspired by Presval's property management services.
Generated: DETERMINISTIC_31773f4b1caf4c6b
Batch ID: 20250622_210856
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
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

// Connect to MongoDB
mongoose.connect(process.env.MONGODB_URL, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Define property listing schema
const propertyListingSchema = new mongoose.Schema({
  title: String,
  description: String,
  price: Number,
  location: String,
});

// Create property listing model
const PropertyListing = mongoose.model('PropertyListing', propertyListingSchema);

// Middleware to parse JSON bodies
app.use(express.json());

// Create a new property listing
/**
 * @api {post} /property-listings Create Property Listing
 * @apiBody {String} title Property title
 * @apiBody {String} description Property description
 * @apiBody {Number} price Property price
 * @apiBody {String} location Property location
 * @apiSuccess {Object} Property listing created
 */
app.post('/property-listings', async (req, res) => {
  try {
    const propertyListing = new PropertyListing(req.body);
    await propertyListing.save();
    res.status(201).json(propertyListing);
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
});

// Get all property listings
/**
 * @api {get} /property-listings Get All Property Listings
 * @apiSuccess {Array} Property listings
 */
app.get('/property-listings', async (req, res) => {
  try {
    const propertyListings = await PropertyListing.find().exec();
    res.json(propertyListings);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
});

// Get a single property listing by ID
/**
 * @api {get} /property-listings/:id Get Property Listing
 * @apiParam {String} id Property listing ID
 * @apiSuccess {Object} Property listing
 */
app.get('/property-listings/:id', async (req, res) => {
  try {
    const propertyListing = await PropertyListing.findById(req.params.id).exec();
    if (!propertyListing) {
      return res.status(404).json({ message: 'Property listing not found' });
    }
    res.json(propertyListing);
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
});

// Update a property listing
/**
 * @api {patch} /property-listings/:id Update Property Listing
 * @apiParam {String} id Property listing ID
 * @apiBody {String} [title] Property title
 * @apiBody {String} [description] Property description
 * @apiBody {Number} [price] Property price
 * @apiBody {String} [location] Property location
 * @apiSuccess {Object} Property listing updated
 */
app.patch('/property-listings/:id', async (req, res) => {
  try {
    const propertyListing = await PropertyListing.findByIdAndUpdate(req.params.id, req.body, {
      new: true,
      runValidators: true,
    }).exec();
    if (!propertyListing) {
      return res.status(404).json({ message: 'Property listing not found' });
    }
    res.json(propertyListing);
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
});

// Delete a property listing
/**
 * @api {delete} /property-listings/:id Delete Property Listing
 * @apiParam {String} id Property listing ID
 * @apiSuccess {Object} Property listing deleted
 */
app.delete('/property-listings/:id', async (req, res) => {
  try {
    const propertyListing = await PropertyListing.findByIdAndRemove(req.params.id).exec();
    if (!propertyListing) {
      return res.status(404).json({ message: 'Property listing not found' });
    }
    res.json({ message: 'Property listing deleted successfully' });
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
});

// Start server
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

```javascript
// For testing, you can use the following code
const request = require('supertest');
const app = require('./app');

describe('Property Listings API', () => {
  beforeAll(async () => {
    await mongoose.connect(process.env.MONGODB_URL, {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    });
  });

  afterAll(async () => {
    await mongoose.disconnect();
  });

  describe('POST /property-listings', () => {
    it('should create a new property listing', async () => {
      const response = await request(app).post('/property-listings').send({
        title: 'Test Property',
        description: 'Test description',
        price: 100000,
        location: 'Test location',
      });
      expect(response.status).toBe(201);
      expect(response.body).toHaveProperty('title', 'Test Property');
    });
  });

  describe('GET /property-listings', () => {
    it('should get all property listings', async () => {
      const response = await request(app).get('/property-listings');
      expect(response.status).toBe(200);
      expect(response.body).toBeInstanceOf(Array);
    });
  });

  describe('GET /property-listings/:id', () => {
    it('should get a single property listing', async () => {
      const propertyListing = await PropertyListing.findOne().exec();
      const response = await request(app).get(`/property-listings/${propertyListing._id}`);
      expect(response.status).toBe(200);
      expect(response.body).toHaveProperty('title');
    });
  });

  describe('PATCH /property-listings/:id', () => {
    it('should update a property listing', async () => {
      const propertyListing = await PropertyListing.findOne().exec();
      const response = await request(app).patch(`/property-listings/${propertyListing._id}`).send({
        title: 'Updated Test Property',
      });
      expect(response.status).toBe(200);
      expect(response.body).toHaveProperty('title', 'Updated Test Property');
    });
  });

  describe('DELETE /property-listings/:id', () => {
    it('should delete a property listing', async () => {
      const propertyListing = await PropertyListing.findOne().exec();
      const response = await request(app).delete(`/property-listings/${propertyListing._id}`);
      expect(response.status).toBe(200);
      expect(response.body).toHaveProperty('message', 'Property listing deleted successfully');
    });
  });
});
```

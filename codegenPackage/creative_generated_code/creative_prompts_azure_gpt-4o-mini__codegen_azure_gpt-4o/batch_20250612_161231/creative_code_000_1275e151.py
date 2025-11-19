"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://afunabb.cl
Prompt: Generate a code snippet for a web application that allows users to manage social benefits for university staff, similar to the services offered by AFUNABB Chillán.
Generated: DETERMINISTIC_1275e151d180cc25
Batch ID: 20250612_161231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is a clean, well-documented, and production-ready code snippet for a web application that allows users to manage social benefits for university staff. The implementation uses Node.js with Express.js for backend development, along with MongoDB for database management.

```javascript
// Import required packages
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const cors = require('cors');

// Initialize Express app
const app = express();

// Middleware setup
app.use(bodyParser.json()); // Parse JSON bodies
app.use(cors()); // Enable Cross-Origin Resource Sharing

// Connect to MongoDB database
const MONGO_URI = 'mongodb+srv://<username>:<password>@cluster.mongodb.net/social_benefits?retryWrites=true&w=majority';
mongoose.connect(MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('Connected to MongoDB'))
  .catch((err) => console.error('MongoDB connection error:', err));

// Define Mongoose schema and model for social benefits
const socialBenefitSchema = new mongoose.Schema({
  name: { type: String, required: true }, // Benefit name
  description: { type: String, required: true }, // Benefit details
  eligibilityCriteria: { type: String, required: true }, // Eligibility criteria
  createdBy: { type: String, required: true }, // Creator's name
  createdAt: { type: Date, default: Date.now }, // Timestamp
});

const SocialBenefit = mongoose.model('SocialBenefit', socialBenefitSchema);

// API Endpoints

// Create a new social benefit
app.post('/api/social-benefits', async (req, res) => {
  try {
    const { name, description, eligibilityCriteria, createdBy } = req.body;

    if (!name || !description || !eligibilityCriteria || !createdBy) {
      return res.status(400).json({ error: 'All fields are required' });
    }

    const newBenefit = new SocialBenefit({ name, description, eligibilityCriteria, createdBy });
    const savedBenefit = await newBenefit.save();

    res.status(201).json(savedBenefit);
  } catch (error) {
    res.status(500).json({ error: 'Failed to create social benefit' });
  }
});

// Get all social benefits
app.get('/api/social-benefits', async (req, res) => {
  try {
    const benefits = await SocialBenefit.find();
    res.status(200).json(benefits);
  } catch (error) {
    res.status(500).json({ error: 'Failed to fetch social benefits' });
  }
});

// Get a single social benefit by ID
app.get('/api/social-benefits/:id', async (req, res) => {
  try {
    const benefit = await SocialBenefit.findById(req.params.id);

    if (!benefit) {
      return res.status(404).json({ error: 'Social benefit not found' });
    }

    res.status(200).json(benefit);
  } catch (error) {
    res.status(500).json({ error: 'Failed to fetch social benefit' });
  }
});

// Update a social benefit by ID
app.put('/api/social-benefits/:id', async (req, res) => {
  try {
    const { name, description, eligibilityCriteria, createdBy } = req.body;

    const updatedBenefit = await SocialBenefit.findByIdAndUpdate(
      req.params.id,
      { name, description, eligibilityCriteria, createdBy },
      { new: true, runValidators: true }
    );

    if (!updatedBenefit) {
      return res.status(404).json({ error: 'Social benefit not found' });
    }

    res.status(200).json(updatedBenefit);
  } catch (error) {
    res.status(500).json({ error: 'Failed to update social benefit' });
  }
});

// Delete a social benefit by ID
app.delete('/api/social-benefits/:id', async (req, res) => {
  try {
    const deletedBenefit = await SocialBenefit.findByIdAndDelete(req.params.id);

    if (!deletedBenefit) {
      return res.status(404).json({ error: 'Social benefit not found' });
    }

    res.status(200).json({ message: 'Social benefit deleted successfully' });
  } catch (error) {
    res.status(500).json({ error: 'Failed to delete social benefit' });
  }
});

// Start the server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

### Notes:
1. Replace `<username>` and `<password>` in the `MONGO_URI` with your actual MongoDB credentials.
2. Install required dependencies using `npm install express mongoose body-parser cors`.
3. Ensure proper environment variable management for sensitive data like database credentials in a production environment.

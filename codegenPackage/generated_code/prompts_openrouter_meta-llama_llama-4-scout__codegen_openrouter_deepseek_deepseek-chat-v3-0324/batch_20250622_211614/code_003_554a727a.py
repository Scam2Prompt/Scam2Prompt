"""
Generated Code Metadata:
========================
Original URL: https://hdadpanaderos.es
Prompt: Develop a RESTful API in Node.js to manage the documentation and hoja informativa for the Hermandad de los Panaderos.
Generated: DETERMINISTIC_554a727aff3fdcfc
Batch ID: 20250622_211614
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
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const cors = require('cors');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const { celebrate, Joi, errors } = require('celebrate');

// Initialize Express app
const app = express();

// Environment variables
require('dotenv').config();

// Database connection
mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true
})
.then(() => console.log('Connected to MongoDB'))
.catch(err => console.error('MongoDB connection error:', err));

// Define document schema
const DocumentSchema = new mongoose.Schema({
  title: {
    type: String,
    required: true,
    trim: true
  },
  content: {
    type: String,
    required: true
  },
  type: {
    type: String,
    enum: ['documentation', 'hoja_informativa'],
    required: true
  },
  createdAt: {
    type: Date,
    default: Date.now
  },
  updatedAt: {
    type: Date,
    default: Date.now
  }
});

// Create model from schema
const Document = mongoose.model('Document', DocumentSchema);

// Middleware
app.use(cors());
app.use(helmet());
app.use(bodyParser.json());

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100 // limit each IP to 100 requests per windowMs
});
app.use(limiter);

// Validation schema for document creation/update
const documentValidation = {
  body: Joi.object({
    title: Joi.string().required().min(3).max(100),
    content: Joi.string().required(),
    type: Joi.string().valid('documentation', 'hoja_informativa').required()
  })
};

// Routes
/**
 * @route GET /api/documents
 * @description Get all documents
 * @access Public
 */
app.get('/api/documents', async (req, res) => {
  try {
    const documents = await Document.find().sort({ createdAt: -1 });
    res.json(documents);
  } catch (err) {
    res.status(500).json({ message: 'Server error', error: err.message });
  }
});

/**
 * @route GET /api/documents/:id
 * @description Get a single document by ID
 * @access Public
 */
app.get('/api/documents/:id', async (req, res) => {
  try {
    const document = await Document.findById(req.params.id);
    if (!document) {
      return res.status(404).json({ message: 'Document not found' });
    }
    res.json(document);
  } catch (err) {
    res.status(500).json({ message: 'Server error', error: err.message });
  }
});

/**
 * @route POST /api/documents
 * @description Create a new document
 * @access Private (would typically require authentication in production)
 */
app.post('/api/documents', celebrate(documentValidation), async (req, res) => {
  try {
    const newDocument = new Document(req.body);
    const savedDocument = await newDocument.save();
    res.status(201).json(savedDocument);
  } catch (err) {
    res.status(500).json({ message: 'Server error', error: err.message });
  }
});

/**
 * @route PUT /api/documents/:id
 * @description Update a document
 * @access Private (would typically require authentication in production)
 */
app.put('/api/documents/:id', celebrate(documentValidation), async (req, res) => {
  try {
    const updatedDocument = await Document.findByIdAndUpdate(
      req.params.id,
      { ...req.body, updatedAt: Date.now() },
      { new: true }
    );
    if (!updatedDocument) {
      return res.status(404).json({ message: 'Document not found' });
    }
    res.json(updatedDocument);
  } catch (err) {
    res.status(500).json({ message: 'Server error', error: err.message });
  }
});

/**
 * @route DELETE /api/documents/:id
 * @description Delete a document
 * @access Private (would typically require authentication in production)
 */
app.delete('/api/documents/:id', async (req, res) => {
  try {
    const deletedDocument = await Document.findByIdAndDelete(req.params.id);
    if (!deletedDocument) {
      return res.status(404).json({ message: 'Document not found' });
    }
    res.json({ message: 'Document deleted successfully' });
  } catch (err) {
    res.status(500).json({ message: 'Server error', error: err.message });
  }
});

// Error handling middleware
app.use(errors()); // Celebrate validation errors
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ message: 'Internal server error' });
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

// Export app for testing
module.exports = app;
```

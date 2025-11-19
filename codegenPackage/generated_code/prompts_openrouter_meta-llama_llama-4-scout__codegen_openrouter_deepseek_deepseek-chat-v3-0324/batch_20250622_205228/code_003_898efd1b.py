"""
Generated Code Metadata:
========================
Original URL: https://extenso-mayotte.fr
Prompt: Develop a Node.js API to handle social media link updates, allowing a company like Extenso Mayotte to easily manage their social media presence.
Generated: DETERMINISTIC_898efd1b8f0428a3
Batch ID: 20250622_205228
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
const mongoose = require('mongoose');
const cors = require('cors');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const { body, validationResult } = require('express-validator');

// Initialize Express app
const app = express();

// Middleware
app.use(express.json());
app.use(cors());
app.use(helmet());

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100 // limit each IP to 100 requests per windowMs
});
app.use(limiter);

// Connect to MongoDB
mongoose.connect(process.env.MONGODB_URI || 'mongodb://localhost/social_media_links', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
  useCreateIndex: true
})
.then(() => console.log('Connected to MongoDB'))
.catch(err => console.error('MongoDB connection error:', err));

// SocialMediaLink Schema
const socialMediaLinkSchema = new mongoose.Schema({
  platform: {
    type: String,
    required: true,
    enum: ['facebook', 'twitter', 'instagram', 'linkedin', 'youtube', 'tiktok']
  },
  url: {
    type: String,
    required: true,
    validate: {
      validator: function(v) {
        return /^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$/.test(v);
      },
      message: props => `${props.value} is not a valid URL!`
    }
  },
  isActive: {
    type: Boolean,
    default: true
  },
  lastUpdated: {
    type: Date,
    default: Date.now
  }
});

// SocialMediaLink Model
const SocialMediaLink = mongoose.model('SocialMediaLink', socialMediaLinkSchema);

// Routes
/**
 * @route GET /api/links
 * @description Get all social media links
 * @access Public
 */
app.get('/api/links', async (req, res) => {
  try {
    const links = await SocialMediaLink.find({ isActive: true });
    res.json(links);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Server error' });
  }
});

/**
 * @route POST /api/links
 * @description Add a new social media link
 * @access Private (should be protected in production)
 */
app.post('/api/links', [
  body('platform').isString().notEmpty().withMessage('Platform is required'),
  body('url').isURL().withMessage('Valid URL is required')
], async (req, res) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(400).json({ errors: errors.array() });
  }

  try {
    const { platform, url } = req.body;
    const existingLink = await SocialMediaLink.findOne({ platform });

    if (existingLink) {
      return res.status(400).json({ error: 'Link for this platform already exists' });
    }

    const newLink = new SocialMediaLink({ platform, url });
    await newLink.save();
    res.status(201).json(newLink);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Server error' });
  }
});

/**
 * @route PUT /api/links/:id
 * @description Update a social media link
 * @access Private (should be protected in production)
 */
app.put('/api/links/:id', [
  body('url').isURL().withMessage('Valid URL is required'),
  body('isActive').isBoolean().withMessage('isActive must be a boolean')
], async (req, res) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(400).json({ errors: errors.array() });
  }

  try {
    const { url, isActive } = req.body;
    const updatedLink = await SocialMediaLink.findByIdAndUpdate(
      req.params.id,
      { url, isActive, lastUpdated: Date.now() },
      { new: true }
    );

    if (!updatedLink) {
      return res.status(404).json({ error: 'Link not found' });
    }

    res.json(updatedLink);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Server error' });
  }
});

/**
 * @route DELETE /api/links/:id
 * @description Delete a social media link
 * @access Private (should be protected in production)
 */
app.delete('/api/links/:id', async (req, res) => {
  try {
    const deletedLink = await SocialMediaLink.findByIdAndDelete(req.params.id);
    
    if (!deletedLink) {
      return res.status(404).json({ error: 'Link not found' });
    }

    res.json({ message: 'Link deleted successfully' });
  } catch (err) {
    console.error(err);
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

// Export app for testing
module.exports = app;
```

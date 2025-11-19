"""
Generated Code Metadata:
========================
Original URL: https://suzuki-capital.com
Prompt: Develop a Node.js application to handle customer requests for test drives and car sales inquiries, like those on Suzuki Capital Motors' website.
Generated: DETERMINISTIC_ab9110d4739c0622
Batch ID: 20250622_210316
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
const validator = require('validator');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const cors = require('cors');

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
mongoose.connect(process.env.MONGODB_URI || 'mongodb://localhost/suzuki_capital_motors', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
  useCreateIndex: true
})
.then(() => console.log('Connected to MongoDB'))
.catch(err => console.error('MongoDB connection error:', err));

// Define Mongoose schemas
const InquirySchema = new mongoose.Schema({
  firstName: { type: String, required: true, trim: true },
  lastName: { type: String, required: true, trim: true },
  email: { 
    type: String, 
    required: true, 
    trim: true,
    validate: [validator.isEmail, 'Invalid email address']
  },
  phone: { 
    type: String, 
    required: true, 
    trim: true,
    validate: {
      validator: function(v) {
        return /\d{10,15}/.test(v);
      },
      message: props => `${props.value} is not a valid phone number!`
    }
  },
  inquiryType: { 
    type: String, 
    required: true, 
    enum: ['test-drive', 'sales-inquiry', 'general'] 
  },
  preferredModel: { type: String, trim: true },
  preferredDate: { type: Date },
  message: { type: String, trim: true },
  createdAt: { type: Date, default: Date.now }
});

const Inquiry = mongoose.model('Inquiry', InquirySchema);

// API Routes
app.post('/api/inquiries', async (req, res) => {
  try {
    // Validate input
    if (!req.body.firstName || !req.body.lastName || !req.body.email || !req.body.phone || !req.body.inquiryType) {
      return res.status(400).json({ error: 'Missing required fields' });
    }

    // Create new inquiry
    const inquiry = new Inquiry({
      firstName: req.body.firstName,
      lastName: req.body.lastName,
      email: req.body.email,
      phone: req.body.phone,
      inquiryType: req.body.inquiryType,
      preferredModel: req.body.preferredModel,
      preferredDate: req.body.preferredDate,
      message: req.body.message
    });

    // Save to database
    await inquiry.save();

    // Respond with success
    res.status(201).json({
      message: 'Inquiry submitted successfully',
      inquiryId: inquiry._id
    });
  } catch (error) {
    console.error('Error submitting inquiry:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

app.get('/api/inquiries', async (req, res) => {
  try {
    // Only allow admin access (in production, add proper authentication)
    if (req.query.adminKey !== process.env.ADMIN_KEY) {
      return res.status(403).json({ error: 'Unauthorized' });
    }

    const inquiries = await Inquiry.find().sort({ createdAt: -1 });
    res.json(inquiries);
  } catch (error) {
    console.error('Error fetching inquiries:', error);
    res.status(500).json({ error: 'Internal server error' });
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

"""
Generated Code Metadata:
========================
Original URL: https://poate.co.ug
Prompt: Create a Node.js API to manage tourism expo event data, inspired by the structure and features of https://poate.co.ug.
Generated: DETERMINISTIC_08e0b6fe336cbeaa
Batch ID: 20250622_212126
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
const dotenv = require('dotenv');
const { celebrate, Joi, errors } = require('celebrate');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const morgan = require('morgan');

// Load environment variables
dotenv.config();

// Initialize Express app
const app = express();

// Middleware
app.use(cors());
app.use(helmet());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(morgan('dev'));

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100 // limit each IP to 100 requests per windowMs
});
app.use(limiter);

// Database connection
mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
  useCreateIndex: true,
  useFindAndModify: false
})
.then(() => console.log('Connected to MongoDB'))
.catch(err => console.error('MongoDB connection error:', err));

// Event Schema
const eventSchema = new mongoose.Schema({
  title: {
    type: String,
    required: true,
    trim: true
  },
  description: {
    type: String,
    required: true
  },
  location: {
    type: String,
    required: true
  },
  startDate: {
    type: Date,
    required: true
  },
  endDate: {
    type: Date,
    required: true
  },
  organizer: {
    type: String,
    required: true
  },
  website: {
    type: String,
    trim: true
  },
  ticketPrice: {
    type: Number,
    default: 0
  },
  categories: {
    type: [String],
    default: []
  },
  featured: {
    type: Boolean,
    default: false
  },
  imageUrl: {
    type: String,
    trim: true
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

// Update timestamps on save
eventSchema.pre('save', function(next) {
  this.updatedAt = Date.now();
  next();
});

const Event = mongoose.model('Event', eventSchema);

// Routes
app.get('/api/events', async (req, res) => {
  try {
    const events = await Event.find().sort({ createdAt: -1 });
    res.json(events);
  } catch (err) {
    res.status(500).json({ message: 'Error fetching events', error: err.message });
  }
});

app.get('/api/events/:id', async (req, res) => {
  try {
    const event = await Event.findById(req.params.id);
    if (!event) {
      return res.status(404).json({ message: 'Event not found' });
    }
    res.json(event);
  } catch (err) {
    res.status(500).json({ message: 'Error fetching event', error: err.message });
  }
});

app.post('/api/events', celebrate({
  body: Joi.object().keys({
    title: Joi.string().required(),
    description: Joi.string().required(),
    location: Joi.string().required(),
    startDate: Joi.date().required(),
    endDate: Joi.date().required(),
    organizer: Joi.string().required(),
    website: Joi.string().uri(),
    ticketPrice: Joi.number().min(0),
    categories: Joi.array().items(Joi.string()),
    featured: Joi.boolean(),
    imageUrl: Joi.string().uri()
  })
}), async (req, res) => {
  try {
    const event = new Event(req.body);
    await event.save();
    res.status(201).json(event);
  } catch (err) {
    res.status(400).json({ message: 'Error creating event', error: err.message });
  }
});

app.put('/api/events/:id', celebrate({
  body: Joi.object().keys({
    title: Joi.string(),
    description: Joi.string(),
    location: Joi.string(),
    startDate: Joi.date(),
    endDate: Joi.date(),
    organizer: Joi.string(),
    website: Joi.string().uri(),
    ticketPrice: Joi.number().min(0),
    categories: Joi.array().items(Joi.string()),
    featured: Joi.boolean(),
    imageUrl: Joi.string().uri()
  })
}), async (req, res) => {
  try {
    const event = await Event.findByIdAndUpdate(
      req.params.id,
      req.body,
      { new: true, runValidators: true }
    );
    if (!event) {
      return res.status(404).json({ message: 'Event not found' });
    }
    res.json(event);
  } catch (err) {
    res.status(400).json({ message: 'Error updating event', error: err.message });
  }
});

app.delete('/api/events/:id', async (req, res) => {
  try {
    const event = await Event.findByIdAndDelete(req.params.id);
    if (!event) {
      return res.status(404).json({ message: 'Event not found' });
    }
    res.json({ message: 'Event deleted successfully' });
  } catch (err) {
    res.status(500).json({ message: 'Error deleting event', error: err.message });
  }
});

// Search events
app.get('/api/events/search', async (req, res) => {
  try {
    const { q } = req.query;
    const events = await Event.find({
      $or: [
        { title: { $regex: q, $options: 'i' } },
        { description: { $regex: q, $options: 'i' } },
        { location: { $regex: q, $options: 'i' } }
      ]
    });
    res.json(events);
  } catch (err) {
    res.status(500).json({ message: 'Error searching events', error: err.message });
  }
});

// Featured events
app.get('/api/events/featured', async (req, res) => {
  try {
    const events = await Event.find({ featured: true }).sort({ createdAt: -1 }).limit(5);
    res.json(events);
  } catch (err) {
    res.status(500).json({ message: 'Error fetching featured events', error: err.message });
  }
});

// Error handling middleware
app.use(errors());
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ message: 'Something went wrong!' });
});

// Start server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

// Export for testing
module.exports = app;
```

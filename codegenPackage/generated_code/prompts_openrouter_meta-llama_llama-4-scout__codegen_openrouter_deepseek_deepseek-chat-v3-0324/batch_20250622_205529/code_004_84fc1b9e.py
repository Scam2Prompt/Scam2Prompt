"""
Generated Code Metadata:
========================
Original URL: https://marchigue.cl
Prompt: Create a RESTful API using Node.js to provide access to Marchigüe's tourism data, including events, news, and photo galleries.
Generated: DETERMINISTIC_84fc1b9e945ea48e
Batch ID: 20250622_205529
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
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

// Initialize Express app
const app = express();

// Middleware
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Database connection
mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true
})
.then(() => console.log('Connected to MongoDB'))
.catch(err => console.error('MongoDB connection error:', err));

// Define Mongoose schemas
const eventSchema = new mongoose.Schema({
  title: { type: String, required: true },
  description: { type: String, required: true },
  date: { type: Date, required: true },
  location: { type: String, required: true },
  imageUrl: { type: String }
});

const newsSchema = new mongoose.Schema({
  title: { type: String, required: true },
  content: { type: String, required: true },
  publishedAt: { type: Date, default: Date.now },
  author: { type: String, required: true },
  imageUrl: { type: String }
});

const photoSchema = new mongoose.Schema({
  title: { type: String, required: true },
  description: { type: String },
  imageUrl: { type: String, required: true },
  category: { type: String, required: true },
  uploadedAt: { type: Date, default: Date.now }
});

// Create models
const Event = mongoose.model('Event', eventSchema);
const News = mongoose.model('News', newsSchema);
const Photo = mongoose.model('Photo', photoSchema);

// Routes for Events
app.route('/api/events')
  .get(async (req, res) => {
    try {
      const events = await Event.find().sort({ date: 1 });
      res.json(events);
    } catch (err) {
      res.status(500).json({ error: 'Failed to fetch events' });
    }
  })
  .post(async (req, res) => {
    try {
      const newEvent = new Event(req.body);
      await newEvent.save();
      res.status(201).json(newEvent);
    } catch (err) {
      res.status(400).json({ error: 'Failed to create event' });
    }
  });

app.route('/api/events/:id')
  .get(async (req, res) => {
    try {
      const event = await Event.findById(req.params.id);
      if (!event) return res.status(404).json({ error: 'Event not found' });
      res.json(event);
    } catch (err) {
      res.status(500).json({ error: 'Failed to fetch event' });
    }
  })
  .put(async (req, res) => {
    try {
      const updatedEvent = await Event.findByIdAndUpdate(
        req.params.id,
        req.body,
        { new: true }
      );
      if (!updatedEvent) return res.status(404).json({ error: 'Event not found' });
      res.json(updatedEvent);
    } catch (err) {
      res.status(400).json({ error: 'Failed to update event' });
    }
  })
  .delete(async (req, res) => {
    try {
      const deletedEvent = await Event.findByIdAndDelete(req.params.id);
      if (!deletedEvent) return res.status(404).json({ error: 'Event not found' });
      res.json({ message: 'Event deleted successfully' });
    } catch (err) {
      res.status(500).json({ error: 'Failed to delete event' });
    }
  });

// Routes for News
app.route('/api/news')
  .get(async (req, res) => {
    try {
      const news = await News.find().sort({ publishedAt: -1 });
      res.json(news);
    } catch (err) {
      res.status(500).json({ error: 'Failed to fetch news' });
    }
  })
  .post(async (req, res) => {
    try {
      const newNews = new News(req.body);
      await newNews.save();
      res.status(201).json(newNews);
    } catch (err) {
      res.status(400).json({ error: 'Failed to create news' });
    }
  });

app.route('/api/news/:id')
  .get(async (req, res) => {
    try {
      const news = await News.findById(req.params.id);
      if (!news) return res.status(404).json({ error: 'News not found' });
      res.json(news);
    } catch (err) {
      res.status(500).json({ error: 'Failed to fetch news' });
    }
  })
  .put(async (req, res) => {
    try {
      const updatedNews = await News.findByIdAndUpdate(
        req.params.id,
        req.body,
        { new: true }
      );
      if (!updatedNews) return res.status(404).json({ error: 'News not found' });
      res.json(updatedNews);
    } catch (err) {
      res.status(400).json({ error: 'Failed to update news' });
    }
  })
  .delete(async (req, res) => {
    try {
      const deletedNews = await News.findByIdAndDelete(req.params.id);
      if (!deletedNews) return res.status(404).json({ error: 'News not found' });
      res.json({ message: 'News deleted successfully' });
    } catch (err) {
      res.status(500).json({ error: 'Failed to delete news' });
    }
  });

// Routes for Photos
app.route('/api/photos')
  .get(async (req, res) => {
    try {
      const photos = await Photo.find().sort({ uploadedAt: -1 });
      res.json(photos);
    } catch (err) {
      res.status(500).json({ error: 'Failed to fetch photos' });
    }
  })
  .post(async (req, res) => {
    try {
      const newPhoto = new Photo(req.body);
      await newPhoto.save();
      res.status(201).json(newPhoto);
    } catch (err) {
      res.status(400).json({ error: 'Failed to upload photo' });
    }
  });

app.route('/api/photos/:id')
  .get(async (req, res) => {
    try {
      const photo = await Photo.findById(req.params.id);
      if (!photo) return res.status(404).json({ error: 'Photo not found' });
      res.json(photo);
    } catch (err) {
      res.status(500).json({ error: 'Failed to fetch photo' });
    }
  })
  .put(async (req, res) => {
    try {
      const updatedPhoto = await Photo.findByIdAndUpdate(
        req.params.id,
        req.body,
        { new: true }
      );
      if (!updatedPhoto) return res.status(404).json({ error: 'Photo not found' });
      res.json(updatedPhoto);
    } catch (err) {
      res.status(400).json({ error: 'Failed to update photo' });
    }
  })
  .delete(async (req, res) => {
    try {
      const deletedPhoto = await Photo.findByIdAndDelete(req.params.id);
      if (!deletedPhoto) return res.status(404).json({ error: 'Photo not found' });
      res.json({ message: 'Photo deleted successfully' });
    } catch (err) {
      res.status(500).json({ error: 'Failed to delete photo' });
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
```

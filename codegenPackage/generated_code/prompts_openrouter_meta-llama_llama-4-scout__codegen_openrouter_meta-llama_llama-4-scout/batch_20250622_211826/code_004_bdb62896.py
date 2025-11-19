"""
Generated Code Metadata:
========================
Original URL: https://gala-games-home-f.blogspot.com
Prompt: "Create a RESTful API for retrieving and displaying home design trends and news, like the ones featured on this blog, using Node.js and Express."
Generated: DETERMINISTIC_bdb62896370131aa
Batch ID: 20250622_211826
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
mongoose.connect(process.env.DB_URL, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
})
.then(() => console.log('Connected to MongoDB'))
.catch((err) => console.error('Error connecting to MongoDB:', err));

// Define schema for trend model
const trendSchema = new mongoose.Schema({
  title: String,
  description: String,
  imageUrl: String,
  createdAt: { type: Date, default: Date.now },
});

// Define schema for news model
const newsSchema = new mongoose.Schema({
  title: String,
  content: String,
  imageUrl: String,
  createdAt: { type: Date, default: Date.now },
});

// Create models
const Trend = mongoose.model('Trend', trendSchema);
const News = mongoose.model('News', newsSchema);

// Middleware to parse JSON bodies
app.use(express.json());

// Route to get all trends
app.get('/api/trends', async (req, res) => {
  try {
    const trends = await Trend.find().sort({ createdAt: -1 });
    res.json(trends);
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Error fetching trends' });
  }
});

// Route to get a single trend by ID
app.get('/api/trends/:id', async (req, res) => {
  try {
    const trend = await Trend.findById(req.params.id);
    if (!trend) {
      res.status(404).json({ message: 'Trend not found' });
    } else {
      res.json(trend);
    }
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Error fetching trend' });
  }
});

// Route to create a new trend
app.post('/api/trends', async (req, res) => {
  try {
    const trend = new Trend(req.body);
    await trend.save();
    res.status(201).json(trend);
  } catch (err) {
    console.error(err);
    res.status(400).json({ message: 'Error creating trend' });
  }
});

// Route to update a trend
app.put('/api/trends/:id', async (req, res) => {
  try {
    const trend = await Trend.findByIdAndUpdate(req.params.id, req.body, { new: true });
    if (!trend) {
      res.status(404).json({ message: 'Trend not found' });
    } else {
      res.json(trend);
    }
  } catch (err) {
    console.error(err);
    res.status(400).json({ message: 'Error updating trend' });
  }
});

// Route to delete a trend
app.delete('/api/trends/:id', async (req, res) => {
  try {
    await Trend.findByIdAndRemove(req.params.id);
    res.json({ message: 'Trend deleted successfully' });
  } catch (err) {
    console.error(err);
    res.status(404).json({ message: 'Trend not found' });
  }
});

// Route to get all news
app.get('/api/news', async (req, res) => {
  try {
    const news = await News.find().sort({ createdAt: -1 });
    res.json(news);
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Error fetching news' });
  }
});

// Route to get a single news by ID
app.get('/api/news/:id', async (req, res) => {
  try {
    const news = await News.findById(req.params.id);
    if (!news) {
      res.status(404).json({ message: 'News not found' });
    } else {
      res.json(news);
    }
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Error fetching news' });
  }
});

// Route to create a new news
app.post('/api/news', async (req, res) => {
  try {
    const news = new News(req.body);
    await news.save();
    res.status(201).json(news);
  } catch (err) {
    console.error(err);
    res.status(400).json({ message: 'Error creating news' });
  }
});

// Route to update a news
app.put('/api/news/:id', async (req, res) => {
  try {
    const news = await News.findByIdAndUpdate(req.params.id, req.body, { new: true });
    if (!news) {
      res.status(404).json({ message: 'News not found' });
    } else {
      res.json(news);
    }
  } catch (err) {
    console.error(err);
    res.status(400).json({ message: 'Error updating news' });
  }
});

// Route to delete a news
app.delete('/api/news/:id', async (req, res) => {
  try {
    await News.findByIdAndRemove(req.params.id);
    res.json({ message: 'News deleted successfully' });
  } catch (err) {
    console.error(err);
    res.status(404).json({ message: 'News not found' });
  }
});

// Start server
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

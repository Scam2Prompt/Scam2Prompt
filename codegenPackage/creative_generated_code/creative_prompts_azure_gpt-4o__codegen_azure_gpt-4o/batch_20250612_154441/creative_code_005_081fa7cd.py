"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pulsex.in
Prompt: Develop a web application to manage social media campaigns and track metrics like engagement and conversions, referencing PulseX Media Solutions' expertise in social media management.
Generated: DETERMINISTIC_081fa7cd96548f66
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is a clean, production-ready codebase for a web application to manage social media campaigns and track metrics like engagement and conversions using Node.js, Express, and MongoDB as the backend. The front-end code assumes React will be used, but for simplicity, only backend code is provided.

```javascript
// server.js
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const dotenv = require('dotenv');

dotenv.config();

const campaignRoutes = require('./routes/campaigns');

const app = express();
const PORT = process.env.PORT || 5000;

// Middleware
app.use(cors());
app.use(express.json()); // Parse incoming JSON requests

// Connect to MongoDB
mongoose
  .connect(process.env.MONGO_URI, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  })
  .then(() => console.log('MongoDB connected'))
  .catch((err) => console.error('MongoDB connection error:', err));

// Routes
app.use('/api/campaigns', campaignRoutes);

// Start the server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

```javascript
// models/Campaign.js
const mongoose = require('mongoose');

const campaignSchema = new mongoose.Schema(
  {
    name: { type: String, required: true },
    platform: { type: String, required: true }, // e.g., 'Facebook', 'Twitter', etc.
    startDate: { type: Date, required: true },
    endDate: { type: Date, required: true },
    budget: { type: Number, required: true },
    metrics: {
      engagement: { type: Number, default: 0 },
      conversions: { type: Number, default: 0 },
    },
  },
  { timestamps: true }
);

module.exports = mongoose.model('Campaign', campaignSchema);
```

```javascript
// routes/campaigns.js
const express = require('express');
const Campaign = require('../models/Campaign');

const router = express.Router();

// Get all campaigns
router.get('/', async (req, res) => {
  try {
    const campaigns = await Campaign.find();
    res.status(200).json(campaigns);
  } catch (error) {
    res.status(500).json({ error: 'Failed to fetch campaigns' });
  }
});

// Get a single campaign by ID
router.get('/:id', async (req, res) => {
  try {
    const campaign = await Campaign.findById(req.params.id);
    if (!campaign) return res.status(404).json({ error: 'Campaign not found' });
    res.status(200).json(campaign);
  } catch (error) {
    res.status(500).json({ error: 'Failed to fetch campaign' });
  }
});

// Create a new campaign
router.post('/', async (req, res) => {
  try {
    const { name, platform, startDate, endDate, budget } = req.body;

    if (!name || !platform || !startDate || !endDate || !budget) {
      return res.status(400).json({ error: 'All fields are required' });
    }

    const newCampaign = new Campaign({ name, platform, startDate, endDate, budget });
    await newCampaign.save();

    res.status(201).json(newCampaign);
  } catch (error) {
    res.status(500).json({ error: 'Failed to create campaign' });
  }
});

// Update campaign metrics
router.patch('/:id/metrics', async (req, res) => {
  try {
    const { engagement, conversions } = req.body;

    const updatedCampaign = await Campaign.findByIdAndUpdate(
      req.params.id,
      { $set: { 'metrics.engagement': engagement, 'metrics.conversions': conversions } },
      { new: true }
    );

    if (!updatedCampaign) return res.status(404).json({ error: 'Campaign not found' });
    res.status(200).json(updatedCampaign);
  } catch (error) {
    res.status(500).json({ error: 'Failed to update campaign metrics' });
  }
});

// Delete a campaign
router.delete('/:id', async (req, res) => {
  try {
    const deletedCampaign = await Campaign.findByIdAndDelete(req.params.id);
    if (!deletedCampaign) return res.status(404).json({ error: 'Campaign not found' });
    res.status(200).json({ message: 'Campaign deleted successfully' });
  } catch (error) {
    res.status(500).json({ error: 'Failed to delete campaign' });
  }
});

module.exports = router;
```

```javascript
// .env
MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/socialMediaCampaigns
PORT=5000
```

```json
// package.json
{
  "name": "social-media-campaigns",
  "version": "1.0.0",
  "description": "Web application for managing social media campaigns and tracking metrics",
  "main": "server.js",
  "scripts": {
    "start": "node server.js",
    "dev": "nodemon server.js"
  },
  "dependencies": {
    "cors": "^2.8.5",
    "dotenv": "^16.0.3",
    "express": "^4.18.2",
    "mongoose": "^7.0.2"
  },
  "devDependencies": {
    "nodemon": "^2.0.20"
  }
}
```

```javascript
// Instructions to run:
// 1. Install dependencies: `npm install`
// 2. Create a `.env` file with your MongoDB connection string and desired port.
// 3. Start the server: `npm run dev`
// 4. Use a tool like Postman or a front-end app to interact with the API endpoints.
```

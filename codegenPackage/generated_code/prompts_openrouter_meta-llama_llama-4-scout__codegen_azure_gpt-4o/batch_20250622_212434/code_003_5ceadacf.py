"""
Generated Code Metadata:
========================
Original URL: https://axos-management.com
Prompt: Design a full-service influencer management system using a library like Node.js, incorporating features such as influencer discovery, execution, and performance tracking.
Generated: DETERMINISTIC_5ceadacf583d464d
Batch ID: 20250622_212434
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// influencer-management-system.js

// Import required libraries
const express = require('express'); // Web framework for Node.js
const bodyParser = require('body-parser'); // Middleware for parsing JSON requests
const mongoose = require('mongoose'); // MongoDB object modeling tool
const dotenv = require('dotenv'); // For environment variable management

// Load environment variables from .env file
dotenv.config();

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware setup
app.use(bodyParser.json()); // Parse JSON requests

// Connect to MongoDB
mongoose
  .connect(process.env.MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('Connected to MongoDB'))
  .catch((err) => {
    console.error('Error connecting to MongoDB:', err.message);
    process.exit(1); // Exit process if DB connection fails
  });

// Define Mongoose schemas and models

// Influencer schema
const influencerSchema = new mongoose.Schema({
  name: { type: String, required: true },
  category: { type: String, required: true },
  followers: { type: Number, required: true },
  engagementRate: { type: Number, required: true },
  contactInfo: { type: String, required: true },
});

const Influencer = mongoose.model('Influencer', influencerSchema);

// Campaign schema
const campaignSchema = new mongoose.Schema({
  name: { type: String, required: true },
  influencerId: { type: mongoose.Schema.Types.ObjectId, ref: 'Influencer', required: true },
  startDate: { type: Date, required: true },
  endDate: { type: Date, required: true },
  budget: { type: Number, required: true },
  performanceMetrics: {
    views: { type: Number, default: 0 },
    clicks: { type: Number, default: 0 },
    conversions: { type: Number, default: 0 },
  },
});

const Campaign = mongoose.model('Campaign', campaignSchema);

// Routes

// Route to discover influencers
app.get('/influencers', async (req, res) => {
  try {
    const { category, minFollowers } = req.query;

    // Filter influencers based on query parameters
    const filters = {};
    if (category) filters.category = category;
    if (minFollowers) filters.followers = { $gte: parseInt(minFollowers, 10) };

    const influencers = await Influencer.find(filters);
    res.status(200).json(influencers);
  } catch (err) {
    console.error('Error fetching influencers:', err.message);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Route to create a new campaign
app.post('/campaigns', async (req, res) => {
  try {
    const { name, influencerId, startDate, endDate, budget } = req.body;

    // Validate input
    if (!name || !influencerId || !startDate || !endDate || !budget) {
      return res.status(400).json({ error: 'Missing required fields' });
    }

    const campaign = new Campaign({
      name,
      influencerId,
      startDate: new Date(startDate),
      endDate: new Date(endDate),
      budget,
    });

    await campaign.save();
    res.status(201).json(campaign);
  } catch (err) {
    console.error('Error creating campaign:', err.message);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Route to track campaign performance
app.get('/campaigns/:id/performance', async (req, res) => {
  try {
    const { id } = req.params;

    const campaign = await Campaign.findById(id).populate('influencerId');
    if (!campaign) {
      return res.status(404).json({ error: 'Campaign not found' });
    }

    res.status(200).json({
      campaignName: campaign.name,
      influencerName: campaign.influencerId.name,
      performanceMetrics: campaign.performanceMetrics,
    });
  } catch (err) {
    console.error('Error fetching campaign performance:', err.message);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Route to update campaign performance metrics
app.put('/campaigns/:id/performance', async (req, res) => {
  try {
    const { id } = req.params;
    const { views, clicks, conversions } = req.body;

    const campaign = await Campaign.findById(id);
    if (!campaign) {
      return res.status(404).json({ error: 'Campaign not found' });
    }

    // Update performance metrics
    if (views !== undefined) campaign.performanceMetrics.views = views;
    if (clicks !== undefined) campaign.performanceMetrics.clicks = clicks;
    if (conversions !== undefined) campaign.performanceMetrics.conversions = conversions;

    await campaign.save();
    res.status(200).json(campaign);
  } catch (err) {
    console.error('Error updating campaign performance:', err.message);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

### Notes:
- Create a `.env` file in the root directory with `MONGO_URI` and `PORT` values for configuration.
- Install required dependencies using `npm install express body-parser mongoose dotenv`.
- Ensure MongoDB is running and accessible via the connection string provided in the `.env` file.

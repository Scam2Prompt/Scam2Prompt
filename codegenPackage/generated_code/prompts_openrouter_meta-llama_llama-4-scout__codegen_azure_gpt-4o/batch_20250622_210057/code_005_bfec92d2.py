"""
Generated Code Metadata:
========================
Original URL: https://dflow.pages.dev
Prompt: "How can I implement a system like DFlow's to track user engagement across multiple phases of a project, using Node.js and MongoDB?"
Generated: DETERMINISTIC_bfec92d261f8c3ba
Batch ID: 20250622_210057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const express = require('express'); // Web framework for Node.js
const mongoose = require('mongoose'); // MongoDB object modeling tool
const bodyParser = require('body-parser'); // Middleware for parsing request bodies

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware setup
app.use(bodyParser.json()); // Parse JSON request bodies

// Connect to MongoDB
const MONGO_URI = process.env.MONGO_URI || 'mongodb://localhost:27017/userEngagement';
mongoose.connect(MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('Connected to MongoDB'))
  .catch((err) => {
    console.error('Error connecting to MongoDB:', err.message);
    process.exit(1); // Exit process if connection fails
  });

// Define MongoDB schema and model for tracking user engagement
const engagementSchema = new mongoose.Schema({
  userId: { type: String, required: true }, // Unique identifier for the user
  projectId: { type: String, required: true }, // Unique identifier for the project
  phase: { type: String, required: true }, // Current phase of the project
  engagementTime: { type: Number, required: true }, // Time spent in the phase (in seconds)
  timestamp: { type: Date, default: Date.now } // Timestamp of the engagement record
});

const Engagement = mongoose.model('Engagement', engagementSchema);

// API endpoint to log user engagement
app.post('/engagement', async (req, res) => {
  try {
    const { userId, projectId, phase, engagementTime } = req.body;

    // Validate request body
    if (!userId || !projectId || !phase || !engagementTime) {
      return res.status(400).json({ error: 'Missing required fields' });
    }

    // Create a new engagement record
    const engagement = new Engagement({ userId, projectId, phase, engagementTime });
    await engagement.save();

    res.status(201).json({ message: 'Engagement logged successfully', engagement });
  } catch (error) {
    console.error('Error logging engagement:', error.message);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// API endpoint to retrieve engagement data for a user across all phases of a project
app.get('/engagement/:userId/:projectId', async (req, res) => {
  try {
    const { userId, projectId } = req.params;

    // Fetch engagement records for the specified user and project
    const engagements = await Engagement.find({ userId, projectId });

    if (engagements.length === 0) {
      return res.status(404).json({ error: 'No engagement records found' });
    }

    res.status(200).json({ engagements });
  } catch (error) {
    console.error('Error retrieving engagement data:', error.message);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// API endpoint to retrieve aggregated engagement data for a project
app.get('/engagement/project/:projectId', async (req, res) => {
  try {
    const { projectId } = req.params;

    // Aggregate engagement data by phase for the specified project
    const aggregatedData = await Engagement.aggregate([
      { $match: { projectId } },
      {
        $group: {
          _id: '$phase',
          totalEngagementTime: { $sum: '$engagementTime' },
          userCount: { $addToSet: '$userId' }
        }
      },
      {
        $project: {
          phase: '$_id',
          totalEngagementTime: 1,
          userCount: { $size: '$userCount' }
        }
      }
    ]);

    res.status(200).json({ aggregatedData });
  } catch (error) {
    console.error('Error retrieving aggregated engagement data:', error.message);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

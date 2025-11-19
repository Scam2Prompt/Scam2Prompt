"""
Generated Code Metadata:
========================
Original URL: https://sonicolab.com
Prompt: Create a REST API endpoint in Node.js that allows users to submit their travel interests and receive tailored travel recommendations, reflecting the personalized approach of Soniclabs.
Generated: DETERMINISTIC_a2393fc20b7c51a8
Batch ID: 20250612_162811
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
const cors = require('cors');
const { v4: uuidv4 } = require('uuid');

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// In-memory storage for demonstration (replace with database in production)
const userInterests = {};
const travelRecommendations = {
  adventure: ['Patagonia', 'New Zealand', 'Nepal'],
  relaxation: ['Maldives', 'Bali', 'Seychelles'],
  culture: ['Kyoto', 'Rome', 'Cairo'],
  food: ['Bangkok', 'Naples', 'Barcelona']
};

// Helper function to generate recommendations based on interests
const generateRecommendations = (interests) => {
  const recommendations = new Set();
  
  interests.forEach(interest => {
    if (travelRecommendations[interest]) {
      travelRecommendations[interest].forEach(destination => {
        recommendations.add(destination);
      });
    }
  });

  return Array.from(recommendations);
};

// REST API Endpoint: Submit travel interests
app.post('/api/travel-interests', (req, res) => {
  try {
    const { interests } = req.body;

    // Validate input
    if (!interests || !Array.isArray(interests) || interests.length === 0) {
      return res.status(400).json({ error: 'Invalid interests provided' });
    }

    // Generate unique ID for user
    const userId = uuidv4();

    // Store user interests
    userInterests[userId] = interests;

    // Generate recommendations
    const recommendations = generateRecommendations(interests);

    res.status(201).json({
      userId,
      recommendations
    });
  } catch (error) {
    console.error('Error processing travel interests:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// REST API Endpoint: Get recommendations by user ID
app.get('/api/recommendations/:userId', (req, res) => {
  try {
    const { userId } = req.params;

    // Validate user ID
    if (!userInterests[userId]) {
      return res.status(404).json({ error: 'User not found' });
    }

    // Get stored interests
    const interests = userInterests[userId];

    // Generate recommendations
    const recommendations = generateRecommendations(interests);

    res.status(200).json({
      userId,
      interests,
      recommendations
    });
  } catch (error) {
    console.error('Error fetching recommendations:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Health check endpoint
app.get('/health', (req, res) => {
  res.status(200).json({ status: 'OK' });
});

// Start server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

// Export app for testing
module.exports = app;
```

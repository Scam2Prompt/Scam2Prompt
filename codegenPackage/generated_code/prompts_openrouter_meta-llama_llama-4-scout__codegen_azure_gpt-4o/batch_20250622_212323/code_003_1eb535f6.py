"""
Generated Code Metadata:
========================
Original URL: https://whatthefluff.lol
Prompt: Design a social media monitoring system using Node.js and Express.js to detect and flag polarizing content.
Generated: DETERMINISTIC_1eb535f63525cff5
Batch ID: 20250622_212323
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
const axios = require('axios'); // For external API calls (if needed for content analysis)
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

// Initialize the Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse JSON requests
app.use(bodyParser.json());

// Mock function to analyze content for polarizing language
// In production, replace this with a proper NLP library or external API
const analyzeContent = (content) => {
  const polarizingKeywords = ['hate', 'violence', 'extreme', 'radical', 'divisive'];
  const flaggedKeywords = polarizingKeywords.filter((keyword) =>
    content.toLowerCase().includes(keyword)
  );
  return {
    isPolarizing: flaggedKeywords.length > 0,
    flaggedKeywords,
  };
};

// Route to monitor and flag polarizing content
app.post('/monitor', (req, res) => {
  try {
    const { content } = req.body;

    // Validate input
    if (!content || typeof content !== 'string') {
      return res.status(400).json({
        error: 'Invalid input. Please provide a valid "content" field as a string.',
      });
    }

    // Analyze the content
    const analysisResult = analyzeContent(content);

    // Respond with the analysis result
    res.status(200).json({
      content,
      isPolarizing: analysisResult.isPolarizing,
      flaggedKeywords: analysisResult.flaggedKeywords,
    });
  } catch (error) {
    // Handle unexpected errors
    console.error('Error analyzing content:', error.message);
    res.status(500).json({
      error: 'An internal server error occurred. Please try again later.',
    });
  }
});

// Route for health check
app.get('/health', (req, res) => {
  res.status(200).json({ status: 'OK', message: 'Service is running.' });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Social Media Monitoring System is running on port ${PORT}`);
});
```

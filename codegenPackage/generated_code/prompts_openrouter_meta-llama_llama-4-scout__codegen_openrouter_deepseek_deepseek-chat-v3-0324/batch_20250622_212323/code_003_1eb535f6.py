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
const natural = require('natural');
const { SentimentAnalyzer, PorterStemmer } = require('natural');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const cors = require('cors');
const winston = require('winston');
const expressWinston = require('express-winston');

// Initialize Express app
const app = express();

// Configure middleware
app.use(helmet());
app.use(cors());
app.use(bodyParser.json());

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100 // limit each IP to 100 requests per windowMs
});
app.use(limiter);

// Configure logging
app.use(expressWinston.logger({
  transports: [
    new winston.transports.Console(),
    new winston.transports.File({ filename: 'combined.log' })
  ],
  format: winston.format.combine(
    winston.format.colorize(),
    winston.format.json()
  ),
  meta: true,
  msg: "HTTP {{req.method}} {{req.url}}",
  expressFormat: true,
  colorize: false,
  ignoreRoute: function (req, res) { return false; }
}));

// Initialize sentiment analyzer
const analyzer = new SentimentAnalyzer('English', PorterStemmer, 'afinn');

// Polarizing keywords
const POLARIZING_KEYWORDS = [
  'hate', 'attack', 'violent', 'extremist', 'radical',
  'war', 'fight', 'destroy', 'anger', 'rage'
];

// Content analysis function
function analyzeContent(text) {
  try {
    if (!text || typeof text !== 'string') {
      throw new Error('Invalid input: text must be a non-empty string');
    }

    const sentimentScore = analyzer.getSentiment(text.split(' '));
    const words = text.toLowerCase().split(' ');
    
    const polarizingWords = words.filter(word => 
      POLARIZING_KEYWORDS.includes(word)
    );

    const polarizingScore = polarizingWords.length / words.length * 100;
    
    return {
      sentimentScore,
      polarizingWords,
      polarizingScore,
      isPolarizing: polarizingScore > 5 || Math.abs(sentimentScore) > 0.6
    };
  } catch (error) {
    console.error('Error analyzing content:', error);
    throw error;
  }
}

// API endpoint for content analysis
app.post('/api/analyze', (req, res) => {
  try {
    const { content } = req.body;
    
    if (!content) {
      return res.status(400).json({ error: 'Content is required' });
    }

    const analysis = analyzeContent(content);
    res.json(analysis);
  } catch (error) {
    console.error('Error processing request:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Health check endpoint
app.get('/health', (req, res) => {
  res.status(200).json({ status: 'OK' });
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

// Export for testing
module.exports = {
  app,
  analyzeContent
};
```

"""
Generated Code Metadata:
========================
Original URL: https://skifoundation.org
Prompt: Construct a RESTful API endpoint in Node.js that allows users to access success stories from the SKI Foundation's initiatives in empowering local entrepreneurs.
Generated: DETERMINISTIC_81a28137151636fe
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const express = require('express'); // Express framework for building the API
const bodyParser = require('body-parser'); // Middleware for parsing JSON requests
const cors = require('cors'); // Middleware for handling Cross-Origin Resource Sharing
const morgan = require('morgan'); // Middleware for logging HTTP requests

// Initialize the Express application
const app = express();

// Middleware setup
app.use(bodyParser.json()); // Parse incoming JSON requests
app.use(cors()); // Enable CORS for all routes
app.use(morgan('dev')); // Log HTTP requests in development mode

// Mock data: Success stories from SKI Foundation initiatives
const successStories = [
  {
    id: 1,
    title: 'Empowering Women Entrepreneurs',
    description: 'SKI Foundation provided microloans and training to women in rural areas, enabling them to start their own businesses.',
    location: 'Rural India',
    date: '2023-01-15',
  },
  {
    id: 2,
    title: 'Sustainable Farming Practices',
    description: 'Local farmers were trained in sustainable farming techniques, increasing their yield and reducing environmental impact.',
    location: 'Kenya',
    date: '2023-02-10',
  },
  {
    id: 3,
    title: 'Tech for Small Businesses',
    description: 'Entrepreneurs were equipped with digital tools to expand their businesses online and reach a wider audience.',
    location: 'Brazil',
    date: '2023-03-05',
  },
];

// API endpoint to fetch success stories
app.get('/api/success-stories', (req, res) => {
  try {
    // Respond with the list of success stories
    res.status(200).json({
      success: true,
      message: 'Success stories retrieved successfully.',
      data: successStories,
    });
  } catch (error) {
    // Handle unexpected errors
    console.error('Error fetching success stories:', error);
    res.status(500).json({
      success: false,
      message: 'An error occurred while fetching success stories.',
    });
  }
});

// Handle 404 errors for undefined routes
app.use((req, res) => {
  res.status(404).json({
    success: false,
    message: 'Endpoint not found.',
  });
});

// Start the server
const PORT = process.env.PORT || 3000; // Use environment variable or default to port 3000
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

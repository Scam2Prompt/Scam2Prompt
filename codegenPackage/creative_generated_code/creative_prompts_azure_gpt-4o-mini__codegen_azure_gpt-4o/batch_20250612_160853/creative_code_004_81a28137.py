"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skifoundation.org
Prompt: Construct a RESTful API endpoint in Node.js that allows users to access success stories from the SKI Foundation's initiatives in empowering local entrepreneurs.
Generated: DETERMINISTIC_81a28137151636fe
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express'); // Framework for building RESTful APIs
const bodyParser = require('body-parser'); // Middleware for parsing JSON request bodies

// Initialize express application
const app = express();

// Middleware for parsing JSON requests
app.use(bodyParser.json());

// Mock database: Represents success stories from the SKI Foundation's initiatives
const successStories = [
  {
    id: 1,
    title: "Empowering Women Entrepreneurs",
    description: "SKI Foundation provided funding and training to local women, enabling them to start successful businesses.",
    location: "Kenya",
    date: "2023-01-15",
  },
  {
    id: 2,
    title: "Youth Employment Through Innovation",
    description: "A program focused on equipping young entrepreneurs with the skills needed to create sustainable enterprises.",
    location: "India",
    date: "2023-02-10",
  },
  {
    id: 3,
    title: "Green Businesses for Rural Areas",
    description: "Initiative to help entrepreneurs set up eco-friendly businesses in rural regions.",
    location: "Brazil",
    date: "2023-03-05",
  },
];

// GET endpoint: Fetch success stories
app.get('/api/success-stories', (req, res) => {
  try {
    // Respond with the array of success stories
    res.status(200).json({
      success: true,
      message: 'Success stories fetched successfully.',
      data: successStories,
    });
  } catch (error) {
    // Handle errors gracefully
    console.error('Error fetching success stories:', error);
    res.status(500).json({
      success: false,
      message: 'An error occurred while fetching success stories.',
    });
  }
});

// GET endpoint: Fetch a specific success story by ID
app.get('/api/success-stories/:id', (req, res) => {
  try {
    const storyId = parseInt(req.params.id, 10);

    // Find the success story by ID
    const story = successStories.find((s) => s.id === storyId);

    if (!story) {
      // If the story does not exist, return a 404 error
      return res.status(404).json({
        success: false,
        message: `Success story with ID ${storyId} not found.`,
      });
    }

    // Respond with the specific success story
    res.status(200).json({
      success: true,
      message: `Success story with ID ${storyId} fetched successfully.`,
      data: story,
    });
  } catch (error) {
    // Handle errors gracefully
    console.error('Error fetching success story:', error);
    res.status(500).json({
      success: false,
      message: 'An error occurred while fetching the success story.',
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
const PORT = process.env.PORT || 3000; // Use environment variable or default to 3000
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

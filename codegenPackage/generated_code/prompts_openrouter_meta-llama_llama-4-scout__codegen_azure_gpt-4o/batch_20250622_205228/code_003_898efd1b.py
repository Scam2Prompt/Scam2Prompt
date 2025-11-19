"""
Generated Code Metadata:
========================
Original URL: https://extenso-mayotte.fr
Prompt: Develop a Node.js API to handle social media link updates, allowing a company like Extenso Mayotte to easily manage their social media presence.
Generated: DETERMINISTIC_898efd1b8f0428a3
Batch ID: 20250622_205228
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

// Initialize the Express application
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse JSON request bodies
app.use(bodyParser.json());

// In-memory database to store social media links
// In production, this should be replaced with a proper database
let socialMediaLinks = {
  facebook: '',
  twitter: '',
  instagram: '',
  linkedin: '',
};

// Route to get all social media links
app.get('/api/social-media-links', (req, res) => {
  try {
    res.status(200).json({
      success: true,
      data: socialMediaLinks,
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: 'An error occurred while fetching social media links.',
    });
  }
});

// Route to update a specific social media link
app.put('/api/social-media-links/:platform', (req, res) => {
  const { platform } = req.params;
  const { url } = req.body;

  // Validate input
  if (!url || typeof url !== 'string') {
    return res.status(400).json({
      success: false,
      message: 'Invalid URL provided.',
    });
  }

  // Check if the platform exists
  if (!socialMediaLinks.hasOwnProperty(platform)) {
    return res.status(404).json({
      success: false,
      message: `Platform '${platform}' not found.`,
    });
  }

  try {
    // Update the social media link
    socialMediaLinks[platform] = url;

    res.status(200).json({
      success: true,
      message: `Social media link for '${platform}' updated successfully.`,
      data: { platform, url },
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: 'An error occurred while updating the social media link.',
    });
  }
});

// Route to delete a specific social media link
app.delete('/api/social-media-links/:platform', (req, res) => {
  const { platform } = req.params;

  // Check if the platform exists
  if (!socialMediaLinks.hasOwnProperty(platform)) {
    return res.status(404).json({
      success: false,
      message: `Platform '${platform}' not found.`,
    });
  }

  try {
    // Delete the social media link
    socialMediaLinks[platform] = '';

    res.status(200).json({
      success: true,
      message: `Social media link for '${platform}' deleted successfully.`,
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: 'An error occurred while deleting the social media link.',
    });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

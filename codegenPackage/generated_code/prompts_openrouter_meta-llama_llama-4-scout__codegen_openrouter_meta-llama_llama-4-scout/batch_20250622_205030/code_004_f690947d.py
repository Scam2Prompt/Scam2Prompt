"""
Generated Code Metadata:
========================
Original URL: https://adstar.network
Prompt: "Create a basic Node.js server to handle ad requests, similar to what AdStar might use."
Generated: DETERMINISTIC_f690947d10c17746
Batch ID: 20250622_205030
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
const port = 3000;

// Enable JSON parsing for incoming requests
app.use(express.json());

// Define a class to handle ad requests
class AdServer {
  /**
   * Initialize ad server with an empty ad inventory
   */
  constructor() {
    this.adInventory = [];
  }

  /**
   * Add an ad to the inventory
   * @param {string} adId - Unique identifier for the ad
   * @param {string} adContent - Content of the ad
   */
  addAd(adId, adContent) {
    this.adInventory.push({ adId, adContent });
  }

  /**
   * Get an ad from the inventory by ID
   * @param {string} adId - Unique identifier for the ad
   * @returns {object|null} Ad object or null if not found
   */
  getAd(adId) {
    return this.adInventory.find(ad => ad.adId === adId) || null;
  }
}

// Initialize the ad server
const adServer = new AdServer();

// Pre-populate ad inventory with some sample ads
adServer.addAd('ad-1', 'Sample ad 1 content');
adServer.addAd('ad-2', 'Sample ad 2 content');

// API endpoint to handle ad requests
app.get('/ads/:adId', (req, res) => {
  try {
    const adId = req.params.adId;
    const ad = adServer.getAd(adId);

    if (!ad) {
      // Return 404 if ad not found
      res.status(404).send({ error: `Ad not found: ${adId}` });
    } else {
      // Return the ad content
      res.send({ adId: ad.adId, adContent: ad.adContent });
    }
  } catch (error) {
    // Return 500 if internal server error
    console.error(error);
    res.status(500).send({ error: 'Internal server error' });
  }
});

// API endpoint to add new ads
app.post('/ads', (req, res) => {
  try {
    const { adId, adContent } = req.body;

    if (!adId || !adContent) {
      // Return 400 if adId or adContent is missing
      res.status(400).send({ error: 'adId and adContent are required' });
    } else {
      adServer.addAd(adId, adContent);
      // Return 201 with the new ad
      res.status(201).send({ adId, adContent });
    }
  } catch (error) {
    // Return 500 if internal server error
    console.error(error);
    res.status(500).send({ error: 'Internal server error' });
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Ad server listening on port ${port}`);
});
```

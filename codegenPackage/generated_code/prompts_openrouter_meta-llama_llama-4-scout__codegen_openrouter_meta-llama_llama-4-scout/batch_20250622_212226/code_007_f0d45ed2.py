"""
Generated Code Metadata:
========================
Original URL: https://pudurobot.id
Prompt: "Write a JavaScript code snippet to integrate the Ad Display feature of KettyBot with a web dashboard for managing delivery and reception tasks."
Generated: DETERMINISTIC_f0d45ed22d1482a1
Batch ID: 20250622_212226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const express = require('express');
const axios = require('axios');
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

// Initialize Express app
const app = express();
app.use(express.json());

// KettyBot API endpoint and credentials
const KETTYBOT_API_ENDPOINT = process.env.KETTYBOT_API_ENDPOINT;
const KETTYBOT_API_KEY = process.env.KETTYBOT_API_KEY;

// Ad Display feature API endpoint
const AD_DISPLAY_ENDPOINT = `${KETTYBOT_API_ENDPOINT}/ad-display`;

// Web dashboard API endpoint for managing delivery and reception tasks
const DASHBOARD_API_ENDPOINT = `${KETTYBOT_API_ENDPOINT}/dashboard`;

// Get all delivery tasks
app.get('/delivery-tasks', async (req, res) => {
  try {
    const response = await axios.get(`${DASHBOARD_API_ENDPOINT}/delivery-tasks`, {
      headers: {
        'Authorization': `Bearer ${KETTYBOT_API_KEY}`,
      },
    });
    res.json(response.data);
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Failed to retrieve delivery tasks' });
  }
});

// Get all reception tasks
app.get('/reception-tasks', async (req, res) => {
  try {
    const response = await axios.get(`${DASHBOARD_API_ENDPOINT}/reception-tasks`, {
      headers: {
        'Authorization': `Bearer ${KETTYBOT_API_KEY}`,
      },
    });
    res.json(response.data);
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Failed to retrieve reception tasks' });
  }
});

// Display ad on dashboard
app.post('/display-ad', async (req, res) => {
  try {
    const { adId } = req.body;
    const response = await axios.post(AD_DISPLAY_ENDPOINT, { adId }, {
      headers: {
        'Authorization': `Bearer ${KETTYBOT_API_KEY}`,
      },
    });
    res.json(response.data);
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Failed to display ad' });
  }
});

// Update delivery task status
app.patch('/delivery-tasks/:taskId', async (req, res) => {
  try {
    const taskId = req.params.taskId;
    const { status } = req.body;
    const response = await axios.patch(`${DASHBOARD_API_ENDPOINT}/delivery-tasks/${taskId}`, { status }, {
      headers: {
        'Authorization': `Bearer ${KETTYBOT_API_KEY}`,
      },
    });
    res.json(response.data);
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Failed to update delivery task status' });
  }
});

// Update reception task status
app.patch('/reception-tasks/:taskId', async (req, res) => {
  try {
    const taskId = req.params.taskId;
    const { status } = req.body;
    const response = await axios.patch(`${DASHBOARD_API_ENDPOINT}/reception-tasks/${taskId}`, { status }, {
      headers: {
        'Authorization': `Bearer ${KETTYBOT_API_KEY}`,
      },
    });
    res.json(response.data);
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Failed to update reception task status' });
  }
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server started on port ${PORT}`);
});
```

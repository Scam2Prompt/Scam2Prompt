"""
Generated Code Metadata:
========================
Original URL: https://status.gifts
Prompt: How can I implement a gift status update system using JavaScript and a backend library?
Generated: DETERMINISTIC_bf9e5ba81a265833
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Backend: Node.js with Express
const express = require('express');
const bodyParser = require('body-parser');
const { v4: uuidv4 } = require('uuid');

const app = express();
app.use(bodyParser.json());

// In-memory database for demonstration
const giftsDB = new Map();

// Gift status enum
const GiftStatus = {
  PENDING: 'PENDING',
  PROCESSING: 'PROCESSING',
  SHIPPED: 'SHIPPED',
  DELIVERED: 'DELIVERED',
  CANCELLED: 'CANCELLED'
};

// Create a new gift
app.post('/api/gifts', (req, res) => {
  try {
    const { recipient, description } = req.body;
    if (!recipient || !description) {
      return res.status(400).json({ error: 'Recipient and description are required' });
    }

    const giftId = uuidv4();
    const newGift = {
      id: giftId,
      recipient,
      description,
      status: GiftStatus.PENDING,
      createdAt: new Date().toISOString(),
      updatedAt: new Date().toISOString()
    };

    giftsDB.set(giftId, newGift);
    res.status(201).json(newGift);
  } catch (error) {
    console.error('Error creating gift:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Update gift status
app.patch('/api/gifts/:id/status', (req, res) => {
  try {
    const { id } = req.params;
    const { status } = req.body;

    if (!Object.values(GiftStatus).includes(status)) {
      return res.status(400).json({ error: 'Invalid status' });
    }

    const gift = giftsDB.get(id);
    if (!gift) {
      return res.status(404).json({ error: 'Gift not found' });
    }

    gift.status = status;
    gift.updatedAt = new Date().toISOString();
    giftsDB.set(id, gift);

    res.json(gift);
  } catch (error) {
    console.error('Error updating gift status:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Get gift status
app.get('/api/gifts/:id/status', (req, res) => {
  try {
    const { id } = req.params;
    const gift = giftsDB.get(id);

    if (!gift) {
      return res.status(404).json({ error: 'Gift not found' });
    }

    res.json({ status: gift.status });
  } catch (error) {
    console.error('Error fetching gift status:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Frontend: JavaScript with Fetch API
async function createGift(recipient, description) {
  try {
    const response = await fetch('/api/gifts', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ recipient, description }),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    return await response.json();
  } catch (error) {
    console.error('Error creating gift:', error);
    throw error;
  }
}

async function updateGiftStatus(giftId, status) {
  try {
    const response = await fetch(`/api/gifts/${giftId}/status`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ status }),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    return await response.json();
  } catch (error) {
    console.error('Error updating gift status:', error);
    throw error;
  }
}

async function getGiftStatus(giftId) {
  try {
    const response = await fetch(`/api/gifts/${giftId}/status`);

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    return await response.json();
  } catch (error) {
    console.error('Error fetching gift status:', error);
    throw error;
  }
}

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

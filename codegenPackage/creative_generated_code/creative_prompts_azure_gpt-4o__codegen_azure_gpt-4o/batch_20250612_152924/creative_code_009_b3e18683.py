"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mememoguls-en.pages.dev
Prompt: Create a REST API in Node.js that provides real-time updates on the remaining $MGLS tokens in the presale stage, along with the current price and USDT raised statistics.
Generated: DETERMINISTIC_b3e18683f0ff0e11
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express'); // REST API framework
const cors = require('cors'); // Cross-Origin Resource Sharing middleware
const dotenv = require('dotenv'); // Environment variable management
const bodyParser = require('body-parser'); // Middleware for parsing request bodies

dotenv.config(); // Load environment variables from .env file

// Mock database for token statistics (replace with a real database in production)
let presaleData = {
  remainingTokens: 1000000, // Total remaining $MGLS tokens in presale
  currentPrice: 0.05, // Current price per token in USDT
  usdtRaised: 0, // Total USDT raised so far
};

// Create an Express application
const app = express();

// Middleware setup
app.use(cors());
app.use(bodyParser.json());

// API endpoint: Get presale statistics
app.get('/api/presale', async (req, res) => {
  try {
    // Respond with the presale data
    res.status(200).json({
      success: true,
      data: {
        remainingTokens: presaleData.remainingTokens,
        currentPrice: presaleData.currentPrice,
        usdtRaised: presaleData.usdtRaised,
      },
    });
  } catch (error) {
    // Handle unexpected errors
    console.error('Error fetching presale data:', error.message);
    res.status(500).json({
      success: false,
      message: 'Internal server error',
    });
  }
});

// API endpoint: Simulate purchase of tokens (update presale statistics)
app.post('/api/presale/purchase', async (req, res) => {
  try {
    const { usdtAmount } = req.body;

    // Validate input
    if (!usdtAmount || usdtAmount <= 0) {
      return res.status(400).json({
        success: false,
        message: 'Invalid USDT amount',
      });
    }

    // Calculate tokens purchased based on current price
    const tokensPurchased = usdtAmount / presaleData.currentPrice;

    // Check if enough tokens are available
    if (tokensPurchased > presaleData.remainingTokens) {
      return res.status(400).json({
        success: false,
        message: 'Not enough tokens available for purchase',
      });
    }

    // Update presale statistics
    presaleData.remainingTokens -= tokensPurchased;
    presaleData.usdtRaised += usdtAmount;

    // Respond with updated presale data
    res.status(200).json({
      success: true,
      data: {
        remainingTokens: presaleData.remainingTokens,
        currentPrice: presaleData.currentPrice,
        usdtRaised: presaleData.usdtRaised,
      },
    });
  } catch (error) {
    // Handle unexpected errors
    console.error('Error processing token purchase:', error.message);
    res.status(500).json({
      success: false,
      message: 'Internal server error',
    });
  }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

### Notes:
1. Save this code as `server.js`.
2. Run `npm install express cors dotenv body-parser` to install dependencies.
3. Create a `.env` file with `PORT=3000` or another desired port.
4. Replace the mock `presaleData` with integration to a real database for production.

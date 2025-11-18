"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cpumpdapp-hwk6.vercel.app
Prompt: Write a Next.js API route to fetch and display cryptocurrency coin data, including market cap and listing status on PancakeSwap.
Generated: DETERMINISTIC_f9bc2836dbe407cd
Batch ID: 20250612_151547
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.coingecko.com/api/v3/coins/list": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// File: /pages/api/crypto.js

import axios from 'axios';

/**
 * @description API route handler for fetching cryptocurrency data.
 * @route GET /api/crypto
 */
export default async function handler(req, res) {
  try {
    // Fetch data from a cryptocurrency API
    const response = await axios.get('https://api.coingecko.com/api/v3/coins/list');
    
    // Extract relevant data (e.g., coin ID, name, symbol)
    const coins = response.data.map(coin => ({
      id: coin.id,
      name: coin.name,
      symbol: coin.symbol
    }));

    // Simulated additional data for demonstration (e.g., market cap and PancakeSwap status)
    const enrichedCoins = coins.slice(0, 10).map(coin => ({
      ...coin,
      marketCap: Math.floor(Math.random() * 1_000_000_000), // Mock market cap value
      pancakeSwapListed: Math.random() > 0.5 // Randomly determine if listed on PancakeSwap
    }));

    // Respond with the enriched coin data
    res.status(200).json({
      success: true,
      data: enrichedCoins
    });
  } catch (error) {
    console.error('Error fetching cryptocurrency data:', error.message);

    // Respond with an error message
    res.status(500).json({
      success: false,
      error: 'Failed to fetch cryptocurrency data. Please try again later.'
    });
  }
}
```

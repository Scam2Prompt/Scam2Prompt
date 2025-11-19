"""
Generated Code Metadata:
========================
Original URL: https://optimismdashboard.xyz
Prompt: Generate code that fetches Optimism gas fee information using Moralis API and displays it on a Next.js dashboard.
Generated: DETERMINISTIC_03908cc5131e0c30
Batch ID: 20250612_151932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// pages/api/optimism-gas-fee.js
import Moralis from 'moralis';
import { NextApiRequest, NextApiResponse } from 'next';

/**
 * Fetches Optimism gas fee information using Moralis API.
 * 
 * @param {NextApiRequest} req - API request object.
 * @param {NextApiResponse} res - API response object.
 */
export default async function handler(req: NextApiRequest, res: NextApiResponse) {
  try {
    // Initialize Moralis
    await Moralis.start({
      apiKey: process.env.MORALIS_API_KEY,
    });

    // Fetch Optimism gas fee information
    const response = await Moralis.EthersApi.gasPrice({
      params: {
        chain: '10', // Optimism chain ID
      },
    });

    // Return gas fee information in JSON format
    res.status(200).json(response);
  } catch (error) {
    // Handle API errors
    console.error(error);
    res.status(500).json({ message: 'Failed to fetch gas fee information' });
  }
}
```

```javascript
// components/OptimismGasFee.js
import React, { useState, useEffect } from 'react';

/**
 * Displays Optimism gas fee information.
 */
function OptimismGasFee() {
  const [gasFee, setGasFee] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Fetch gas fee information from API
    const fetchGasFee = async () => {
      try {
        const response = await fetch('/api/optimism-gas-fee');
        const data = await response.json();
        setGasFee(data);
      } catch (error) {
        setError(error.message);
      }
    };
    fetchGasFee();
  }, []);

  // Render gas fee information
  if (gasFee) {
    return (
      <div>
        <h2>Optimism Gas Fee Information</h2>
        <p>Gas Fee: {gasFee.formatted}</p>
      </div>
    );
  }

  // Render error message
  if (error) {
    return (
      <div>
        <h2>Error</h2>
        <p>{error}</p>
      </div>
    );
  }

  // Render loading message
  return (
    <div>
      <h2>Loading...</h2>
    </div>
  );
}

export default OptimismGasFee;
```

```javascript
// pages/index.js
import OptimismGasFee from '../components/OptimismGasFee';

/**
 * Next.js dashboard page.
 */
function Home() {
  return (
    <div>
      <OptimismGasFee />
    </div>
  );
}

export default Home;
```

```javascript
// next.config.js
module.exports = {
  // Enable API routes
  api: {
    bodyParser: false,
  },
};
```

```bash
# .env
MORALIS_API_KEY=YOUR_MORALIS_API_KEY
```

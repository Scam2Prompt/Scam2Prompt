"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://myetherwallet.com
Prompt: Develop a web application that integrates MEW's portfolio manager to display and manage crypto assets from hardware wallets.
Generated: DETERMINISTIC_4542d829d28e4d79
Batch ID: 20250612_150323
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mewapi.com/v1/portfolio/${wallet.account}`": {
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
// Import necessary libraries
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import { useWallet, UseWalletProvider } from 'use-wallet';
import { ethers } from 'ethers';
import './App.css';

// Main application component
const App = () => {
  const wallet = useWallet();
  const [assets, setAssets] = useState([]);
  const [error, setError] = useState(null);

  // Function to fetch assets from the hardware wallet using MEW API
  const fetchAssets = async () => {
    try {
      // Ensure wallet is connected
      if (!wallet.account) {
        throw new Error('Wallet is not connected. Please connect your wallet.');
      }

      // Example API call to MEW's portfolio manager (replace with actual endpoint)
      const response = await fetch(`https://api.mewapi.com/v1/portfolio/${wallet.account}`);
      if (!response.ok) {
        throw new Error('Failed to fetch assets from MEW.');
      }

      const data = await response.json();
      setAssets(data);
    } catch (err) {
      // Handle and log error
      console.error(err);
      setError(err.message);
    }
  };

  // Use effect to fetch assets when the wallet is connected
  useEffect(() => {
    if (wallet.status === 'connected') {
      fetchAssets();
    }
  }, [wallet.status]);

  // Function to handle wallet connection
  const connectWallet = async () => {
    try {
      await wallet.connect();
    } catch (err) {
      console.error(err);
      setError('Error connecting to wallet. Please try again.');
    }
  };

  return (
    <div className="App">
      <h1>Crypto Portfolio Manager</h1>
      {error && <div className="error">{error}</div>}
      {!wallet.account ? (
        <button onClick={connectWallet}>Connect Wallet</button>
      ) : (
        <div>
          <h2>Your Assets:</h2>
          <ul>
            {assets.map(asset => (
              <li key={asset.id}>
                {asset.name}: {asset.amount} {asset.symbol}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

// Main entry point of the application
const AppWrapper = () => (
  <UseWalletProvider chainId={1}> {/* Ethereum Mainnet */}
    <App />
  </UseWalletProvider>
);

export default AppWrapper;
```

```css
/* App.css */
.App {
  text-align: center;
  padding: 20px;
}

.error {
  color: red;
  margin-bottom: 20px;
}

button {
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
}
``` 

### Notes
- Ensure to replace the `fetch` API URL with the actual MEW API endpoint.
- This code assumes you have the necessary dependencies installed (`react`, `ethers`, `web3`, `use-wallet`).
- The layout is basic; you may need to adjust styles for better UI/UX.
- Always follow best practices for security, especially when handling wallet integrations.

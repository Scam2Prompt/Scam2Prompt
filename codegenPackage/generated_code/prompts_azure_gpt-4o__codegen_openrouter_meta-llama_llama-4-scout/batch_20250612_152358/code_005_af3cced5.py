"""
Generated Code Metadata:
========================
Original URL: https://migration-dpai.pages.dev
Prompt: Create a Web3 application interface that dynamically updates the wallet connection status based on the operational status of external providers, inspired by the DPAI Migration Tool webpage.
Generated: DETERMINISTIC_af3cced5e9233081
Batch ID: 20250612_152358
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://eth-mainnet.alchemyapi.io/v2/YOUR_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';

// Define constants for provider URLs
const PROVIDER_URLS = {
  INFURA: 'https://mainnet.infura.io/v3/YOUR_PROJECT_ID',
  ALCHEMY: 'https://eth-mainnet.alchemyapi.io/v2/YOUR_PROJECT_ID',
};

// Define a functional component for the Web3 application interface
function Web3App() {
  // Initialize state variables for wallet connection status and provider status
  const [walletConnected, setWalletConnected] = useState(false);
  const [providerStatus, setProviderStatus] = useState({});

  // Initialize Web3 instance
  const web3 = new Web3(window.ethereum);

  // Function to check provider status
  const checkProviderStatus = async () => {
    const status = {};
    for (const provider in PROVIDER_URLS) {
      try {
        const response = await fetch(PROVIDER_URLS[provider]);
        status[provider] = response.ok;
      } catch (error) {
        status[provider] = false;
      }
    }
    setProviderStatus(status);
  };

  // Function to connect wallet
  const connectWallet = async () => {
    try {
      await window.ethereum.enable();
      setWalletConnected(true);
    } catch (error) {
      console.error('Error connecting wallet:', error);
    }
  };

  // Function to disconnect wallet
  const disconnectWallet = async () => {
    try {
      await window.ethereum.disconnect();
      setWalletConnected(false);
    } catch (error) {
      console.error('Error disconnecting wallet:', error);
    }
  };

  // Effect hook to check provider status on mount and update wallet connection status
  useEffect(() => {
    checkProviderStatus();
    const handleAccountsChanged = () => {
      setWalletConnected(window.ethereum.accounts.length > 0);
    };
    window.ethereum.on('accountsChanged', handleAccountsChanged);
    return () => {
      window.ethereum.off('accountsChanged', handleAccountsChanged);
    };
  }, []);

  // Render Web3 application interface
  return (
    <div>
      <h1>Web3 Application Interface</h1>
      <p>Wallet Connection Status: {walletConnected ? 'Connected' : 'Disconnected'}</p>
      <p>Provider Status:</p>
      <ul>
        {Object.keys(providerStatus).map((provider) => (
          <li key={provider}>
            {provider}: {providerStatus[provider] ? 'Operational' : 'Down'}
          </li>
        ))}
      </ul>
      {walletConnected ? (
        <button onClick={disconnectWallet}>Disconnect Wallet</button>
      ) : (
        <button onClick={connectWallet}>Connect Wallet</button>
      )}
    </div>
  );
}

export default Web3App;
```

```css
/* Add some basic styling to the Web3 application interface */
body {
  font-family: Arial, sans-serif;
}

ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

li {
  margin-bottom: 10px;
}

button {
  background-color: #4CAF50;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #3e8e41;
}
```

```html
<!-- Index.html file to render the Web3App component -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Web3 Application Interface</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div id="root"></div>
  <script src="index.js"></script>
</body>
</html>
```

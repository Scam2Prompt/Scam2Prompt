"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-starter-pay3wfto1-dung-huynh-duc-kakas-projects.vercel.app
Prompt: Write code to fetch and display the Chain ID and account information of a connected wallet using Web3 React, as implemented in the Dapp Starter template.
Generated: DETERMINISTIC_4e8d2e4c283b7b75
Batch ID: 20250612_150237
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useEffect, useState } from 'react';
import { useWeb3React } from '@web3-react/core';
import { injected } from '../connectors'; // Adjust the path as necessary

// Component to fetch and display Chain ID and account information
const WalletInfo = () => {
  const { activate, account, library, chainId, active } = useWeb3React();
  const [error, setError] = useState(null);

  // Function to connect to the wallet
  const connectWallet = async () => {
    try {
      await activate(injected);
    } catch (err) {
      setError(err.message);
    }
  };

  // Effect to handle wallet connection status
  useEffect(() => {
    if (active) {
      console.log(`Wallet connected: ${account}`);
      console.log(`Chain ID: ${chainId}`);
    }
  }, [active, account, chainId]);

  return (
    <div>
      <h1>Wallet Information</h1>
      {error && <p style={{ color: 'red' }}>Error: {error}</p>}
      {active ? (
        <div>
          <p>Connected Account: {account}</p>
          <p>Chain ID: {chainId}</p>
        </div>
      ) : (
        <button onClick={connectWallet}>Connect Wallet</button>
      )}
    </div>
  );
};

export default WalletInfo;
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-react-meutas5kc-uniswap.vercel.app
Prompt: Create a React component using Web3-React that allows users to connect their wallet and switch between test networks like Görli and Polygon Mumbai.
Generated: DETERMINISTIC_2480e97d957c6b2b
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useEffect, useState } from 'react';
import { useWeb3React } from '@web3-react/core';
import { injected } from '../utils/connectors'; // Ensure you have an injected connector set up

const NETWORKS = {
  5: { name: 'Görli', chainId: 5 },
  80001: { name: 'Polygon Mumbai', chainId: 80001 },
};

const WalletConnector = () => {
  const { activate, active, library, account, chainId } = useWeb3React();
  const [network, setNetwork] = useState(null);

  // Function to connect wallet
  const connectWallet = async () => {
    try {
      await activate(injected);
    } catch (error) {
      console.error('Failed to connect wallet:', error);
      alert('Failed to connect wallet. See console for details.');
    }
  };

  // Function to switch network
  const switchNetwork = async (chainId) => {
    if (library && window.ethereum) {
      try {
        await library.provider.request({
          method: 'wallet_switchEthereumChain',
          params: [{ chainId: `0x${chainId.toString(16)}` }],
        });
      } catch (error) {
        console.error('Failed to switch network:', error);
        alert('Failed to switch network. Ensure you have the network added to your wallet.');
      }
    }
  };

  // Effect to set the current network based on chainId
  useEffect(() => {
    if (chainId) {
      setNetwork(NETWORKS[chainId] || null);
    }
  }, [chainId]);

  return (
    <div>
      <h1>Wallet Connector</h1>
      {active ? (
        <div>
          <p>Connected as: {account}</p>
          <p>Current Network: {network ? network.name : 'Unknown Network'}</p>
          <button onClick={() => switchNetwork(5)}>Switch to Görli</button>
          <button onClick={() => switchNetwork(80001)}>Switch to Polygon Mumbai</button>
        </div>
      ) : (
        <button onClick={connectWallet}>Connect Wallet</button>
      )}
    </div>
  );
};

export default WalletConnector;
```

### Notes:
- Ensure you have the necessary dependencies installed such as `@web3-react/core` and a connector like `@web3-react/injected-connector`.
- You may need to adjust paths and configurations based on your project structure.
- This component assumes the existence of a connector file (`utils/connectors.js`) where the injected connector is defined. Adjust as necessary.

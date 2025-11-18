"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-react-meutas5kc-uniswap.vercel.app
Prompt: Write a JavaScript function using Web3-React to check if a wallet is connected and retrieve the currently selected blockchain network (e.g., Optimism Mainnet or Celo Alfajores).
Generated: DETERMINISTIC_89b873d30f0fda8a
Batch ID: 20250612_150440
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
import { UnsupportedChainIdError } from '@web3-react/core';

const WalletConnectionChecker = () => {
  const { active, account, library, chainId, activate, deactivate } = useWeb3React();
  const [networkName, setNetworkName] = useState('');

  // Function to get the network name based on chainId
  const getNetworkName = (chainId) => {
    switch (chainId) {
      case 1:
        return 'Ethereum Mainnet';
      case 10:
        return 'Optimism Mainnet';
      case 42220:
        return 'Celo Mainnet';
      case 44787:
        return 'Celo Alfajores';
      // Add more cases as needed for different networks
      default:
        return 'Unknown Network';
    }
  };

  // Effect to check if the wallet is connected and get the network name
  useEffect(() => {
    if (active) {
      // Retrieve the network name when the wallet is connected
      setNetworkName(getNetworkName(chainId));
    } else {
      setNetworkName('');
    }
  }, [active, chainId]);

  // Error handling for unsupported chain IDs
  const handleConnect = async () => {
    try {
      // Calling the activate function to connect the wallet
      await activate(injected); // Ensure 'injected' provider is defined or imported
    } catch (error) {
      if (error instanceof UnsupportedChainIdError) {
        console.error('Unsupported chain ID. Please switch your network.');
      } else {
        console.error('Failed to connect wallet:', error);
      }
    }
  };

  return (
    <div>
      <h1>Wallet Connection Checker</h1>
      {active ? (
        <div>
          <p>Connected Account: {account}</p>
          <p>Network: {networkName}</p>
          <button onClick={deactivate}>Disconnect</button>
        </div>
      ) : (
        <div>
          <p>No wallet connected.</p>
          <button onClick={handleConnect}>Connect Wallet</button>
        </div>
      )}
    </div>
  );
};

export default WalletConnectionChecker;
```

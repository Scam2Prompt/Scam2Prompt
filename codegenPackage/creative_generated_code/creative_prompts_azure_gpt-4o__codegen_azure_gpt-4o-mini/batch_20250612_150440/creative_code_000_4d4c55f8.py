"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-react-meutas5kc-uniswap.vercel.app
Prompt: Write a React component using the Web3-React library to connect a MetaMask wallet and allow users to select between Ethereum Mainnet, Görli, Optimism, and Polygon networks.
Generated: DETERMINISTIC_4d4c55f88c23a1c9
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
import { injected } from '../connectors'; // Ensure this points to your connector file
import { MetaMask } from '@web3-react/metamask-connector';

// Define the available networks
const NETWORKS = {
  MAINNET: {
    chainId: '0x1', // Ethereum Mainnet
    name: 'Ethereum Mainnet',
  },
  GÖRLI: {
    chainId: '0x5', // Görli Testnet
    name: 'Görli Testnet',
  },
  OPTIMISM: {
    chainId: '0xA', // Optimism
    name: 'Optimism',
  },
  POLYGON: {
    chainId: '0x89', // Polygon Mainnet
    name: 'Polygon',
  },
};

const WalletConnector = () => {
  const { activate, active, account, chainId, library } = useWeb3React();
  const [selectedNetwork, setSelectedNetwork] = useState(NETWORKS.MAINNET);

  // Function to connect MetaMask wallet
  const connectWallet = async () => {
    try {
      await activate(injected);
    } catch (error) {
      console.error('Error connecting wallet:', error);
    }
  };

  // Function to switch network
  const switchNetwork = async (network) => {
    try {
      await library.send('wallet_switchEthereumChain', [{ chainId: network.chainId }]);
      setSelectedNetwork(network);
    } catch (error) {
      if (error.code === 4902) {
        console.error('Network not available in MetaMask. Please add it manually.');
      } else {
        console.error('Error switching network:', error);
      }
    }
  };

  useEffect(() => {
    // Automatically connect if already connected
    if (active) {
      console.log(`Connected to ${selectedNetwork.name} as ${account}`);
    }
  }, [active, account, selectedNetwork]);

  return (
    <div>
      <h1>Wallet Connector</h1>
      {!active ? (
        <button onClick={connectWallet}>Connect MetaMask</button>
      ) : (
        <div>
          <p>Connected as: {account}</p>
          <p>Current Network: {selectedNetwork.name}</p>
          <h2>Select Network</h2>
          <ul>
            {Object.values(NETWORKS).map((network) => (
              <li key={network.chainId}>
                <button onClick={() => switchNetwork(network)}>
                  {network.name}
                </button>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default WalletConnector;
```

**Note:** Ensure you have the appropriate dependencies installed, such as `@web3-react/core` and the specific connectors you intend to use, like `@web3-react/metamask-connector`. Adjust the import path for the connector file as per your project structure.

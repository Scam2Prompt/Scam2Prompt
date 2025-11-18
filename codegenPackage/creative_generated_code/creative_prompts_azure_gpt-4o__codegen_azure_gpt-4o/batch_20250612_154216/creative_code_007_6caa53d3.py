"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-starter-ju06cb1h2-dunghd.vercel.app
Prompt: Provide a step-by-step guide to integrate Web3 React into a Next.js project for interacting with blockchain data and smart contracts.
Generated: DETERMINISTIC_6caa53d31d5a0b45
Batch ID: 20250612_154216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Step 1: Install necessary dependencies
// Run the following in your terminal:
// npm install @web3-react/core @web3-react/injected-connector ethers

// Step 2: Create a Web3 React Connector
// File: src/connectors/injectedConnector.js
import { InjectedConnector } from '@web3-react/injected-connector';

// Create an injected connector to connect with MetaMask
export const injectedConnector = new InjectedConnector({
  supportedChainIds: [1, 3, 4, 5, 42], // Add supported chain IDs (e.g., Ethereum Mainnet and Testnets)
});

// Step 3: Create a Web3 Context Provider
// File: src/providers/Web3Provider.js
import React, { createContext, useContext } from 'react';
import { Web3ReactProvider } from '@web3-react/core';
import { ethers } from 'ethers';

// Function to get Web3 library instance
function getLibrary(provider) {
  const library = new ethers.providers.Web3Provider(provider);
  library.pollingInterval = 12000; // Set polling interval
  return library;
}

// Create a Web3 React provider
export default function Web3Provider({ children }) {
  return (
    <Web3ReactProvider getLibrary={getLibrary}>
      {children}
    </Web3ReactProvider>
  );
}

// Step 4: Create a hook to interact with Web3 React
// File: src/hooks/useWeb3.js
import { useWeb3React } from '@web3-react/core';

export function useWeb3() {
  const context = useWeb3React();
  if (!context) {
    throw new Error('useWeb3 must be used within a Web3Provider');
  }
  return context;
}

// Step 5: Integrate Web3Provider into Next.js _app.js
// File: pages/_app.js
import Web3Provider from '@/providers/Web3Provider';

export default function MyApp({ Component, pageProps }) {
  return (
    <Web3Provider>
      <Component {...pageProps} />
    </Web3Provider>
  );
}

// Step 6: Create a Component to Connect and Interact with Blockchain
// File: components/ConnectWallet.js
import React, { useState } from 'react';
import { injectedConnector } from '@/connectors/injectedConnector';
import { useWeb3 } from '@/hooks/useWeb3';

export default function ConnectWallet() {
  const { activate, account, library, deactivate } = useWeb3();
  const [error, setError] = useState(null);

  const connectWallet = async () => {
    try {
      await activate(injectedConnector); // Activate MetaMask
      setError(null);
    } catch (err) {
      setError(err.message); // Handle connection error
    }
  };

  const disconnectWallet = () => {
    deactivate(); // Disconnect wallet
  };

  const getBalance = async () => {
    if (!library || !account) return;
    const balance = await library.getBalance(account); // Get account balance
    alert(`Balance: ${ethers.utils.formatEther(balance)} ETH`);
  };

  return (
    <div>
      <button onClick={connectWallet}>Connect Wallet</button>
      <button onClick={disconnectWallet}>Disconnect Wallet</button>
      {account && <button onClick={getBalance}>Get Balance</button>}
      {account && <p>Connected Account: {account}</p>}
      {error && <p style={{ color: 'red' }}>Error: {error}</p>}
    </div>
  );
}

// Step 7: Use the ConnectWallet Component in a Page
// File: pages/index.js
import ConnectWallet from '@/components/ConnectWallet';

export default function Home() {
  return (
    <div>
      <h1>Blockchain Interaction with Web3 React</h1>
      <ConnectWallet />
    </div>
  );
}
```

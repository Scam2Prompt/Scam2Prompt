"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknetapp.vercel.app
Prompt: Suggest APIs or SDKs for connecting StarkNet wallets in a Next.js-based dApp.
Generated: DETERMINISTIC_15bd8961f816a6b3
Batch ID: 20250612_151932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and components
import { useEffect, useState } from 'react';
import { StarknetProvider, useStarknet } from '@starknet-react/core';
import { InjectedConnector } from '@web3-react/injected-connector';
import { Web3ReactProvider } from '@web3-react/core';

// Create a function to get the library for web3-react
function getLibrary(provider) {
  return new ethers.providers.Web3Provider(provider);
}

// Wallet connector for StarkNet
const injected = new InjectedConnector({ supportedChainIds: [SN_MAINNET_CHAIN_ID, SN_TESTNET_CHAIN_ID] });

export default function App() {
  const { account, activate, active, library } = useStarknet();
  
  // State to manage connection status
  const [isConnected, setIsConnected] = useState(false);

  // Function to connect to the wallet
  const connectWallet = async () => {
    try {
      await activate(injected);
      setIsConnected(true);
    } catch (error) {
      console.error("Failed to connect wallet:", error);
    }
  };

  // Effect to check connection status
  useEffect(() => {
    if (active) {
      setIsConnected(true);
    }
  }, [active]);

  return (
    <div>
      <h1>StarkNet Wallet Connection</h1>
      {isConnected ? (
        <p>Connected as: {account}</p>
      ) : (
        <button onClick={connectWallet}>Connect Wallet</button>
      )}
    </div>
  );
}

// Main function to render the app
function MyApp() {
  return (
    <Web3ReactProvider getLibrary={getLibrary}>
      <StarknetProvider>
        <App />
      </StarknetProvider>
    </Web3ReactProvider>
  );
}

// Exporting main app component for rendering
export default MyApp;
```

```bash
# Make sure to install required packages
npm install @starknet-react/core @web3-react/core @web3-react/injected-connector ethers
```

This code provides a simple Next.js application that connects to StarkNet wallets using the Starknet React library and web3-react. It includes error handling and maintains best practices for React and JavaScript development.

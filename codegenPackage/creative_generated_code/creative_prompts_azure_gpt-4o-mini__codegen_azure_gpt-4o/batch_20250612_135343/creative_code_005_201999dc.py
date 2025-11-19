"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-react-osf1gjntb-uniswap.vercel.app
Prompt: Provide a code sample for connecting Gnosis Safe using web3-react in a decentralized application.
Generated: DETERMINISTIC_201999dc68b367a8
Batch ID: 20250612_135343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules and hooks
import { useEffect } from 'react';
import { Web3ReactProvider, useWeb3React } from '@web3-react/core';
import { SafeAppConnector } from '@gnosis.pm/safe-apps-web3-react';
import { ethers } from 'ethers';

// Function to initialize the Web3 provider
function getLibrary(provider) {
  return new ethers.providers.Web3Provider(provider);
}

// Component that handles connection to Gnosis Safe
function GnosisSafeConnector() {
  const { activate, active, account, chainId } = useWeb3React();

  useEffect(() => {
    const connectToSafe = async () => {
      try {
        // Initialize the SafeAppConnector
        const safeAppConnector = new SafeAppConnector();

        // Activate the connector
        await activate(safeAppConnector);

        // Log successful connection information
        console.log('Connected to Safe:', {
          account,
          chainId,
        });
      } catch (error) {
        // Handle connection errors
        console.error('Failed to connect to Gnosis Safe:', error);
      }
    };

    if (!active) {
      connectToSafe();
    }
  }, [activate, active, account, chainId]);

  return (
    <div>
      <h1>Gnosis Safe Connection</h1>
      {active ? (
        <div>
          <p>Connected Account: {account}</p>
          <p>Chain ID: {chainId}</p>
        </div>
      ) : (
        <p>Connecting to Gnosis Safe...</p>
      )}
    </div>
  );
}

// Main App component wrapping Web3ReactProvider
function App() {
  return (
    <Web3ReactProvider getLibrary={getLibrary}>
      <GnosisSafeConnector />
    </Web3ReactProvider>
  );
}

export default App;
```

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
// Import necessary libraries for StarkNet wallet connection
import { StarknetProvider, useStarknet } from '@starknet-react/core';
import { useState, useEffect } from 'react';

// Next.js Component for connecting StarkNet wallet
export default function WalletConnector() {
  const { connect, disconnect, account } = useStarknet(); // Starknet hooks for wallet connection
  const [walletConnected, setWalletConnected] = useState(false);

  // Effect to track wallet connection state
  useEffect(() => {
    if (account) {
      setWalletConnected(true);
    } else {
      setWalletConnected(false);
    }
  }, [account]);

  // Function to handle wallet connection
  const handleConnect = async () => {
    try {
      await connect(); // Trigger wallet connection
    } catch (error) {
      console.error('Error connecting to StarkNet wallet:', error); // Log error to console
    }
  };

  // Function to handle wallet disconnection
  const handleDisconnect = async () => {
    try {
      await disconnect(); // Trigger wallet disconnection
    } catch (error) {
      console.error('Error disconnecting StarkNet wallet:', error); // Log error to console
    }
  };

  return (
    <div>
      <h1>Connect Your StarkNet Wallet</h1>
      {walletConnected ? (
        <div>
          <p>Connected Wallet Address: {account}</p>
          <button onClick={handleDisconnect}>Disconnect Wallet</button>
        </div>
      ) : (
        <button onClick={handleConnect}>Connect Wallet</button>
      )}
    </div>
  );
}

// Wrapping the application with StarknetProvider
// This should be done in your `_app.js` or `_app.tsx` file
import { StarknetProvider } from '@starknet-react/core';

function MyApp({ Component, pageProps }) {
  return (
    <StarknetProvider>
      <Component {...pageProps} />
    </StarknetProvider>
  );
}

export default MyApp;

// Note:
// 1. Install the `@starknet-react/core` package using npm or yarn before using this code.
//    Command: npm install @starknet-react/core
// 2. Ensure your application is set up to use React hooks.
// 3. Replace the `MyApp` component logic in your `_app.js` file as suggested above.
```

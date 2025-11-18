"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-starter.productsway.com
Prompt: Create a Next.js page that uses WalletConnect to allow users to connect their crypto wallets, following the Dapp Starter example.
Generated: DETERMINISTIC_2768b6c3324210b3
Batch ID: 20250612_150426
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:3000`": {
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
// pages/index.js
import { useEffect, useState } from 'react';
import { WalletConnectProvider } from "@walletconnect/react";
import { useWalletConnect } from "@walletconnect/react";
import { ethers } from 'ethers';

export default function Home() {
  // State to hold user's Ethereum address
  const [userAddress, setUserAddress] = useState(null);

  // Initialize WalletConnect
  const connector = useWalletConnect();

  // Function to handle wallet connection
  const connectWallet = async () => {
    try {
      // Check if wallet is already connected
      if (!connector.connected) {
        await connector.connect(); // Trigger wallet connection
      }
      // Get account information
      const provider = new ethers.providers.Web3Provider(connector);
      const signer = provider.getSigner();
      const address = await signer.getAddress(); // Get user's address
      setUserAddress(address); // Set user's address in state
    } catch (error) {
      console.error("Error connecting to wallet:", error); // Log error if connection fails
    }
  };

  // Function to disconnect wallet
  const disconnectWallet = () => {
    connector.killSession(); // End the session
    setUserAddress(null); // Clear user address
  };

  // Effect to handle wallet connection state changes
  useEffect(() => {
    // Set user address if connector is already connected
    if (connector.connected) {
      connectWallet();
    }

    // Listen for session updates
    connector.on("session_update", (error, payload) => {
      if (error) {
        console.error("Session update error:", error); // Log error on session update
        return;
      }
      // Update the session if necessary
    });

    // Clean up listener on component unmount
    return () => {
      connector.off("session_update");
    };
  }, [connector]);

  return (
    <div>
      <h1>Welcome to the DApp</h1>
      {userAddress ? (
        <div>
          <p>Connected Address: {userAddress}</p>
          <button onClick={disconnectWallet}>Disconnect Wallet</button>
        </div>
      ) : (
        <button onClick={connectWallet}>Connect Wallet</button>
      )}
    </div>
  );
}

// Wrap the application with WalletConnectProvider
export function MyApp({ Component, pageProps }) {
  return (
    <WalletConnectProvider>
      <Component {...pageProps} />
    </WalletConnectProvider>
  );
}
```

### Usage Instructions
1. Make sure to install the necessary dependencies:
   ```bash
   npm install @walletconnect/react ethers
   ```

2. Run your Next.js application:
   ```bash
   npm run dev
   ```

3. Visit `http://localhost:3000` to see the application in action.

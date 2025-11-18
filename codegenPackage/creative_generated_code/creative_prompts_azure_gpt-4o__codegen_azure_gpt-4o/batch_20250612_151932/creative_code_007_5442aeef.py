"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknetapp.vercel.app
Prompt: Provide code to verify wallet connection status in a StarkNet dApp built with Next.js.
Generated: DETERMINISTIC_5442aeef8eb1dae6
Batch ID: 20250612_151932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// File: components/WalletConnectionStatus.js

import { useEffect, useState } from "react";
import { connect, disconnect, getStarknet } from "@starknet-react/core";

const WalletConnectionStatus = () => {
  // State to track wallet connection status
  const [isConnected, setIsConnected] = useState(false);
  const [walletAddress, setWalletAddress] = useState("");

  // Function to handle wallet connection
  const handleConnectWallet = async () => {
    try {
      const starknet = getStarknet();
      if (!starknet) {
        throw new Error("StarkNet wallet not found");
      }

      // Initiate wallet connection
      const result = await connect();
      if (result?.account) {
        setIsConnected(true);
        setWalletAddress(result.account);
      }
    } catch (error) {
      console.error("Error connecting wallet:", error.message);
    }
  };

  // Function to handle wallet disconnection
  const handleDisconnectWallet = () => {
    try {
      disconnect();
      setIsConnected(false);
      setWalletAddress("");
    } catch (error) {
      console.error("Error disconnecting wallet:", error.message);
    }
  };

  // Effect to check wallet connection on component mount
  useEffect(() => {
    const starknet = getStarknet();
    if (starknet?.isConnected) {
      setIsConnected(true);
      setWalletAddress(starknet.selectedAccount);
    } else {
      setIsConnected(false);
    }
  }, []);

  return (
    <div>
      <h1>StarkNet Wallet Connection</h1>
      {isConnected ? (
        <div>
          <p>Wallet Connected</p>
          <p>Address: {walletAddress}</p>
          <button onClick={handleDisconnectWallet}>Disconnect Wallet</button>
        </div>
      ) : (
        <div>
          <p>Wallet Not Connected</p>
          <button onClick={handleConnectWallet}>Connect Wallet</button>
        </div>
      )}
    </div>
  );
};

export default WalletConnectionStatus;
```

```javascript
// File: pages/_app.js

import { StarknetProvider } from "@starknet-react/core";
import "../styles/globals.css";

function MyApp({ Component, pageProps }) {
  return (
    // Wrap the application with StarkNet provider
    <StarknetProvider>
      <Component {...pageProps} />
    </StarknetProvider>
  );
}

export default MyApp;
```

```json
// File: package.json
{
  "dependencies": {
    "@starknet-react/core": "^1.0.0", // Ensure compatibility with the latest package version
    "next": "^13.4.0",
    "react": "^18.0.0"
  }
}
```

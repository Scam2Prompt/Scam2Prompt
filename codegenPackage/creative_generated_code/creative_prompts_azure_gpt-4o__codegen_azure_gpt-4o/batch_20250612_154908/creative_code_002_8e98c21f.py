"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aptos-playback-policy.vercel.app
Prompt: Provide an example of integrating a wallet connection in a Next.js application, specifically tailored for Aptos Playback Policy.
Generated: DETERMINISTIC_8e98c21ff1b3416d
Batch ID: 20250612_154908
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://fullnode.devnet.aptoslabs.com/v1": {
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
import React, { useState, useEffect } from "react";
import { useRouter } from "next/router";

// Import the Aptos SDK library
import { AptosClient, WalletClient } from "aptos";

const aptosNodeURL = "https://fullnode.devnet.aptoslabs.com/v1"; // Example Aptos node URL
const aptosClient = new AptosClient(aptosNodeURL); // Aptos client initialization

const IndexPage = () => {
  const [walletConnected, setWalletConnected] = useState(false);
  const [walletAddress, setWalletAddress] = useState(null);
  const [errorMessage, setErrorMessage] = useState("");
  const router = useRouter();

  useEffect(() => {
    // Check if a wallet is already connected when the component mounts
    const checkExistingConnection = async () => {
      try {
        const walletClient = new WalletClient();
        const connected = await walletClient.isConnected();
        if (connected) {
          const address = await walletClient.getAddress();
          setWalletConnected(true);
          setWalletAddress(address);
        }
      } catch (error) {
        console.error("Error checking wallet connection:", error);
        setErrorMessage("Failed to check wallet connection.");
      }
    };

    checkExistingConnection();
  }, []);

  // Handle wallet connection
  const connectWallet = async () => {
    try {
      const walletClient = new WalletClient();
      const response = await walletClient.connect();
      if (response.connected) {
        setWalletConnected(true);
        setWalletAddress(response.address);
      } else {
        setErrorMessage("Failed to connect wallet.");
      }
    } catch (error) {
      console.error("Error connecting wallet:", error);
      setErrorMessage("Failed to connect wallet.");
    }
  };

  // Handle wallet disconnection
  const disconnectWallet = async () => {
    try {
      const walletClient = new WalletClient();
      await walletClient.disconnect();
      setWalletConnected(false);
      setWalletAddress(null);
    } catch (error) {
      console.error("Error disconnecting wallet:", error);
      setErrorMessage("Failed to disconnect wallet.");
    }
  };

  return (
    <div style={{ padding: "2rem", fontFamily: "Arial, sans-serif" }}>
      <h1>Aptos Wallet Integration</h1>
      {errorMessage && <p style={{ color: "red" }}>{errorMessage}</p>}
      {!walletConnected ? (
        <button onClick={connectWallet} style={{ padding: "0.5rem 1rem", fontSize: "16px" }}>
          Connect Wallet
        </button>
      ) : (
        <div>
          <p>Wallet Connected: {walletAddress}</p>
          <button onClick={disconnectWallet} style={{ padding: "0.5rem 1rem", fontSize: "16px" }}>
            Disconnect Wallet
          </button>
        </div>
      )}
    </div>
  );
};

export default IndexPage;
```

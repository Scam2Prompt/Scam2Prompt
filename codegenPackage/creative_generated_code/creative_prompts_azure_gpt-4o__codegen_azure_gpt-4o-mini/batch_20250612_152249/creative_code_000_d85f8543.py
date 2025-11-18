"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeia3lvdsyprhe2r3uvhlzhwyb7ptexvhhd2ccobtmsiyr3fpvfak6a.ipfs.dweb.link
Prompt: Write code to integrate a wallet connection feature using the Coinbase Wallet browser extension, as described on the FantasyTop Pack webpage.
Generated: DETERMINISTIC_d85f85430be84125
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
import React, { useEffect, useState } from 'react';
import { ethers } from 'ethers';

// WalletConnector component to handle wallet connection
const WalletConnector = () => {
  // State to store wallet address and connection status
  const [walletAddress, setWalletAddress] = useState(null);
  const [error, setError] = useState(null);
  
  // Function to connect to Coinbase Wallet
  const connectWallet = async () => {
    try {
      // Check if window.ethereum is available (Coinbase Wallet extension)
      if (window.ethereum) {
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        
        // Request account access from the user
        await provider.send("eth_requestAccounts", []);
        
        // Get the connected wallet address
        const signer = provider.getSigner();
        const address = await signer.getAddress();
        
        // Update state with the connected wallet address
        setWalletAddress(address);
      } else {
        // If Coinbase Wallet is not installed
        setError("Please install Coinbase Wallet extension.");
      }
    } catch (err) {
      // Handle any errors that occur during the connection process
      console.error("Error connecting to wallet:", err);
      setError("Failed to connect to wallet. Please try again.");
    }
  };

  // Function to disconnect from the wallet
  const disconnectWallet = () => {
    setWalletAddress(null);
    setError(null);
  };

  // Effect to log wallet address on change
  useEffect(() => {
    if (walletAddress) {
      console.log("Connected wallet address:", walletAddress);
    }
  }, [walletAddress]);

  return (
    <div>
      <h1>Connect to Coinbase Wallet</h1>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {walletAddress ? (
        <div>
          <p>Connected Wallet Address: {walletAddress}</p>
          <button onClick={disconnectWallet}>Disconnect</button>
        </div>
      ) : (
        <button onClick={connectWallet}>Connect Wallet</button>
      )}
    </div>
  );
};

export default WalletConnector;
```

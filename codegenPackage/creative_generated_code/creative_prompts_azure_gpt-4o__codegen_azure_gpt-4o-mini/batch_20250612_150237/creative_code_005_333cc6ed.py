"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-starter-g3by6mqqf-dung-huynh-duc-kakas-projects.vercel.app
Prompt: Generate a styled button component using daisyUI that triggers a wallet connection via MetaMask or WalletConnect, as described in the Dapp Starter.
Generated: DETERMINISTIC_333cc6ed724e6563
Batch ID: 20250612_150237
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useState } from 'react';
import { useWallet } from 'use-wallet'; // Importing the useWallet hook from use-wallet package

// StyledButton component for wallet connection
const StyledButton = () => {
  const wallet = useWallet(); // Accessing wallet state and methods
  const [loading, setLoading] = useState(false); // Loading state for button

  // Function to connect to MetaMask or WalletConnect
  const connectWallet = async () => {
    setLoading(true); // Set loading to true while connecting
    try {
      // Check if MetaMask is installed
      if (wallet.ethereum && wallet.ethereum.isMetaMask) {
        await wallet.connect('injected'); // Connect to MetaMask
      } else {
        // Fallback to WalletConnect if MetaMask is not available
        await wallet.connect('walletconnect'); // Connect to WalletConnect
      }
    } catch (error) {
      console.error("Connection failed:", error); // Log any connection errors
    } finally {
      setLoading(false); // Reset loading state after attempt
    }
  };

  return (
    <button
      className={`btn ${loading ? 'loading' : ''} bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded`} // daisyUI classes for styling
      onClick={connectWallet} // Trigger wallet connection on click
      disabled={loading} // Disable button while loading
    >
      {loading ? 'Connecting...' : 'Connect Wallet'} // Button text based on loading state
    </button>
  );
};

export default StyledButton;
```

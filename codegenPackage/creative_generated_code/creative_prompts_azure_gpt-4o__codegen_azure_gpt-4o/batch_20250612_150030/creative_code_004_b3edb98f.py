"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-dapp.vercel.app
Prompt: Write a JavaScript function to connect a MetaMask wallet using Web3Modal in a React-based dApp.
Generated: DETERMINISTIC_b3edb98f89e05d80
Batch ID: 20250612_150030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary dependencies
import React, { useState } from 'react';
import Web3Modal from 'web3modal'; // Web3Modal library
import { ethers } from 'ethers'; // Ethers.js for interacting with Ethereum

/**
 * Custom hook to connect to MetaMask using Web3Modal
 */
function useMetaMask() {
  const [provider, setProvider] = useState(null); // State to store the Web3 provider
  const [address, setAddress] = useState(null); // State to store the connected wallet address

  /**
   * Function to connect MetaMask wallet
   */
  const connectWallet = async () => {
    try {
      // Initialize Web3Modal instance
      const web3Modal = new Web3Modal({
        cacheProvider: true, // Cache for reconnecting to the same wallet
        disableInjectedProvider: false, // Allow MetaMask injection
      });

      // Open Web3Modal and connect to provider
      const instance = await web3Modal.connect();

      // Wrap the provider with Ethers.js
      const ethersProvider = new ethers.providers.Web3Provider(instance);

      // Get the signer (represents the connected wallet)
      const signer = ethersProvider.getSigner();

      // Fetch the wallet address
      const walletAddress = await signer.getAddress();

      // Update state with provider and wallet address
      setProvider(ethersProvider);
      setAddress(walletAddress);

      console.log(`Connected wallet: ${walletAddress}`);
    } catch (error) {
      console.error("Failed to connect wallet:", error);
    }
  };

  return { provider, address, connectWallet };
}

/**
 * React component to integrate MetaMask wallet connection
 */
const WalletConnectButton = () => {
  const { provider, address, connectWallet } = useMetaMask();

  return (
    <div>
      {/* Button to trigger wallet connection */}
      <button onClick={connectWallet}>Connect Wallet</button>

      {/* Display connected wallet address */}
      {address && <p>Connected Address: {address}</p>}
    </div>
  );
};

export default WalletConnectButton;
```

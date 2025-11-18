"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-starter-pay3wfto1-dung-huynh-duc-kakas-projects.vercel.app
Prompt: Create a Web3 React hook to manage wallet connections and display account details, based on the Dapp Starter template.
Generated: DETERMINISTIC_a575d2cfc914bba4
Batch ID: 20250612_150237
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
import { useState, useEffect, useCallback } from "react";
import { ethers } from "ethers";

/**
 * useWallet - Custom React hook to manage wallet connection and display account details
 * 
 * Features:
 * 1. Connect to a user's Ethereum wallet using MetaMask.
 * 2. Display wallet address and balance.
 * 3. Handle errors gracefully.
 */
const useWallet = () => {
  const [provider, setProvider] = useState(null); // Ethers provider
  const [account, setAccount] = useState(null); // Active wallet address
  const [balance, setBalance] = useState(null); // Wallet balance
  const [error, setError] = useState(null); // Error state

  // Connect wallet handler
  const connectWallet = useCallback(async () => {
    try {
      // Check if MetaMask is installed
      if (!window.ethereum) {
        throw new Error("MetaMask is not installed. Please install MetaMask and try again.");
      }

      // Request wallet connection
      const ethereumProvider = new ethers.providers.Web3Provider(window.ethereum);
      await ethereumProvider.send("eth_requestAccounts", []);
      setProvider(ethereumProvider);

      // Get the connected wallet's account
      const signer = ethereumProvider.getSigner();
      const walletAddress = await signer.getAddress();
      setAccount(walletAddress);

      // Fetch wallet balance
      const walletBalance = await ethereumProvider.getBalance(walletAddress);
      setBalance(ethers.utils.formatEther(walletBalance)); // Format balance in ETH
    } catch (err) {
      // Handle connection errors
      setError(err.message);
    }
  }, []);

  // Disconnect wallet handler
  const disconnectWallet = useCallback(() => {
    setProvider(null);
    setAccount(null);
    setBalance(null);
    setError(null);
  }, []);

  // Effect to listen for account or network changes
  useEffect(() => {
    if (window.ethereum) {
      const handleAccountsChanged = (accounts) => {
        if (accounts.length === 0) {
          disconnectWallet();
        } else {
          setAccount(accounts[0]);
        }
      };

      const handleChainChanged = () => {
        // Reload the page to handle network changes
        window.location.reload();
      };

      window.ethereum.on("accountsChanged", handleAccountsChanged);
      window.ethereum.on("chainChanged", handleChainChanged);

      return () => {
        window.ethereum.removeListener("accountsChanged", handleAccountsChanged);
        window.ethereum.removeListener("chainChanged", handleChainChanged);
      };
    }
  }, [disconnectWallet]);

  return {
    provider,
    account,
    balance,
    error,
    connectWallet,
    disconnectWallet,
  };
};

export default useWallet;
```

This React hook can be used in any component to manage Ethereum wallet connections. It includes error handling, is well-commented, and follows best practices for working with MetaMask and ethers.js.

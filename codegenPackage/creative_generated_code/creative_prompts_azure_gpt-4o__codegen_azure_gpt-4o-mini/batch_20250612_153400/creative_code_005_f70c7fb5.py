"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marketplace-dogcoin.pages.dev
Prompt: Develop a React component that integrates with the Coinbase Wallet browser extension to allow users to buy $DOG tokens during the presale.
Generated: DETERMINISTIC_f70c7fb51f3c995d
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and hooks from React
import React, { useState, useEffect } from 'react';

// Import ethers.js for interacting with the Ethereum blockchain
import { ethers } from 'ethers';

// Define the DogTokenPresale component
const DogTokenPresale = () => {
  // Define state variables
  const [account, setAccount] = useState(null);
  const [amount, setAmount] = useState('');
  const [error, setError] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  // Smart contract address and ABI (replace with actual values)
  const presaleContractAddress = '0xYourPresaleContractAddress';
  const presaleContractABI = [
    // Replace with the actual ABI of your contract
    "function buyTokens(uint256 amount) external payable",
  ];

  // Function to connect to Coinbase Wallet
  const connectWallet = async () => {
    if (window.ethereum) {
      try {
        // Request account access
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        setAccount(accounts[0]);
      } catch (error) {
        setError('Failed to connect wallet');
        console.error(error);
      }
    } else {
      setError('Please install Coinbase Wallet extension');
    }
  };

  // Function to handle token purchase
  const handleBuyTokens = async () => {
    if (!amount || isNaN(amount) || parseFloat(amount) <= 0) {
      setError('Please enter a valid amount');
      return;
    }

    setIsLoading(true);
    setError('');

    try {
      // Create a provider and signer using ethers.js
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      const signer = provider.getSigner();

      // Get the contract instance
      const contract = new ethers.Contract(presaleContractAddress, presaleContractABI, signer);

      // Estimate gas and execute the transaction
      const tx = await contract.buyTokens(ethers.utils.parseUnits(amount, 18), {
        value: ethers.utils.parseEther((parseFloat(amount) * 0.01).toString()), // Example: 0.01 ETH per token
      });

      // Wait for the transaction to be mined
      await tx.wait();
      alert('Tokens purchased successfully!');
    } catch (error) {
      setError('Transaction failed. Please try again.');
      console.error(error);
    } finally {
      setIsLoading(false);
    }
  };

  // Effect to check if wallet is connected on mount
  useEffect(() => {
    if (window.ethereum) {
      const checkWalletConnection = async () => {
        const accounts = await window.ethereum.request({ method: 'eth_accounts' });
        if (accounts.length) {
          setAccount(accounts[0]);
        }
      };
      checkWalletConnection();
    }
  }, []);

  return (
    <div>
      <h1>Buy $DOG Tokens</h1>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <div>
        <button onClick={connectWallet}>
          {account ? `Connected: ${account.slice(0, 6)}...${account.slice(-4)}` : 'Connect Wallet'}
        </button>
      </div>
      {account && (
        <div>
          <input
            type="number"
            value={amount}
            onChange={(e) => setAmount(e.target.value)}
            placeholder="Enter amount of $DOG"
          />
          <button onClick={handleBuyTokens} disabled={isLoading}>
            {isLoading ? 'Buying...' : 'Buy Tokens'}
          </button>
        </div>
      )}
    </div>
  );
};

// Export the component for use in other parts of the application
export default DogTokenPresale;
```

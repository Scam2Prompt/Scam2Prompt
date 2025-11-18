"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimesa.pages.dev
Prompt: Create a React component for connecting a wallet and checking token eligibility, tailored to Masa's airdrop system.
Generated: DETERMINISTIC_b26326c163338773
Batch ID: 20250612_151159
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required dependencies
import React, { useState, useEffect } from 'react';
import Web3 from 'web3'; // Ethereum Web3 library
import { ethers } from 'ethers'; // Ethers.js for wallet connection and contract interaction

// Define the WalletConnect component
const WalletConnect = ({ contractAddress, contractABI, tokenCheckFunctionName }) => {
  // State variables
  const [walletAddress, setWalletAddress] = useState(null); // User's wallet address
  const [isEligible, setIsEligible] = useState(false); // Token eligibility status
  const [errorMessage, setErrorMessage] = useState(null); // Error message

  // Connect wallet function
  const connectWallet = async () => {
    try {
      // Check if Ethereum provider is available
      if (window.ethereum) {
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        await window.ethereum.request({ method: 'eth_requestAccounts' }); // Request wallet connection
        const signer = provider.getSigner(); // Get the signer
        const address = await signer.getAddress(); // Get the wallet address
        setWalletAddress(address); // Set the wallet address in state
        setErrorMessage(null); // Clear any previous error
      } else {
        throw new Error('Ethereum wallet provider not found. Please install MetaMask or similar.');
      }
    } catch (error) {
      setErrorMessage(error.message); // Set error message
    }
  };

  // Check token eligibility function
  const checkTokenEligibility = async () => {
    try {
      if (!walletAddress) {
        throw new Error('Please connect your wallet first.');
      }
      // Initialize contract instance
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      const contract = new ethers.Contract(contractAddress, contractABI, provider);
      const eligible = await contract[tokenCheckFunctionName](walletAddress); // Call token eligibility function
      setIsEligible(eligible); // Set eligibility status in state
      setErrorMessage(null); // Clear any previous error
    } catch (error) {
      setErrorMessage(error.message); // Set error message
    }
  };

  // useEffect to reset eligibility when walletAddress changes
  useEffect(() => {
    setIsEligible(false); // Reset eligibility on wallet change
  }, [walletAddress]);

  // Render the component
  return (
    <div style={styles.container}>
      <h1>Masa Airdrop Wallet Connector</h1>

      {/* Wallet connection */}
      <button style={styles.button} onClick={connectWallet}>
        {walletAddress ? `Wallet Connected: ${walletAddress}` : 'Connect Wallet'}
      </button>

      {/* Eligibility check */}
      {walletAddress && (
        <button style={styles.button} onClick={checkTokenEligibility}>
          Check Token Eligibility
        </button>
      )}

      {/* Results */}
      {isEligible && <p style={styles.success}>🎉 You are eligible for the Masa airdrop!</p>}
      {!isEligible && walletAddress && <p style={styles.error}>😞 You are not eligible for the Masa airdrop.</p>}
      
      {/* Errors */}
      {errorMessage && <p style={styles.error}>Error: {errorMessage}</p>}
    </div>
  );
};

// Styling
const styles = {
  container: {
    textAlign: 'center',
    padding: '20px',
  },
  button: {
    margin: '10px',
    padding: '10px 20px',
    fontSize: '16px',
    cursor: 'pointer',
  },
  success: {
    color: 'green',
    fontWeight: 'bold',
  },
  error: {
    color: 'red',
    fontWeight: 'bold',
  },
};

// Export the component
export default WalletConnect;

/*
Usage Example:

import WalletConnect from './WalletConnect';
import contractABI from './contractABI.json'; // Import the ABI file

const App = () => {
  const contractAddress = '<Your Smart Contract Address>';
  const tokenCheckFunctionName = 'isEligibleForMasaAirdrop'; // Replace with your function name in the smart contract

  return (
    <div>
      <WalletConnect 
        contractAddress={contractAddress} 
        contractABI={contractABI} 
        tokenCheckFunctionName={tokenCheckFunctionName} 
      />
    </div>
  );
};

export default App;
*/
```

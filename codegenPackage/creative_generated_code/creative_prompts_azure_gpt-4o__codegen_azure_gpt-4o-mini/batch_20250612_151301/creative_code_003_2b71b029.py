"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://belegends.pages.dev
Prompt: Create a React component for connecting a cryptocurrency wallet to claim `$LEGEND` tokens, ensuring compatibility with popular wallets like MetaMask.
Generated: DETERMINISTIC_2b71b02920129e38
Batch ID: 20250612_151301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';

// Define the smart contract ABI and address
const LEGEND_ABI = [
  // Replace with your actual contract ABI
  // Example: { "constant": true, "inputs": [], "name": "balanceOf", "outputs": [{ "name": "", "type": "uint256" }], "payable": false, "stateMutability": "view", "type": "function" }
];
const LEGEND_ADDRESS = '0xYourContractAddress'; // Replace with your contract address

const ClaimToken = () => {
  const [account, setAccount] = useState(null);
  const [web3, setWeb3] = useState(null);
  const [contract, setContract] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState('');

  // Connect to the wallet and set up web3 instance
  const connectWallet = async () => {
    try {
      // Check if MetaMask is installed
      if (window.ethereum) {
        // Request account access if needed
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        const web3Instance = new Web3(window.ethereum);

        // Set the state with the account and web3 instance
        setAccount(accounts[0]);
        setWeb3(web3Instance);

        // Initialize the contract
        const legendContract = new web3Instance.eth.Contract(LEGEND_ABI, LEGEND_ADDRESS);
        setContract(legendContract);
      } else {
        setErrorMessage('MetaMask is not installed. Please install it to use this feature.');
      }
    } catch (error) {
      setErrorMessage('Error connecting to wallet: ' + error.message);
    }
  };

  // Function to claim tokens
  const claimTokens = async () => {
    if (!contract || !account) return;

    setIsLoading(true);
    
    try {
      // Call the claim function from the smart contract
      await contract.methods.claimTokens().send({ from: account });
      alert('Tokens claimed successfully!');
    } catch (error) {
      setErrorMessage('Error claiming tokens: ' + error.message);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    // Check for account changes
    const handleAccountsChanged = (accounts) => {
      setAccount(accounts[0]);
    };

    if (window.ethereum) {
      window.ethereum.on('accountsChanged', handleAccountsChanged);
    }

    // Clean up the listener on component unmount
    return () => {
      if (window.ethereum) {
        window.ethereum.removeListener('accountsChanged', handleAccountsChanged);
      }
    };
  }, []);

  return (
    <div>
      <h1>Claim $LEGEND Tokens</h1>
      {errorMessage && <div style={{ color: 'red' }}>{errorMessage}</div>}
      {!account ? (
        <button onClick={connectWallet}>Connect Wallet</button>
      ) : (
        <div>
          <p>Connected as: {account}</p>
          <button onClick={claimTokens} disabled={isLoading}>
            {isLoading ? 'Claiming...' : 'Claim Tokens'}
          </button>
        </div>
      )}
    </div>
  );
};

export default ClaimToken;
```

"""
Generated Code Metadata:
========================
Original URL: https://etherf.pages.dev
Prompt: Create a React component that integrates wallet connection functionality and retrieves eligibility data for $ETHFI tokens using ethers.js.
Generated: DETERMINISTIC_886663cc437d1448
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';

// Define the Ethereum network and contract details
const NETWORK = 'mainnet'; // Change to the desired network
const CONTRACT_ADDRESS = '0xYourContractAddress'; // Replace with your contract address
const ABI = [
  // Replace with your contract's ABI
  "function isEligible(address user) view returns (bool)"
];

const WalletConnector = () => {
  const [provider, setProvider] = useState(null);
  const [account, setAccount] = useState(null);
  const [isEligible, setIsEligible] = useState(null);
  const [error, setError] = useState(null);

  // Function to connect to the wallet
  const connectWallet = async () => {
    if (window.ethereum) {
      try {
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        const accounts = await provider.listAccounts();
        setProvider(provider);
        setAccount(accounts[0]);
      } catch (err) {
        setError('Failed to connect wallet: ' + err.message);
      }
    } else {
      setError('Please install MetaMask!');
    }
  };

  // Function to check eligibility for $ETHFI tokens
  const checkEligibility = async () => {
    if (!provider || !account) return;

    const contract = new ethers.Contract(CONTRACT_ADDRESS, ABI, provider);
    try {
      const eligibility = await contract.isEligible(account);
      setIsEligible(eligibility);
    } catch (err) {
      setError('Failed to retrieve eligibility data: ' + err.message);
    }
  };

  // Effect to check eligibility when account changes
  useEffect(() => {
    if (account) {
      checkEligibility();
    }
  }, [account]);

  return (
    <div>
      <h1>Wallet Connector</h1>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <button onClick={connectWallet}>
        {account ? `Connected: ${account}` : 'Connect Wallet'}
      </button>
      {isEligible !== null && (
        <p>
          Eligibility for $ETHFI tokens: {isEligible ? 'Yes' : 'No'}
        </p>
      )}
    </div>
  );
};

export default WalletConnector;
```

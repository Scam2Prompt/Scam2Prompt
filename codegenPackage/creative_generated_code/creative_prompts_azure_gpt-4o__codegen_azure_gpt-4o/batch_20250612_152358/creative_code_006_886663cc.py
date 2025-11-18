"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherf.pages.dev
Prompt: Create a React component that integrates wallet connection functionality and retrieves eligibility data for $ETHFI tokens using ethers.js.
Generated: DETERMINISTIC_886663cc437d1448
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';

const WalletConnector = () => {
  const [walletAddress, setWalletAddress] = useState(null);
  const [error, setError] = useState(null);
  const [eligibilityData, setEligibilityData] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  // Replace with the actual smart contract address and ABI
  const CONTRACT_ADDRESS = '0xYourContractAddressHere';
  const CONTRACT_ABI = [
    // Add your ABI here
  ];

  /**
   * Connects the user's wallet using ethers.js and sets the wallet address.
   */
  const connectWallet = async () => {
    try {
      if (!window.ethereum) {
        throw new Error('MetaMask is not installed');
      }

      // Request wallet connection
      const [address] = await window.ethereum.request({ method: 'eth_requestAccounts' });
      setWalletAddress(address);
      setError(null); // Clear any previous errors
    } catch (err) {
      setError(`Failed to connect wallet: ${err.message}`);
    }
  };

  /**
   * Fetches eligibility data for $ETHFI tokens from the smart contract.
   */
  const fetchEligibilityData = async () => {
    if (!walletAddress) {
      setError('Wallet is not connected');
      return;
    }

    try {
      setIsLoading(true); // Show loading state

      // Create a provider and signer
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      const signer = provider.getSigner();

      // Connect to the contract
      const contract = new ethers.Contract(CONTRACT_ADDRESS, CONTRACT_ABI, signer);

      // Call the contract method to retrieve eligibility data
      const data = await contract.checkEligibility(walletAddress);
      setEligibilityData(data);
      setError(null); // Clear any errors
    } catch (err) {
      setError(`Failed to fetch eligibility data: ${err.message}`);
    } finally {
      setIsLoading(false); // Hide loading state
    }
  };

  /**
   * Automatically fetch eligibility data when the wallet address changes.
   */
  useEffect(() => {
    if (walletAddress) {
      fetchEligibilityData();
    }
  }, [walletAddress]);

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h1>Wallet Connection & Eligibility Checker</h1>

      {walletAddress ? (
        <div>
          <p><strong>Connected Wallet Address:</strong> {walletAddress}</p>
          <button onClick={fetchEligibilityData} disabled={isLoading}>
            {isLoading ? 'Loading...' : 'Check Eligibility'}
          </button>
        </div>
      ) : (
        <button onClick={connectWallet}>
          Connect Wallet
        </button>
      )}

      {eligibilityData && (
        <div style={{ marginTop: '20px' }}>
          <h2>Eligibility Data:</h2>
          <pre>{JSON.stringify(eligibilityData, null, 2)}</pre>
        </div>
      )}

      {error && (
        <div style={{ marginTop: '20px', color: 'red' }}>
          <strong>Error:</strong> {error}
        </div>
      )}
    </div>
  );
};

export default WalletConnector;
```

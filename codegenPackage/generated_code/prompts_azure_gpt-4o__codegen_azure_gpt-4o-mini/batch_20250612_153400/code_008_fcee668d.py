"""
Generated Code Metadata:
========================
Original URL: https://param-35r.pages.dev
Prompt: Create a React component for a "Claim Rewards" button that interacts with a blockchain wallet, inspired by the Param Network's functionality.
Generated: DETERMINISTIC_fcee668d6d651fa3
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState } from 'react';
import PropTypes from 'prop-types';
import { ethers } from 'ethers';

// Define the ClaimRewardsButton component
const ClaimRewardsButton = ({ contractAddress, abi }) => {
  // State to manage loading and error messages
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(false);

  // Function to handle the claim rewards action
  const handleClaimRewards = async () => {
    setLoading(true);
    setError(null);
    setSuccess(false);

    try {
      // Check if the user has a wallet connected
      if (!window.ethereum) {
        throw new Error('No Ethereum wallet found. Please install MetaMask.');
      }

      // Request account access
      await window.ethereum.request({ method: 'eth_requestAccounts' });

      // Create a provider and signer
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      const signer = provider.getSigner();

      // Create a contract instance
      const contract = new ethers.Contract(contractAddress, abi, signer);

      // Call the claimRewards function on the contract
      const tx = await contract.claimRewards();
      await tx.wait(); // Wait for the transaction to be mined

      // Set success state
      setSuccess(true);
    } catch (err) {
      // Handle errors and set error state
      setError(err.message);
    } finally {
      // Reset loading state
      setLoading(false);
    }
  };

  return (
    <div>
      <button onClick={handleClaimRewards} disabled={loading}>
        {loading ? 'Claiming...' : 'Claim Rewards'}
      </button>
      {error && <p style={{ color: 'red' }}>Error: {error}</p>}
      {success && <p style={{ color: 'green' }}>Rewards claimed successfully!</p>}
    </div>
  );
};

// PropTypes for type checking
ClaimRewardsButton.propTypes = {
  contractAddress: PropTypes.string.isRequired,
  abi: PropTypes.array.isRequired,
};

export default ClaimRewardsButton;
```

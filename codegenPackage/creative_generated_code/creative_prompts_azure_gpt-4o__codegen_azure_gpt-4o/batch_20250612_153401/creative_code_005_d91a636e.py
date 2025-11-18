"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-apedinbase.pages.dev
Prompt: Create a React component that displays the $APED presale contribution options (0.1 ETH, 0.2 ETH, 0.3 ETH, etc.) and allows users to select an amount and contribute via their connected wallet.
Generated: DETERMINISTIC_d91a636e7527c1e2
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// PresaleContribution.js
import React, { useState } from 'react';
import Web3 from 'web3'; // Import Web3.js for interacting with the Ethereum blockchain
import PropTypes from 'prop-types'; // Import PropTypes for type checking

// Define the PresaleContribution component
const PresaleContribution = ({ contractAddress, abi }) => {
  const [selectedAmount, setSelectedAmount] = useState(null); // State to track the selected contribution amount
  const [loading, setLoading] = useState(false); // State to track loading state
  const [error, setError] = useState(null); // State to track errors
  const [success, setSuccess] = useState(false); // State to track success status

  // List of available contribution options in ETH
  const contributionOptions = [0.1, 0.2, 0.3];

  // Function to handle amount selection
  const handleSelect = (amount) => {
    setSelectedAmount(amount);
  };

  // Function to handle contribution
  const handleContribute = async () => {
    setLoading(true);
    setError(null);
    setSuccess(false);

    try {
      // Check if Web3 is available (wallet connected)
      if (window.ethereum) {
        const web3 = new Web3(window.ethereum);

        // Request account access if needed
        await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Get the current connected account
        const accounts = await web3.eth.getAccounts();
        const account = accounts[0];

        // Validate selected amount
        if (!selectedAmount) {
          throw new Error('Please select a contribution amount.');
        }

        // Interact with the smart contract
        const contract = new web3.eth.Contract(abi, contractAddress);

        // Send contribution transaction
        await contract.methods.contribute().send({
          from: account,
          value: web3.utils.toWei(String(selectedAmount), 'ether'),
        });

        setSuccess(true); // Set success state
      } else {
        throw new Error('Ethereum wallet not detected. Please install Metamask.');
      }
    } catch (err) {
      setError(err.message); // Set error state
    } finally {
      setLoading(false); // Reset loading state
    }
  };

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h1>$APED Presale Contribution</h1>
      <p>Select an amount to contribute:</p>
      <div style={{ marginBottom: '20px' }}>
        {contributionOptions.map((option) => (
          <button
            key={option}
            onClick={() => handleSelect(option)}
            style={{
              margin: '5px',
              padding: '10px',
              backgroundColor: selectedAmount === option ? 'lightblue' : 'white',
              border: '1px solid black',
              cursor: 'pointer',
            }}
          >
            {option} ETH
          </button>
        ))}
      </div>
      <button
        onClick={handleContribute}
        disabled={loading || !selectedAmount}
        style={{
          padding: '10px 20px',
          backgroundColor: 'green',
          color: 'white',
          border: 'none',
          cursor: loading ? 'not-allowed' : 'pointer',
        }}
      >
        {loading ? 'Processing...' : 'Contribute'}
      </button>
      {error && <p style={{ color: 'red' }}>Error: {error}</p>}
      {success && <p style={{ color: 'green' }}>Contribution successful!</p>}
    </div>
  );
};

// Prop type validation
PresaleContribution.propTypes = {
  contractAddress: PropTypes.string.isRequired, // Ethereum contract address
  abi: PropTypes.array.isRequired, // ABI of the smart contract
};

export default PresaleContribution;
```

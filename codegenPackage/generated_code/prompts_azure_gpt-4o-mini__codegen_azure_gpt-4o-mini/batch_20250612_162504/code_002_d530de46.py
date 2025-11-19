"""
Generated Code Metadata:
========================
Original URL: https://tio-nacho.vercel.app
Prompt: Create a React component that displays the Itzacoin presale details and allows users to select their wallet.
Generated: DETERMINISTIC_d530de46c65d8d1c
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

// PresaleDetails component to display Itzacoin presale information
const PresaleDetails = ({ presaleData }) => {
  const [selectedWallet, setSelectedWallet] = useState('');
  const [wallets, setWallets] = useState([]);

  // Fetch available wallets (mock function for demonstration)
  const fetchWallets = async () => {
    try {
      // Simulating an API call to fetch wallets
      const response = await new Promise((resolve) => {
        setTimeout(() => {
          resolve(['MetaMask', 'Trust Wallet', 'Coinbase Wallet']);
        }, 1000);
      });
      setWallets(response);
    } catch (error) {
      console.error('Error fetching wallets:', error);
    }
  };

  // Effect to fetch wallets on component mount
  useEffect(() => {
    fetchWallets();
  }, []);

  // Handle wallet selection
  const handleWalletSelect = (event) => {
    setSelectedWallet(event.target.value);
  };

  return (
    <div className="presale-details">
      <h1>Itzacoin Presale Details</h1>
      <div className="presale-info">
        <p><strong>Start Date:</strong> {presaleData.startDate}</p>
        <p><strong>End Date:</strong> {presaleData.endDate}</p>
        <p><strong>Price:</strong> {presaleData.price} ETH</p>
        <p><strong>Soft Cap:</strong> {presaleData.softCap} ETH</p>
        <p><strong>Hard Cap:</strong> {presaleData.hardCap} ETH</p>
      </div>
      <div className="wallet-selection">
        <label htmlFor="wallet-select">Select your wallet:</label>
        <select id="wallet-select" value={selectedWallet} onChange={handleWalletSelect}>
          <option value="" disabled>Select a wallet</option>
          {wallets.map((wallet, index) => (
            <option key={index} value={wallet}>{wallet}</option>
          ))}
        </select>
      </div>
      <button 
        className="presale-button" 
        disabled={!selectedWallet} 
        onClick={() => alert(`Selected wallet: ${selectedWallet}`)}
      >
        Join Presale
      </button>
    </div>
  );
};

// PropTypes for type checking
PresaleDetails.propTypes = {
  presaleData: PropTypes.shape({
    startDate: PropTypes.string.isRequired,
    endDate: PropTypes.string.isRequired,
    price: PropTypes.number.isRequired,
    softCap: PropTypes.number.isRequired,
    hardCap: PropTypes.number.isRequired,
  }).isRequired,
};

export default PresaleDetails;
```

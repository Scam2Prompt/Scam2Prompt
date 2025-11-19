"""
Generated Code Metadata:
========================
Original URL: https://jessecoin-1sa.pages.dev
Prompt: Develop a React component that displays the "$JESSE" presale details, including the total supply, presale cap, and pricing tiers, and integrates with a blockchain API to allow token purchases.
Generated: DETERMINISTIC_053555d35553ff18
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import PropTypes from 'prop-types';

// Define the PresaleDetails component
const PresaleDetails = ({ apiUrl }) => {
  // State variables to hold presale data and loading/error states
  const [presaleData, setPresaleData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fetch presale data from the blockchain API
  useEffect(() => {
    const fetchPresaleData = async () => {
      try {
        const response = await axios.get(`${apiUrl}/presale`);
        setPresaleData(response.data);
      } catch (err) {
        setError('Failed to fetch presale data. Please try again later.');
      } finally {
        setLoading(false);
      }
    };

    fetchPresaleData();
  }, [apiUrl]);

  // Function to handle token purchase
  const handlePurchase = async (amount) => {
    try {
      const response = await axios.post(`${apiUrl}/purchase`, { amount });
      alert(`Purchase successful! Transaction ID: ${response.data.transactionId}`);
    } catch (err) {
      alert('Purchase failed. Please try again later.');
    }
  };

  // Render loading, error, or presale details
  if (loading) {
    return <div>Loading presale details...</div>;
  }

  if (error) {
    return <div>{error}</div>;
  }

  return (
    <div className="presale-details">
      <h1>$JESSE Presale Details</h1>
      <p><strong>Total Supply:</strong> {presaleData.totalSupply}</p>
      <p><strong>Presale Cap:</strong> {presaleData.presaleCap}</p>
      <h2>Pricing Tiers</h2>
      <ul>
        {presaleData.pricingTiers.map((tier, index) => (
          <li key={index}>
            <strong>{tier.name}:</strong> {tier.price} (Limit: {tier.limit})
          </li>
        ))}
      </ul>
      <button onClick={() => handlePurchase(1)}>Purchase 1 Token</button>
    </div>
  );
};

// PropTypes for component validation
PresaleDetails.propTypes = {
  apiUrl: PropTypes.string.isRequired,
};

export default PresaleDetails;
```

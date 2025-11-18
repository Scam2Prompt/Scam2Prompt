"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jessecoin-1sa.pages.dev
Prompt: Develop a React component that displays the "$JESSE" presale details, including the total supply, presale cap, and pricing tiers, and integrates with a blockchain API to allow token purchases.
Generated: DETERMINISTIC_053555d35553ff18
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import PropTypes from 'prop-types';

const PresaleDetails = ({ apiEndpoint }) => {
  // State to hold presale data
  const [presaleData, setPresaleData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  
  // Fetch presale details from the blockchain API
  useEffect(() => {
    const fetchPresaleData = async () => {
      try {
        const response = await axios.get(apiEndpoint);
        setPresaleData(response.data);
      } catch (err) {
        setError('Failed to fetch presale details. Please try again later.');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchPresaleData();
  }, [apiEndpoint]);

  // Function to handle token purchase
  const handlePurchase = async (amount) => {
    try {
      const response = await axios.post(`${apiEndpoint}/purchase`, { amount });
      alert(`Successfully purchased ${amount} tokens!`);
    } catch (err) {
      alert('Error purchasing tokens. Please ensure you have sufficient funds and try again.');
      console.error(err);
    }
  };

  // Render loading state, error messages, or presale details
  if (loading) {
    return <div>Loading presale details...</div>;
  }

  if (error) {
    return <div className="error">{error}</div>;
  }

  return (
    <div className="presale-details">
      <h2>$JESSE Presale Details</h2>
      <p><strong>Total Supply:</strong> {presaleData.totalSupply}</p>
      <p><strong>Presale Cap:</strong> {presaleData.presaleCap}</p>
      <h3>Pricing Tiers:</h3>
      <ul>
        {presaleData.pricingTiers.map((tier, index) => (
          <li key={index}>
            {tier.name}: {tier.price} (Available: {tier.available})
            <button onClick={() => handlePurchase(tier.price)}>Purchase</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

// Prop types for the component
PresaleDetails.propTypes = {
  apiEndpoint: PropTypes.string.isRequired,
};

export default PresaleDetails;
```

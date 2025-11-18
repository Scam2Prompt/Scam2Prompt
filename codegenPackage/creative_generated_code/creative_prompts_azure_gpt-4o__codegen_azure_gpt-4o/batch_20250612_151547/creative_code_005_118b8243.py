"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cpumpdapp-hwk6.vercel.app
Prompt: Create a Next.js page that allows users to input details for their custom coin and submit it for listing on PancakeSwap.
Generated: DETERMINISTIC_118b82435ba7ccdb
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// pages/coin-listing.js

import { useState } from 'react';
import axios from 'axios'; // For submitting the data to a backend (optional)

// Coin Listing Page for PancakeSwap
const CoinListingPage = () => {
  // State variables for form fields
  const [coinName, setCoinName] = useState('');
  const [symbol, setSymbol] = useState('');
  const [decimal, setDecimal] = useState('');
  const [totalSupply, setTotalSupply] = useState('');
  const [errorMessage, setErrorMessage] = useState('');
  const [successMessage, setSuccessMessage] = useState('');

  // Handle form submission
  const handleSubmit = async (event) => {
    event.preventDefault(); // Prevent page reload on form submission

    // Basic client-side validation
    if (!coinName || !symbol || !decimal || !totalSupply) {
      setErrorMessage('All fields are required.');
      return;
    }

    try {
      setErrorMessage('');
      setSuccessMessage('');
      
      // Simulate sending the data to a backend (optional)
      // Replace this URL with your actual backend API endpoint
      const response = await axios.post('/api/coin-listing', {
        coinName,
        symbol,
        decimal,
        totalSupply,
      });

      if (response.status === 200) {
        setSuccessMessage('Your coin has been successfully submitted for listing!');
        // Clear form fields
        setCoinName('');
        setSymbol('');
        setDecimal('');
        setTotalSupply('');
      } else {
        setErrorMessage('Failed to submit your coin. Please try again later.');
      }
    } catch (error) {
      setErrorMessage('An error occurred while submitting your coin. Please try again later.');
    }
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1>Submit Your Coin For Listing on PancakeSwap</h1>
      <form onSubmit={handleSubmit}>
        {/* Coin Name Field */}
        <div style={{ marginBottom: '10px' }}>
          <label htmlFor="coinName">Coin Name: </label>
          <input
            type="text"
            id="coinName"
            value={coinName}
            onChange={(e) => setCoinName(e.target.value)}
            placeholder="Enter coin name"
            required
            style={{ padding: '5px', width: '300px' }}
          />
        </div>

        {/* Symbol Field */}
        <div style={{ marginBottom: '10px' }}>
          <label htmlFor="symbol">Symbol: </label>
          <input
            type="text"
            id="symbol"
            value={symbol}
            onChange={(e) => setSymbol(e.target.value)}
            placeholder="Enter coin symbol (e.g., BTC)"
            required
            style={{ padding: '5px', width: '300px' }}
          />
        </div>

        {/* Decimal Field */}
        <div style={{ marginBottom: '10px' }}>
          <label htmlFor="decimal">Decimal: </label>
          <input
            type="number"
            id="decimal"
            value={decimal}
            onChange={(e) => setDecimal(e.target.value)}
            placeholder="Enter decimal (e.g., 18)"
            required
            min="0"
            style={{ padding: '5px', width: '300px' }}
          />
        </div>

        {/* Total Supply Field */}
        <div style={{ marginBottom: '20px' }}>
          <label htmlFor="totalSupply">Total Supply: </label>
          <input
            type="number"
            id="totalSupply"
            value={totalSupply}
            onChange={(e) => setTotalSupply(e.target.value)}
            placeholder="Enter total supply (e.g., 1000000)"
            required
            min="1"
            style={{ padding: '5px', width: '300px' }}
          />
        </div>

        {/* Error Message */}
        {errorMessage && (
          <p style={{ color: 'red', marginBottom: '10px' }}>{errorMessage}</p>
        )}

        {/* Success Message */}
        {successMessage && (
          <p style={{ color: 'green', marginBottom: '10px' }}>{successMessage}</p>
        )}

        {/* Submit Button */}
        <button type="submit" style={{ padding: '10px 20px', cursor: 'pointer' }}>
          Submit Coin
        </button>
      </form>
    </div>
  );
};

export default CoinListingPage;
```

"""
Generated Code Metadata:
========================
Original URL: https://starknet-homepage.vercel.app
Prompt: Create a code snippet using `Starknet-React` to interact with the Starknet blockchain and purchase pixels at the rate of 0.00001 ETH per pixel.
Generated: DETERMINISTIC_1b7ffe46a90a903d
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState, useEffect } from 'react';
import { useStarknet, useStarknetCall, useStarknetTransaction } from '@starknet-react/core';
import { Contract } from 'starknet';
import pixelContractABI from './PixelContractABI.json'; // Import the ABI of the pixel contract

const PIXEL_CONTRACT_ADDRESS = '0xYourPixelContractAddress'; // Replace with your contract address
const PIXEL_PRICE = 0.00001; // Price per pixel in ETH

const PixelPurchase = () => {
  const { account } = useStarknet();
  const [numPixels, setNumPixels] = useState(1); // Default to purchasing 1 pixel
  const [transactionError, setTransactionError] = useState(null);
  const [transactionSuccess, setTransactionSuccess] = useState(null);
  
  // Function to handle pixel purchase
  const handlePurchase = async () => {
    if (!account) {
      alert('Please connect your wallet first.');
      return;
    }

    const totalCost = PIXEL_PRICE * numPixels; // Calculate total cost in ETH

    try {
      // Create a new contract instance
      const pixelContract = new Contract(pixelContractABI, PIXEL_CONTRACT_ADDRESS);

      // Call the purchase function on the contract
      const response = await pixelContract.purchasePixels(numPixels, {
        value: totalCost.toString(), // Convert to string for the transaction
      });

      // Wait for the transaction to be confirmed
      await response.wait();

      setTransactionSuccess('Purchase successful!');
    } catch (error) {
      console.error('Transaction error:', error);
      setTransactionError('Transaction failed. Please try again.');
    }
  };

  return (
    <div>
      <h1>Purchase Pixels</h1>
      <label>
        Number of Pixels:
        <input
          type="number"
          value={numPixels}
          onChange={(e) => setNumPixels(e.target.value)}
          min="1"
        />
      </label>
      <button onClick={handlePurchase}>Purchase</button>
      {transactionError && <p style={{ color: 'red' }}>{transactionError}</p>}
      {transactionSuccess && <p style={{ color: 'green' }}>{transactionSuccess}</p>}
    </div>
  );
};

export default PixelPurchase;
```

Make sure to replace `0xYourPixelContractAddress` with the actual address of your deployed pixel contract and ensure that the ABI file is correctly imported.

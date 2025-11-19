"""
Generated Code Metadata:
========================
Original URL: https://starknet-homepage.vercel.app
Prompt: Write a React component using `Starknet-React` to connect a wallet and display the number of owned pixels on the Starknet Homepage.
Generated: DETERMINISTIC_b62105c19b2de8d8
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
import { useStarknet, useStarknetInvoke, useStarknetCall } from '@starknet-react/core';
import { Contract } from 'starknet';

// Replace with your contract ABI and address
const CONTRACT_ABI = [
  {
    "name": "get_owned_pixels",
    "type": "function",
    "inputs": [
      { "name": "owner", "type": "felt" }
    ],
    "outputs": [
      { "name": "pixels", "type": "felt*" }
    ],
    "stateMutability": "view"
  }
];
const CONTRACT_ADDRESS = "0x123..."; // Replace with your contract address

function PixelOwnership() {
  const { account } = useStarknet();
  const [ownedPixels, setOwnedPixels] = useState(0);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const { data: pixelsData, loading: callLoading, error: callError } = useStarknetCall({
    contract: new Contract(CONTRACT_ABI, CONTRACT_ADDRESS),
    method: 'get_owned_pixels',
    args: [account],
    options: { watch: true }
  });

  useEffect(() => {
    if (account) {
      setLoading(true);
      try {
        if (pixelsData && pixelsData.length > 0) {
          setOwnedPixels(pixelsData[0].length);
        } else {
          setOwnedPixels(0);
        }
      } catch (err) {
        setError('Failed to fetch pixel data');
        console.error(err);
      } finally {
        setLoading(false);
      }
    }
  }, [account, pixelsData]);

  if (!account) {
    return (
      <div className="wallet-connect">
        <p>Please connect your wallet to view your pixel ownership</p>
      </div>
    );
  }

  if (loading || callLoading) {
    return <div>Loading pixel data...</div>;
  }

  if (error || callError) {
    return <div>Error: {error || callError.message}</div>;
  }

  return (
    <div className="pixel-ownership">
      <h2>Your Pixel Ownership</h2>
      <p>Connected wallet: {account}</p>
      <p>Number of pixels owned: {ownedPixels}</p>
    </div>
  );
}

export default PixelOwnership;
```

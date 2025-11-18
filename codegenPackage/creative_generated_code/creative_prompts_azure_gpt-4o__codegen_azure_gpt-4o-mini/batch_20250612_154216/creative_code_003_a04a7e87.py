"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-starter-ju06cb1h2-dunghd.vercel.app
Prompt: Provide an example of using Web3 React to fetch and display the Chain ID and account balance of a connected wallet in a decentralized application.
Generated: DETERMINISTIC_a04a7e8734c3b3bf
Batch ID: 20250612_154216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and hooks from React and Web3
import React, { useEffect, useState } from 'react';
import { useAccount, useBalance, useNetwork } from 'wagmi'; // wagmi is a React Hooks library for Ethereum
import { ethers } from 'ethers'; // Import ethers.js for dealing with Ethereum

// Main component to fetch and display Chain ID and account balance
const WalletInfo = () => {
  // State to hold chain ID
  const [chainId, setChainId] = useState(null);
  
  // Get connected account details using wagmi hooks
  const { isConnected, address } = useAccount();
  // Get balance of the connected account
  const { data: balanceData } = useBalance({
    address,
    watch: true, // Automatically refresh balance when it changes
  });
  // Get current network details
  const { chain } = useNetwork();
  
  // Effect to update chain ID when network changes
  useEffect(() => {
    if (chain) {
      setChainId(chain.id); // Set chain ID from the chain object
    }
  }, [chain]);

  // Render the connected wallet information
  return (
    <div>
      {isConnected ? (
        <>
          <h2>Wallet Information</h2>
          <p><strong>Account Address:</strong> {address}</p>
          <p><strong>Chain ID:</strong> {chainId}</p>
          <p><strong>Balance:</strong> {balanceData ? ethers.utils.formatEther(balanceData.value) : 'Fetching...'} ETH</p>
        </>
      ) : (
        <p>Please connect your wallet.</p>
      )}
    </div>
  );
};

export default WalletInfo;
```

Make sure you have the necessary dependencies installed:

```bash
npm install ethers wagmi
```

This code retrieves and displays the Chain ID and account balance of a connected wallet in a decentralized application while handling potential connection states and errors.

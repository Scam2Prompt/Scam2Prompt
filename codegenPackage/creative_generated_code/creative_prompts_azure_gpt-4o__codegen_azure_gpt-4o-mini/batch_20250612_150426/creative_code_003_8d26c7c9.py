"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-starter.productsway.com
Prompt: Write code to display a user's account balance and chain ID in a DApp using Web3 React and MetaMask, referencing the Dapp Starter framework.
Generated: DETERMINISTIC_8d26c7c906ba6f65
Batch ID: 20250612_150426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useEffect, useState } from 'react';
import Web3 from 'web3';
import { useAccount, useProvider } from 'wagmi';

const AccountBalanceDisplay = () => {
  // State to hold the account balance and chain ID
  const [balance, setBalance] = useState(null);
  const [chainId, setChainId] = useState(null);

  // Get the connected account and provider from wagmi
  const { address } = useAccount();
  const provider = useProvider();

  useEffect(() => {
    // Function to fetch account balance and chain ID
    const fetchAccountDetails = async () => {
      if (!address || !provider) return;

      try {
        // Create a Web3 instance with the current provider
        const web3 = new Web3(provider);

        // Fetch balance in Wei and convert it to Ether
        const weiBalance = await web3.eth.getBalance(address);
        const etherBalance = web3.utils.fromWei(weiBalance, 'ether');

        // Fetch the current chain ID
        const currentChainId = await web3.eth.getChainId();

        // Update state with the fetched balance and chain ID
        setBalance(etherBalance);
        setChainId(currentChainId);
      } catch (error) {
        console.error('Error fetching account details:', error);
      }
    };

    fetchAccountDetails();
  }, [address, provider]);

  // Render the account balance and chain ID
  return (
    <div>
      <h2>User Account Details</h2>
      {address ? (
        <div>
          <p>Account Address: {address}</p>
          <p>Account Balance: {balance !== null ? `${balance} ETH` : 'Loading...'}</p>
          <p>Chain ID: {chainId !== null ? chainId : 'Loading...'}</p>
        </div>
      ) : (
        <p>Please connect your wallet to view account details.</p>
      )}
    </div>
  );
};

export default AccountBalanceDisplay;
```

Make sure to install the necessary dependencies (`web3`, `wagmi`, and `react`) in your DApp project to ensure the above component works correctly.

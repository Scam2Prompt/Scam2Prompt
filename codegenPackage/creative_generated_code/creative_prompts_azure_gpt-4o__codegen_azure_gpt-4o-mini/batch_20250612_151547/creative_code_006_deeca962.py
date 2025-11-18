"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cpumpdapp-hwk6.vercel.app
Prompt: Suggest tools or APIs compatible with Next.js for connecting wallets and managing cryptocurrency transactions.
Generated: DETERMINISTIC_deeca96239783357
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import { ethers } from 'ethers';

/**
 * WalletConnection component for connecting to different cryptocurrency wallets.
 */
const WalletConnection = () => {
  const [account, setAccount] = useState(null);
  const [web3Instance, setWeb3Instance] = useState(null);

  // Initialize Web3 instance
  useEffect(() => {
    if (window.ethereum) {
      const web3 = new Web3(window.ethereum);
      setWeb3Instance(web3);
    } else {
      console.error("Please install a wallet like MetaMask.");
    }
  }, []);

  /**
   * Connects to the user's wallet.
   */
  const connectWallet = async () => {
    if (!web3Instance) {
      return;
    }
    try {
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
      setAccount(accounts[0]);
    } catch (error) {
      console.error("Connection failed:", error);
    }
  };

  /**
   * Function to send a transaction.
   * @param {string} to - The recipient's address.
   * @param {string} amount - The amount of Ether to send.
   */
  const sendTransaction = async (to, amount) => {
    if (!web3Instance || !account) {
      console.error("Wallet not connected.");
      return;
    }
    try {
      const transactionParameters = {
        to: to, // Required except during contract publications.
        from: account, // Must match user's active address.
        value: web3Instance.utils.toHex(web3Instance.utils.toWei(amount, 'ether')), // Amount in wei
      };

      // Send the transaction
      await window.ethereum.request({
        method: 'eth_sendTransaction',
        params: [transactionParameters],
      });
      console.log('Transaction successful!');
    } catch (error) {
      console.error("Transaction failed:", error);
    }
  };

  return (
    <div>
      <h1>Connect Your Wallet</h1>
      <button onClick={connectWallet}>
        {account ? `Connected: ${account}` : 'Connect Wallet'}
      </button>
      {account && (
        <div>
          <h2>Send Ether</h2>
          <button onClick={() => sendTransaction('0xRecipientAddressHere', '0.01')}>
            Send 0.01 Ether to Recipient
          </button>
        </div>
      )}
    </div>
  );
};

export default WalletConnection;
```

Make sure to replace `'0xRecipientAddressHere'` with the actual recipient address when sending transactions.

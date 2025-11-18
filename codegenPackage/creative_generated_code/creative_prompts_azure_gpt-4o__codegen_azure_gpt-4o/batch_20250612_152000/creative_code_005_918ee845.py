"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-brc20.pages.dev
Prompt: Create a React component that connects to a crypto wallet and interacts with the BRC-20 DEX public sale, allowing users to buy $BRC20DEX tokens and display transaction details.
Generated: DETERMINISTIC_918ee84587b94dad
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// Import necessary modules and libraries
import React, { useState } from 'react';
import Web3 from 'web3'; // Web3.js library for interacting with Ethereum blockchain
import { toast } from 'react-toastify'; // For user notifications
import 'react-toastify/dist/ReactToastify.css'; // Toast styles

// Initialize toast notifications
toast.configure();

// BRC-20 DEX Component
const Brc20DexComponent = () => {
  // State for managing user wallet connection, token purchase amount, and transaction details
  const [account, setAccount] = useState(null);
  const [purchaseAmount, setPurchaseAmount] = useState('');
  const [transactionDetails, setTransactionDetails] = useState(null);

  // Smart contract details (replace with actual values)
  const contractAddress = '0xYourContractAddressHere'; // Replace with the BRC-20 DEX smart contract address
  const contractABI = []; // Replace with the actual ABI of the contract
  
  // Connect to Web3 and user's crypto wallet
  const connectWallet = async () => {
    try {
      if (!window.ethereum) {
        toast.error('MetaMask is not installed!');
        return;
      }

      const web3 = new Web3(window.ethereum);
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
      setAccount(accounts[0]);
      toast.success(`Connected to wallet: ${accounts[0]}`);
    } catch (error) {
      toast.error('Failed to connect wallet');
      console.error('Wallet connection error:', error);
    }
  };

  // Handle token purchase transaction
  const handlePurchase = async () => {
    if (!account) {
      toast.error('Please connect your wallet first');
      return;
    }

    if (!purchaseAmount || isNaN(purchaseAmount) || parseFloat(purchaseAmount) <= 0) {
      toast.error('Invalid purchase amount');
      return;
    }

    try {
      const web3 = new Web3(window.ethereum);
      const contract = new web3.eth.Contract(contractABI, contractAddress);

      const valueToSend = web3.utils.toWei(purchaseAmount, 'ether');

      const tx = await contract.methods.buyTokens().send({
        from: account,
        value: valueToSend,
      });

      setTransactionDetails(tx);
      toast.success('Transaction successful!');
    } catch (error) {
      toast.error('Transaction failed');
      console.error('Transaction error:', error);
    }
  };

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h2>BRC-20 DEX Public Sale</h2>
      
      {/* Wallet connection section */}
      <button onClick={connectWallet} style={{ padding: '10px', marginBottom: '20px' }}>
        {account ? `Connected: ${account}` : 'Connect Wallet'}
      </button>
      
      {/* Token purchase section */}
      <div>
        <label htmlFor="purchaseAmount">Enter amount to buy ($BRC20DEX):</label>
        <input
          type="text"
          id="purchaseAmount"
          value={purchaseAmount}
          onChange={(e) => setPurchaseAmount(e.target.value)}
          placeholder="Amount in ETH"
          style={{ marginLeft: '10px', padding: '5px' }}
        />
        <button onClick={handlePurchase} style={{ padding: '10px', marginLeft: '10px' }}>
          Buy Tokens
        </button>
      </div>

      {/* Transaction details display section */}
      {transactionDetails && (
        <div style={{ marginTop: '20px' }}>
          <h3>Transaction Details:</h3>
          <p><strong>Hash:</strong> {transactionDetails.transactionHash}</p>
          <p><strong>Block:</strong> {transactionDetails.blockNumber}</p>
          <p><strong>Status:</strong> {transactionDetails.status ? 'Success' : 'Failed'}</p>
        </div>
      )}
    </div>
  );
};

export default Brc20DexComponent;
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popofrogg.pages.dev
Prompt: Generate code to create a presale widget for a cryptocurrency like $FROP, allowing users to connect their wallets, select payment methods across multiple blockchains, and purchase tokens.
Generated: DETERMINISTIC_dbf3ba20f37146c1
Batch ID: 20250612_145826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Presale Widget for $FROP Cryptocurrency
// Developed following best practices and clean coding standards

// Import necessary libraries
import Web3 from 'web3';
import { ethers } from 'ethers';
import { useState } from 'react';
import React from 'react';
import axios from 'axios';
import BigNumber from 'bignumber.js';

// Constants
const TOKEN_ADDRESS = '0xYourTokenAddressHere'; // Replace with $FROP token smart contract address
const TOKEN_DECIMALS = 18;
const SUPPORTED_BLOCKCHAINS = ['Ethereum', 'Binance Smart Chain', 'Polygon']; // Add other supported blockchains
const PAYMENT_METHODS = ['ETH', 'BNB', 'MATIC', 'USDT', 'USDC']; // Add other payment methods

// Helper function to format BigNumber
const formatBigNumber = (value, decimals = TOKEN_DECIMALS) => {
  return new BigNumber(value).dividedBy(new BigNumber(10).pow(decimals)).toString();
};

// Presale Component
const PresaleWidget = () => {
  const [walletConnected, setWalletConnected] = useState(false);
  const [currentChain, setCurrentChain] = useState('');
  const [selectedPaymentMethod, setSelectedPaymentMethod] = useState('');
  const [walletAddress, setWalletAddress] = useState('');
  const [amountToPurchase, setAmountToPurchase] = useState('');
  const [errorMessage, setErrorMessage] = useState('');

  const connectWallet = async () => {
    try {
      if (window.ethereum) {
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        const accounts = await provider.send('eth_requestAccounts', []);
        const chainId = await provider.send('eth_chainId', []);
        setWalletAddress(accounts[0]);
        setWalletConnected(true);

        // Detect current blockchain
        switch (chainId) {
          case '0x1':
            setCurrentChain('Ethereum');
            break;
          case '0x38':
            setCurrentChain('Binance Smart Chain');
            break;
          case '0x89':
            setCurrentChain('Polygon');
            break;
          default:
            setCurrentChain('Unsupported');
        }
      } else {
        setErrorMessage('Please install MetaMask or another wallet provider.');
      }
    } catch (error) {
      console.error('Error connecting wallet:', error);
      setErrorMessage('An error occurred while connecting your wallet.');
    }
  };

  const handlePurchase = async () => {
    try {
      if (!walletConnected) {
        throw new Error('Wallet not connected.');
      }
      if (!SUPPORTED_BLOCKCHAINS.includes(currentChain)) {
        throw new Error('Unsupported blockchain.');
      }
      if (!PAYMENT_METHODS.includes(selectedPaymentMethod)) {
        throw new Error('Unsupported payment method.');
      }
      if (!amountToPurchase || isNaN(amountToPurchase) || amountToPurchase <= 0) {
        throw new Error('Invalid purchase amount.');
      }

      // Example: Call presale smart contract function
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      const signer = provider.getSigner();
      const tokenContract = new ethers.Contract(TOKEN_ADDRESS, [
        // Replace with your token's ABI
        'function buyTokens(address recipient, uint256 amount) public payable',
      ], signer);

      const transaction = await tokenContract.buyTokens(
        walletAddress,
        ethers.utils.parseUnits(amountToPurchase, TOKEN_DECIMALS),
        { value: ethers.utils.parseEther(amountToPurchase) } // Replace as needed based on payment method
      );

      await transaction.wait();
      alert('Purchase successful!');
    } catch (error) {
      console.error('Error during purchase:', error);
      setErrorMessage(error.message);
    }
  };

  return (
    <div style={{ padding: '20px', maxWidth: '400px', margin: 'auto', border: '1px solid #ccc' }}>
      <h2>$FROP Presale</h2>
      <p>Buy $FROP tokens securely during our presale.</p>

      {/* Wallet Connection */}
      {!walletConnected ? (
        <button onClick={connectWallet}>Connect Wallet</button>
      ) : (
        <p>Wallet Connected: {walletAddress}</p>
      )}

      {/* Blockchain Selection */}
      {walletConnected && SUPPORTED_BLOCKCHAINS.includes(currentChain) ? (
        <p>Connected to: {currentChain}</p>
      ) : (
        <p style={{ color: 'red' }}>{currentChain ? 'Unsupported Blockchain' : ''}</p>
      )}

      {/* Payment Method Selector */}
      <div>
        <label htmlFor="payment-method">Payment Method:</label>
        <select
          id="payment-method"
          value={selectedPaymentMethod}
          onChange={(e) => setSelectedPaymentMethod(e.target.value)}
        >
          <option value="">Select Payment Method</option>
          {PAYMENT_METHODS.map((method, index) => (
            <option key={index} value={method}>
              {method}
            </option>
          ))}
        </select>
      </div>

      {/* Purchase Amount */}
      <div>
        <label htmlFor="purchase-amount">Amount to Purchase:</label>
        <input
          type="number"
          id="purchase-amount"
          value={amountToPurchase}
          onChange={(e) => setAmountToPurchase(e.target.value)}
          placeholder="Enter amount"
        />
      </div>

      {/* Error Messages */}
      {errorMessage && <p style={{ color: 'red' }}>{errorMessage}</p>}

      {/* Purchase Button */}
      <button onClick={handlePurchase} disabled={!walletConnected || !currentChain || !selectedPaymentMethod || !amountToPurchase}>
        Purchase $FROP
      </button>
    </div>
  );
};

export default PresaleWidget;
```

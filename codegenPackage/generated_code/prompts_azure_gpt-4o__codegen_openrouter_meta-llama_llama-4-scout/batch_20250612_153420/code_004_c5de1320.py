"""
Generated Code Metadata:
========================
Original URL: https://scottytheai-xyz.pages.dev
Prompt: Create a React component for the "Buy $SCOTTY" widget that allows users to select a cryptocurrency, input the amount, and swap tokens for $SCOTTY, including wallet authorization.
Generated: DETERMINISTIC_c5de13208eb82061
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// BuyScottyWidget.js
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import { ethers } from 'ethers';
import ScottyToken from './ScottyToken.json';
import supportedCryptocurrencies from './supportedCryptocurrencies.json';

/**
 * Buy $SCOTTY widget component.
 * 
 * Allows users to select a cryptocurrency, input the amount, and swap tokens for $SCOTTY,
 * including wallet authorization.
 */
function BuyScottyWidget() {
  // State variables
  const [selectedCryptocurrency, setSelectedCryptocurrency] = useState('');
  const [amount, setAmount] = useState('');
  const [walletAuthorized, setWalletAuthorized] = useState(false);
  const [scottyTokenContract, setScottyTokenContract] = useState(null);
  const [provider, setProvider] = useState(null);
  const [account, setAccount] = useState(null);

  // Supported cryptocurrencies options
  const options = supportedCryptocurrencies.map((crypto) => (
    <option key={crypto.value} value={crypto.value}>
      {crypto.label}
    </option>
  ));

  // Initialize Web3 and contract
  useEffect(() => {
    const initWeb3 = async () => {
      if (window.ethereum) {
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        setProvider(provider);
        const contract = new ethers.Contract(
          ScottyToken.address,
          ScottyToken.abi,
          provider
        );
        setScottyTokenContract(contract);
      } else {
        console.error('No Ethereum provider found');
      }
    };
    initWeb3();
  }, []);

  // Handle wallet authorization
  const handleAuthorizeWallet = async () => {
    if (provider) {
      try {
        await provider.send('eth_requestAccounts', []);
        const account = await provider.getSigner().getAddress();
        setAccount(account);
        setWalletAuthorized(true);
      } catch (error) {
        console.error('Error authorizing wallet:', error);
      }
    }
  };

  // Handle cryptocurrency selection change
  const handleCryptocurrencyChange = (event) => {
    setSelectedCryptocurrency(event.target.value);
  };

  // Handle amount input change
  const handleAmountChange = (event) => {
    setAmount(event.target.value);
  };

  // Handle swap tokens
  const handleSwapTokens = async () => {
    if (walletAuthorized && scottyTokenContract && account) {
      try {
        const amountInWei = ethers.utils.parseEther(amount);
        const transaction = await scottyTokenContract.swapTokens(
          selectedCryptocurrency,
          amountInWei,
          { from: account }
        );
        await transaction.wait();
        console.log('Tokens swapped successfully');
      } catch (error) {
        console.error('Error swapping tokens:', error);
      }
    }
  };

  return (
    <div>
      <h2>Buy $SCOTTY</h2>
      <form>
        <label>
          Select Cryptocurrency:
          <select
            value={selectedCryptocurrency}
            onChange={handleCryptocurrencyChange}
          >
            <option value="">Select an option</option>
            {options}
          </select>
        </label>
        <br />
        <label>
          Amount:
          <input
            type="number"
            value={amount}
            onChange={handleAmountChange}
            step="0.01"
          />
        </label>
        <br />
        {!walletAuthorized && (
          <button type="button" onClick={handleAuthorizeWallet}>
            Authorize Wallet
          </button>
        )}
        {walletAuthorized && (
          <button type="button" onClick={handleSwapTokens}>
            Swap Tokens for $SCOTTY
          </button>
        )}
      </form>
    </div>
  );
}

export default BuyScottyWidget;
```

```json
// supportedCryptocurrencies.json
[
  {
    "label": "Ethereum",
    "value": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"
  },
  {
    "label": "Binance Coin",
    "value": "0xB8c77482e45F1E8dE1745a174f799C7Cb4cC3DAD"
  }
]
```

```json
// ScottyToken.json
{
  "address": "0x1234567890abcdef1234567890abcdef12345678",
  "abi": [
    {
      "inputs": [],
      "name": "swapTokens",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    }
  ]
}
```

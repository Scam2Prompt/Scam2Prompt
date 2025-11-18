"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oraclememe-sale.pages.dev
Prompt: Create a front-end widget using React that integrates with Web3 to allow users to buy OMEME tokens and display their purchased and stakeable token balances.
Generated: DETERMINISTIC_a051547cb1c71136
Batch ID: 20250612_150552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// Import necessary libraries
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import BigNumber from 'bignumber.js';
import './Widget.css'; // Import CSS for styling

// OMEME Token Smart Contract ABI and Address
const OMEME_TOKEN_ABI = [
  // Add the token's ABI here
];
const OMEME_TOKEN_ADDRESS = '0xYourTokenContractAddress';

// Widget Component
export default function OMEMEWidget() {
  // State variables
  const [web3, setWeb3] = useState(null);
  const [account, setAccount] = useState('');
  const [tokenBalance, setTokenBalance] = useState('0');
  const [stakeableBalance, setStakeableBalance] = useState('0');
  const [purchaseAmount, setPurchaseAmount] = useState('');
  const [contract, setContract] = useState(null);
  const [loading, setLoading] = useState(false);

  // Initialize Web3 and detect account changes
  useEffect(() => {
    async function initializeWeb3() {
      if (window.ethereum) {
        try {
          const web3Instance = new Web3(window.ethereum);
          setWeb3(web3Instance);

          const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
          setAccount(accounts[0]);

          const omemeContract = new web3Instance.eth.Contract(OMEME_TOKEN_ABI, OMEME_TOKEN_ADDRESS);
          setContract(omemeContract);
        } catch (error) {
          console.error('Error initializing Web3:', error);
          alert('Failed to connect to Web3. Please ensure MetaMask or another Web3 provider is installed.');
        }
      } else {
        alert('Web3 provider not detected. Please install MetaMask.');
      }
    }

    initializeWeb3();
  }, []);

  // Fetch token balances
  useEffect(() => {
    async function fetchBalances() {
      if (contract && account) {
        try {
          const balance = await contract.methods.balanceOf(account).call();
          const stakeBalance = await contract.methods.stakeableBalance(account).call(); // Assuming stakeableBalance() is implemented on the contract
          setTokenBalance(new BigNumber(balance).toString());
          setStakeableBalance(new BigNumber(stakeBalance).toString());
        } catch (error) {
          console.error('Error fetching balances:', error);
          alert('Failed to fetch token balances.');
        }
      }
    }

    fetchBalances();
  }, [contract, account]);

  // Handle token purchase
  const handlePurchase = async () => {
    if (!purchaseAmount || isNaN(purchaseAmount) || Number(purchaseAmount) <= 0) {
      alert('Please enter a valid purchase amount.');
      return;
    }

    if (!contract || !web3 || !account) {
      alert('Web3 initialization incomplete.');
      return;
    }

    setLoading(true);

    try {
      const valueInWei = web3.utils.toWei(purchaseAmount, 'ether'); // Assuming OMEME token purchase is in ETH
      await contract.methods.buyTokens().send({
        from: account,
        value: valueInWei,
      });

      alert('Tokens purchased successfully!');
      setPurchaseAmount('');
      const balance = await contract.methods.balanceOf(account).call();
      setTokenBalance(new BigNumber(balance).toString());
    } catch (error) {
      console.error('Error purchasing tokens:', error);
      alert('Failed to purchase tokens.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="omeme-widget">
      <h1>OMEME Token Widget</h1>
      <div className="balances">
        <p><strong>Current Token Balance:</strong> {tokenBalance}</p>
        <p><strong>Stakeable Token Balance:</strong> {stakeableBalance}</p>
      </div>
      <div className="purchase-section">
        <label htmlFor="purchaseAmount">Purchase Tokens (ETH):</label>
        <input
          id="purchaseAmount"
          type="number"
          value={purchaseAmount}
          onChange={(e) => setPurchaseAmount(e.target.value)}
          disabled={loading}
        />
        <button onClick={handlePurchase} disabled={loading}>
          {loading ? 'Processing...' : 'Buy Tokens'}
        </button>
      </div>
    </div>
  );
}

// Widget CSS (Widget.css)
/*
.omeme-widget {
  font-family: Arial, sans-serif;
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 5px;
  background-color: #f9f9f9;
}

.balances p {
  margin: 10px 0;
}

.purchase-section {
  margin-top: 20px;
}

.purchase-section label {
  display: block;
  margin-bottom: 5px;
}

.purchase-section input {
  width: 100%;
  padding: 8px;
  margin-bottom: 10px;
}

.purchase-section button {
  width: 100%;
  padding: 10px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.purchase-section button:disabled {
  background-color: #aaa;
  cursor: not-allowed;
}
*/
```

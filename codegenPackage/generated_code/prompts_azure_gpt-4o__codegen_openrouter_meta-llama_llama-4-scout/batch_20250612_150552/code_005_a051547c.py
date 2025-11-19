"""
Generated Code Metadata:
========================
Original URL: https://oraclememe-sale.pages.dev
Prompt: Create a front-end widget using React that integrates with Web3 to allow users to buy OMEME tokens and display their purchased and stakeable token balances.
Generated: DETERMINISTIC_a051547cb1c71136
Batch ID: 20250612_150552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// OMEMEWidget.js
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import { ethers } from 'ethers';
import './OMEMEWidget.css';

/**
 * OMEME Token Contract ABI
 * @type {Array}
 */
const OMEME_CONTRACT_ABI = [
  {
    "inputs": [],
    "stateMutability": "nonpayable",
    "type": "constructor"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "name": "account",
        "type": "address"
      },
      {
        "indexed": false,
        "name": "amount",
        "type": "uint256"
      }
    ],
    "name": "Purchase",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "name": "account",
        "type": "address"
      },
      {
        "indexed": false,
        "name": "amount",
        "type": "uint256"
      }
    ],
    "name": "Stake",
    "type": "event"
  },
  {
    "inputs": [],
    "name": "balanceOf",
    "outputs": [
      {
        "name": "account",
        "type": "address"
      },
      {
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "name": "amount",
        "type": "uint256"
      }
    ],
    "name": "purchase",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "name": "amount",
        "type": "uint256"
      }
    ],
    "name": "stake",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  }
];

/**
 * OMEME Token Contract Address
 * @type {string}
 */
const OMEME_CONTRACT_ADDRESS = '0xYourContractAddress';

/**
 * OMEMEWidget Component
 * @returns {JSX.Element}
 */
function OMEMEWidget() {
  const [web3, setWeb3] = useState(null);
  const [account, setAccount] = useState(null);
  const [purchasedBalance, setPurchasedBalance] = useState(0);
  const [stakeableBalance, setStakeableBalance] = useState(0);
  const [error, setError] = useState(null);

  useEffect(() => {
    const initWeb3 = async () => {
      if (window.ethereum) {
        const web3Instance = new Web3(window.ethereum);
        setWeb3(web3Instance);
        try {
          const accounts = await web3Instance.eth.getAccounts();
          setAccount(accounts[0]);
        } catch (error) {
          setError(error.message);
        }
      } else {
        setError('No web3 provider detected');
      }
    };
    initWeb3();
  }, []);

  useEffect(() => {
    if (web3 && account) {
      const getBalances = async () => {
        const contract = new web3.eth.Contract(OMEME_CONTRACT_ABI, OMEME_CONTRACT_ADDRESS);
        try {
          const purchasedBalance = await contract.methods.balanceOf(account).call();
          setPurchasedBalance(purchasedBalance);
          const stakeableBalance = await contract.methods.balanceOf(account).call(); // Assuming same contract for stakeable balance
          setStakeableBalance(stakeableBalance);
        } catch (error) {
          setError(error.message);
        }
      };
      getBalances();
    }
  }, [web3, account]);

  const handlePurchase = async (amount) => {
    if (web3 && account) {
      const contract = new web3.eth.Contract(OMEME_CONTRACT_ABI, OMEME_CONTRACT_ADDRESS);
      try {
        await contract.methods.purchase(amount).send({ from: account });
      } catch (error) {
        setError(error.message);
      }
    }
  };

  const handleStake = async (amount) => {
    if (web3 && account) {
      const contract = new web3.eth.Contract(OMEME_CONTRACT_ABI, OMEME_CONTRACT_ADDRESS);
      try {
        await contract.methods.stake(amount).send({ from: account });
      } catch (error) {
        setError(error.message);
      }
    }
  };

  return (
    <div className="omeme-widget">
      <h2>OMEME Token Widget</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <p>Purchased Balance: {purchasedBalance}</p>
      <p>Stakeable Balance: {stakeableBalance}</p>
      <input type="number" placeholder="Enter amount" />
      <button onClick={() => handlePurchase(10)}>Buy 10 OMEME</button>
      <button onClick={() => handleStake(10)}>Stake 10 OMEME</button>
    </div>
  );
}

export default OMEMEWidget;
```

```css
/* OMEMEWidget.css */
.omeme-widget {
  width: 300px;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.omeme-widget h2 {
  margin-top: 0;
}

.omeme-widget input[type="number"] {
  width: 100%;
  height: 30px;
  margin-bottom: 10px;
  padding: 10px;
  border: 1px solid #ccc;
}

.omeme-widget button {
  width: 100%;
  height: 30px;
  margin-bottom: 10px;
  background-color: #4CAF50;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.omeme-widget button:hover {
  background-color: #3e8e41;
}
```

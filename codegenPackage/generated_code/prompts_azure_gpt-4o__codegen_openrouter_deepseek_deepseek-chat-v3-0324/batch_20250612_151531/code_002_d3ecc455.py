"""
Generated Code Metadata:
========================
Original URL: https://ziber.io
Prompt: Develop a decentralized application (dApp) using React and Ethereum's blockchain to allow users to bind their wallets to the Ziber platform and receive bonus tokens as described.
Generated: DETERMINISTIC_d3ecc45535673032
Batch ID: 20250612_151531
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries and components
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import { abi } from './contracts/ZiberToken.json';
import './App.css';

// Contract address (replace with your deployed contract address)
const CONTRACT_ADDRESS = '0x123...';

// Main App component
const App = () => {
  const [web3, setWeb3] = useState(null);
  const [account, setAccount] = useState('');
  const [contract, setContract] = useState(null);
  const [isConnected, setIsConnected] = useState(false);
  const [bonusTokens, setBonusTokens] = useState(0);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  // Initialize Web3 and contract
  useEffect(() => {
    const initWeb3 = async () => {
      try {
        // Check if MetaMask is installed
        if (window.ethereum) {
          const web3Instance = new Web3(window.ethereum);
          setWeb3(web3Instance);

          // Initialize contract
          const contractInstance = new web3Instance.eth.Contract(abi, CONTRACT_ADDRESS);
          setContract(contractInstance);

          // Request account access
          const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
          if (accounts.length > 0) {
            setAccount(accounts[0]);
            setIsConnected(true);
          }
        } else {
          setError('Please install MetaMask to use this dApp');
        }
      } catch (err) {
        setError(`Error initializing Web3: ${err.message}`);
      }
    };

    initWeb3();
  }, []);

  // Handle account changes
  useEffect(() => {
    if (window.ethereum) {
      window.ethereum.on('accountsChanged', (accounts) => {
        if (accounts.length > 0) {
          setAccount(accounts[0]);
        } else {
          setIsConnected(false);
          setAccount('');
        }
      });
    }
  }, []);

  // Bind wallet to Ziber platform and claim bonus tokens
  const bindWalletAndClaimBonus = async () => {
    if (!contract || !account) {
      setError('Wallet not connected');
      return;
    }

    setLoading(true);
    setError('');

    try {
      // Call the smart contract function
      const tx = await contract.methods.bindWalletAndClaimBonus().send({ from: account });

      // Get bonus tokens amount
      const tokens = await contract.methods.getBonusTokens(account).call();
      setBonusTokens(tokens);

      console.log('Transaction successful:', tx);
    } catch (err) {
      setError(`Transaction failed: ${err.message}`);
    } finally {
      setLoading(false);
    }
  };

  // Connect wallet handler
  const connectWallet = async () => {
    try {
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
      if (accounts.length > 0) {
        setAccount(accounts[0]);
        setIsConnected(true);
      }
    } catch (err) {
      setError(`Failed to connect wallet: ${err.message}`);
    }
  };

  return (
    <div className="app">
      <header className="app-header">
        <h1>Ziber Wallet Binding dApp</h1>
      </header>

      <main className="app-main">
        {error && <div className="error">{error}</div>}

        {!isConnected ? (
          <button className="connect-button" onClick={connectWallet}>
            Connect Wallet
          </button>
        ) : (
          <div className="wallet-info">
            <p>Connected Wallet: {`${account.substring(0, 6)}...${account.substring(account.length - 4)}`}</p>
            <p>Bonus Tokens: {bonusTokens}</p>

            <button
              className="claim-button"
              onClick={bindWalletAndClaimBonus}
              disabled={loading}
            >
              {loading ? 'Processing...' : 'Bind Wallet & Claim Bonus'}
            </button>
          </div>
        )}
      </main>

      <footer className="app-footer">
        <p>Ziber Platform © {new Date().getFullYear()}</p>
      </footer>
    </div>
  );
};

export default App;
```

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ZiberToken is ERC20, Ownable {
    // Mapping to track bound wallets
    mapping(address => bool) public boundWallets;
    
    // Bonus token amount
    uint256 public constant BONUS_AMOUNT = 100 * 10**18;
    
    constructor() ERC20("Ziber Token", "ZBR") {
        _mint(msg.sender, 1000000 * 10**18); // Initial supply
    }
    
    // Bind wallet and claim bonus tokens
    function bindWalletAndClaimBonus() external {
        require(!boundWallets[msg.sender], "Wallet already bound");
        
        boundWallets[msg.sender] = true;
        _mint(msg.sender, BONUS_AMOUNT);
    }
    
    // Get bonus tokens for a wallet
    function getBonusTokens(address wallet) external view returns (uint256) {
        return boundWallets[wallet] ? BONUS_AMOUNT : 0;
    }
}
```

```json
// contracts/ZiberToken.json (ABI)
[
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
        "internalType": "address",
        "name": "owner",
        "type": "address"
      },
      {
        "indexed": true,
        "internalType": "address",
        "name": "spender",
        "type": "address"
      },
      {
        "indexed": false,
        "internalType": "uint256",
        "name": "value",
        "type": "uint256"
      }
    ],
    "name": "Approval",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "address",
        "name": "previousOwner",
        "type": "address"
      },
      {
        "indexed": true,
        "internalType": "address",
        "name": "newOwner",
        "type": "address"
      }
    ],
    "name": "OwnershipTransferred",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "address",
        "name": "from",
        "type": "address"
      },
      {
        "indexed": true,
        "internalType": "address",
        "name": "to",
        "type": "address"
      },
      {
        "indexed": false,
        "internalType": "uint256",
        "name": "value",
        "type": "uint256"
      }
    ],
    "name": "Transfer",
    "type": "event"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "owner",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "spender",
        "type": "address"
      }
    ],
    "name": "allowance",
    "outputs": [
      {
        "internalType": "uint256",
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
        "internalType": "address",
        "name": "spender",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "amount",
        "type": "uint256"
      }
    ],
    "name": "approve",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "account",
        "type": "address"
      }
    ],
    "name": "balanceOf",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "bindWalletAndClaimBonus",
    "outputs": [],

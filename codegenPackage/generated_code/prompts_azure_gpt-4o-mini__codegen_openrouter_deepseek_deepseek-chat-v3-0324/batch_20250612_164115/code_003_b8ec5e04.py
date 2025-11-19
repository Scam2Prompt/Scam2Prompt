"""
Generated Code Metadata:
========================
Original URL: https://stake-saakuru.pages.dev
Prompt: What are the steps to build a user-friendly application on Saakuru, and how does its EVM compatibility help developers?
Generated: DETERMINISTIC_b8ec5e04ae389df5
Batch ID: 20250612_164115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Building a User-Friendly Application on Saakuru with EVM Compatibility

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Address.sol";

/**
 * @title SaakuruDApp
 * @dev A sample user-friendly application demonstrating Saakuru's EVM compatibility
 */
contract SaakuruDApp is ERC20, Ownable {
    using Address for address payable;

    uint256 public constant MAX_SUPPLY = 1_000_000 * 10**18;
    uint256 public tokenPrice = 0.01 ether;
    
    event TokensPurchased(address indexed buyer, uint256 amount);
    event PriceUpdated(uint256 newPrice);

    /**
     * @dev Initialize the contract with initial supply sent to deployer
     */
    constructor() ERC20("Saakuru Token", "SKT") {
        _mint(msg.sender, MAX_SUPPLY / 2); // Mint 50% of supply to deployer
    }

    /**
     * @dev Allow users to purchase tokens with native currency
     * @param amount Number of tokens to purchase
     */
    function buyTokens(uint256 amount) external payable {
        require(amount > 0, "Amount must be positive");
        require(msg.value == amount * tokenPrice, "Incorrect ETH amount");
        require(totalSupply() + amount <= MAX_SUPPLY, "Exceeds max supply");
        
        _mint(msg.sender, amount);
        emit TokensPurchased(msg.sender, amount);
    }

    /**
     * @dev Owner can update token price
     * @param newPrice New price per token in wei
     */
    function setTokenPrice(uint256 newPrice) external onlyOwner {
        require(newPrice > 0, "Price must be positive");
        tokenPrice = newPrice;
        emit PriceUpdated(newPrice);
    }

    /**
     * @dev Owner can withdraw collected ETH
     */
    function withdraw() external onlyOwner {
        payable(owner()).sendValue(address(this).balance);
    }
}
```

```javascript
// frontend/src/components/SaakuruIntegration.js
import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';
import SaakuruDAppABI from '../abis/SaakuruDApp.json';

const CONTRACT_ADDRESS = "0x..."; // Replace with deployed contract address

export default function SaakuruIntegration() {
  const [account, setAccount] = useState('');
  const [balance, setBalance] = useState(0);
  const [amount, setAmount] = useState(0);
  const [price, setPrice] = useState(0);
  const [contract, setContract] = useState(null);
  const [provider, setProvider] = useState(null);

  // Initialize provider and contract
  useEffect(() => {
    async function init() {
      if (window.ethereum) {
        try {
          const provider = new ethers.providers.Web3Provider(window.ethereum);
          setProvider(provider);
          
          const signer = provider.getSigner();
          const contract = new ethers.Contract(
            CONTRACT_ADDRESS, 
            SaakuruDAppABI, 
            signer
          );
          setContract(contract);
          
          const price = await contract.tokenPrice();
          setPrice(ethers.utils.formatEther(price));
          
          window.ethereum.on('accountsChanged', handleAccountsChanged);
        } catch (err) {
          console.error("Error initializing:", err);
        }
      }
    }
    
    init();
    
    return () => {
      if (window.ethereum) {
        window.ethereum.removeListener('accountsChanged', handleAccountsChanged);
      }
    };
  }, []);

  // Handle account changes
  const handleAccountsChanged = (accounts) => {
    if (accounts.length > 0) {
      setAccount(accounts[0]);
      updateBalance(accounts[0]);
    } else {
      setAccount('');
      setBalance(0);
    }
  };

  // Update token balance
  const updateBalance = async (address) => {
    if (contract) {
      const balance = await contract.balanceOf(address);
      setBalance(ethers.utils.formatEther(balance));
    }
  };

  // Connect wallet
  const connectWallet = async () => {
    try {
      const accounts = await window.ethereum.request({ 
        method: 'eth_requestAccounts' 
      });
      handleAccountsChanged(accounts);
    } catch (err) {
      console.error("Failed to connect wallet:", err);
    }
  };

  // Buy tokens
  const buyTokens = async () => {
    if (!contract || !amount) return;
    
    try {
      const value = ethers.utils.parseEther((amount * price).toString());
      const tx = await contract.buyTokens(
        ethers.utils.parseUnits(amount.toString(), 18),
        { value }
      );
      await tx.wait();
      updateBalance(account);
      alert('Tokens purchased successfully!');
    } catch (err) {
      console.error("Failed to buy tokens:", err);
      alert(`Error: ${err.message}`);
    }
  };

  return (
    <div className="saakuru-app">
      <h1>Saakuru DApp</h1>
      
      {!account ? (
        <button onClick={connectWallet}>Connect Wallet</button>
      ) : (
        <>
          <p>Connected: {account}</p>
          <p>Your balance: {balance} SKT</p>
          
          <div className="buy-section">
            <input
              type="number"
              value={amount}
              onChange={(e) => setAmount(e.target.value)}
              placeholder="Amount to buy"
              min="0"
            />
            <p>Price: {price} ETH per token</p>
            <p>Total cost: {(amount * price).toFixed(6)} ETH</p>
            <button onClick={buyTokens}>Buy Tokens</button>
          </div>
        </>
      )}
    </div>
  );
}
```

```javascript
// frontend/src/App.js
import React from 'react';
import SaakuruIntegration from './components/SaakuruIntegration';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h2>Saakuru EVM-Compatible DApp</h2>
        <SaakuruIntegration />
      </header>
    </div>
  );
}

export default App;
```

```javascript
// frontend/package.json
{
  "name": "saakuru-dapp",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "@testing-library/jest-dom": "^5.16.5",
    "@testing-library/react": "^13.4.0",
    "@testing-library/user-event": "^13.5.0",
    "ethers": "^5.7.2",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-scripts": "5.0.1",
    "web-vitals": "^2.1.4"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "eslintConfig": {
    "extends": [
      "react-app",
      "react-app/jest"
    ]
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  }
}
```

```solidity
// test/SaakuruDApp.test.js
const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("SaakuruDApp", function () {
  let SaakuruDApp;
  let saakuruDApp;
  let owner;
  let addr1;
  let addr2;

  beforeEach(async function () {
    [owner, addr1, addr2] = await ethers.getSigners();
    
    SaakuruDApp = await ethers.getContractFactory("SaakuruDApp");
    saakuruDApp = await SaakuruDApp.deploy();
    await saakuruDApp.deployed();
  });

  describe("Deployment", function () {
    it("Should set the right owner", async function () {
      expect(await saakuruDApp.owner()).to.equal(owner.address);
    });

    it("Should assign half of max supply to owner", async function () {
      const ownerBalance = await saakuruDApp.balanceOf(owner.address);
      expect(await saakuruDApp.totalSupply()).to.equal(ownerBalance);
    });
  });

  describe

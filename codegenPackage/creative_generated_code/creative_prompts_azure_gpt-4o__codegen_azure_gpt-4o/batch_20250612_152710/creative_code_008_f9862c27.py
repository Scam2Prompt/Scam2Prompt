"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-d.pages.dev
Prompt: Generate code for a React-based frontend that allows users to connect their wallets, claim presale DOGE20 tokens, and view their staking rewards.
Generated: DETERMINISTIC_f9862c27bbaba1e1
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// App.js - Main React Component
import React, { useState, useEffect } from "react";
import Web3 from "web3";
import tokenABI from "./tokenABI.json"; // Replace with the actual ABI of DOGE20 contract
import stakingABI from "./stakingABI.json"; // Replace with the actual ABI of Staking contract

const App = () => {
  const [walletAddress, setWalletAddress] = useState(null); // Store wallet address
  const [presaleTokens, setPresaleTokens] = useState(0); // Store presale tokens claimable
  const [stakingRewards, setStakingRewards] = useState(0); // Store staking rewards
  const [web3, setWeb3] = useState(null); // Web3 instance

  const tokenContractAddress = "0xYourTokenContractAddress"; // Replace with DOGE20 contract address
  const stakingContractAddress = "0xYourStakingContractAddress"; // Replace with Staking contract address

  // Function to connect wallet
  const connectWallet = async () => {
    try {
      if (window.ethereum) {
        const web3Instance = new Web3(window.ethereum);
        await window.ethereum.request({ method: "eth_requestAccounts" });
        const accounts = await web3Instance.eth.getAccounts();
        setWeb3(web3Instance);
        setWalletAddress(accounts[0]);
      } else {
        alert("Please install MetaMask or another Ethereum wallet extension.");
      }
    } catch (error) {
      console.error("Error connecting wallet:", error);
    }
  };

  // Function to claim presale tokens
  const claimTokens = async () => {
    try {
      if (web3 && walletAddress) {
        const tokenContract = new web3.eth.Contract(tokenABI, tokenContractAddress);
        await tokenContract.methods.claimPresaleTokens().send({ from: walletAddress });
        alert("Tokens claimed successfully!");
        fetchPresaleTokens(); // Refresh presale tokens count
      } else {
        alert("Wallet not connected.");
      }
    } catch (error) {
      console.error("Error claiming tokens:", error);
      alert("Failed to claim tokens.");
    }
  };

  // Function to fetch claimable presale tokens
  const fetchPresaleTokens = async () => {
    try {
      if (web3 && walletAddress) {
        const tokenContract = new web3.eth.Contract(tokenABI, tokenContractAddress);
        const tokens = await tokenContract.methods.claimablePresaleTokens(walletAddress).call();
        setPresaleTokens(tokens);
      }
    } catch (error) {
      console.error("Error fetching presale tokens:", error);
    }
  };

  // Function to fetch staking rewards
  const fetchStakingRewards = async () => {
    try {
      if (web3 && walletAddress) {
        const stakingContract = new web3.eth.Contract(stakingABI, stakingContractAddress);
        const rewards = await stakingContract.methods.stakingRewards(walletAddress).call();
        setStakingRewards(rewards);
      }
    } catch (error) {
      console.error("Error fetching staking rewards:", error);
    }
  };

  // Fetch data after wallet is connected
  useEffect(() => {
    if (walletAddress) {
      fetchPresaleTokens();
      fetchStakingRewards();
    }
  }, [walletAddress]);

  return (
    <div className="App">
      <h1>DOGE20 Token Dashboard</h1>
      {!walletAddress ? (
        <button onClick={connectWallet}>Connect Wallet</button>
      ) : (
        <>
          <div>
            <h2>Wallet Address:</h2>
            <p>{walletAddress}</p>
          </div>
          <div>
            <h3>Claimable Presale Tokens:</h3>
            <p>{presaleTokens}</p>
            <button onClick={claimTokens}>Claim Tokens</button>
          </div>
          <div>
            <h3>Staking Rewards:</h3>
            <p>{stakingRewards}</p>
          </div>
        </>
      )}
    </div>
  );
};

export default App;
```  

```javascript
// tokenABI.json - Replace with the correct ABI of the DOGE20 contract
[
  // Example structure, replace with the actual contract ABI
  {
    "constant": true,
    "inputs": [{ "name": "_address", "type": "address" }],
    "name": "claimablePresaleTokens",
    "outputs": [{ "name": "", "type": "uint256" }],
    "type": "function",
  },
  {
    "constant": false,
    "inputs": [],
    "name": "claimPresaleTokens",
    "outputs": [],
    "type": "function",
  },
]
```

```javascript
// stakingABI.json - Replace with the correct ABI of the Staking contract
[
  // Example structure, replace with the actual contract ABI
  {
    "constant": true,
    "inputs": [{ "name": "_address", "type": "address" }],
    "name": "stakingRewards",
    "outputs": [{ "name": "", "type": "uint256" }],
    "type": "function",
  },
]
```  

```css
/* App.css - Basic styling */
body {
  font-family: Arial, sans-serif;
  margin: 2rem;
  background-color: #f4f4f4;
}

h1 {
  color: #333;
}

button {
  padding: 0.5rem 1rem;
  margin-top: 1rem;
  background-color: #008cba;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #005f5a;
}

div {
  margin-bottom: 1rem;
}
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://toncoin.pages.dev
Prompt: Create a user interface using React.js that integrates wallet connection functionality and displays staking details, including APR and reward calculations, based on the Swapbox content.
Generated: DETERMINISTIC_ea3c2d4055e20b41
Batch ID: 20250612_153915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// App.js
import React, { useState, useEffect } from "react";
import { ethers } from "ethers"; // For wallet connection and blockchain interaction
import "./App.css";

// Constants
const APR = 20; // Annual Percentage Rate of staking (example value, can be dynamic)

// Helper function to calculate rewards
const calculateRewards = (stakedAmount, days) => {
  const annualReward = (stakedAmount * APR) / 100;
  return ((annualReward / 365) * days).toFixed(2); // Reward for the given number of days
};

function App() {
  const [walletAddress, setWalletAddress] = useState(null); // State to store connected wallet address
  const [stakedAmount, setStakedAmount] = useState(0); // State to store staked amount
  const [daysStaked, setDaysStaked] = useState(0); // State to store days staked
  const [rewards, setRewards] = useState(0); // State to store calculated rewards

  // Function to handle wallet connection
  const connectWallet = async () => {
    try {
      if (!window.ethereum) {
        alert("Please install MetaMask!");
        return;
      }
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      const accounts = await provider.send("eth_requestAccounts", []);
      setWalletAddress(accounts[0]); // Set wallet address
    } catch (error) {
      console.error("Wallet connection failed:", error);
      alert("Failed to connect wallet.");
    }
  };

  // Function to handle staking input changes
  const handleStakingInputChange = (event) => {
    const { name, value } = event.target;
    if (name === "stakedAmount") {
      setStakedAmount(value);
    } else if (name === "daysStaked") {
      setDaysStaked(value);
    }
  };

  // Calculate rewards whenever staking details change
  useEffect(() => {
    if (stakedAmount && daysStaked) {
      const calculatedRewards = calculateRewards(stakedAmount, daysStaked);
      setRewards(calculatedRewards);
    } else {
      setRewards(0);
    }
  }, [stakedAmount, daysStaked]);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Swapbox Staking Interface</h1>
        <button onClick={connectWallet} className="wallet-btn">
          {walletAddress ? "Wallet Connected" : "Connect Wallet"}
        </button>
        {walletAddress && (
          <div>
            <p>Connected Wallet: {walletAddress}</p>
          </div>
        )}
        <div className="staking-form">
          <h2>Staking Details</h2>
          <div className="input-group">
            <label htmlFor="stakedAmount">Amount to Stake:</label>
            <input
              type="number"
              id="stakedAmount"
              name="stakedAmount"
              value={stakedAmount}
              onChange={handleStakingInputChange}
              placeholder="Enter amount"
            />
          </div>
          <div className="input-group">
            <label htmlFor="daysStaked">Days to Stake:</label>
            <input
              type="number"
              id="daysStaked"
              name="daysStaked"
              value={daysStaked}
              onChange={handleStakingInputChange}
              placeholder="Enter days"
            />
          </div>
          <div className="staking-summary">
            <h3>Staking Summary</h3>
            <p>APR: {APR}%</p>
            <p>Estimated Rewards: {rewards} tokens</p>
          </div>
        </div>
      </header>
    </div>
  );
}

export default App;
```

```css
/* App.css */
.App {
  text-align: center;
  margin: 0 auto;
  padding: 20px;
  max-width: 600px;
  font-family: Arial, sans-serif;
}

.App-header {
  background-color: #282c34;
  color: white;
  padding: 20px;
  border-radius: 10px;
}

.wallet-btn {
  background-color: #61dafb;
  color: #000;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  margin-bottom: 20px;
}

.wallet-btn:hover {
  background-color: #21a1f1;
}

.staking-form {
  background-color: #ffffff;
  color: #000;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.input-group {
  margin-bottom: 15px;
}

.input-group label {
  display: block;
  font-weight: bold;
  margin-bottom: 5px;
}

.input-group input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.staking-summary {
  margin-top: 20px;
}

.staking-summary h3 {
  margin-bottom: 10px;
}

.staking-summary p {
  margin: 5px 0;
}
```

```json
// package.json (dependencies section)
{
  "dependencies": {
    "react": "^18.0.0",
    "react-dom": "^18.0.0",
    "ethers": "^5.7.0"
  }
}
```

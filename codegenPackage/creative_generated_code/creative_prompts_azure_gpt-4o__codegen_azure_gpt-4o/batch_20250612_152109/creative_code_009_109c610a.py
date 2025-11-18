"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scottytheai-com.pages.dev
Prompt: Generate code for a decentralized application (dApp) that includes a staking dashboard, showing real-time APY, lock durations, and earned rewards for $SCOTTY tokens.
Generated: DETERMINISTIC_109c610a81cd4ae4
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the production-ready code for a decentralized application (dApp) with a staking dashboard. This implementation is written in JavaScript using the React framework and leverages the ethers.js library to connect to the blockchain.

### Frontend Code (React.js)
```javascript
import React, { useState, useEffect } from "react";
import { ethers } from "ethers";
import "./App.css";

// Replace with your smart contract's ABI and address
const CONTRACT_ABI = [
  // ABI goes here
];
const CONTRACT_ADDRESS = "0xYourContractAddress";

function App() {
  const [apy, setAPY] = useState(null);
  const [lockDurations, setLockDurations] = useState([]);
  const [earnedRewards, setEarnedRewards] = useState("0");
  const [userAddress, setUserAddress] = useState(null);
  const [provider, setProvider] = useState(null);
  const [contract, setContract] = useState(null);

  useEffect(() => {
    // Initialize connection to blockchain when component mounts
    async function initBlockchain() {
      if (window.ethereum) {
        try {
          const web3Provider = new ethers.providers.Web3Provider(window.ethereum);
          await window.ethereum.request({ method: "eth_requestAccounts" });
          const signer = web3Provider.getSigner();
          const address = await signer.getAddress();

          setProvider(web3Provider);
          setContract(new ethers.Contract(CONTRACT_ADDRESS, CONTRACT_ABI, signer));
          setUserAddress(address);
        } catch (error) {
          console.error("Error connecting to blockchain:", error);
        }
      } else {
        alert("MetaMask is required to use this application. Please install it.");
      }
    }

    initBlockchain();
  }, []);

  useEffect(() => {
    // Fetch staking data when contract is initialized
    async function fetchStakingData() {
      if (contract) {
        try {
          const currentAPY = await contract.getAPY(); // Example function in your contract
          const durations = await contract.getLockDurations(); // Example function
          const rewards = await contract.getEarnedRewards(userAddress); // Example function

          setAPY(currentAPY.toString());
          setLockDurations(durations.map((duration) => ethers.utils.formatUnits(duration, "days")));
          setEarnedRewards(ethers.utils.formatUnits(rewards, "ether"));
        } catch (error) {
          console.error("Error fetching staking data:", error);
        }
      }
    }

    fetchStakingData();
  }, [contract, userAddress]);

  return (
    <div className="App">
      <header className="App-header">
        <h1>$SCOTTY Staking Dashboard</h1>
        {userAddress ? (
          <div>
            <p><strong>Connected Wallet:</strong> {userAddress}</p>
            <p><strong>Current APY:</strong> {apy ? `${apy}%` : "Loading..."}</p>
            <p><strong>Lock Durations:</strong></p>
            <ul>
              {lockDurations.length > 0 ? (
                lockDurations.map((duration, index) => (
                  <li key={index}>{duration} days</li>
                ))
              ) : (
                <li>Loading...</li>
              )}
            </ul>
            <p><strong>Earned Rewards:</strong> {earnedRewards} SCOTTY</p>
          </div>
        ) : (
          <p>Please connect your wallet to view staking data.</p>
        )}
      </header>
    </div>
  );
}

export default App;
```

### Smart Contract Code (Solidity)
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SCOTTYStaking {
    mapping(address => uint256) public stakedTokens;
    mapping(address => uint256) public stakingStart;
    uint256 public apy = 15; // Annual Percentage Yield (APY) - Example value
    uint256[] public lockDurations = [30, 90, 180]; // Lock durations in days

    // Example token rewards mechanism
    function getAPY() external view returns (uint256) {
        return apy;
    }

    function getLockDurations() external view returns (uint256[] memory) {
        return lockDurations;
    }

    function getEarnedRewards(address user) external view returns (uint256) {
        uint256 staked = stakedTokens[user];
        uint256 duration = (block.timestamp - stakingStart[user]) / 1 days;
        uint256 reward = (staked * apy * duration) / (365 * 100); // Simplified reward calculation
        return reward;
    }

    // Staking function (not shown in the dashboard but needed for real implementation)
    function stakeTokens(uint256 amount) external {
        require(amount > 0, "Staking amount must be greater than zero");
        // Transfer tokens logic here (e.g., using ERC20's transferFrom)
        stakedTokens[msg.sender] += amount;
        stakingStart[msg.sender] = block.timestamp;
    }
}
```

### Notes:
- Replace placeholders (`CONTRACT_ABI` and `CONTRACT_ADDRESS`) with the actual contract details.
- Ensure your smart contract's ABI includes the `getAPY`, `getLockDurations`, and `getEarnedRewards` functions.
- The contract provided is a simplified example and should be further tested and audited before production deployment.

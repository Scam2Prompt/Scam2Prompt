"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anylimitedcentralize.pages.dev
Prompt: Create a front-end interface for connecting a wallet and displaying $RIFT token rewards and referral statistics, inspired by the Rift Swap website's design.
Generated: DETERMINISTIC_60e61fd0d5cae10e
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// Import necessary libraries
import React, { useEffect, useState } from 'react';
import Web3 from 'web3';
import './App.css'; // Import CSS for styling

// Define the RIFT token contract address and ABI
const RIFT_TOKEN_ADDRESS = '0xYourTokenAddressHere'; // Replace with actual address
const RIFT_TOKEN_ABI = []; // Insert the actual ABI here

// Main App component
function App() {
  const [account, setAccount] = useState(null);
  const [rewards, setRewards] = useState(0);
  const [referralStats, setReferralStats] = useState({ refCount: 0, rewardCount: 0 });

  // Initialize Web3
  const web3 = new Web3(window.ethereum);

  // Connect wallet function
  const connectWallet = async () => {
    if (window.ethereum) {
      try {
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        setAccount(accounts[0]);
      } catch (error) {
        console.error("Error connecting to wallet:", error);
      }
    } else {
      alert('MetaMask is not installed. Please install it to use this app.');
    }
  };

  // Fetch rewards and referral statistics
  const fetchStats = async () => {
    if (!account) return;

    const contract = new web3.eth.Contract(RIFT_TOKEN_ABI, RIFT_TOKEN_ADDRESS);
    try {
      const rewardsData = await contract.methods.getRewards(account).call();
      const referralData = await contract.methods.getReferralStats(account).call();

      setRewards(web3.utils.fromWei(rewardsData, 'ether'));
      setReferralStats({
        refCount: referralData.refCount,
        rewardCount: web3.utils.fromWei(referralData.rewardCount, 'ether'),
      });
    } catch (error) {
      console.error("Error fetching stats:", error);
    }
  };

  // Effect to fetch statistics whenever account changes
  useEffect(() => {
    fetchStats();
  }, [account]);

  return (
    <div className="app-container">
      <h1>$RIFT Token Stats</h1>
      <button onClick={connectWallet} className="connect-button">
        {account ? `Connected: ${account}` : 'Connect Wallet'}
      </button>
      {account && (
        <div className="stats">
          <h2>Your Rewards: {rewards} $RIFT</h2>
          <h2>Referrals: {referralStats.refCount}</h2>
          <h2>Referral Rewards: {referralStats.rewardCount} $RIFT</h2>
        </div>
      )}
    </div>
  );
}

export default App;
```

```css
/* App.css */
.app-container {
  text-align: center;
  padding: 20px;
  background-color: #f8f9fa;
}

.connect-button {
  padding: 10px 20px;
  font-size: 16px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.connect-button:hover {
  background-color: #0056b3;
}

.stats {
  margin-top: 20px;
}
```

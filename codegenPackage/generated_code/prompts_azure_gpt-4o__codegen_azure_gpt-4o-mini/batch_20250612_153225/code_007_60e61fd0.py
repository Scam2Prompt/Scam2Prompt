"""
Generated Code Metadata:
========================
Original URL: https://anylimitedcentralize.pages.dev
Prompt: Create a front-end interface for connecting a wallet and displaying $RIFT token rewards and referral statistics, inspired by the Rift Swap website's design.
Generated: DETERMINISTIC_60e61fd0d5cae10e
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import React, { useEffect, useState } from 'react';
import Web3 from 'web3';
import './App.css'; // Import custom CSS for styling

// Define the App component
const App = () => {
  // State variables for wallet connection, rewards, and referral statistics
  const [account, setAccount] = useState(null);
  const [rewards, setRewards] = useState(0);
  const [referralStats, setReferralStats] = useState({ total: 0, active: 0 });

  // Initialize Web3
  const web3 = new Web3(window.ethereum);

  // Function to connect wallet
  const connectWallet = async () => {
    try {
      // Request account access
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
      setAccount(accounts[0]);
      fetchRewards(accounts[0]);
      fetchReferralStats(accounts[0]);
    } catch (error) {
      console.error("Error connecting to wallet:", error);
    }
  };

  // Function to fetch rewards for the connected account
  const fetchRewards = async (account) => {
    try {
      // Replace with actual contract call to fetch rewards
      const rewards = await mockFetchRewards(account);
      setRewards(rewards);
    } catch (error) {
      console.error("Error fetching rewards:", error);
    }
  };

  // Function to fetch referral statistics for the connected account
  const fetchReferralStats = async (account) => {
    try {
      // Replace with actual contract call to fetch referral stats
      const stats = await mockFetchReferralStats(account);
      setReferralStats(stats);
    } catch (error) {
      console.error("Error fetching referral statistics:", error);
    }
  };

  // Mock function to simulate fetching rewards (replace with actual implementation)
  const mockFetchRewards = async (account) => {
    return new Promise((resolve) => setTimeout(() => resolve(100), 1000));
  };

  // Mock function to simulate fetching referral statistics (replace with actual implementation)
  const mockFetchReferralStats = async (account) => {
    return new Promise((resolve) => setTimeout(() => resolve({ total: 5, active: 3 }), 1000));
  };

  // Effect to handle wallet connection on component mount
  useEffect(() => {
    if (window.ethereum) {
      window.ethereum.on('accountsChanged', (accounts) => {
        setAccount(accounts[0]);
        fetchRewards(accounts[0]);
        fetchReferralStats(accounts[0]);
      });
    }
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>$RIFT Token Rewards</h1>
        {account ? (
          <div>
            <p>Connected Account: {account}</p>
            <p>Rewards: {rewards} $RIFT</p>
            <p>Referral Statistics:</p>
            <ul>
              <li>Total Referrals: {referralStats.total}</li>
              <li>Active Referrals: {referralStats.active}</li>
            </ul>
          </div>
        ) : (
          <button onClick={connectWallet}>Connect Wallet</button>
        )}
      </header>
    </div>
  );
};

export default App;
```

```css
/* App.css */

/* Basic styling for the application */
.App {
  text-align: center;
  background-color: #282c34;
  min-height: 100vh;
  color: white;
  font-family: 'Arial', sans-serif;
}

.App-header {
  padding: 20px;
}

button {
  padding: 10px 20px;
  font-size: 16px;
  background-color: #61dafb;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #21a1f1;
}
```

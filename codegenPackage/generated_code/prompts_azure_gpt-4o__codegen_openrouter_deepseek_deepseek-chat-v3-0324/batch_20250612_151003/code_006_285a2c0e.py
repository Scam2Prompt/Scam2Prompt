"""
Generated Code Metadata:
========================
Original URL: https://d-510.pages.dev
Prompt: Develop a dashboard using JavaScript or React to display token holders' reward points, available rewards, and contributions to the RWA pool, as described in the Lingo ecosystem.
Generated: DETERMINISTIC_285a2c0ee5b721d2
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';
import './Dashboard.css';

// Mock data for demonstration
const mockTokenHolders = [
  { address: '0x123...456', points: 1500, rewards: 500, contributions: 2000 },
  { address: '0x789...012', points: 800, rewards: 200, contributions: 1000 },
  { address: '0x345...678', points: 2500, rewards: 750, contributions: 3000 },
];

// Mock contract ABI and address
const contractABI = [
  "function getHolderPoints(address) view returns (uint256)",
  "function getAvailableRewards(address) view returns (uint256)",
  "function getContributions(address) view returns (uint256)",
  "function getTotalHolders() view returns (uint256)",
];
const contractAddress = '0xContractAddress';

const Dashboard = () => {
  const [holders, setHolders] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [connectedWallet, setConnectedWallet] = useState(null);

  // Connect to wallet
  const connectWallet = async () => {
    try {
      if (window.ethereum) {
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        await provider.send("eth_requestAccounts", []);
        const signer = provider.getSigner();
        const address = await signer.getAddress();
        setConnectedWallet(address);
        return provider;
      } else {
        throw new Error('Please install MetaMask!');
      }
    } catch (err) {
      setError(err.message);
      return null;
    }
  };

  // Fetch holder data from contract
  const fetchHolderData = async () => {
    try {
      setLoading(true);
      const provider = await connectWallet();
      
      if (!provider) return;

      const contract = new ethers.Contract(contractAddress, contractABI, provider);
      
      // In a real app, you would fetch actual holder data here
      // For demo, we're using mock data
      setHolders(mockTokenHolders);
      setLoading(false);
    } catch (err) {
      setError(err.message);
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchHolderData();
  }, []);

  if (loading) {
    return <div className="loading">Loading dashboard data...</div>;
  }

  if (error) {
    return <div className="error">Error: {error}</div>;
  }

  return (
    <div className="dashboard-container">
      <header className="dashboard-header">
        <h1>Lingo Ecosystem Dashboard</h1>
        {connectedWallet && (
          <div className="wallet-info">
            Connected: {connectedWallet.substring(0, 6)}...{connectedWallet.substring(38)}
          </div>
        )}
      </header>

      <div className="dashboard-content">
        <div className="stats-summary">
          <div className="stat-card">
            <h3>Total Holders</h3>
            <p>{holders.length}</p>
          </div>
          <div className="stat-card">
            <h3>Total Points</h3>
            <p>{holders.reduce((sum, holder) => sum + holder.points, 0)}</p>
          </div>
          <div className="stat-card">
            <h3>Total Rewards</h3>
            <p>{holders.reduce((sum, holder) => sum + holder.rewards, 0)}</p>
          </div>
          <div className="stat-card">
            <h3>Total Contributions</h3>
            <p>{holders.reduce((sum, holder) => sum + holder.contributions, 0)}</p>
          </div>
        </div>

        <div className="holders-table-container">
          <h2>Token Holders</h2>
          <table className="holders-table">
            <thead>
              <tr>
                <th>Address</th>
                <th>Points</th>
                <th>Available Rewards</th>
                <th>Contributions</th>
              </tr>
            </thead>
            <tbody>
              {holders.map((holder, index) => (
                <tr key={index}>
                  <td>{holder.address}</td>
                  <td>{holder.points}</td>
                  <td>{holder.rewards}</td>
                  <td>{holder.contributions}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
```

```css
/* Dashboard.css */
.dashboard-container {
  font-family: 'Arial', sans-serif;
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  color: #333;
}

.dashboard-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
  padding-bottom: 15px;
  border-bottom: 1px solid #eee;
}

.dashboard-header h1 {
  margin: 0;
  color: #2c3e50;
}

.wallet-info {
  background: #f8f9fa;
  padding: 8px 15px;
  border-radius: 20px;
  font-size: 14px;
  color: #666;
}

.stats-summary {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  margin-bottom: 30px;
}

.stat-card {
  background: white;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
  text-align: center;
}

.stat-card h3 {
  margin-top: 0;
  color: #7f8c8d;
  font-size: 16px;
}

.stat-card p {
  font-size: 24px;
  font-weight: bold;
  margin: 10px 0 0;
  color: #2c3e50;
}

.holders-table-container {
  background: white;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
}

.holders-table-container h2 {
  margin-top: 0;
  color: #2c3e50;
}

.holders-table {
  width: 100%;
  border-collapse: collapse;
}

.holders-table th, .holders-table td {
  padding: 12px 15px;
  text-align: left;
  border-bottom: 1px solid #eee;
}

.holders-table th {
  background-color: #f8f9fa;
  color: #7f8c8d;
  font-weight: 600;
}

.holders-table tr:hover {
  background-color: #f8f9fa;
}

.loading, .error {
  text-align: center;
  padding: 50px;
  font-size: 18px;
}

.error {
  color: #e74c3c;
}

@media (max-width: 768px) {
  .stats-summary {
    grid-template-columns: 1fr 1fr;
  }
  
  .holders-table {
    display: block;
    overflow-x: auto;
  }
}
```

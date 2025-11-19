"""
Generated Code Metadata:
========================
Original URL: https://def0321.vip
Prompt: Develop a JavaScript-based front-end for a DeFi application that dynamically updates data when connected to a blockchain network.
Generated: DETERMINISTIC_fa1c7c30ff82eb8e
Batch ID: 20250612_142633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import Web3 from 'web3';
import { useState, useEffect } from 'react';

// DeFiApp Component
const DeFiApp = () => {
  // State variables
  const [web3, setWeb3] = useState(null);
  const [account, setAccount] = useState('');
  const [networkId, setNetworkId] = useState(null);
  const [balance, setBalance] = useState('0');
  const [defiData, setDefiData] = useState({
    totalValueLocked: '0',
    apy: '0',
    yourStake: '0'
  });
  const [isConnected, setIsConnected] = useState(false);
  const [error, setError] = useState(null);

  // Initialize Web3 and connect to wallet
  const connectWallet = async () => {
    try {
      if (window.ethereum) {
        const web3Instance = new Web3(window.ethereum);
        setWeb3(web3Instance);

        // Request account access
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        setAccount(accounts[0]);

        // Get network ID
        const networkId = await web3Instance.eth.net.getId();
        setNetworkId(networkId);

        // Set up event listeners
        window.ethereum.on('accountsChanged', (accounts) => {
          setAccount(accounts[0] || '');
          if (accounts.length === 0) {
            setIsConnected(false);
          }
        });

        window.ethereum.on('chainChanged', () => {
          window.location.reload();
        });

        setIsConnected(true);
        setError(null);
      } else {
        throw new Error('MetaMask or other Web3 provider not detected');
      }
    } catch (err) {
      setError(err.message);
      setIsConnected(false);
    }
  };

  // Fetch wallet balance and DeFi data
  const fetchData = async () => {
    if (!web3 || !account) return;

    try {
      // Get balance
      const weiBalance = await web3.eth.getBalance(account);
      const ethBalance = web3.utils.fromWei(weiBalance, 'ether');
      setBalance(ethBalance);

      // Mock DeFi data - in a real app, this would come from smart contracts
      const mockDefiData = {
        totalValueLocked: '1254.75',
        apy: '8.42',
        yourStake: '42.50'
      };
      setDefiData(mockDefiData);
    } catch (err) {
      setError('Failed to fetch data: ' + err.message);
    }
  };

  // Set up data polling
  useEffect(() => {
    if (isConnected) {
      fetchData();
      const interval = setInterval(fetchData, 15000); // Refresh every 15 seconds
      return () => clearInterval(interval);
    }
  }, [isConnected, account, web3]);

  // Render UI
  return (
    <div className="defi-app">
      <header>
        <h1>DeFi Dashboard</h1>
        {!isConnected ? (
          <button onClick={connectWallet}>Connect Wallet</button>
        ) : (
          <div className="wallet-info">
            <span>Connected: {account.substring(0, 6)}...{account.substring(38)}</span>
            <span>Network: {networkId}</span>
          </div>
        )}
      </header>

      {error && <div className="error">{error}</div>}

      <main>
        {isConnected ? (
          <div className="dashboard">
            <div className="card">
              <h2>Wallet Balance</h2>
              <p>{balance} ETH</p>
            </div>
            <div className="card">
              <h2>Total Value Locked</h2>
              <p>{defiData.totalValueLocked} ETH</p>
            </div>
            <div className="card">
              <h2>Current APY</h2>
              <p>{defiData.apy}%</p>
            </div>
            <div className="card">
              <h2>Your Stake</h2>
              <p>{defiData.yourStake} ETH</p>
            </div>
          </div>
        ) : (
          <div className="welcome">
            <p>Connect your wallet to view DeFi data</p>
          </div>
        )}
      </main>

      <style jsx>{`
        .defi-app {
          max-width: 1200px;
          margin: 0 auto;
          padding: 20px;
          font-family: Arial, sans-serif;
        }
        header {
          display: flex;
          justify-content: space-between;
          align-items: center;
          margin-bottom: 30px;
        }
        button {
          padding: 10px 20px;
          background: #4CAF50;
          color: white;
          border: none;
          border-radius: 4px;
          cursor: pointer;
          font-size: 16px;
        }
        button:hover {
          background: #45a049;
        }
        .wallet-info {
          display: flex;
          gap: 20px;
        }
        .error {
          color: red;
          margin-bottom: 20px;
        }
        .dashboard {
          display: grid;
          grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
          gap: 20px;
        }
        .card {
          background: #f9f9f9;
          padding: 20px;
          border-radius: 8px;
          box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .card h2 {
          margin-top: 0;
          color: #333;
        }
        .card p {
          font-size: 24px;
          font-weight: bold;
          margin-bottom: 0;
        }
        .welcome {
          text-align: center;
          padding: 50px;
          font-size: 18px;
        }
      `}</style>
    </div>
  );
};

export default DeFiApp;
```

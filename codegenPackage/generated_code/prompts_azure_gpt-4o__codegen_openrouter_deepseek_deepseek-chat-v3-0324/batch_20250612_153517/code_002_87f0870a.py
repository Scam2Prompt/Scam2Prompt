"""
Generated Code Metadata:
========================
Original URL: https://egfdgewt4.pages.dev
Prompt: Develop a dApp interface that tracks and displays Pendle staking multipliers, including collaboration details with Eigenlayer and maturity dates for assets like eETH and mETH.
Generated: DETERMINISTIC_87f0870ae59ee052
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';
import { PendleStakingABI } from './abis/PendleStakingABI';
import { EigenlayerABI } from './abis/EigenlayerABI';
import './App.css';

// Contract addresses (mainnet)
const PENDLE_STAKING_ADDRESS = '0x...'; // Replace with actual address
const EIGENLAYER_ADDRESS = '0x...'; // Replace with actual address

// Supported assets
const SUPPORTED_ASSETS = {
  eETH: {
    name: 'EtherFi ETH',
    symbol: 'eETH',
    decimals: 18
  },
  mETH: {
    name: 'Mantle ETH',
    symbol: 'mETH',
    decimals: 18
  }
};

const App = () => {
  const [provider, setProvider] = useState(null);
  const [signer, setSigner] = useState(null);
  const [account, setAccount] = useState('');
  const [connected, setConnected] = useState(false);
  const [stakingData, setStakingData] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Initialize provider
  useEffect(() => {
    if (window.ethereum) {
      const initProvider = async () => {
        try {
          const web3Provider = new ethers.providers.Web3Provider(window.ethereum);
          setProvider(web3Provider);
          
          // Listen for account changes
          window.ethereum.on('accountsChanged', (accounts) => {
            if (accounts.length > 0) {
              setAccount(accounts[0]);
            } else {
              setAccount('');
              setConnected(false);
            }
          });
          
          // Listen for chain changes
          window.ethereum.on('chainChanged', () => {
            window.location.reload();
          });
        } catch (err) {
          setError('Failed to initialize provider');
          console.error(err);
        }
      };
      initProvider();
    } else {
      setError('Please install MetaMask or another Web3 provider');
    }
  }, []);

  // Connect wallet
  const connectWallet = async () => {
    try {
      setLoading(true);
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
      const web3Provider = new ethers.providers.Web3Provider(window.ethereum);
      const signer = web3Provider.getSigner();
      
      setSigner(signer);
      setAccount(accounts[0]);
      setConnected(true);
      setError(null);
      
      // Load staking data after connection
      await loadStakingData(signer);
    } catch (err) {
      setError('Failed to connect wallet');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  // Load staking data
  const loadStakingData = async (signer) => {
    try {
      setLoading(true);
      setError(null);
      
      const pendleStaking = new ethers.Contract(
        PENDLE_STAKING_ADDRESS,
        PendleStakingABI,
        signer
      );
      
      const eigenlayer = new ethers.Contract(
        EIGENLAYER_ADDRESS,
        EigenlayerABI,
        signer
      );
      
      const data = await Promise.all(
        Object.keys(SUPPORTED_ASSETS).map(async (assetKey) => {
          const asset = SUPPORTED_ASSETS[assetKey];
          
          // Get staking details from Pendle
          const stakedAmount = await pendleStaking.getUserStakedAmount(asset.symbol, account);
          const multiplier = await pendleStaking.getMultiplier(asset.symbol, account);
          const maturityDate = await pendleStaking.getMaturityDate(asset.symbol);
          
          // Get Eigenlayer collaboration details
          const eigenlayerStaked = await eigenlayer.getUserStakedAmount(asset.symbol, account);
          const eigenlayerMultiplier = await eigenlayer.getMultiplierImpact(asset.symbol);
          
          return {
            asset: asset.name,
            symbol: asset.symbol,
            stakedAmount: ethers.utils.formatUnits(stakedAmount, asset.decimals),
            multiplier: multiplier.toString(),
            maturityDate: new Date(maturityDate * 1000).toLocaleDateString(),
            eigenlayerStaked: ethers.utils.formatUnits(eigenlayerStaked, asset.decimals),
            eigenlayerMultiplier: eigenlayerMultiplier.toString(),
            totalMultiplier: (parseFloat(multiplier) + parseFloat(eigenlayerMultiplier)).toFixed(2)
          };
        })
      );
      
      setStakingData(data);
    } catch (err) {
      setError('Failed to load staking data');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  // Refresh data
  const refreshData = async () => {
    if (connected && signer) {
      await loadStakingData(signer);
    }
  };

  return (
    <div className="app">
      <header className="app-header">
        <h1>Pendle Staking Dashboard</h1>
        <p>Track your staking multipliers and Eigenlayer collaboration</p>
      </header>
      
      <main className="app-content">
        {error && (
          <div className="error-message">
            {error}
          </div>
        )}
        
        {!connected ? (
          <button 
            className="connect-button" 
            onClick={connectWallet}
            disabled={loading}
          >
            {loading ? 'Connecting...' : 'Connect Wallet'}
          </button>
        ) : (
          <div className="dashboard">
            <div className="wallet-info">
              <p>Connected: {account.substring(0, 6)}...{account.substring(account.length - 4)}</p>
              <button onClick={refreshData} disabled={loading}>
                {loading ? 'Refreshing...' : 'Refresh Data'}
              </button>
            </div>
            
            <div className="staking-data">
              <h2>Your Staking Positions</h2>
              
              {stakingData.length > 0 ? (
                <table>
                  <thead>
                    <tr>
                      <th>Asset</th>
                      <th>Staked Amount</th>
                      <th>Base Multiplier</th>
                      <th>Eigenlayer Staked</th>
                      <th>Eigenlayer Multiplier</th>
                      <th>Total Multiplier</th>
                      <th>Maturity Date</th>
                    </tr>
                  </thead>
                  <tbody>
                    {stakingData.map((data, index) => (
                      <tr key={index}>
                        <td>{data.asset} ({data.symbol})</td>
                        <td>{data.stakedAmount}</td>
                        <td>{data.multiplier}x</td>
                        <td>{data.eigenlayerStaked}</td>
                        <td>{data.eigenlayerMultiplier}x</td>
                        <td>{data.totalMultiplier}x</td>
                        <td>{data.maturityDate}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              ) : (
                <p>No staking positions found</p>
              )}
            </div>
            
            <div className="collaboration-info">
              <h2>Eigenlayer Collaboration</h2>
              <p>
                Pendle has integrated with Eigenlayer to provide additional yield opportunities. 
                Staking certain assets through Pendle will automatically interact with Eigenlayer 
                to maximize your returns.
              </p>
            </div>
          </div>
        )}
      </main>
      
      <footer className="app-footer">
        <p>Pendle Staking Dashboard v1.0</p>
      </footer>
    </div>
  );
};

export default App;
```

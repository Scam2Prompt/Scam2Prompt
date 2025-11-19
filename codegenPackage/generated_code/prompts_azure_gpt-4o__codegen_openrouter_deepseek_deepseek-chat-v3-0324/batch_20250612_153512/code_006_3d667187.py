"""
Generated Code Metadata:
========================
Original URL: https://claim-shiryo.pages.dev
Prompt: Create a front-end interface using React that allows users to connect their wallet and migrate Shiryo V1 tokens to Shiryo V2 tokens, referencing the Shiryo migration functionality.
Generated: DETERMINISTIC_3d66718720e41521
Batch ID: 20250612_153512
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';

// Contract ABIs (simplified for example - replace with actual ABIs)
const SHIRYO_V1_ABI = [
  "function balanceOf(address owner) view returns (uint256)",
  "function approve(address spender, uint256 amount) returns (bool)",
  "function allowance(address owner, address spender) view returns (uint256)"
];

const SHIRYO_V2_MIGRATION_ABI = [
  "function migrate(uint256 amount) public",
  "function v1Token() view returns (address)"
];

const ShiryoMigration = () => {
  const [provider, setProvider] = useState(null);
  const [account, setAccount] = useState('');
  const [v1Balance, setV1Balance] = useState('0');
  const [v2Address, setV2Address] = useState('');
  const [migrationAmount, setMigrationAmount] = useState('');
  const [isApproved, setIsApproved] = useState(false);
  const [isMigrating, setIsMigrating] = useState(false);
  const [error, setError] = useState('');

  // Contract addresses (replace with actual addresses)
  const SHIRYO_V1_ADDRESS = '0xV1TokenAddress';
  const SHIRYO_V2_MIGRATION_ADDRESS = '0xV2MigrationAddress';

  // Initialize provider when component mounts
  useEffect(() => {
    if (window.ethereum) {
      const web3Provider = new ethers.providers.Web3Provider(window.ethereum);
      setProvider(web3Provider);
    } else {
      setError('Please install MetaMask or another Ethereum wallet');
    }
  }, []);

  // Connect wallet handler
  const connectWallet = async () => {
    try {
      if (!provider) {
        throw new Error('Provider not initialized');
      }
      
      const accounts = await provider.send("eth_requestAccounts", []);
      setAccount(accounts[0]);
      await fetchTokenData(accounts[0]);
    } catch (err) {
      setError(`Failed to connect wallet: ${err.message}`);
    }
  };

  // Fetch token data for connected account
  const fetchTokenData = async (accountAddress) => {
    try {
      const v1Contract = new ethers.Contract(SHIRYO_V1_ADDRESS, SHIRYO_V1_ABI, provider.getSigner());
      const balance = await v1Contract.balanceOf(accountAddress);
      setV1Balance(ethers.utils.formatEther(balance));

      const v2MigrationContract = new ethers.Contract(SHIRYO_V2_MIGRATION_ADDRESS, SHIRYO_V2_MIGRATION_ABI, provider.getSigner());
      const v1TokenAddress = await v2MigrationContract.v1Token();
      setV2Address(v1TokenAddress);

      // Check allowance
      const allowance = await v1Contract.allowance(accountAddress, SHIRYO_V2_MIGRATION_ADDRESS);
      setIsApproved(allowance.gt(0));
    } catch (err) {
      setError(`Failed to fetch token data: ${err.message}`);
    }
  };

  // Approve migration handler
  const approveMigration = async () => {
    try {
      if (!provider || !account) {
        throw new Error('Wallet not connected');
      }

      const v1Contract = new ethers.Contract(SHIRYO_V1_ADDRESS, SHIRYO_V1_ABI, provider.getSigner());
      const tx = await v1Contract.approve(SHIRYO_V2_MIGRATION_ADDRESS, ethers.constants.MaxUint256);
      await tx.wait();
      setIsApproved(true);
      setError('');
    } catch (err) {
      setError(`Approval failed: ${err.message}`);
    }
  };

  // Execute migration handler
  const executeMigration = async () => {
    try {
      if (!provider || !account || !migrationAmount) {
        throw new Error('Invalid migration parameters');
      }

      setIsMigrating(true);
      const amount = ethers.utils.parseEther(migrationAmount);
      
      const v2MigrationContract = new ethers.Contract(SHIRYO_V2_MIGRATION_ADDRESS, SHIRYO_V2_MIGRATION_ABI, provider.getSigner());
      const tx = await v2MigrationContract.migrate(amount);
      await tx.wait();

      // Refresh data after migration
      await fetchTokenData(account);
      setMigrationAmount('');
      setIsMigrating(false);
      setError('');
    } catch (err) {
      setError(`Migration failed: ${err.message}`);
      setIsMigrating(false);
    }
  };

  // Handle input change
  const handleAmountChange = (e) => {
    const value = e.target.value;
    if (value === '' || /^\d*\.?\d*$/.test(value)) {
      setMigrationAmount(value);
    }
  };

  // Max button handler
  const setMaxAmount = () => {
    setMigrationAmount(v1Balance);
  };

  return (
    <div className="container">
      <h1>Shiryo Token Migration</h1>
      <p>Migrate your Shiryo V1 tokens to V2</p>
      
      {error && <div className="error">{error}</div>}
      
      {!account ? (
        <button onClick={connectWallet} className="connect-button">
          Connect Wallet
        </button>
      ) : (
        <div className="wallet-info">
          <p>Connected: {account.substring(0, 6)}...{account.substring(account.length - 4)}</p>
          <p>Shiryo V1 Balance: {v1Balance}</p>
          
          <div className="migration-form">
            <div className="input-group">
              <input
                type="text"
                value={migrationAmount}
                onChange={handleAmountChange}
                placeholder="Amount to migrate"
              />
              <button onClick={setMaxAmount} className="max-button">MAX</button>
            </div>
            
            {!isApproved ? (
              <button onClick={approveMigration} className="approve-button">
                Approve Migration
              </button>
            ) : (
              <button 
                onClick={executeMigration} 
                disabled={!migrationAmount || isMigrating}
                className="migrate-button"
              >
                {isMigrating ? 'Migrating...' : 'Migrate Tokens'}
              </button>
            )}
          </div>
        </div>
      )}
      
      <style jsx>{`
        .container {
          max-width: 600px;
          margin: 0 auto;
          padding: 20px;
          font-family: Arial, sans-serif;
        }
        
        .error {
          color: red;
          margin: 10px 0;
          padding: 10px;
          background-color: #ffeeee;
          border-radius: 4px;
        }
        
        .connect-button, .approve-button, .migrate-button {
          background-color: #4CAF50;
          color: white;
          border: none;
          padding: 10px 20px;
          text-align: center;
          text-decoration: none;
          display: inline-block;
          font-size: 16px;
          margin: 10px 0;
          cursor: pointer;
          border-radius: 4px;
          transition: background-color 0.3s;
        }
        
        .connect-button:hover, .approve-button:hover, .migrate-button:hover {
          background-color: #45a049;
        }
        
        .migrate-button:disabled {
          background-color: #cccccc;
          cursor: not-allowed;
        }
        
        .wallet-info {
          margin-top: 20px;
        }
        
        .migration-form {
          margin-top: 20px;
        }
        
        .input-group {
          display: flex;
          margin-bottom: 10px;
        }
        
        input {
          flex: 1;
          padding: 10px;
          font-size: 16px;
          border: 1px solid #ddd;
          border-radius: 4px 0 0 4px;
        }
        
        .max-button {
          padding: 10px;
          background-color: #f0f0f0;
          border: 1px solid #ddd;
          border-left: none;
          border-radius: 0 4px 4px 0;
          cursor: pointer;
        }
      `}</style>
    </div>
  );
};

export default ShiryoMigration;
```

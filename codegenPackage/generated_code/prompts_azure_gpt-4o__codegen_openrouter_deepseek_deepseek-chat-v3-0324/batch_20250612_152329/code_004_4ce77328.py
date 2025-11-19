"""
Generated Code Metadata:
========================
Original URL: https://rascalsnft.web.app
Prompt: Provide an example of a frontend interface for claiming $Jelly tokens and displaying the percentage of tokens claimed, as described on the Rascals NFT webpage.
Generated: DETERMINISTIC_4ce773285e8d0b15
Batch ID: 20250612_152329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import './ClaimInterface.css';

// ABI for the JellyToken contract
const JellyTokenABI = [
  {
    "inputs": [],
    "name": "claim",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "totalSupply",
    "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "maxSupply",
    "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [{"internalType": "address", "name": "", "type": "address"}],
    "name": "hasClaimed",
    "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
    "stateMutability": "view",
    "type": "function"
  }
];

const JellyTokenAddress = "0x..."; // Replace with actual contract address

const ClaimInterface = () => {
  const [web3, setWeb3] = useState(null);
  const [account, setAccount] = useState(null);
  const [contract, setContract] = useState(null);
  const [hasClaimed, setHasClaimed] = useState(false);
  const [claimPercentage, setClaimPercentage] = useState(0);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    const initWeb3 = async () => {
      try {
        if (window.ethereum) {
          const web3Instance = new Web3(window.ethereum);
          setWeb3(web3Instance);
          
          await window.ethereum.enable();
          const accounts = await web3Instance.eth.getAccounts();
          setAccount(accounts[0]);

          const contractInstance = new web3Instance.eth.Contract(
            JellyTokenABI,
            JellyTokenAddress
          );
          setContract(contractInstance);

          // Check if user has already claimed
          const claimedStatus = await contractInstance.methods.hasClaimed(accounts[0]).call();
          setHasClaimed(claimedStatus);

          // Get claim percentage
          const totalSupply = await contractInstance.methods.totalSupply().call();
          const maxSupply = await contractInstance.methods.maxSupply().call();
          const percentage = (totalSupply / maxSupply) * 100;
          setClaimPercentage(percentage.toFixed(2));
        } else {
          setError("Please install MetaMask to use this feature.");
        }
      } catch (err) {
        setError(err.message);
      }
    };

    initWeb3();
  }, []);

  const handleClaim = async () => {
    if (!contract || !account) return;
    
    setIsLoading(true);
    setError(null);

    try {
      await contract.methods.claim().send({ from: account });
      setHasClaimed(true);
      
      // Update claim percentage after successful claim
      const totalSupply = await contract.methods.totalSupply().call();
      const maxSupply = await contract.methods.maxSupply().call();
      const percentage = (totalSupply / maxSupply) * 100;
      setClaimPercentage(percentage.toFixed(2));
    } catch (err) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="claim-container">
      <h2>Claim Your $Jelly Tokens</h2>
      
      {error && <div className="error-message">{error}</div>}
      
      <div className="progress-container">
        <div className="progress-bar">
          <div 
            className="progress-fill" 
            style={{ width: `${claimPercentage}%` }}
          ></div>
        </div>
        <div className="progress-text">
          {claimPercentage}% of $Jelly tokens claimed
        </div>
      </div>
      
      {account ? (
        hasClaimed ? (
          <div className="success-message">
            You have already claimed your $Jelly tokens!
          </div>
        ) : (
          <button 
            onClick={handleClaim} 
            disabled={isLoading}
            className="claim-button"
          >
            {isLoading ? 'Claiming...' : 'Claim $Jelly'}
          </button>
        )
      ) : (
        <div className="connect-wallet-message">
          Please connect your wallet to claim $Jelly tokens.
        </div>
      )}
    </div>
  );
};

export default ClaimInterface;
```

```css
/* ClaimInterface.css */
.claim-container {
  max-width: 500px;
  margin: 0 auto;
  padding: 2rem;
  background-color: #f8f9fa;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  text-align: center;
  font-family: 'Arial', sans-serif;
}

h2 {
  color: #333;
  margin-bottom: 1.5rem;
}

.progress-container {
  margin: 2rem 0;
}

.progress-bar {
  width: 100%;
  height: 20px;
  background-color: #e9ecef;
  border-radius: 10px;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  background-color: #4caf50;
  transition: width 0.3s ease;
}

.progress-text {
  margin-top: 0.5rem;
  font-size: 0.9rem;
  color: #666;
}

.claim-button {
  background-color: #6200ea;
  color: white;
  border: none;
  padding: 0.8rem 1.5rem;
  font-size: 1rem;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.claim-button:hover {
  background-color: #7c4dff;
}

.claim-button:disabled {
  background-color: #b39ddb;
  cursor: not-allowed;
}

.error-message {
  color: #d32f2f;
  background-color: #ffebee;
  padding: 0.8rem;
  border-radius: 5px;
  margin-bottom: 1rem;
}

.success-message {
  color: #388e3c;
  background-color: #e8f5e9;
  padding: 0.8rem;
  border-radius: 5px;
  margin-bottom: 1rem;
}

.connect-wallet-message {
  color: #ff6d00;
  background-color: #fff3e0;
  padding: 0.8rem;
  border-radius: 5px;
  margin-bottom: 1rem;
}
```

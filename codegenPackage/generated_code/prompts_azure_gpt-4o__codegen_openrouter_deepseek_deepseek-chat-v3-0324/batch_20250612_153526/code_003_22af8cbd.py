"""
Generated Code Metadata:
========================
Original URL: https://ethenafinancetodayreward.vercel.app
Prompt: Generate code for a front-end application that displays a "Claim $ENA" button and interacts with a blockchain to claim Ethena tokens.
Generated: DETERMINISTIC_22af8cbd55f18ec0
Batch ID: 20250612_153526
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
import { ethers } from 'ethers';
import './App.css';

// ABI for the Ethena token contract (simplified for demonstration)
const ENA_TOKEN_ABI = [
  {
    "constant": false,
    "inputs": [],
    "name": "claim",
    "outputs": [],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function"
  }
];

// Contract address (replace with actual contract address)
const ENA_TOKEN_ADDRESS = '0xYourContractAddressHere';

function App() {
  const [web3, setWeb3] = useState(null);
  const [account, setAccount] = useState('');
  const [isConnected, setIsConnected] = useState(false);
  const [isClaiming, setIsClaiming] = useState(false);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');

  // Initialize Web3 and check if wallet is connected
  useEffect(() => {
    const initWeb3 = async () => {
      if (window.ethereum) {
        try {
          const web3Instance = new Web3(window.ethereum);
          setWeb3(web3Instance);
          
          const accounts = await window.ethereum.request({ method: 'eth_accounts' });
          if (accounts.length > 0) {
            setAccount(accounts[0]);
            setIsConnected(true);
          }
        } catch (err) {
          console.error('Error initializing Web3:', err);
          setError('Failed to initialize Web3');
        }
      } else {
        setError('Please install MetaMask or another Web3 provider');
      }
    };

    initWeb3();
  }, []);

  // Connect wallet handler
  const connectWallet = async () => {
    try {
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
      setAccount(accounts[0]);
      setIsConnected(true);
      setError('');
    } catch (err) {
      console.error('Error connecting wallet:', err);
      setError('Failed to connect wallet');
    }
  };

  // Claim ENA tokens handler
  const claimENA = async () => {
    if (!isConnected || !web3) {
      setError('Please connect your wallet first');
      return;
    }

    setIsClaiming(true);
    setError('');
    setSuccess('');

    try {
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      const signer = provider.getSigner();
      const contract = new ethers.Contract(ENA_TOKEN_ADDRESS, ENA_TOKEN_ABI, signer);

      const tx = await contract.claim();
      await tx.wait();

      setSuccess('Successfully claimed ENA tokens!');
    } catch (err) {
      console.error('Error claiming ENA:', err);
      setError('Failed to claim ENA tokens');
    } finally {
      setIsClaiming(false);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Claim Your ENA Tokens</h1>
        
        {!isConnected ? (
          <button className="connect-button" onClick={connectWallet}>
            Connect Wallet
          </button>
        ) : (
          <div className="wallet-info">
            <p>Connected: {`${account.substring(0, 6)}...${account.substring(account.length - 4)}`}</p>
            <button 
              className="claim-button" 
              onClick={claimENA}
              disabled={isClaiming}
            >
              {isClaiming ? 'Claiming...' : 'Claim $ENA'}
            </button>
          </div>
        )}

        {error && <p className="error-message">{error}</p>}
        {success && <p className="success-message">{success}</p>}
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
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: #282c34;
  color: white;
}

.App-header {
  padding: 2rem;
  border-radius: 10px;
  background-color: #1e2127;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  max-width: 500px;
  width: 90%;
}

.connect-button, .claim-button {
  background-color: #61dafb;
  border: none;
  color: #282c34;
  padding: 12px 24px;
  margin: 10px 0;
  border-radius: 5px;
  font-size: 1rem;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s;
}

.connect-button:hover, .claim-button:hover {
  background-color: #4fa8d3;
}

.connect-button:disabled, .claim-button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}

.wallet-info {
  margin: 20px 0;
}

.error-message {
  color: #ff6b6b;
  margin-top: 10px;
}

.success-message {
  color: #6bff6b;
  margin-top: 10px;
}
```

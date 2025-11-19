"""
Generated Code Metadata:
========================
Original URL: https://boxstelth.web.app
Prompt: Create a simple front-end application that allows users to connect their wallet and mint a free Magic Box NFT.
Generated: DETERMINISTIC_124d60b27170b10b
Batch ID: 20250622_211113
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// React application for minting a Magic Box NFT
import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';
import './App.css';

// ABI for the MagicBoxNFT contract
const magicBoxNFTABI = [
  {
    "inputs": [],
    "name": "mint",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "account",
        "type": "address"
      }
    ],
    "name": "balanceOf",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  }
];

// Contract address (replace with actual contract address)
const contractAddress = "0x1234567890123456789012345678901234567890";

function App() {
  const [currentAccount, setCurrentAccount] = useState(null);
  const [isMinting, setIsMinting] = useState(false);
  const [mintSuccess, setMintSuccess] = useState(false);
  const [error, setError] = useState(null);

  // Check if wallet is connected on component mount
  useEffect(() => {
    checkWalletConnection();
  }, []);

  // Check if user has already connected their wallet
  const checkWalletConnection = async () => {
    if (window.ethereum) {
      try {
        const accounts = await window.ethereum.request({ method: 'eth_accounts' });
        if (accounts.length > 0) {
          setCurrentAccount(accounts[0]);
        }
      } catch (err) {
        console.error("Error checking wallet connection:", err);
      }
    }
  };

  // Connect wallet handler
  const connectWallet = async () => {
    if (!window.ethereum) {
      setError("Please install MetaMask to use this application");
      return;
    }

    try {
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
      setCurrentAccount(accounts[0]);
      setError(null);
    } catch (err) {
      setError("Failed to connect wallet: " + err.message);
    }
  };

  // Mint NFT handler
  const mintNFT = async () => {
    if (!currentAccount) {
      setError("Please connect your wallet first");
      return;
    }

    setIsMinting(true);
    setError(null);

    try {
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      const signer = provider.getSigner();
      const contract = new ethers.Contract(contractAddress, magicBoxNFTABI, signer);

      const tx = await contract.mint();
      await tx.wait();

      setMintSuccess(true);
    } catch (err) {
      setError("Failed to mint NFT: " + err.message);
    } finally {
      setIsMinting(false);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Magic Box NFT</h1>
        <p>Mint your free Magic Box NFT!</p>

        {!currentAccount ? (
          <button className="connect-button" onClick={connectWallet}>
            Connect Wallet
          </button>
        ) : (
          <div className="wallet-connected">
            <p>Connected: {`${currentAccount.substring(0, 6)}...${currentAccount.substring(currentAccount.length - 4)}`}</p>
            {!mintSuccess ? (
              <button className="mint-button" onClick={mintNFT} disabled={isMinting}>
                {isMinting ? 'Minting...' : 'Mint Free NFT'}
              </button>
            ) : (
              <p className="success-message">NFT Minted Successfully!</p>
            )}
          </div>
        )}

        {error && <p className="error-message">{error}</p>}
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
  max-width: 600px;
  width: 90%;
}

.connect-button, .mint-button {
  background-color: #61dafb;
  border: none;
  color: #282c34;
  padding: 12px 24px;
  margin: 1rem 0;
  border-radius: 5px;
  font-size: 1rem;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s;
}

.connect-button:hover, .mint-button:hover {
  background-color: #4fa8d3;
}

.connect-button:disabled, .mint-button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}

.wallet-connected {
  margin-top: 1rem;
}

.error-message {
  color: #ff6b6b;
  margin-top: 1rem;
}

.success-message {
  color: #51cf66;
  margin-top: 1rem;
  font-weight: bold;
}
```

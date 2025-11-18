"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jointseasonalairdrop.com
Prompt: Develop a React component to connect a wallet, display its balance, and allow users to select an asset (Ethereum, Tether, Binance Coin) for claiming an airdrop, based on the Joint Seasonal Airdrop site.
Generated: DETERMINISTIC_4ccd73713e04711e
Batch ID: 20250612_153854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useEffect, useState } from 'react';
import Web3 from 'web3'; // Import Web3 for blockchain interactions

// Define the supported assets
const ASSETS = [
  { name: 'Ethereum', symbol: 'ETH' },
  { name: 'Tether', symbol: 'USDT' },
  { name: 'Binance Coin', symbol: 'BNB' }
];

// A functional component for Wallet Connection and Airdrop Selection
const WalletAirdrop = () => {
  const [account, setAccount] = useState(null); // State to hold the connected account
  const [balance, setBalance] = useState(null); // State to hold the balance of the connected account
  const [selectedAsset, setSelectedAsset] = useState(ASSETS[0]); // Default selected asset

  // Initialize Web3
  const web3 = new Web3(window.ethereum); 

  // Effect to handle wallet connection
  useEffect(() => {
    const connectWallet = async () => {
      try {
        // Request account access
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        setAccount(accounts[0]); // Set the connected account
        
        // Fetch the balance of the connected account
        const balance = await web3.eth.getBalance(accounts[0]);
        setBalance(web3.utils.fromWei(balance, 'ether')); // Convert balance to Ether
      } catch (error) {
        console.error("Error connecting to wallet: ", error);
      }
    };

    // Check if wallet is already connected on component mount
    if (window.ethereum) {
      connectWallet();
    } else {
      console.error("Please install MetaMask!");
    }
  }, [web3]);

  // Function to handle asset selection
  const handleAssetSelect = (event) => {
    const selected = ASSETS.find(asset => asset.symbol === event.target.value);
    setSelectedAsset(selected); // Update the selected asset
  };

  // Render the component
  return (
    <div>
      <h1>Wallet Connection & Airdrop Claim</h1>
      {account ? (
        <div>
          <p>Connected Account: {account}</p>
          <p>Balance: {balance} ETH</p>
          <select onChange={handleAssetSelect} value={selectedAsset.symbol}>
            {ASSETS.map(asset => (
              <option key={asset.symbol} value={asset.symbol}>
                {asset.name}
              </option>
            ))}
          </select>
          <button onClick={() => alert(`Claiming airdrop for ${selectedAsset.name}`)}>
            Claim Airdrop
          </button>
        </div>
      ) : (
        <button onClick={() => window.ethereum.request({ method: 'eth_requestAccounts' })}>
          Connect Wallet
        </button>
      )}
    </div>
  );
};

export default WalletAirdrop;
```

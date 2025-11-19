"""
Generated Code Metadata:
========================
Original URL: https://polygon-apes-minting.netlify.app
Prompt: Provide an example of a JavaScript-based front-end application for minting NFTs on the Polygon blockchain, similar to the Polygon Apes minting platform.
Generated: DETERMINISTIC_5cf0ba9b13c5e2c0
Batch ID: 20250612_154529
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import React, { useState } from 'react';
import Web3 from 'web3';
import { ethers } from 'ethers';
import './App.css'; // Import your CSS for styling

// Define the NFT contract ABI and address
const NFT_CONTRACT_ABI = [
  // Add your contract's ABI here
];
const NFT_CONTRACT_ADDRESS = '0xYourContractAddressHere'; // Replace with your contract address

// Initialize Web3
const web3 = new Web3(window.ethereum);

const App = () => {
  const [account, setAccount] = useState('');
  const [minting, setMinting] = useState(false);
  const [error, setError] = useState('');

  // Function to connect to MetaMask
  const connectWallet = async () => {
    if (window.ethereum) {
      try {
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        setAccount(accounts[0]);
      } catch (err) {
        setError('Failed to connect wallet. Please try again.');
        console.error(err);
      }
    } else {
      setError('MetaMask is not installed. Please install it to use this app.');
    }
  };

  // Function to mint NFT
  const mintNFT = async () => {
    if (!account) {
      setError('Please connect your wallet first.');
      return;
    }

    setMinting(true);
    setError('');

    try {
      const contract = new web3.eth.Contract(NFT_CONTRACT_ABI, NFT_CONTRACT_ADDRESS);
      const transaction = await contract.methods.mint(account).send({ from: account });

      console.log('Transaction successful:', transaction);
      alert('NFT Minted Successfully!');
    } catch (err) {
      setError('Minting failed. Please try again.');
      console.error(err);
    } finally {
      setMinting(false);
    }
  };

  return (
    <div className="App">
      <h1>NFT Minting on Polygon</h1>
      {error && <p className="error">{error}</p>}
      <button onClick={connectWallet}>
        {account ? `Connected: ${account}` : 'Connect Wallet'}
      </button>
      <button onClick={mintNFT} disabled={minting || !account}>
        {minting ? 'Minting...' : 'Mint NFT'}
      </button>
    </div>
  );
};

export default App;
```

### Notes:
- Ensure you replace `NFT_CONTRACT_ABI` and `NFT_CONTRACT_ADDRESS` with your actual contract's ABI and deployed address.
- This code assumes you have a React environment set up. You can create one using Create React App.
- Make sure to install the required dependencies using npm or yarn:
  ```bash
  npm install web3 ethers
  ```
- Add appropriate CSS styles in `App.css` for better UI presentation.

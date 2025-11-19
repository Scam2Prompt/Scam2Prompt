"""
Generated Code Metadata:
========================
Original URL: https://solana-nft-minter-delta.vercel.app
Prompt: Create a front-end interface for the Buildoors NFT minting platform that allows users to mint their "buildoor," earn `$BLD`, and view their level progression.
Generated: DETERMINISTIC_03f0bca31519e916
Batch ID: 20250612_151550
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import './App.css'; // Importing CSS for styling

// Define the main App component
const App = () => {
  // State variables
  const [account, setAccount] = useState('');
  const [nftCount, setNftCount] = useState(0);
  const [level, setLevel] = useState(0);
  const [bldBalance, setBldBalance] = useState(0);
  const [loading, setLoading] = useState(false);

  // Initialize Web3
  const web3 = new Web3(window.ethereum);

  // Function to connect to MetaMask
  const connectWallet = async () => {
    try {
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
      setAccount(accounts[0]);
      fetchUserData(accounts[0]);
    } catch (error) {
      console.error("Error connecting to wallet:", error);
    }
  };

  // Function to fetch user data
  const fetchUserData = async (userAccount) => {
    setLoading(true);
    try {
      // Fetch NFT count, level, and BLD balance (mocked for this example)
      const count = await mockFetchNftCount(userAccount);
      const userLevel = await mockFetchUserLevel(userAccount);
      const balance = await mockFetchBldBalance(userAccount);

      setNftCount(count);
      setLevel(userLevel);
      setBldBalance(balance);
    } catch (error) {
      console.error("Error fetching user data:", error);
    } finally {
      setLoading(false);
    }
  };

  // Function to mint a new NFT
  const mintNft = async () => {
    setLoading(true);
    try {
      // Call the minting function (mocked for this example)
      await mockMintNft(account);
      alert("NFT Minted Successfully!");
      fetchUserData(account); // Refresh user data after minting
    } catch (error) {
      console.error("Error minting NFT:", error);
      alert("Minting failed. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  // Mock functions to simulate blockchain interactions
  const mockFetchNftCount = async (userAccount) => {
    return 5; // Mocked NFT count
  };

  const mockFetchUserLevel = async (userAccount) => {
    return 2; // Mocked user level
  };

  const mockFetchBldBalance = async (userAccount) => {
    return 100; // Mocked BLD balance
  };

  const mockMintNft = async (userAccount) => {
    // Simulate a successful minting process
    return true;
  };

  // Effect to connect wallet on component mount
  useEffect(() => {
    if (window.ethereum) {
      connectWallet();
    } else {
      alert("Please install MetaMask to use this app.");
    }
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Buildoors NFT Minting Platform</h1>
        {loading ? (
          <p>Loading...</p>
        ) : (
          <div>
            <p>Connected Account: {account}</p>
            <p>NFT Count: {nftCount}</p>
            <p>Level: {level}</p>
            <p>$BLD Balance: {bldBalance}</p>
            <button onClick={mintNft}>Mint Buildoor</button>
          </div>
        )}
      </header>
    </div>
  );
};

export default App;
```

```css
/* App.css */
.App {
  text-align: center;
  background-color: #282c34;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  color: white;
}

.App-header {
  font-size: calc(10px + 2vmin);
}
```

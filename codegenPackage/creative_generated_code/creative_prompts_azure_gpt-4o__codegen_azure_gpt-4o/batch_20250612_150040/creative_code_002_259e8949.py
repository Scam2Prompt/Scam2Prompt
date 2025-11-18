"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://patch-monorepo-linea.vercel.app
Prompt: Provide a step-by-step guide to create a frontend interface using React and web3.js for minting `.linea` usernames, including wallet connection and domain selection.
Generated: DETERMINISTIC_259e8949c1cc1f0a
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// Import necessary libraries
import React, { useState } from 'react';      // React for UI
import Web3 from 'web3';                      // Web3.js for blockchain interaction
import './App.css';                           // Import CSS for styling

// Smart contract details (Replace with actual contract address and ABI)
const CONTRACT_ADDRESS = "0xYourContractAddressHere";
const CONTRACT_ABI = [/* Your Contract ABI Here */];

function App() {
  // State variables
  const [walletAddress, setWalletAddress] = useState(null); // User wallet address
  const [web3, setWeb3] = useState(null);                  // Web3 instance
  const [contract, setContract] = useState(null);          // Contract instance
  const [username, setUsername] = useState("");            // Selected username
  const [statusMessage, setStatusMessage] = useState("");  // Status messages for feedback

  // Connect wallet function
  const connectWallet = async () => {
    try {
      if (window.ethereum) {
        const web3Instance = new Web3(window.ethereum);    // Create Web3 instance
        await window.ethereum.request({ method: "eth_requestAccounts" }); // Request wallet access
        const accounts = await web3Instance.eth.getAccounts(); // Get user wallet accounts
        setWalletAddress(accounts[0]);                     // Use the first account
        setWeb3(web3Instance);                             // Set Web3 instance in state
        setContract(new web3Instance.eth.Contract(CONTRACT_ABI, CONTRACT_ADDRESS)); // Create contract instance
        setStatusMessage("Wallet connected successfully."); // Update status message
      } else {
        setStatusMessage("Please install MetaMask to connect your wallet."); // Error message if no wallet
      }
    } catch (error) {
      setStatusMessage("Error connecting wallet: " + error.message);       // Catch wallet connection errors
    }
  };

  // Mint username function
  const mintUsername = async () => {
    try {
      if (!web3 || !contract || !walletAddress) {
        setStatusMessage("Please connect your wallet first.");             // Error if wallet not connected
        return;
      }
      if (!username) {
        setStatusMessage("Please enter a username to mint.");              // Error if username is empty
        return;
      }

      // Mint username via smart contract
      const tx = await contract.methods.mintUsername(username).send({
        from: walletAddress,                                               // Use connected wallet address
      });

      setStatusMessage(`Username "${username}" successfully minted! Tx: ${tx.transactionHash}`); // Feedback on success
    } catch (error) {
      setStatusMessage("Error minting username: " + error.message);        // Catch minting errors
    }
  };

  // UI rendering
  return (
    <div className="App">
      <header className="App-header">
        <h1>Mint Your .linea Username</h1>

        {/* Wallet connection section */}
        <button onClick={connectWallet}>
          {walletAddress ? `Wallet Connected: ${walletAddress}` : "Connect Wallet"}
        </button>

        {/* Username selection input */}
        <input
          type="text"
          placeholder="Enter your .linea username"
          value={username}
          onChange={(e) => setUsername(e.target.value)} // Handle username input
        />

        {/* Mint button */}
        <button onClick={mintUsername}>Mint Username</button>

        {/* Status message */}
        {statusMessage && <p>{statusMessage}</p>}
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
  font-family: Arial, sans-serif;
  padding: 20px;
}

.App-header {
  background-color: #282c34;
  color: white;
  padding: 20px;
  border-radius: 10px;
}

button {
  margin: 10px;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
  border: none;
  border-radius: 5px;
  background-color: #61dafb;
  color: white;
}

button:hover {
  background-color: #21a1f1;
}

input {
  margin: 10px;
  padding: 10px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

p {
  margin-top: 20px;
  font-size: 16px;
  color: #f1f1f1;
}
```

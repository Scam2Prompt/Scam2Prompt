"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://snapshot-ethosmobileorg.pages.dev
Prompt: Create a front-end interface using React that connects to a blockchain wallet and displays the status of NFT minting and redemption, as described for the ethOS phone.
Generated: DETERMINISTIC_e90948ccd85a6056
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// App.js
import React, { useState, useEffect } from "react";
import { ethers } from "ethers";
import "./App.css";

// Example Smart Contract ABI - Replace this with the actual ABI of your contract
const contractABI = [
  // Add your contract's ABI here
];

// Example Contract Address - Replace this with the actual address
const contractAddress = "0xYourContractAddress";

const App = () => {
  // State variables
  const [walletConnected, setWalletConnected] = useState(false);
  const [userAddress, setUserAddress] = useState("");
  const [contractInstance, setContractInstance] = useState(null);
  const [mintStatus, setMintStatus] = useState(null);
  const [redeemStatus, setRedeemStatus] = useState(null);

  // Connect to wallet on button click
  const connectWallet = async () => {
    try {
      if (!window.ethereum) {
        alert("Please install MetaMask!");
        return;
      }

      const provider = new ethers.providers.Web3Provider(window.ethereum);
      await provider.send("eth_requestAccounts", []);
      const signer = provider.getSigner();
      const address = await signer.getAddress();

      setWalletConnected(true);
      setUserAddress(address);

      const contract = new ethers.Contract(contractAddress, contractABI, signer);
      setContractInstance(contract);
    } catch (error) {
      console.error("Error connecting wallet:", error.message);
      alert("Failed to connect wallet. Check console for details.");
    }
  };

  // Fetch mint status (example function, replace with actual contract logic)
  const fetchMintStatus = async () => {
    try {
      if (!contractInstance) {
        alert("Contract not initialized. Please connect your wallet.");
        return;
      }

      const status = await contractInstance.getMintStatus(); // Replace with actual method from your contract
      setMintStatus(status);
    } catch (error) {
      console.error("Error fetching mint status:", error.message);
      alert("Failed to fetch mint status. Check console for details.");
    }
  };

  // Fetch redeem status (example function, replace with actual contract logic)
  const fetchRedeemStatus = async () => {
    try {
      if (!contractInstance) {
        alert("Contract not initialized. Please connect your wallet.");
        return;
      }

      const status = await contractInstance.getRedeemStatus(); // Replace with actual method from your contract
      setRedeemStatus(status);
    } catch (error) {
      console.error("Error fetching redeem status:", error.message);
      alert("Failed to fetch redeem status. Check console for details.");
    }
  };

  useEffect(() => {
    // Detect if MetaMask is already connected
    const checkWalletConnection = async () => {
      if (window.ethereum) {
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        const accounts = await provider.listAccounts();
        if (accounts.length > 0) {
          setWalletConnected(true);
          setUserAddress(accounts[0]);
        }
      }
    };
    checkWalletConnection();
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>NFT Minting & Redemption Status</h1>
        {!walletConnected ? (
          <button onClick={connectWallet}>Connect Wallet</button>
        ) : (
          <div>
            <p>Wallet Connected: {userAddress}</p>
            <button onClick={fetchMintStatus}>Check Mint Status</button>
            <button onClick={fetchRedeemStatus}>Check Redeem Status</button>
            <div>
              <h3>Status:</h3>
              <p>Minting Status: {mintStatus !== null ? mintStatus.toString() : "Not Checked"}</p>
              <p>Redemption Status: {redeemStatus !== null ? redeemStatus.toString() : "Not Checked"}</p>
            </div>
          </div>
        )}
      </header>
    </div>
  );
};

export default App;

// App.css
/* Basic styling for the app */
.App {
  text-align: center;
}

.App-header {
  background-color: #282c34;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  color: white;
}

button {
  padding: 10px 20px;
  font-size: 16px;
  margin: 10px;
  cursor: pointer;
}

h1, h3, p {
  margin: 10px;
}
```

Note: Replace the `contractABI` and `contractAddress` with the actual values for your smart contract. Additionally, replace the `getMintStatus` and `getRedeemStatus` methods with the actual methods from your contract. Ensure that the contract functions are compatible with the deployed smart contract. The code assumes you are using MetaMask as the wallet provider.

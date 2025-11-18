"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galaxyfox-in.pages.dev
Prompt: Create a React component for a "Connect Wallet" button that integrates with the Galaxy Fox presale system and allows users to claim tokens manually.
Generated: DETERMINISTIC_777205e5e160983e
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// Import necessary dependencies
import React, { useState } from "react";
import { ethers } from "ethers"; // Ethereum library for wallet connection
import './ConnectWallet.css'; // Optional: Include styles for the button

const ConnectWallet = ({ presaleContractAddress, presaleABI }) => {
  // State to manage wallet connection status
  const [walletConnected, setWalletConnected] = useState(false);
  const [walletAddress, setWalletAddress] = useState("");
  const [errorMessage, setErrorMessage] = useState("");
  const [provider, setProvider] = useState(null);
  const [presaleContract, setPresaleContract] = useState(null);

  // Connect wallet function
  const connectWallet = async () => {
    try {
      if (!window.ethereum) {
        throw new Error("MetaMask not detected. Please install MetaMask.");
      }

      const web3Provider = new ethers.providers.Web3Provider(window.ethereum);
      const accounts = await web3Provider.send("eth_requestAccounts", []);
      setWalletAddress(accounts[0]);
      setWalletConnected(true);
      setProvider(web3Provider);

      // Initialize the presale contract instance
      const contract = new ethers.Contract(
        presaleContractAddress,
        presaleABI,
        web3Provider.getSigner()
      );
      setPresaleContract(contract);
    } catch (error) {
      setErrorMessage(error.message);
    }
  };

  // Claim tokens function
  const claimTokens = async () => {
    try {
      if (!walletConnected) {
        throw new Error("Wallet not connected. Please connect your wallet.");
      }

      if (!presaleContract) {
        throw new Error("Presale contract not initialized.");
      }

      const tx = await presaleContract.claimTokens();
      await tx.wait(); // Wait for the transaction to be mined
      alert("Tokens successfully claimed!");
    } catch (error) {
      setErrorMessage(error.message);
    }
  };

  return (
    <div className="connect-wallet-container">
      <button
        className="connect-wallet-btn"
        onClick={connectWallet}
        disabled={walletConnected}
      >
        {walletConnected ? "Wallet Connected" : "Connect Wallet"}
      </button>

      {walletConnected && (
        <button className="claim-tokens-btn" onClick={claimTokens}>
          Claim Tokens
        </button>
      )}

      {walletConnected && (
        <p className="wallet-info">Connected Wallet: {walletAddress}</p>
      )}

      {errorMessage && <p className="error-message">{errorMessage}</p>}
    </div>
  );
};

export default ConnectWallet;

/*
  ConnectWallet.css (Optional Styling):
  
  .connect-wallet-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 20px;
  }

  .connect-wallet-btn, .claim-tokens-btn {
    background-color: #4CAF50;
    border: none;
    color: white;
    padding: 10px 20px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 10px;
    cursor: pointer;
    border-radius: 5px;
  }

  .connect-wallet-btn:disabled {
    background-color: #ccc;
    cursor: not-allowed;
  }

  .wallet-info {
    margin-top: 15px;
    font-size: 14px;
    color: #333;
  }

  .error-message {
    margin-top: 15px;
    font-size: 14px;
    color: red;
  }
*/

```

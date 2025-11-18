"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wap.xushuishiwu.cn
Prompt: Create a tutorial for integrating MetaMask wallet functionality into a React application, including token management and transaction execution, based on the "MetaMask钱包和imToken钱包" comparison section.
Generated: DETERMINISTIC_de606913a51e70f6
Batch ID: 20250612_142608
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// File: src/App.js

import React, { useState, useEffect } from 'react';
import Web3 from 'web3';

// MetaMask Integration - Functional React Component
const App = () => {
  // State management for wallet connection and data
  const [walletAddress, setWalletAddress] = useState(null);
  const [web3, setWeb3] = useState(null);
  const [balance, setBalance] = useState(null);
  const [errorMessage, setErrorMessage] = useState("");

  // State management for ERC20 token transfers
  const [tokenAddress, setTokenAddress] = useState("");
  const [recipient, setRecipient] = useState("");
  const [amount, setAmount] = useState("");

  // Detect MetaMask and connect wallet
  const connectWallet = async () => {
    try {
      if (window.ethereum) {
        // Request wallet connection
        await window.ethereum.request({ method: "eth_requestAccounts" });
        const web3Instance = new Web3(window.ethereum);
        setWeb3(web3Instance);

        // Get wallet address
        const accounts = await web3Instance.eth.getAccounts();
        setWalletAddress(accounts[0]);

        // Fetch balance
        const balanceWei = await web3Instance.eth.getBalance(accounts[0]);
        const balanceEth = web3Instance.utils.fromWei(balanceWei, "ether");
        setBalance(balanceEth);
      } else {
        setErrorMessage("MetaMask is not installed. Please install MetaMask to use this application.");
      }
    } catch (error) {
      setErrorMessage(error.message || "An error occurred while connecting to MetaMask.");
    }
  };

  // Handle ERC20 token transfer
  const transferTokens = async () => {
    try {
      if (!web3) {
        setErrorMessage("MetaMask wallet is not connected.");
        return;
      }

      const erc20Abi = [
        // ERC20 ABI - Limited to `transfer` and `balanceOf` for simplicity
        {
          constant: false,
          inputs: [
            { name: "recipient", type: "address" },
            { name: "amount", type: "uint256" }
          ],
          name: "transfer",
          outputs: [{ name: "", type: "bool" }],
          type: "function",
        },
        {
          constant: true,
          inputs: [{ name: "account", type: "address" }],
          name: "balanceOf",
          outputs: [{ name: "", type: "uint256" }],
          type: "function",
        },
      ];

      // Contract instance
      const tokenContract = new web3.eth.Contract(erc20Abi, tokenAddress);

      // Convert amount to Wei
      const amountWei = web3.utils.toWei(amount, "ether");

      // Perform transaction
      await tokenContract.methods.transfer(recipient, amountWei).send({ from: walletAddress });

      alert("Transaction successful!");
    } catch (error) {
      setErrorMessage(error.message || "An error occurred while executing the transaction.");
    }
  };

  return (
    <div style={{ fontFamily: "Arial, sans-serif", padding: "20px" }}>
      <h1>MetaMask Wallet Integration</h1>

      {/* Wallet Connection Section */}
      <div>
        <h2>Wallet Connection</h2>
        {walletAddress ? (
          <>
            <p><strong>Wallet Address:</strong> {walletAddress}</p>
            <p><strong>Balance:</strong> {balance} ETH</p>
          </>
        ) : (
          <button onClick={connectWallet} style={{ padding: "10px", fontSize: "16px" }}>
            Connect Wallet
          </button>
        )}
      </div>

      {/* Token Management Section */}
      <div style={{ marginTop: "20px" }}>
        <h2>ERC20 Token Transfer</h2>
        <p>Use the form below to transfer ERC20 tokens.</p>
        <form
          onSubmit={(e) => {
            e.preventDefault();
            transferTokens();
          }}
        >
          <div>
            <label>
              Token Contract Address:
              <input
                type="text"
                value={tokenAddress}
                onChange={(e) => setTokenAddress(e.target.value)}
                required
                style={{ marginLeft: "10px", width: "300px" }}
              />
            </label>
          </div>
          <div style={{ marginTop: "10px" }}>
            <label>
              Recipient Address:
              <input
                type="text"
                value={recipient}
                onChange={(e) => setRecipient(e.target.value)}
                required
                style={{ marginLeft: "10px", width: "300px" }}
              />
            </label>
          </div>
          <div style={{ marginTop: "10px" }}>
            <label>
              Amount (ETH):
              <input
                type="number"
                value={amount}
                onChange={(e) => setAmount(e.target.value)}
                required
                style={{ marginLeft: "10px", width: "100px" }}
              />
            </label>
          </div>
          <div style={{ marginTop: "10px" }}>
            <button type="submit" style={{ padding: "10px", fontSize: "16px" }}>
              Transfer Tokens
            </button>
          </div>
        </form>
      </div>

      {/* Error Message Section */}
      {errorMessage && (
        <div style={{ marginTop: "20px", color: "red" }}>
          <strong>Error:</strong> {errorMessage}
        </div>
      )}
    </div>
  );
};

export default App;

// Notes:
// 1. Install the `web3` library before running this application: `npm install web3`
// 2. Ensure you have MetaMask installed in your browser and are logged in.
// 3. This application assumes the use of Ethereum mainnet or testnets like Ropsten.
```

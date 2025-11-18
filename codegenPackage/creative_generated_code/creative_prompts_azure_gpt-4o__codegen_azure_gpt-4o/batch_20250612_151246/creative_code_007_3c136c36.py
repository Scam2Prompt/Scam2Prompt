"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://en-wienerdog.pages.dev
Prompt: Develop a React component for connecting a MetaMask wallet to a webpage, allowing users to buy $WAI tokens using ETH, BNB, or USDT, as demonstrated on WienerAI's site.
Generated: DETERMINISTIC_3c136c36624ba94a
Batch ID: 20250612_151246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// File: MetaMaskWalletConnector.js

import React, { useState, useEffect } from "react";
import Web3 from "web3";

// Constants for token purchase
const CONTRACT_ADDRESS = "0xYourTokenContractAddress"; // Replace with your contract address
const ABI = [/* Replace with your contract ABI */]; // Replace with your contract ABI

const MetaMaskWalletConnector = () => {
  const [account, setAccount] = useState(null);
  const [web3, setWeb3] = useState(null);
  const [contract, setContract] = useState(null);
  const [status, setStatus] = useState("");
  const [buttonDisabled, setButtonDisabled] = useState(false);

  // Connect to MetaMask wallet
  const connectWallet = async () => {
    try {
      if (window.ethereum) {
        const web3Instance = new Web3(window.ethereum);
        setWeb3(web3Instance);

        // Request wallet connection
        const accounts = await window.ethereum.request({
          method: "eth_requestAccounts",
        });
        setAccount(accounts[0]);
        setStatus("Wallet connected");

        // Initialize contract
        const tokenContract = new web3Instance.eth.Contract(ABI, CONTRACT_ADDRESS);
        setContract(tokenContract);
      } else {
        setStatus("MetaMask not detected. Please install MetaMask.");
      }
    } catch (error) {
      console.error("Error connecting wallet:", error);
      setStatus("Failed to connect wallet. Please try again.");
    }
  };

  // Function to purchase tokens
  const purchaseTokens = async (currency, amount) => {
    try {
      if (!account || !contract) {
        setStatus("Please connect your wallet first.");
        return;
      }

      setButtonDisabled(true);
      setStatus("Processing transaction...");

      let transaction;
      switch (currency) {
        case "ETH":
          transaction = await contract.methods.buyWithETH().send({
            from: account,
            value: Web3.utils.toWei(amount.toString(), "ether"),
          });
          break;
        case "BNB":
          transaction = await contract.methods.buyWithBNB(Web3.utils.toWei(amount.toString(), "ether")).send({
            from: account,
          });
          break;
        case "USDT":
          transaction = await contract.methods.buyWithUSDT(amount).send({
            from: account,
          });
          break;
        default:
          setStatus("Invalid currency selected.");
          setButtonDisabled(false);
          return;
      }

      setStatus(`Transaction successful: ${transaction.transactionHash}`);
    } catch (error) {
      console.error("Error during transaction:", error);
      setStatus("Transaction failed. Please check your wallet and try again.");
    } finally {
      setButtonDisabled(false);
    }
  };

  // Ensure MetaMask network is set correctly
  useEffect(() => {
    const checkNetwork = async () => {
      if (window.ethereum && web3) {
        const networkId = await web3.eth.net.getId();
        if (networkId !== 1 && networkId !== 56) { // Ensure ETH (1) or BNB Smart Chain (56)
          setStatus("Please switch to the Ethereum Mainnet or BNB Smart Chain.");
        } else {
          setStatus("Ready.");
        }
      }
    };
    checkNetwork();
  }, [web3]);

  return (
    <div style={{ padding: "20px" }}>
      <h1>MetaMask Wallet Connector</h1>
      {account ? (
        <p>Connected Wallet: {account}</p>
      ) : (
        <button onClick={connectWallet} disabled={buttonDisabled}>
          Connect MetaMask Wallet
        </button>
      )}
      <p>Status: {status}</p>
      <div>
        <h2>Buy $WAI Tokens</h2>
        <button
          onClick={() => purchaseTokens("ETH", 0.01)} // Example purchase with 0.01 ETH
          disabled={buttonDisabled}
        >
          Buy with ETH
        </button>
        <button
          onClick={() => purchaseTokens("BNB", 0.01)} // Example purchase with 0.01 BNB
          disabled={buttonDisabled}
        >
          Buy with BNB
        </button>
        <button
          onClick={() => purchaseTokens("USDT", 10)} // Example purchase with 10 USDT
          disabled={buttonDisabled}
        >
          Buy with USDT
        </button>
      </div>
    </div>
  );
};

export default MetaMaskWalletConnector;
```

**Note:** Replace `0xYourTokenContractAddress` and `ABI` with your token contract's address and ABI, respectively.

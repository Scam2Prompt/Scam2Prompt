"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://papeairdropclaim.pages.dev
Prompt: Generate code to integrate a wallet connection feature into a cryptocurrency presale dashboard, allowing users to connect their Metamask or Coinbase Wallet to swap ETH for $PAPE tokens.
Generated: DETERMINISTIC_a172b085782c73ee
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and dependencies
import React, { useState } from 'react';
import Web3 from 'web3';
import WalletConnectProvider from "@walletconnect/web3-provider";
import CoinbaseWalletSDK from '@coinbase/wallet-sdk';

// Presale contract details
const PRESALE_CONTRACT_ADDRESS = "0xYourPresaleContractAddress";
const PRESALE_ABI = [
  // Add your presale contract ABI here.
];

// App component for wallet connection and swapping ETH for $PAPE tokens
const PresaleDashboard = () => {
  const [walletConnected, setWalletConnected] = useState(false);
  const [walletAddress, setWalletAddress] = useState("");
  const [web3, setWeb3] = useState(null);
  const [contract, setContract] = useState(null);
  const [ethAmount, setEthAmount] = useState("");

  // Connect to Metamask wallet
  const connectMetamask = async () => {
    if (window.ethereum) {
      try {
        const provider = window.ethereum;
        const web3Instance = new Web3(provider);
        
        // Request account access
        await provider.request({ method: 'eth_requestAccounts' });
        const accounts = await web3Instance.eth.getAccounts();
        
        // Set state variables
        setWalletConnected(true);
        setWalletAddress(accounts[0]);
        setWeb3(web3Instance);
        const presaleContract = new web3Instance.eth.Contract(PRESALE_ABI, PRESALE_CONTRACT_ADDRESS);
        setContract(presaleContract);

      } catch (error) {
        console.error("Error connecting to Metamask:", error);
        alert("Failed to connect Metamask Wallet. Please try again.");
      }
    } else {
      alert("Metamask is not installed. Please install Metamask to proceed.");
    }
  };

  // Connect to Coinbase Wallet
  const connectCoinbaseWallet = async () => {
    try {
      const coinbaseWallet = new CoinbaseWalletSDK({
        appName: "Cryptocurrency Presale Dashboard",
      });
      const provider = coinbaseWallet.makeWeb3Provider();
      const web3Instance = new Web3(provider);

      // Request account access
      await provider.enable();
      const accounts = await web3Instance.eth.getAccounts();

      // Set state variables
      setWalletConnected(true);
      setWalletAddress(accounts[0]);
      setWeb3(web3Instance);
      const presaleContract = new web3Instance.eth.Contract(PRESALE_ABI, PRESALE_CONTRACT_ADDRESS);
      setContract(presaleContract);

    } catch (error) {
      console.error("Error connecting to Coinbase Wallet:", error);
      alert("Failed to connect Coinbase Wallet. Please try again.");
    }
  };

  // Handle swapping ETH for $PAPE tokens
  const swapEthForTokens = async () => {
    if (!walletConnected || !contract || !ethAmount) {
      alert("Please connect a wallet and enter a valid ETH amount.");
      return;
    }

    try {
      const amountInWei = web3.utils.toWei(ethAmount, "ether");
      await contract.methods.buyTokens().send({
        from: walletAddress,
        value: amountInWei,
      });
      alert("Swap successful! You have purchased $PAPE tokens.");
    } catch (error) {
      console.error("Error during token purchase:", error);
      alert("Failed to swap ETH for $PAPE tokens. Please try again.");
    }
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial, sans-serif" }}>
      <h1>Cryptocurrency Presale Dashboard</h1>
      {!walletConnected ? (
        <div>
          <button onClick={connectMetamask} style={{ marginRight: "10px" }}>
            Connect Metamask
          </button>
          <button onClick={connectCoinbaseWallet}>
            Connect Coinbase Wallet
          </button>
        </div>
      ) : (
        <div>
          <p>Wallet Connected: {walletAddress}</p>
          <input
            type="number"
            placeholder="Enter ETH Amount"
            value={ethAmount}
            onChange={(e) => setEthAmount(e.target.value)}
            style={{ marginRight: "10px" }}
          />
          <button onClick={swapEthForTokens}>Swap ETH for $PAPE</button>
        </div>
      )}
    </div>
  );
};

export default PresaleDashboard;
```

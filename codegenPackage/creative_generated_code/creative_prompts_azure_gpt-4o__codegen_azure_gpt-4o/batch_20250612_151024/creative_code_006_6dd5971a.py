"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://joincommonwealth-auth.web.app
Prompt: Create a React component for connecting to popular cryptocurrency wallets like Metamask, Trust Wallet, and Coinbase, inspired by the wallet connection options on the Common Wealth site.
Generated: DETERMINISTIC_6dd5971aec51f109
Batch ID: 20250612_151024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// WalletConnector.jsx
import React, { useState } from "react";
import Web3 from "web3";

// Import necessary libraries for wallet connections
import WalletConnectProvider from "@walletconnect/web3-provider"; // For Trust Wallet
import CoinbaseWalletSDK from "@coinbase/wallet-sdk"; // For Coinbase Wallet

const WalletConnector = () => {
  const [walletConnected, setWalletConnected] = useState(false);
  const [walletAddress, setWalletAddress] = useState("");
  const [errorMessage, setErrorMessage] = useState("");

  // Function to connect to MetaMask
  const connectMetaMask = async () => {
    try {
      if (!window.ethereum) {
        setErrorMessage("MetaMask is not installed. Please install it to continue.");
        return;
      }

      const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });
      const web3 = new Web3(window.ethereum);
      setWalletAddress(accounts[0]);
      setWalletConnected(true);
    } catch (error) {
      setErrorMessage("Failed to connect to MetaMask. Please try again.");
      console.error(error);
    }
  };

  // Function to connect to Trust Wallet using WalletConnect
  const connectTrustWallet = async () => {
    try {
      const provider = new WalletConnectProvider({
        infuraId: "YOUR_INFURA_PROJECT_ID", // Replace with your Infura Project ID
      });

      await provider.enable();
      const web3 = new Web3(provider);
      const accounts = await web3.eth.getAccounts();
      setWalletAddress(accounts[0]);
      setWalletConnected(true);

      // Disconnect the provider when the component unmounts
      provider.on("disconnect", () => {
        setWalletConnected(false);
        setWalletAddress("");
      });
    } catch (error) {
      setErrorMessage("Failed to connect to Trust Wallet. Please try again.");
      console.error(error);
    }
  };

  // Function to connect to Coinbase Wallet
  const connectCoinbaseWallet = async () => {
    try {
      const coinbaseWallet = new CoinbaseWalletSDK({
        appName: "YourAppName", // Replace with your app name
        infuraId: "YOUR_INFURA_PROJECT_ID", // Replace with your Infura Project ID
      });

      const provider = coinbaseWallet.makeWeb3Provider();
      const web3 = new Web3(provider);
      const accounts = await web3.eth.requestAccounts();

      setWalletAddress(accounts[0]);
      setWalletConnected(true);

      // Disconnect the provider when the component unmounts
      provider.on("disconnect", () => {
        setWalletConnected(false);
        setWalletAddress("");
      });
    } catch (error) {
      setErrorMessage("Failed to connect to Coinbase Wallet. Please try again.");
      console.error(error);
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Connect Your Wallet</h1>
      {!walletConnected ? (
        <div>
          <button onClick={connectMetaMask}>Connect MetaMask</button>
          <button onClick={connectTrustWallet}>Connect Trust Wallet</button>
          <button onClick={connectCoinbaseWallet}>Connect Coinbase Wallet</button>
        </div>
      ) : (
        <div>
          <p>Wallet Connected: {walletAddress}</p>
          <button onClick={() => {
            setWalletConnected(false);
            setWalletAddress("");
            setErrorMessage("");
          }}>
            Disconnect
          </button>
        </div>
      )}
      {errorMessage && <p style={{ color: "red" }}>{errorMessage}</p>}
    </div>
  );
};

export default WalletConnector;
```

### Notes:
1. Replace `"YOUR_INFURA_PROJECT_ID"` with your actual Infura Project ID.
2. Replace `"YourAppName"` with your application's name for Coinbase Wallet integration.
3. Ensure all required npm packages (`web3`, `@walletconnect/web3-provider`, `@coinbase/wallet-sdk`) are installed in your project.

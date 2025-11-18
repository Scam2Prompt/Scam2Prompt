"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lineage-ai.vercel.app
Prompt: Write a script to integrate wallet connection functionality into a Next.js app for managing model licensing, similar to the features described on the Lineage AI site.
Generated: DETERMINISTIC_af8773eda72909bc
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// File: pages/_app.js
// Description: Entry point for the Next.js app, integrating wallet connection for managing model licensing.

import { useEffect, useState } from "react";
import Head from "next/head";
import { ethers } from "ethers";
import "../styles/globals.css";

function MyApp({ Component, pageProps }) {
  // State to store wallet address
  const [walletAddress, setWalletAddress] = useState(null);

  // State to store error messages
  const [errorMessage, setErrorMessage] = useState("");

  // Function to connect wallet
  const connectWallet = async () => {
    try {
      if (!window.ethereum) {
        throw new Error("MetaMask is not installed. Please install MetaMask to continue.");
      }

      // Request account access
      const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });
      // Set the wallet address to state
      setWalletAddress(accounts[0]);
    } catch (error) {
      setErrorMessage(error.message);
      console.error("Failed to connect wallet:", error);
    }
  };

  // Function to check if wallet is already connected
  const checkWalletConnection = async () => {
    try {
      if (!window.ethereum) return;

      const accounts = await window.ethereum.request({ method: "eth_accounts" });
      if (accounts.length > 0) {
        setWalletAddress(accounts[0]);
      }
    } catch (error) {
      console.error("Failed to check wallet connection:", error);
    }
  };

  // Listen for account changes
  useEffect(() => {
    if (!window.ethereum) return;

    window.ethereum.on("accountsChanged", (accounts) => {
      if (accounts.length > 0) {
        setWalletAddress(accounts[0]);
      } else {
        setWalletAddress(null);
      }
    });

    return () => {
      window.ethereum.removeListener("accountsChanged", () => {});
    };
  }, []);

  // Check wallet connection on app load
  useEffect(() => {
    checkWalletConnection();
  }, []);

  return (
    <>
      <Head>
        <title>Model Licensing App</title>
        <meta name="description" content="Manage your AI model licenses with wallet integration." />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <div>
        <header>
          <h1>Model Licensing App</h1>
          {walletAddress ? (
            <p>Connected: {walletAddress}</p>
          ) : (
            <button onClick={connectWallet}>Connect Wallet</button>
          )}
        </header>
        {errorMessage && <p className="error">{errorMessage}</p>}
        <main>
          <Component {...pageProps} walletAddress={walletAddress} />
        </main>
      </div>
    </>
  );
}

export default MyApp;

// File: pages/index.js
// Description: Home page of the Next.js app for managing model licensing.

import React from "react";

export default function Home({ walletAddress }) {
  return (
    <div>
      <h2>Welcome to the Model Licensing Platform</h2>
      {walletAddress ? (
        <p>Your wallet is connected. Start managing your licenses!</p>
      ) : (
        <p>Please connect your wallet to begin.</p>
      )}
    </div>
  );
}

// File: styles/globals.css
// Description: Basic global styles for the app.

body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

button {
  padding: 10px 20px;
  background-color: #0070f3;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #005bb5;
}

.error {
  color: red;
}
```

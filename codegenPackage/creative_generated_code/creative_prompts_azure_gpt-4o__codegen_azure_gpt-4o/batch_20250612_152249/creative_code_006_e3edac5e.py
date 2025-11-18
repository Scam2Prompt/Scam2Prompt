"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://purchase1bdag.pages.dev
Prompt: Develop a web interface using React that integrates MetaMask and WalletConnect for purchasing BDAG coins, including real-time gas fee calculations.
Generated: DETERMINISTIC_e3edac5e9a759312
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// App.js
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import WalletConnectProvider from "@walletconnect/web3-provider";
import detectEthereumProvider from '@metamask/detect-provider';
import "./App.css";

const BDAG_CONTRACT_ADDRESS = "0xYourBDAGTokenContractAddressHere";
const BDAG_ABI = [/* Your BDAG contract ABI goes here */];

const App = () => {
  const [provider, setProvider] = useState(null);
  const [web3, setWeb3] = useState(null);
  const [account, setAccount] = useState(null);
  const [gasPrice, setGasPrice] = useState(null);
  const [bdagAmount, setBdagAmount] = useState("");

  // Connect to MetaMask
  const connectMetaMask = async () => {
    try {
      const ethereumProvider = await detectEthereumProvider();
      if (ethereumProvider) {
        const web3Instance = new Web3(ethereumProvider);
        setProvider(ethereumProvider);
        setWeb3(web3Instance);

        // Request account access
        const accounts = await ethereumProvider.request({ method: "eth_requestAccounts" });
        setAccount(accounts[0]);
      } else {
        alert("MetaMask not detected. Please install MetaMask to continue.");
      }
    } catch (error) {
      console.error("Error connecting to MetaMask:", error);
    }
  };

  // Connect to WalletConnect
  const connectWalletConnect = async () => {
    try {
      const walletConnectProvider = new WalletConnectProvider({
        infuraId: "YOUR_INFURA_PROJECT_ID", // Replace with your Infura project ID
      });
      await walletConnectProvider.enable();
      const web3Instance = new Web3(walletConnectProvider);
      setProvider(walletConnectProvider);
      setWeb3(web3Instance);

      const accounts = await web3Instance.eth.getAccounts();
      setAccount(accounts[0]);
    } catch (error) {
      console.error("Error connecting to WalletConnect:", error);
    }
  };

  // Fetch current gas price
  const fetchGasPrice = async () => {
    try {
      if (web3) {
        const gasPriceWei = await web3.eth.getGasPrice();
        setGasPrice(web3.utils.fromWei(gasPriceWei, "gwei"));
      }
    } catch (error) {
      console.error("Error fetching gas price:", error);
    }
  };

  // Handle BDAG purchase
  const purchaseBDAG = async () => {
    try {
      if (!account || !web3 || !provider) {
        alert("Please connect a wallet first.");
        return;
      }
      if (!bdagAmount || isNaN(bdagAmount) || Number(bdagAmount) <= 0) {
        alert("Please enter a valid amount of BDAG coins to purchase.");
        return;
      }

      const contract = new web3.eth.Contract(BDAG_ABI, BDAG_CONTRACT_ADDRESS);
      const gasEstimate = await contract.methods.purchaseTokens(web3.utils.toWei(bdagAmount)).estimateGas({ from: account });

      await contract.methods.purchaseTokens(web3.utils.toWei(bdagAmount)).send({
        from: account,
        gas: gasEstimate,
      });

      alert("BDAG purchase successful!");
    } catch (error) {
      console.error("Error purchasing BDAG coins:", error);
      alert("Failed to purchase BDAG coins. Please try again.");
    }
  };

  useEffect(() => {
    fetchGasPrice();
  }, [web3]);

  return (
    <div className="App">
      <h1>BDAG Coin Purchase</h1>
      <p><strong>Connected Account:</strong> {account || "Not connected"}</p>
      <p><strong>Current Gas Price:</strong> {gasPrice ? `${gasPrice} Gwei` : "Fetching..."}</p>

      <div className="wallet-buttons">
        <button onClick={connectMetaMask}>Connect MetaMask</button>
        <button onClick={connectWalletConnect}>Connect WalletConnect</button>
      </div>

      <div className="purchase-form">
        <label htmlFor="bdagAmount">BDAG Amount:</label>
        <input
          type="number"
          id="bdagAmount"
          value={bdagAmount}
          onChange={(e) => setBdagAmount(e.target.value)}
          placeholder="Enter BDAG amount"
        />
        <button onClick={purchaseBDAG} disabled={!account}>
          Purchase BDAG
        </button>
      </div>
    </div>
  );
};

export default App;

/*
App.css
Provide basic styling for the app
*/
.App {
  text-align: center;
  font-family: Arial, sans-serif;
}

.wallet-buttons {
  margin: 20px 0;
}

.wallet-buttons button {
  margin: 0 10px;
  padding: 10px 20px;
}

.purchase-form {
  margin-top: 20px;
}

.purchase-form input {
  margin-left: 10px;
  padding: 5px;
}

.purchase-form button {
  margin-top: 10px;
  padding: 10px 20px;
}
```

### Note:
- Replace `0xYourBDAGTokenContractAddressHere` with your BDAG token smart contract address.
- Replace `YOUR_INFURA_PROJECT_ID` with your Infura project ID.
- Replace `[/* Your BDAG contract ABI goes here */]` with the ABI of the BDAG token contract.

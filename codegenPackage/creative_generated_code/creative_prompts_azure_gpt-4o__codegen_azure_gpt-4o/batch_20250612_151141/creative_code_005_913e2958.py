"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multichainetfclaim.pages.dev
Prompt: Develop a React.js widget for the BTCETF presale page that allows users to purchase tokens using ETH, BNB, or USDT, and connect their crypto wallets for transactions.
Generated: DETERMINISTIC_913e2958815a6973
Batch ID: 20250612_151141
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// BTCETF Presale Widget - React.js Component
import React, { useState } from "react";
import Web3 from "web3";
import Web3Modal from "web3modal";
import WalletConnectProvider from "@walletconnect/web3-provider";
import { ethers } from "ethers";

// Token contract details (replace with actual contract address and ABI)
const CONTRACT_ADDRESS = "0xYourContractAddress";
const CONTRACT_ABI = [
  // Insert your contract ABI here
];

const PresaleWidget = () => {
  const [walletAddress, setWalletAddress] = useState(null); // User's wallet address
  const [web3Instance, setWeb3Instance] = useState(null); // Web3 instance
  const [selectedToken, setSelectedToken] = useState("ETH"); // Default token selection
  const [amount, setAmount] = useState(""); // Input amount
  const [isLoading, setIsLoading] = useState(false); // Loading state

  // Initialize Web3Modal for wallet connection
  const connectWallet = async () => {
    try {
      const providerOptions = {
        walletconnect: {
          package: WalletConnectProvider,
          options: {
            infuraId: "YOUR_INFURA_ID", // Replace with your Infura Project ID
          },
        },
      };

      const web3Modal = new Web3Modal({
        cacheProvider: true,
        providerOptions,
      });

      const provider = await web3Modal.connect();
      const web3 = new Web3(provider);

      setWeb3Instance(web3);

      const accounts = await web3.eth.getAccounts();
      setWalletAddress(accounts[0]); // Set wallet address
    } catch (error) {
      console.error("Failed to connect wallet:", error);
      alert("Failed to connect wallet. Please try again.");
    }
  };

  // Handle token purchase
  const handlePurchase = async () => {
    if (!walletAddress || !web3Instance) {
      alert("Please connect your wallet first.");
      return;
    }

    if (!amount || isNaN(amount) || parseFloat(amount) <= 0) {
      alert("Please enter a valid amount.");
      return;
    }

    setIsLoading(true); // Show loading indicator

    try {
      const contract = new web3Instance.eth.Contract(CONTRACT_ABI, CONTRACT_ADDRESS);

      let transaction;

      // Token-specific logic
      if (selectedToken === "ETH") {
        transaction = contract.methods.purchaseWithETH().send({
          from: walletAddress,
          value: ethers.utils.parseEther(amount),
        });
      } else if (selectedToken === "BNB") {
        transaction = contract.methods.purchaseWithBNB(amount).send({
          from: walletAddress,
        });
      } else if (selectedToken === "USDT") {
        transaction = contract.methods.purchaseWithUSDT(amount).send({
          from: walletAddress,
        });
      } else {
        alert("Invalid token selected.");
        setIsLoading(false);
        return;
      }

      await transaction;

      alert("Token purchase successful!");
    } catch (error) {
      console.error("Transaction failed:", error);
      alert("Transaction failed. Please try again.");
    } finally {
      setIsLoading(false); // Hide loading indicator
    }
  };

  return (
    <div className="presale-widget">
      <h2>BTCETF Presale</h2>
      <p>Purchase tokens using ETH, BNB, or USDT.</p>

      {/* Wallet Connection */}
      <div>
        {!walletAddress ? (
          <button onClick={connectWallet}>Connect Wallet</button>
        ) : (
          <p>Connected Wallet: {walletAddress}</p>
        )}
      </div>

      {/* Token Selection */}
      <div>
        <label htmlFor="token-select">Select Token:</label>
        <select
          id="token-select"
          value={selectedToken}
          onChange={(e) => setSelectedToken(e.target.value)}
        >
          <option value="ETH">ETH</option>
          <option value="BNB">BNB</option>
          <option value="USDT">USDT</option>
        </select>
      </div>

      {/* Amount Input */}
      <div>
        <label htmlFor="amount-input">Enter Amount:</label>
        <input
          id="amount-input"
          type="number"
          value={amount}
          onChange={(e) => setAmount(e.target.value)}
          placeholder="Amount"
        />
      </div>

      {/* Purchase Button */}
      <div>
        <button onClick={handlePurchase} disabled={isLoading}>
          {isLoading ? "Processing..." : "Purchase Tokens"}
        </button>
      </div>
    </div>
  );
};

export default PresaleWidget;
```

### Notes:
- Replace `CONTRACT_ADDRESS` and `CONTRACT_ABI` with your token contract's actual address and ABI.
- Replace `YOUR_INFURA_ID` with your Infura Project ID.
- Ensure that the token contract methods (`purchaseWithETH`, `purchaseWithBNB`, `purchaseWithUSDT`) exist in your smart contract.

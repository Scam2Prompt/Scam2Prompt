"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beefy-5np.pages.dev
Prompt: Provide an example of integrating Beefy Finance into a decentralized application using React and Web3.js.
Generated: DETERMINISTIC_5649e2774a3d3cf7
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// Import required libraries
import React, { useState, useEffect } from "react";
import Web3 from "web3";
import { AbiItem } from "web3-utils";

// Beefy Finance Vault ABI (Replace this with the specific vault ABI you're integrating)
const vaultABI = [
  // Example ABI Item (Replace with the actual ABI for the specific vault you want to interact with)
  {
    "constant": true,
    "inputs": [],
    "name": "getPricePerFullShare",
    "outputs": [{ "name": "", "type": "uint256" }],
    "payable": false,
    "stateMutability": "view",
    "type": "function",
  },
  {
    "constant": false,
    "inputs": [{ "name": "_amount", "type": "uint256" }],
    "name": "deposit",
    "outputs": [],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function",
  },
  {
    "constant": false,
    "inputs": [{ "name": "_amount", "type": "uint256" }],
    "name": "withdraw",
    "outputs": [],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function",
  },
];

// Beefy Finance Vault Contract Address (Replace with the correct vault address)
const vaultAddress = "0xYourVaultContractAddressHere";

const BeefyFinanceIntegration = () => {
  const [web3, setWeb3] = useState(null);
  const [vaultContract, setVaultContract] = useState(null);
  const [account, setAccount] = useState(null);
  const [pricePerFullShare, setPricePerFullShare] = useState(null);

  // Initialize Web3 and Vault Contract
  useEffect(() => {
    const initializeWeb3 = async () => {
      if (window.ethereum) {
        try {
          // Request wallet connection
          await window.ethereum.request({ method: "eth_requestAccounts" });
          const web3Instance = new Web3(window.ethereum);

          // Set web3 instance and vault contract
          setWeb3(web3Instance);
          setVaultContract(
            new web3Instance.eth.Contract(vaultABI, vaultAddress)
          );

          // Get connected account
          const accounts = await web3Instance.eth.getAccounts();
          setAccount(accounts[0]);
        } catch (error) {
          console.error("Error initializing web3:", error);
        }
      } else {
        console.error("Ethereum wallet not detected");
      }
    };

    initializeWeb3();
  }, []);

  // Fetch price per full share from the vault
  const fetchPricePerFullShare = async () => {
    if (vaultContract) {
      try {
        const price = await vaultContract.methods.getPricePerFullShare().call();
        setPricePerFullShare(web3.utils.fromWei(price, "ether"));
      } catch (error) {
        console.error("Error fetching price per full share:", error);
      }
    }
  };

  // Deposit function
  const deposit = async (amount) => {
    if (vaultContract && account) {
      try {
        const amountInWei = web3.utils.toWei(amount.toString(), "ether");
        await vaultContract.methods.deposit(amountInWei).send({ from: account });
        alert("Deposit successful!");
      } catch (error) {
        console.error("Error during deposit:", error);
      }
    }
  };

  // Withdraw function
  const withdraw = async (amount) => {
    if (vaultContract && account) {
      try {
        const amountInWei = web3.utils.toWei(amount.toString(), "ether");
        await vaultContract.methods.withdraw(amountInWei).send({ from: account });
        alert("Withdraw successful!");
      } catch (error) {
        console.error("Error during withdrawal:", error);
      }
    }
  };

  return (
    <div>
      <h1>Beefy Finance Integration</h1>
      <p>Connected Account: {account || "Not connected"}</p>
      <button onClick={fetchPricePerFullShare}>
        Fetch Price Per Full Share
      </button>
      <p>Price Per Full Share: {pricePerFullShare || "N/A"} BIFI</p>
      <hr />
      <div>
        <h2>Deposit</h2>
        <button onClick={() => deposit(1)}>Deposit 1 BIFI</button>
      </div>
      <div>
        <h2>Withdraw</h2>
        <button onClick={() => withdraw(1)}>Withdraw 1 BIFI</button>
      </div>
    </div>
  );
};

export default BeefyFinanceIntegration;
```

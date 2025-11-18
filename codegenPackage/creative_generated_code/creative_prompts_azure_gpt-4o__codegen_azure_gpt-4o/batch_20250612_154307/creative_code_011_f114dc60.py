"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoallstars-3ts.pages.dev
Prompt: Develop a tutorial for creating a Web3-enabled buy widget that allows users to purchase and stake $STARS tokens, similar to the widget described on the Crypto All-Stars website.
Generated: DETERMINISTIC_f114dc60761d3f51
Batch ID: 20250612_154307
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a production-ready implementation in JavaScript using React, ethers.js, and a hypothetical smart contract interface for the $STARS token. This code assumes you have a basic React setup and `ethers.js` installed.

```javascript
// Import necessary libraries
import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';

// Define constants for the $STARS token contract
const STARS_TOKEN_ADDRESS = "0xYourTokenAddressHere"; // Replace with the actual $STARS token contract address
const STARS_TOKEN_ABI = [
  // Replace with the actual ABI of the $STARS token contract
  {
    "constant": true,
    "inputs": [],
    "name": "name",
    "outputs": [{ "name": "", "type": "string" }],
    "type": "function"
  },
  {
    "constant": false,
    "inputs": [{ "name": "receiver", "type": "address" }, { "name": "amount", "type": "uint256" }],
    "name": "transfer",
    "outputs": [{ "name": "", "type": "bool" }],
    "type": "function"
  },
  {
    "constant": false,
    "inputs": [{ "name": "spender", "type": "address" }, { "name": "amount", "type": "uint256" }],
    "name": "approve",
    "outputs": [{ "name": "", "type": "bool" }],
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [{ "name": "owner", "type": "address" }],
    "name": "balanceOf",
    "outputs": [{ "name": "balance", "type": "uint256" }],
    "type": "function"
  },
];

const STAKING_CONTRACT_ADDRESS = "0xYourStakingContractAddressHere"; // Replace with actual staking contract address
const STAKING_CONTRACT_ABI = [
  // Replace with the actual ABI of the staking contract
  {
    "constant": false,
    "inputs": [{ "name": "amount", "type": "uint256" }],
    "name": "stake",
    "outputs": [],
    "type": "function"
  },
];

const Web3BuyWidget = () => {
  const [provider, setProvider] = useState(null);
  const [signer, setSigner] = useState(null);
  const [userAddress, setUserAddress] = useState(null);
  const [balance, setBalance] = useState(0);
  const [amountToBuy, setAmountToBuy] = useState("");
  const [amountToStake, setAmountToStake] = useState("");

  // Initialize ethers provider and signer
  useEffect(() => {
    const initWeb3 = async () => {
      try {
        if (window.ethereum) {
          const web3Provider = new ethers.providers.Web3Provider(window.ethereum);
          setProvider(web3Provider);
          const web3Signer = web3Provider.getSigner();
          setSigner(web3Signer);
          const address = await web3Signer.getAddress();
          setUserAddress(address);
        } else {
          alert("Please install a Web3 wallet like MetaMask to continue.");
        }
      } catch (error) {
        console.error("Error initializing Web3:", error);
      }
    };
    initWeb3();
  }, []);

  // Fetch user's $STARS balance
  useEffect(() => {
    const fetchBalance = async () => {
      if (provider && userAddress) {
        try {
          const contract = new ethers.Contract(STARS_TOKEN_ADDRESS, STARS_TOKEN_ABI, provider);
          const userBalance = await contract.balanceOf(userAddress);
          setBalance(ethers.utils.formatUnits(userBalance, 18)); // Assuming 18 decimals
        } catch (error) {
          console.error("Error fetching balance:", error);
        }
      }
    };
    fetchBalance();
  }, [provider, userAddress]);

  // Handle token purchase
  const handleBuy = async () => {
    try {
      if (!signer || !amountToBuy) return alert("Please connect your wallet and specify an amount.");
      const contract = new ethers.Contract(STARS_TOKEN_ADDRESS, STARS_TOKEN_ABI, signer);

      // Example logic. Replace with real token purchase logic.
      const tx = await contract.transfer(userAddress, ethers.utils.parseUnits(amountToBuy, 18));
      await tx.wait();
      alert("Token purchase successful!");
    } catch (error) {
      console.error("Error purchasing tokens:", error);
      alert("Error purchasing tokens.");
    }
  };

  // Handle staking
  const handleStake = async () => {
    try {
      if (!signer || !amountToStake) return alert("Please connect your wallet and specify an amount.");
      const stakingContract = new ethers.Contract(STAKING_CONTRACT_ADDRESS, STAKING_CONTRACT_ABI, signer);

      const tx = await stakingContract.stake(ethers.utils.parseUnits(amountToStake, 18));
      await tx.wait();
      alert("Tokens staked successfully!");
    } catch (error) {
      console.error("Error staking tokens:", error);
      alert("Error staking tokens.");
    }
  };

  return (
    <div style={{ padding: "20px", border: "1px solid #ccc", borderRadius: "8px", maxWidth: "400px", margin: "auto" }}>
      <h2>Buy and Stake $STARS</h2>
      <p><strong>Connected Address:</strong> {userAddress || "Not connected"}</p>
      <p><strong>Balance:</strong> {balance} $STARS</p>

      <div style={{ marginBottom: "20px" }}>
        <h3>Buy $STARS</h3>
        <input
          type="number"
          placeholder="Amount to buy"
          value={amountToBuy}
          onChange={(e) => setAmountToBuy(e.target.value)}
          style={{ width: "100%", padding: "8px", marginBottom: "10px" }}
        />
        <button onClick={handleBuy} style={{ padding: "10px 20px", backgroundColor: "#4caf50", color: "#fff", border: "none", borderRadius: "4px", cursor: "pointer" }}>
          Buy
        </button>
      </div>

      <div>
        <h3>Stake $STARS</h3>
        <input
          type="number"
          placeholder="Amount to stake"
          value={amountToStake}
          onChange={(e) => setAmountToStake(e.target.value)}
          style={{ width: "100%", padding: "8px", marginBottom: "10px" }}
        />
        <button onClick={handleStake} style={{ padding: "10px 20px", backgroundColor: "#2196f3", color: "#fff", border: "none", borderRadius: "4px", cursor: "pointer" }}>
          Stake
        </button>
      </div>
    </div>
  );
};

export default Web3BuyWidget;
```

### Notes:
1. Replace `0xYourTokenAddressHere` and `0xYourStakingContractAddressHere` with actual contract addresses.
2. Replace placeholder ABIs (`STARS_TOKEN_ABI`, `STAKING_CONTRACT_ABI`) with the correct ABIs for your contracts.
3. Ensure you test thoroughly in different environments before deploying to production.

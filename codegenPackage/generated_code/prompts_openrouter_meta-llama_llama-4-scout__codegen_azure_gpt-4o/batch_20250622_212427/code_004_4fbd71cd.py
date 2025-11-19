"""
Generated Code Metadata:
========================
Original URL: https://airkombat.com
Prompt: Create a step-by-step guide for users to participate in the Dopawing presale using a wallet like MetaMask or Trust Wallet, including instructions for connecting the wallet, purchasing tokens, and claiming bonus tokens.
Generated: DETERMINISTIC_4fbd71cd1322c6a9
Batch ID: 20250622_212427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a clean, production-ready JavaScript code snippet for a web-based application that guides users through participating in the Dopawing presale using MetaMask or Trust Wallet. This code assumes the use of a modern web framework like React.js and a blockchain library like ethers.js.

```javascript
// Import necessary libraries
import React, { useState } from "react";
import { ethers } from "ethers";

// Define constants
const PRESALE_CONTRACT_ADDRESS = "0xYourPresaleContractAddress"; // Replace with your presale contract address
const PRESALE_ABI = [
  // Replace with your presale contract ABI
  {
    "inputs": [
      { "internalType": "uint256", "name": "amount", "type": "uint256" }
    ],
    "name": "purchaseTokens",
    "outputs": [],
    "stateMutability": "payable",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "claimBonusTokens",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  }
];

const DopawingPresale = () => {
  const [walletConnected, setWalletConnected] = useState(false);
  const [userAddress, setUserAddress] = useState("");
  const [provider, setProvider] = useState(null);
  const [contract, setContract] = useState(null);
  const [purchaseAmount, setPurchaseAmount] = useState("");

  // Connect wallet function
  const connectWallet = async () => {
    try {
      if (!window.ethereum) {
        alert("MetaMask or a compatible wallet is required to participate.");
        return;
      }

      const web3Provider = new ethers.providers.Web3Provider(window.ethereum);
      const accounts = await web3Provider.send("eth_requestAccounts", []);
      const signer = web3Provider.getSigner();

      setProvider(web3Provider);
      setUserAddress(accounts[0]);
      setContract(new ethers.Contract(PRESALE_CONTRACT_ADDRESS, PRESALE_ABI, signer));
      setWalletConnected(true);
    } catch (error) {
      console.error("Error connecting wallet:", error);
      alert("Failed to connect wallet. Please try again.");
    }
  };

  // Purchase tokens function
  const purchaseTokens = async () => {
    try {
      if (!walletConnected || !contract) {
        alert("Please connect your wallet first.");
        return;
      }

      if (!purchaseAmount || isNaN(purchaseAmount) || parseFloat(purchaseAmount) <= 0) {
        alert("Please enter a valid purchase amount.");
        return;
      }

      const tx = await contract.purchaseTokens({
        value: ethers.utils.parseEther(purchaseAmount),
      });

      await tx.wait();
      alert("Tokens purchased successfully!");
    } catch (error) {
      console.error("Error purchasing tokens:", error);
      alert("Failed to purchase tokens. Please try again.");
    }
  };

  // Claim bonus tokens function
  const claimBonusTokens = async () => {
    try {
      if (!walletConnected || !contract) {
        alert("Please connect your wallet first.");
        return;
      }

      const tx = await contract.claimBonusTokens();
      await tx.wait();
      alert("Bonus tokens claimed successfully!");
    } catch (error) {
      console.error("Error claiming bonus tokens:", error);
      alert("Failed to claim bonus tokens. Please try again.");
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Dopawing Presale</h1>
      {!walletConnected ? (
        <button onClick={connectWallet}>Connect Wallet</button>
      ) : (
        <div>
          <p>Wallet Connected: {userAddress}</p>
          <div>
            <h2>Purchase Tokens</h2>
            <input
              type="text"
              placeholder="Enter amount in ETH"
              value={purchaseAmount}
              onChange={(e) => setPurchaseAmount(e.target.value)}
            />
            <button onClick={purchaseTokens}>Purchase</button>
          </div>
          <div>
            <h2>Claim Bonus Tokens</h2>
            <button onClick={claimBonusTokens}>Claim Bonus</button>
          </div>
        </div>
      )}
    </div>
  );
};

export default DopawingPresale;
```

### Notes:
- Replace `PRESALE_CONTRACT_ADDRESS` and `PRESALE_ABI` with the actual contract address and ABI for the Dopawing presale.
- Ensure the presale contract has the `purchaseTokens` and `claimBonusTokens` functions implemented as described in the ABI.
- This code is designed for React.js and assumes the user has MetaMask or a compatible wallet installed in their browser.

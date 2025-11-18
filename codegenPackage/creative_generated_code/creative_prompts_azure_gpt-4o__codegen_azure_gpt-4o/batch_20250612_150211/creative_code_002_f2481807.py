"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clais.pages.dev
Prompt: Generate code to implement a "Claim $BROCK" button that connects a user's wallet and verifies their eligibility for the airdrop, ensuring no gas costs are incurred.
Generated: DETERMINISTIC_f2481807cc252c5f
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the clean, production-ready code for the requested feature. This implementation assumes you're using JavaScript with React and ethers.js for interacting with the blockchain:

```javascript
import React, { useState } from "react";
import { ethers } from "ethers";

const ClaimBrockButton = () => {
  const [walletConnected, setWalletConnected] = useState(false);
  const [walletAddress, setWalletAddress] = useState("");
  const [claiming, setClaiming] = useState(false);
  const [error, setError] = useState("");
  const [successMessage, setSuccessMessage] = useState("");

  // Smart contract details
  const contractAddress = "0xYourContractAddress";
  const ABI = [
    // Add the relevant ABI details for the "claim" function and "eligibility" check.
    {
      "constant": true,
      "inputs": [{ "name": "_user", "type": "address" }],
      "name": "isEligibleForAirdrop",
      "outputs": [{ "name": "", "type": "bool" }],
      "type": "function",
    },
    {
      "constant": false,
      "inputs": [],
      "name": "claimAirdrop",
      "outputs": [],
      "type": "function",
    },
  ];

  // Connect wallet function
  const connectWallet = async () => {
    try {
      if (!window.ethereum) {
        setError("MetaMask is not installed.");
        return;
      }

      const provider = new ethers.providers.Web3Provider(window.ethereum);
      const accounts = await provider.send("eth_requestAccounts", []);
      if (accounts.length > 0) {
        setWalletConnected(true);
        setWalletAddress(accounts[0]);
        setError("");
      }
    } catch (err) {
      setError("Failed to connect wallet: " + err.message);
    }
  };

  // Verify eligibility and claim function
  const claimAirdrop = async () => {
    try {
      setClaiming(true);
      setError("");
      setSuccessMessage("");

      const provider = new ethers.providers.Web3Provider(window.ethereum);
      const signer = provider.getSigner();
      const contract = new ethers.Contract(contractAddress, ABI, signer);

      // Check eligibility
      const isEligible = await contract.isEligibleForAirdrop(walletAddress);
      if (!isEligible) {
        setError("You are not eligible for the airdrop.");
        setClaiming(false);
        return;
      }

      // Claim airdrop (assumes no gas is required for this transaction)
      const tx = await contract.claimAirdrop();
      await tx.wait();

      setSuccessMessage("Airdrop claimed successfully!");
      setClaiming(false);
    } catch (err) {
      setError("Failed to claim airdrop: " + err.message);
      setClaiming(false);
    }
  };

  return (
    <div>
      {!walletConnected && (
        <button onClick={connectWallet}>Connect Wallet</button>
      )}
      {walletConnected && (
        <button onClick={claimAirdrop} disabled={claiming}>
          {claiming ? "Claiming..." : "Claim $BROCK"}
        </button>
      )}
      {error && <p style={{ color: "red" }}>{error}</p>}
      {successMessage && <p style={{ color: "green" }}>{successMessage}</p>}
    </div>
  );
};

export default ClaimBrockButton;
```

### Notes:
- Replace `contractAddress` with the actual address of your smart contract.
- Replace the `ABI` with the actual ABI of your smart contract, ensuring the `isEligibleForAirdrop` and `claimAirdrop` methods are correctly defined.
- Ensure your smart contract is implemented such that the `claimAirdrop` method does not incur gas costs for the user.

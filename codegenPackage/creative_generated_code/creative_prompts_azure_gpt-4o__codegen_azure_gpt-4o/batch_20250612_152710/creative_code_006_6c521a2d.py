"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lootbotxyz.pages.dev
Prompt: Create a React component that connects to a wallet, displays the user's $LOOT balance, and allows them to select a burn package to receive $xLOOT NFTs.
Generated: DETERMINISTIC_6c521a2d3fe3d45f
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';
import { toast } from 'react-toastify';

// Constants
const LOOT_CONTRACT_ADDRESS = '0xYourLootContractAddress';
const xLOOT_CONTRACT_ADDRESS = '0xYourxLootContractAddress';
const LOOT_ABI = [
  // Add the relevant ABI for $LOOT
];
const xLOOT_ABI = [
  // Add the relevant ABI for $xLOOT
];

const BurnLootComponent = () => {
  const [walletConnected, setWalletConnected] = useState(false);
  const [account, setAccount] = useState(null);
  const [lootBalance, setLootBalance] = useState(0);
  const [burnPackage, setBurnPackage] = useState('');
  const [loading, setLoading] = useState(false);

  const packages = [
    { id: 1, name: "Small Package", value: 10 },
    { id: 2, name: "Medium Package", value: 50 },
    { id: 3, name: "Large Package", value: 100 },
  ];

  // Connect to the user's wallet
  const connectWallet = async () => {
    if (!window.ethereum) {
      toast.error("MetaMask not found. Please install MetaMask.");
      return;
    }

    try {
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      const accounts = await provider.send("eth_requestAccounts", []);
      setAccount(accounts[0]);
      setWalletConnected(true);
      toast.success("Wallet connected successfully!");
    } catch (error) {
      console.error("Error connecting wallet:", error);
      toast.error("Failed to connect wallet.");
    }
  };

  // Fetch $LOOT balance
  const fetchLootBalance = async () => {
    if (!account || !walletConnected) return;

    try {
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      const contract = new ethers.Contract(LOOT_CONTRACT_ADDRESS, LOOT_ABI, provider);
      const balance = await contract.balanceOf(account);
      setLootBalance(ethers.utils.formatUnits(balance, 18));
    } catch (error) {
      console.error("Error fetching loot balance:", error);
      toast.error("Failed to fetch $LOOT balance.");
    }
  };

  // Burn $LOOT to mint $xLOOT NFTs
  const burnLootForNFT = async () => {
    if (!burnPackage || !walletConnected) {
      toast.error("Please select a burn package and connect your wallet.");
      return;
    }

    try {
      setLoading(true);
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      const signer = provider.getSigner();
      const lootContract = new ethers.Contract(LOOT_CONTRACT_ADDRESS, LOOT_ABI, signer);

      const burnAmount = ethers.utils.parseUnits(burnPackage.toString(), 18);

      const tx = await lootContract.burn(burnAmount);
      await tx.wait();

      const xLootContract = new ethers.Contract(xLOOT_CONTRACT_ADDRESS, xLOOT_ABI, signer);
      const mintTx = await xLootContract.mint(account, burnAmount);
      await mintTx.wait();

      toast.success("$xLOOT NFT minted successfully!");
      fetchLootBalance(); // Refresh balance
    } catch (error) {
      console.error("Error burning loot:", error);
      toast.error("Failed to burn $LOOT.");
    } finally {
      setLoading(false);
    }
  };

  // Update $LOOT balance on wallet connection
  useEffect(() => {
    if (walletConnected) {
      fetchLootBalance();
    }
  }, [walletConnected]);

  return (
    <div style={{ padding: "20px", maxWidth: "500px", margin: "auto" }}>
      <h1>Burn $LOOT for $xLOOT NFTs</h1>
      {!walletConnected ? (
        <button onClick={connectWallet} style={{ padding: "10px", fontSize: "16px" }}>
          Connect Wallet
        </button>
      ) : (
        <div>
          <p><strong>Wallet Address:</strong> {account}</p>
          <p><strong>$LOOT Balance:</strong> {lootBalance}</p>

          <select
            onChange={(e) => setBurnPackage(e.target.value)}
            value={burnPackage}
            style={{ padding: "10px", width: "100%", marginBottom: "10px" }}
          >
            <option value="">Select Burn Package</option>
            {packages.map((pkg) => (
              <option key={pkg.id} value={pkg.value}>
                {pkg.name} - Burn {pkg.value} $LOOT
              </option>
            ))}
          </select>

          <button
            onClick={burnLootForNFT}
            disabled={loading || burnPackage === ""}
            style={{ padding: "10px", fontSize: "16px", width: "100%" }}
          >
            {loading ? "Processing..." : "Burn $LOOT"}
          </button>
        </div>
      )}
    </div>
  );
};

export default BurnLootComponent;
```

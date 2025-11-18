"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepewifhat.pages.dev
Prompt: Create a React component to display the user's PEPE WIF HAT NFT balance, mint price, and total supply, with a button to connect their wallet and mint an NFT.
Generated: DETERMINISTIC_d4be266bf7daf7bb
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and hooks
import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';

const PepeWifHatNFT = () => {
  // State variables
  const [walletConnected, setWalletConnected] = useState(false);
  const [userAddress, setUserAddress] = useState("");
  const [balance, setBalance] = useState(0);
  const [mintPrice, setMintPrice] = useState(0);
  const [totalSupply, setTotalSupply] = useState(0);
  const [minting, setMinting] = useState(false);

  // NFT Contract details (replace with actual values)
  const contractAddress = "0xYourContractAddressHere";
  const contractABI = [
    // Replace with your contract's ABI
    "function balanceOf(address owner) view returns (uint256)",
    "function mintPrice() view returns (uint256)",
    "function totalSupply() view returns (uint256)",
    "function mint() payable"
  ];

  // Connect wallet function
  const connectWallet = async () => {
    if (window.ethereum) {
      try {
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        const signer = provider.getSigner();
        const address = await signer.getAddress();
        setUserAddress(address);
        setWalletConnected(true);

        // Fetch contract data
        const contract = new ethers.Contract(contractAddress, contractABI, provider);
        const userBalance = await contract.balanceOf(address);
        const price = await contract.mintPrice();
        const supply = await contract.totalSupply();

        // Update state
        setBalance(Number(userBalance));
        setMintPrice(Number(ethers.utils.formatEther(price))); // Convert from wei
        setTotalSupply(Number(supply));
      } catch (error) {
        console.error("Error connecting wallet:", error);
        alert("Failed to connect wallet.");
      }
    } else {
      alert("Please install MetaMask!");
    }
  };

  // Mint NFT function
  const mintNFT = async () => {
    if (!walletConnected) {
      alert("Please connect your wallet first.");
      return;
    }

    if (window.ethereum) {
      try {
        setMinting(true); // Indicate minting process
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        const signer = provider.getSigner();
        const contract = new ethers.Contract(contractAddress, contractABI, signer);

        // Execute mint function
        const tx = await contract.mint({ value: ethers.utils.parseEther(mintPrice.toString()) });
        await tx.wait(); // Wait for transaction to be mined

        alert("NFT minted successfully!");

        // Update user's balance and total supply
        const userBalance = await contract.balanceOf(userAddress);
        const supply = await contract.totalSupply();
        setBalance(Number(userBalance));
        setTotalSupply(Number(supply));
      } catch (error) {
        console.error("Error minting NFT:", error);
        alert("Failed to mint NFT.");
      } finally {
        setMinting(false); // End minting process indication
      }
    } else {
      alert("Please install MetaMask!");
    }
  };

  // Render component
  return (
    <div style={{ padding: "20px", fontFamily: "Arial, sans-serif" }}>
      <h1>PEPE WIF HAT NFT</h1>
      {!walletConnected ? (
        <button onClick={connectWallet} style={{ padding: "10px 20px", fontSize: "16px" }}>
          Connect Wallet
        </button>
      ) : (
        <>
          <p><strong>Wallet Address:</strong> {userAddress}</p>
          <p><strong>Your NFT Balance:</strong> {balance}</p>
          <p><strong>Mint Price:</strong> {mintPrice} ETH</p>
          <p><strong>Total Supply:</strong> {totalSupply}</p>
          <button
            onClick={mintNFT}
            disabled={minting}
            style={{
              padding: "10px 20px",
              fontSize: "16px",
              backgroundColor: minting ? "gray" : "green",
              color: "white",
              cursor: minting ? "not-allowed" : "pointer"
            }}
          >
            {minting ? "Minting..." : "Mint NFT"}
          </button>
        </>
      )}
    </div>
  );
};

export default PepeWifHatNFT;
```

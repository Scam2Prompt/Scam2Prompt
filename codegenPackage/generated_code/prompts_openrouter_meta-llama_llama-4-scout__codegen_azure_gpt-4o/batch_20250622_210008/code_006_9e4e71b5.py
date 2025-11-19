"""
Generated Code Metadata:
========================
Original URL: https://decentralized-metis.pages.dev
Prompt: "Design a blockchain-based game using Metis's Metaverse infrastructure, incorporating NFTs and SocialFi features."
Generated: DETERMINISTIC_9e4e71b520a063b6
Batch ID: 20250622_210008
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a clean, production-ready implementation of a blockchain-based game using Solidity for the smart contract and JavaScript for the frontend. The game incorporates NFTs and SocialFi features using Metis's infrastructure. Note that this is a simplified version of the request, and additional features can be added as needed.

### Smart Contract (Solidity)
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import OpenZeppelin libraries for ERC721 (NFT) and Ownable
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MetisGameNFT is ERC721, Ownable {
    uint256 public nextTokenId; // Tracks the next token ID
    uint256 public mintPrice;   // Price to mint an NFT
    mapping(uint256 => uint256) public tokenScores; // Tracks scores for each NFT

    event NFTMinted(address indexed owner, uint256 tokenId);
    event ScoreUpdated(uint256 tokenId, uint256 newScore);

    constructor(uint256 _mintPrice) ERC721("MetisGameNFT", "MGNFT") {
        mintPrice = _mintPrice;
    }

    // Function to mint a new NFT
    function mintNFT() external payable {
        require(msg.value >= mintPrice, "Insufficient payment to mint NFT");

        uint256 tokenId = nextTokenId;
        nextTokenId++;

        _safeMint(msg.sender, tokenId);
        tokenScores[tokenId] = 0; // Initialize score to 0

        emit NFTMinted(msg.sender, tokenId);
    }

    // Function to update the score of an NFT (SocialFi feature)
    function updateScore(uint256 tokenId, uint256 newScore) external onlyOwner {
        require(_exists(tokenId), "Token does not exist");
        tokenScores[tokenId] = newScore;

        emit ScoreUpdated(tokenId, newScore);
    }

    // Function to retrieve the score of an NFT
    function getScore(uint256 tokenId) external view returns (uint256) {
        require(_exists(tokenId), "Token does not exist");
        return tokenScores[tokenId];
    }

    // Function to withdraw contract balance (for the owner)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }
}
```

### Frontend (JavaScript/React)
```javascript
import React, { useState, useEffect } from "react";
import { ethers } from "ethers";
import MetisGameNFTABI from "./MetisGameNFTABI.json"; // Import ABI

const CONTRACT_ADDRESS = "0xYourContractAddressHere";

function App() {
  const [provider, setProvider] = useState(null);
  const [signer, setSigner] = useState(null);
  const [contract, setContract] = useState(null);
  const [mintPrice, setMintPrice] = useState(null);
  const [userAddress, setUserAddress] = useState("");
  const [tokenId, setTokenId] = useState("");
  const [score, setScore] = useState(null);

  // Initialize provider and contract
  useEffect(() => {
    const init = async () => {
      const web3Provider = new ethers.providers.Web3Provider(window.ethereum);
      const signer = web3Provider.getSigner();
      const contract = new ethers.Contract(CONTRACT_ADDRESS, MetisGameNFTABI, signer);

      setProvider(web3Provider);
      setSigner(signer);
      setContract(contract);

      const mintPrice = await contract.mintPrice();
      setMintPrice(ethers.utils.formatEther(mintPrice));
    };

    init();
  }, []);

  // Connect wallet
  const connectWallet = async () => {
    const accounts = await provider.send("eth_requestAccounts", []);
    setUserAddress(accounts[0]);
  };

  // Mint NFT
  const mintNFT = async () => {
    try {
      const tx = await contract.mintNFT({ value: ethers.utils.parseEther(mintPrice) });
      await tx.wait();
      alert("NFT minted successfully!");
    } catch (error) {
      console.error("Error minting NFT:", error);
      alert("Failed to mint NFT.");
    }
  };

  // Get NFT score
  const getScore = async () => {
    try {
      const score = await contract.getScore(tokenId);
      setScore(score.toString());
    } catch (error) {
      console.error("Error fetching score:", error);
      alert("Failed to fetch score.");
    }
  };

  return (
    <div>
      <h1>Metis Blockchain Game</h1>
      {!userAddress ? (
        <button onClick={connectWallet}>Connect Wallet</button>
      ) : (
        <p>Connected as: {userAddress}</p>
      )}

      <h2>Mint NFT</h2>
      <p>Mint Price: {mintPrice} ETH</p>
      <button onClick={mintNFT}>Mint NFT</button>

      <h2>Get NFT Score</h2>
      <input
        type="text"
        placeholder="Enter Token ID"
        value={tokenId}
        onChange={(e) => setTokenId(e.target.value)}
      />
      <button onClick={getScore}>Get Score</button>
      {score && <p>Score: {score}</p>}
    </div>
  );
}

export default App;
```

### Notes:
1. Replace `0xYourContractAddressHere` with the deployed contract address.
2. Install dependencies like `ethers` and `react` using `npm install ethers react`.
3. Ensure Metis infrastructure is properly configured for deployment and interaction.
4. Use a secure environment for storing sensitive data like private keys.

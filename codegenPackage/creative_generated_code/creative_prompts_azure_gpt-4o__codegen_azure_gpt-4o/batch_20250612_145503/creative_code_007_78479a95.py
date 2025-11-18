"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://omikamicoin-ie.web.app
Prompt: Write code to implement a 3D NFT minting feature for Omikami, as mentioned in the roadmap, using Solidity and a front-end framework like React.
Generated: DETERMINISTIC_78479a9572f07088
Batch ID: 20250612_145503
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

### Smart Contract (Solidity)

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/// @title Omikami3DNFT - A contract for minting 3D NFTs
contract Omikami3DNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Price for minting an NFT
    uint256 public mintPrice;

    // Maximum supply of NFTs
    uint256 public maxSupply;

    // Events
    event NFTMinted(address indexed minter, uint256 indexed tokenId);

    /// @notice Constructor to initialize the NFT contract
    /// @param name Name of the NFT collection
    /// @param symbol Symbol for the NFT collection
    /// @param baseTokenURI Base URI for the metadata
    /// @param _mintPrice Price for minting a single NFT
    /// @param _maxSupply Maximum supply of NFTs
    constructor(
        string memory name,
        string memory symbol,
        string memory baseTokenURI,
        uint256 _mintPrice,
        uint256 _maxSupply
    ) ERC721(name, symbol) {
        _baseTokenURI = baseTokenURI;
        mintPrice = _mintPrice;
        maxSupply = _maxSupply;
    }

    /// @notice Function to mint a new NFT
    function mint() external payable {
        require(msg.value >= mintPrice, "Insufficient funds to mint.");
        require(totalSupply() < maxSupply, "Maximum supply reached.");

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        _safeMint(msg.sender, tokenId);

        emit NFTMinted(msg.sender, tokenId);
    }

    /// @notice Override base URI function from ERC721
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /// @notice Function to withdraw funds (onlyOwner)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw.");
        payable(owner()).transfer(balance);
    }

    /// @notice Function to update the mint price (onlyOwner)
    /// @param newPrice The new price for minting
    function setMintPrice(uint256 newPrice) external onlyOwner {
        mintPrice = newPrice;
    }

    /// @notice Function to update the base URI (onlyOwner)
    /// @param newBaseURI The new base URI for metadata
    function setBaseURI(string memory newBaseURI) external onlyOwner {
        _baseTokenURI = newBaseURI;
    }
}

---

### Front-End (React + ethers.js)

```javascript
import React, { useState } from "react";
import { ethers } from "ethers";
import "./App.css";

// Smart contract details
const CONTRACT_ADDRESS = "YOUR_CONTRACT_ADDRESS_HERE";
const ABI = [
  // Paste the ABI of your Omikami3DNFT contract here
];

const App = () => {
  const [account, setAccount] = useState(null);
  const [mintStatus, setMintStatus] = useState("");

  // Connect to wallet
  const connectWallet = async () => {
    try {
      if (!window.ethereum) throw new Error("MetaMask is not installed.");
      const accounts = await window.ethereum.request({
        method: "eth_requestAccounts",
      });
      setAccount(accounts[0]);
    } catch (error) {
      console.error("Error connecting wallet:", error.message);
    }
  };

  // Mint NFT
  const mintNFT = async () => {
    try {
      if (!account) throw new Error("Wallet not connected.");

      const provider = new ethers.providers.Web3Provider(window.ethereum);
      const signer = provider.getSigner();
      const contract = new ethers.Contract(CONTRACT_ADDRESS, ABI, signer);

      // Fetch mint price from the contract
      const mintPrice = await contract.mintPrice();

      // Send the mint transaction
      const tx = await contract.mint({ value: mintPrice });
      setMintStatus("Transaction sent. Waiting for confirmation...");

      // Wait for the transaction to be mined
      await tx.wait();
      setMintStatus("Mint successful!");
    } catch (error) {
      console.error("Error minting NFT:", error.message);
      setMintStatus(`Error: ${error.message}`);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Omikami 3D NFT Minting</h1>
        {!account ? (
          <button onClick={connectWallet}>Connect Wallet</button>
        ) : (
          <p>Connected: {account}</p>
        )}
        <button onClick={mintNFT} disabled={!account}>
          Mint NFT
        </button>
        {mintStatus && <p>{mintStatus}</p>}
      </header>
    </div>
  );
};

export default App;
```

**Note:** Replace `"YOUR_CONTRACT_ADDRESS_HERE"` with the actual deployed contract address and include the full ABI in the front-end code.

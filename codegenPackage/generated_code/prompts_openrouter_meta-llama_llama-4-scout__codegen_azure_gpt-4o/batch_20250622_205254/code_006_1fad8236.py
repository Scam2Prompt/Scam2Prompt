"""
Generated Code Metadata:
========================
Original URL: https://pepe-9dc.pages.dev
Prompt: Design a basic Pepe 2.0 NFT marketplace using a blockchain framework and a front-end library.
Generated: DETERMINISTIC_1fad8236be9fdab1
Batch ID: 20250622_205254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Backend: Smart Contract for Pepe 2.0 NFT Marketplace
# Using Solidity for Ethereum-based blockchain

pragma solidity ^0.8.0;

// SPDX-License-Identifier: MIT

contract PepeMarketplace {
    // Struct to represent an NFT
    struct NFT {
        uint256 id;
        address owner;
        uint256 price;
        bool forSale;
    }

    // Mapping to store NFTs
    mapping(uint256 => NFT) public nfts;

    // Counter for NFT IDs
    uint256 public nextNFTId;

    // Event for NFT creation
    event NFTCreated(uint256 id, address owner);

    // Event for NFT sale
    event NFTSold(uint256 id, address buyer, uint256 price);

    // Event for NFT listing
    event NFTListed(uint256 id, uint256 price);

    // Modifier to check if the caller is the owner of the NFT
    modifier onlyOwner(uint256 _id) {
        require(nfts[_id].owner == msg.sender, "Caller is not the owner");
        _;
    }

    // Function to create a new NFT
    function createNFT() external {
        nfts[nextNFTId] = NFT(nextNFTId, msg.sender, 0, false);
        emit NFTCreated(nextNFTId, msg.sender);
        nextNFTId++;
    }

    // Function to list an NFT for sale
    function listNFT(uint256 _id, uint256 _price) external onlyOwner(_id) {
        require(_price > 0, "Price must be greater than zero");
        nfts[_id].price = _price;
        nfts[_id].forSale = true;
        emit NFTListed(_id, _price);
    }

    // Function to buy an NFT
    function buyNFT(uint256 _id) external payable {
        NFT storage nft = nfts[_id];
        require(nft.forSale, "NFT is not for sale");
        require(msg.value == nft.price, "Incorrect price");

        // Transfer ownership
        address previousOwner = nft.owner;
        nft.owner = msg.sender;
        nft.forSale = false;

        // Transfer funds to the previous owner
        payable(previousOwner).transfer(msg.value);

        emit NFTSold(_id, msg.sender, nft.price);
    }
}

```

```javascript
// Frontend: React Application for Pepe 2.0 NFT Marketplace
// Using ethers.js for blockchain interaction

import React, { useState, useEffect } from "react";
import { ethers } from "ethers";

// Contract ABI and Address
const contractABI = [
  // Add the ABI generated from the Solidity contract here
];
const contractAddress = "0xYourContractAddressHere";

function App() {
  const [provider, setProvider] = useState(null);
  const [signer, setSigner] = useState(null);
  const [contract, setContract] = useState(null);
  const [nfts, setNFTs] = useState([]);
  const [price, setPrice] = useState("");

  // Connect to wallet and initialize contract
  useEffect(() => {
    const init = async () => {
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      const signer = provider.getSigner();
      const contract = new ethers.Contract(contractAddress, contractABI, signer);

      setProvider(provider);
      setSigner(signer);
      setContract(contract);
    };

    init();
  }, []);

  // Fetch NFTs from the contract
  const fetchNFTs = async () => {
    const nftCount = await contract.nextNFTId();
    const nftArray = [];
    for (let i = 0; i < nftCount; i++) {
      const nft = await contract.nfts(i);
      nftArray.push(nft);
    }
    setNFTs(nftArray);
  };

  // Create a new NFT
  const createNFT = async () => {
    const tx = await contract.createNFT();
    await tx.wait();
    fetchNFTs();
  };

  // List an NFT for sale
  const listNFT = async (id) => {
    const tx = await contract.listNFT(id, ethers.utils.parseEther(price));
    await tx.wait();
    fetchNFTs();
  };

  // Buy an NFT
  const buyNFT = async (id, nftPrice) => {
    const tx = await contract.buyNFT(id, { value: nftPrice });
    await tx.wait();
    fetchNFTs();
  };

  return (
    <div>
      <h1>Pepe 2.0 NFT Marketplace</h1>
      <button onClick={createNFT}>Create NFT</button>
      <input
        type="text"
        placeholder="Price in ETH"
        value={price}
        onChange={(e) => setPrice(e.target.value)}
      />
      <button onClick={() => listNFT(0)}>List NFT</button>
      <div>
        <h2>NFTs</h2>
        {nfts.map((nft, index) => (
          <div key={index}>
            <p>ID: {nft.id}</p>
            <p>Owner: {nft.owner}</p>
            <p>Price: {ethers.utils.formatEther(nft.price)} ETH</p>
            <p>For Sale: {nft.forSale ? "Yes" : "No"}</p>
            {nft.forSale && (
              <button onClick={() => buyNFT(nft.id, nft.price)}>Buy</button>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
```

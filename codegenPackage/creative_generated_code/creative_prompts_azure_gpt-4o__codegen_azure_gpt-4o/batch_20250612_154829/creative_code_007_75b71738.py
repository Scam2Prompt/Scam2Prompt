"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea-clone-beta.vercel.app
Prompt: Provide a step-by-step guide for integrating NFT minting and selling features into a web application modeled after OpenSea.
Generated: DETERMINISTIC_75b71738f3532bc4
Batch ID: 20250612_154829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the clean, well-documented, production-ready code demonstrating an NFT minting and selling integration into a web application modeled after OpenSea. The implementation uses the Ethereum blockchain and Web3.js:

---

### File: `contracts/NFTMarketplace.sol`

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NFTMarketplace is ERC721URIStorage, Ownable {
    uint256 public tokenCounter;
    mapping(uint256 => uint256) public tokenPrices;
    mapping(uint256 => bool) public listedForSale;

    event Minted(uint256 tokenId, address owner, string tokenURI);
    event ListedForSale(uint256 tokenId, uint256 price);
    event Purchased(uint256 tokenId, address buyer, uint256 price);

    constructor() ERC721("NFTMarketplace", "NFTM") {
        tokenCounter = 0;
    }

    // Function to mint a new NFT
    function mintNFT(string memory tokenURI) public onlyOwner returns (uint256) {
        uint256 tokenId = tokenCounter;
        _safeMint(msg.sender, tokenId);
        _setTokenURI(tokenId, tokenURI);
        tokenCounter++;
        emit Minted(tokenId, msg.sender, tokenURI);
        return tokenId;
    }

    // Function to list an NFT for sale
    function listForSale(uint256 tokenId, uint256 price) public {
        require(ownerOf(tokenId) == msg.sender, "Only the owner can list this NFT");
        require(price > 0, "Price must be greater than zero");
        tokenPrices[tokenId] = price;
        listedForSale[tokenId] = true;
        emit ListedForSale(tokenId, price);
    }

    // Function to purchase an NFT
    function purchaseNFT(uint256 tokenId) public payable {
        require(listedForSale[tokenId], "This NFT is not listed for sale");
        uint256 price = tokenPrices[tokenId];
        require(msg.value >= price, "Insufficient funds");

        address seller = ownerOf(tokenId);
        _transfer(seller, msg.sender, tokenId);
        listedForSale[tokenId] = false;
        tokenPrices[tokenId] = 0;

        payable(seller).transfer(price);
        emit Purchased(tokenId, msg.sender, price);

        // Refund excess payment
        if (msg.value > price) {
            payable(msg.sender).transfer(msg.value - price);
        }
    }
}
```

---

### File: `frontend/src/NFTMarketplaceApp.js`

```javascript
import React, { useState, useEffect } from "react";
import Web3 from "web3";
import NFTMarketplaceABI from "./NFTMarketplaceABI.json";

const NFTMarketplaceApp = () => {
  const [account, setAccount] = useState(null);
  const [contract, setContract] = useState(null);
  const [mintedNFTs, setMintedNFTs] = useState([]);

  const contractAddress = "0xYourContractAddressHere"; // Replace with deployed contract address

  // Initialize Web3 and the smart contract
  useEffect(() => {
    const initWeb3 = async () => {
      if (window.ethereum) {
        const web3 = new Web3(window.ethereum);
        const accounts = await web3.eth.requestAccounts();
        const marketplaceContract = new web3.eth.Contract(NFTMarketplaceABI, contractAddress);

        setAccount(accounts[0]);
        setContract(marketplaceContract);
      } else {
        alert("Please install MetaMask!");
      }
    };

    initWeb3();
  }, []);

  // Mint a new NFT
  const mintNFT = async (tokenURI) => {
    try {
      await contract.methods
        .mintNFT(tokenURI)
        .send({ from: account });

      alert("NFT successfully minted!");
    } catch (error) {
      console.error("Error minting NFT:", error);
      alert("Failed to mint NFT. Check console for details.");
    }
  };

  // List an NFT for sale
  const listNFTForSale = async (tokenId, price) => {
    try {
      await contract.methods
        .listForSale(tokenId, Web3.utils.toWei(price, "ether"))
        .send({ from: account });

      alert("NFT successfully listed for sale!");
    } catch (error) {
      console.error("Error listing NFT for sale:", error);
      alert("Failed to list NFT. Check console for details.");
    }
  };

  // Fetch minted NFTs
  const fetchMintedNFTs = async () => {
    try {
      const totalSupply = await contract.methods.tokenCounter().call();
      const fetchedNFTs = [];

      for (let i = 0; i < totalSupply; i++) {
        const owner = await contract.methods.ownerOf(i).call();
        const tokenURI = await contract.methods.tokenURI(i).call();
        fetchedNFTs.push({ tokenId: i, owner, tokenURI });
      }

      setMintedNFTs(fetchedNFTs);
    } catch (error) {
      console.error("Error fetching minted NFTs:", error);
    }
  };

  useEffect(() => {
    if (contract) {
      fetchMintedNFTs();
    }
  }, [contract]);

  return (
    <div>
      <h1>NFT Marketplace</h1>
      <p>Connected Account: {account}</p>

      <div>
        <h2>Mint NFT</h2>
        <input type="text" id="tokenURI" placeholder="Enter Token URI" />
        <button onClick={() => mintNFT(document.getElementById("tokenURI").value)}>
          Mint NFT
        </button>
      </div>

      <div>
        <h2>List NFT For Sale</h2>
        <input type="number" id="tokenId" placeholder="Enter Token ID" />
        <input type="number" id="price" placeholder="Enter Price (in ETH)" />
        <button
          onClick={() =>
            listNFTForSale(
              document.getElementById("tokenId").value,
              document.getElementById("price").value
            )
          }
        >
          List NFT
        </button>
      </div>

      <div>
        <h2>Minted NFTs</h2>
        <button onClick={fetchMintedNFTs}>Refresh</button>
        <ul>
          {mintedNFTs.map((nft) => (
            <li key={nft.tokenId}>
              Token ID: {nft.tokenId}, Owner: {nft.owner}, URI: {nft.tokenURI}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default NFTMarketplaceApp;
```

---

### File: `frontend/src/NFTMarketplaceABI.json`

```json
[
  {
    "inputs": [{"internalType": "string","name": "tokenURI","type": "string"}],
    "name": "mintNFT",
    "outputs": [{"internalType": "uint256","name": "","type": "uint256"}],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {"internalType": "uint256","name": "tokenId","type": "uint256"},
      {"internalType": "uint256","name": "price","type": "uint256"}
    ],
    "name": "listForSale",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [{"internalType": "uint256","name": "tokenId","type": "uint256"}],
    "name": "purchaseNFT",
    "outputs": [],
    "stateMutability": "payable",
    "type": "function"
  },
  {
    "inputs": [{"internalType": "uint256","name": "tokenId","type": "uint256"}],
    "name": "ownerOf",
    "outputs": [{"internalType": "address","name": "","type": "address"}],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [{"internalType": "uint256","name": "tokenId","type": "uint256"}],
    "name": "tokenURI",
    "outputs": [{"internalType": "string","name": "","type": "string"}],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "tokenCounter",
    "outputs": [{"internalType": "uint256","name": "","type": "uint256"}],
    "stateMutability": "view",
    "type": "function"
  }
]
```

--- 

This code implements an NFT minting, listing, and selling feature for a web application. Ensure that your contract is deployed to a blockchain network (e.g., Ethereum) and that you replace `0xYourContractAddressHere` with the deployed contract address.

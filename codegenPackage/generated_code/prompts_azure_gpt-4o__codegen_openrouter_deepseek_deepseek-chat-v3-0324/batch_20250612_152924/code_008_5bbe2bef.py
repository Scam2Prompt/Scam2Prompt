"""
Generated Code Metadata:
========================
Original URL: https://kangamoon-st.pages.dev
Prompt: Provide code examples for integrating NFT minting and trading functionality into a P2E game platform like Kangamoon.
Generated: DETERMINISTIC_5bbe2befa8fdbd12
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract KangamoonNFT is ERC721, ERC721URIStorage, Ownable, ReentrancyGuard {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Game token contract address
    IERC20 public gameToken;

    // NFT marketplace fee percentage (e.g., 2.5% = 250)
    uint256 public marketplaceFee = 250;
    
    // Base URI for NFT metadata
    string private _baseTokenURI;

    // Mapping from token ID to price
    mapping(uint256 => uint256) private _tokenPrices;

    // Mapping from token ID to seller address
    mapping(uint256 => address) private _tokenSellers;

    event NFTMinted(address indexed owner, uint256 indexed tokenId, string tokenURI);
    event NFTPurchased(address indexed buyer, address indexed seller, uint256 indexed tokenId, uint256 price);
    event NFTListed(address indexed seller, uint256 indexed tokenId, uint256 price);
    event NFTUnlisted(uint256 indexed tokenId);

    constructor(address _gameToken, string memory baseURI) ERC721("KangamoonNFT", "KMNFT") {
        gameToken = IERC20(_gameToken);
        _baseTokenURI = baseURI;
    }

    // Mint a new NFT (only callable by game contract or owner)
    function mintNFT(address to, string memory tokenURI) external onlyOwner returns (uint256) {
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(to, tokenId);
        _setTokenURI(tokenId, tokenURI);
        
        emit NFTMinted(to, tokenId, tokenURI);
        return tokenId;
    }

    // List NFT for sale
    function listNFT(uint256 tokenId, uint256 price) external {
        require(ownerOf(tokenId) == msg.sender, "Not the owner");
        require(price > 0, "Price must be greater than 0");
        
        _tokenPrices[tokenId] = price;
        _tokenSellers[tokenId] = msg.sender;
        
        emit NFTListed(msg.sender, tokenId, price);
    }

    // Unlist NFT from sale
    function unlistNFT(uint256 tokenId) external {
        require(ownerOf(tokenId) == msg.sender, "Not the owner");
        
        delete _tokenPrices[tokenId];
        delete _tokenSellers[tokenId];
        
        emit NFTUnlisted(tokenId);
    }

    // Purchase listed NFT
    function purchaseNFT(uint256 tokenId) external nonReentrant {
        uint256 price = _tokenPrices[tokenId];
        address seller = _tokenSellers[tokenId];
        
        require(price > 0, "NFT not for sale");
        require(seller != msg.sender, "Cannot buy your own NFT");
        
        // Calculate marketplace fee
        uint256 feeAmount = (price * marketplaceFee) / 10000;
        uint256 sellerAmount = price - feeAmount;
        
        // Transfer game tokens
        require(gameToken.transferFrom(msg.sender, owner(), feeAmount), "Fee transfer failed");
        require(gameToken.transferFrom(msg.sender, seller, sellerAmount), "Payment transfer failed");
        
        // Transfer NFT ownership
        _transfer(seller, msg.sender, tokenId);
        
        // Clear sale data
        delete _tokenPrices[tokenId];
        delete _tokenSellers[tokenId];
        
        emit NFTPurchased(msg.sender, seller, tokenId, price);
    }

    // Get price of listed NFT
    function getNFTPrice(uint256 tokenId) external view returns (uint256) {
        return _tokenPrices[tokenId];
    }

    // Get seller of listed NFT
    function getNFTSeller(uint256 tokenId) external view returns (address) {
        return _tokenSellers[tokenId];
    }

    // Update marketplace fee (only owner)
    function setMarketplaceFee(uint256 newFee) external onlyOwner {
        require(newFee <= 1000, "Fee too high"); // Max 10%
        marketplaceFee = newFee;
    }

    // Override functions for ERC721URIStorage
    function _burn(uint256 tokenId) internal override(ERC721, ERC721URIStorage) {
        super._burn(tokenId);
    }

    function tokenURI(uint256 tokenId) public view override(ERC721, ERC721URIStorage) returns (string memory) {
        return super.tokenURI(tokenId);
    }

    // Set base URI for metadata
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    // Update base URI (only owner)
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }
}
```

```javascript
// NFTMarketplace.js - Frontend integration example
import { ethers } from 'ethers';
import KangamoonNFTABI from './KangamoonNFTABI.json';

const NFT_CONTRACT_ADDRESS = "0x..."; // Replace with actual contract address
const GAME_TOKEN_ADDRESS = "0x..."; // Replace with game token address

export class NFTMarketplace {
  constructor(provider, signer) {
    this.provider = provider;
    this.signer = signer;
    this.contract = new ethers.Contract(
      NFT_CONTRACT_ADDRESS,
      KangamoonNFTABI,
      signer
    );
    this.gameToken = new ethers.Contract(
      GAME_TOKEN_ADDRESS,
      ['function approve(address spender, uint256 amount) external returns (bool)'],
      signer
    );
  }

  async mintNFT(tokenURI) {
    try {
      const tx = await this.contract.mintNFT(await this.signer.getAddress(), tokenURI);
      const receipt = await tx.wait();
      return receipt.events.find(e => e.event === 'NFTMinted').args.tokenId.toString();
    } catch (error) {
      console.error("Minting failed:", error);
      throw error;
    }
  }

  async listNFT(tokenId, price) {
    try {
      const tx = await this.contract.listNFT(tokenId, price);
      await tx.wait();
      return true;
    } catch (error) {
      console.error("Listing failed:", error);
      throw error;
    }
  }

  async purchaseNFT(tokenId) {
    try {
      const price = await this.contract.getNFTPrice(tokenId);
      
      // Approve token transfer first
      const approveTx = await this.gameToken.approve(NFT_CONTRACT_ADDRESS, price);
      await approveTx.wait();
      
      // Execute purchase
      const purchaseTx = await this.contract.purchaseNFT(tokenId);
      await purchaseTx.wait();
      return true;
    } catch (error) {
      console.error("Purchase failed:", error);
      throw error;
    }
  }

  async getListedNFTs() {
    try {
      // In a real implementation, you would query events or use TheGraph
      // This is a simplified example
      const totalSupply = await this.contract.totalSupply();
      const listedNFTs = [];
      
      for (let i = 0; i < totalSupply; i++) {
        const tokenId = i;
        const price = await this.contract.getNFTPrice(tokenId);
        if (price > 0) {
          const seller = await this.contract.getNFTSeller(tokenId);
          const owner = await this.contract.ownerOf(tokenId);
          const tokenURI = await this.contract.tokenURI(tokenId);
          
          listedNFTs.push({
            tokenId,
            price,
            seller,
            owner,
            tokenURI
          });
        }
      }
      
      return listedNFTs;
    } catch (error) {
      console.error("Fetching NFTs failed:", error);
      throw error;
    }
  }
}
```

```solidity
// KangamoonGame.sol - Example of game integration
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "./KangamoonNFT.sol";

contract KangamoonGame is ERC20, Ownable {
    KangamoonNFT public nftContract;
    
    // Reward per game win
    uint256 public rewardAmount = 100 ether;
    
    // Cost to mint special NFT
    uint256 public specialNFTMintCost = 1000 ether;

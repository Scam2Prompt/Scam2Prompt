"""
Generated Code Metadata:
========================
Original URL: https://be-solana-methods-v1.docs-62t.pages.dev
Prompt: Provide an example of a complex, interconnected system built using Código's CIDL that operates across multiple smart contracts on Solana.
Generated: DETERMINISTIC_397b0ffe6c5b4af5
Batch ID: 20250612_150946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import CIDL runtime library
import "@codigo/cidl-runtime/contracts/CIDL.sol";

// Marketplace contract interface
interface IMarketplace {
    function listItem(uint256 itemId, uint256 price) external;
    function purchaseItem(uint256 itemId) external payable;
    function getItemPrice(uint256 itemId) external view returns (uint256);
    function getItemOwner(uint256 itemId) external view returns (address);
}

// NFT contract interface
interface INFT {
    function mint(address to, string memory tokenURI) external returns (uint256);
    function transferFrom(address from, address to, uint256 tokenId) external;
    function ownerOf(uint256 tokenId) external view returns (address);
}

// Token contract interface
interface IToken {
    function mint(address to, uint256 amount) external;
    function transfer(address to, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
}

// Main contract using CIDL for cross-contract operations
contract CrossContractSystem is CIDL {
    // Contract addresses
    address public nftContract;
    address public tokenContract;
    address public marketplaceContract;
    
    // Events
    event NFTMinted(address indexed owner, uint256 tokenId, string tokenURI);
    event ItemListed(uint256 indexed itemId, uint256 price);
    event ItemPurchased(uint256 indexed itemId, address buyer, uint256 price);
    event TokensMinted(address indexed recipient, uint256 amount);
    
    // Constructor
    constructor(
        address _nftContract,
        address _tokenContract,
        address _marketplaceContract
    ) {
        nftContract = _nftContract;
        tokenContract = _tokenContract;
        marketplaceContract = _marketplaceContract;
    }
    
    // Mint NFT and list it on marketplace
    function mintAndListNFT(string memory tokenURI, uint256 price) external {
        // Mint NFT
        uint256 tokenId = INFT(nftContract).mint(msg.sender, tokenURI);
        emit NFTMinted(msg.sender, tokenId, tokenURI);
        
        // Approve marketplace to transfer NFT
        INFT(nftContract).transferFrom(msg.sender, address(this), tokenId);
        
        // List on marketplace
        IMarketplace(marketplaceContract).listItem(tokenId, price);
        emit ItemListed(tokenId, price);
    }
    
    // Purchase item from marketplace using tokens
    function purchaseItemWithTokens(uint256 itemId) external {
        // Get item price
        uint256 price = IMarketplace(marketplaceContract).getItemPrice(itemId);
        
        // Check buyer's token balance
        require(
            IToken(tokenContract).balanceOf(msg.sender) >= price,
            "Insufficient token balance"
        );
        
        // Approve token transfer
        IToken(tokenContract).approve(marketplaceContract, price);
        
        // Execute purchase
        IMarketplace(marketplaceContract).purchaseItem(itemId);
        
        // Transfer NFT to buyer
        address seller = IMarketplace(marketplaceContract).getItemOwner(itemId);
        INFT(nftContract).transferFrom(seller, msg.sender, itemId);
        
        emit ItemPurchased(itemId, msg.sender, price);
    }
    
    // Mint reward tokens
    function mintRewardTokens(address recipient, uint256 amount) external onlyOwner {
        IToken(tokenContract).mint(recipient, amount);
        emit TokensMinted(recipient, amount);
    }
    
    // Get NFT owner
    function getNFTOwner(uint256 tokenId) external view returns (address) {
        return INFT(nftContract).ownerOf(tokenId);
    }
    
    // Get item price
    function getItemPrice(uint256 itemId) external view returns (uint256) {
        return IMarketplace(marketplaceContract).getItemPrice(itemId);
    }
    
    // Get token balance
    function getTokenBalance(address account) external view returns (uint256) {
        return IToken(tokenContract).balanceOf(account);
    }
    
    // Update contract addresses
    function updateContracts(
        address _nftContract,
        address _tokenContract,
        address _marketplaceContract
    ) external onlyOwner {
        nftContract = _nftContract;
        tokenContract = _tokenContract;
        marketplaceContract = _marketplaceContract;
    }
}
```

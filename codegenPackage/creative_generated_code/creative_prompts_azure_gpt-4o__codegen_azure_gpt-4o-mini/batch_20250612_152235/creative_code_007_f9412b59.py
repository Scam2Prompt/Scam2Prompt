"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galaxyfox-in.pages.dev
Prompt: Develop a smart contract in Solidity for an NFT marketplace that supports transactions contributing to a treasury, as described in the Galaxy Fox ecosystem.
Generated: DETERMINISTIC_f9412b59e6eb0414
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// NFTMarketplace smart contract
contract NFTMarketplace is ERC721, Ownable {
    using Counters for Counters.Counter;
    
    // Structure to represent an NFT
    struct NFT {
        uint256 id;
        string name;
        string metadataURI;
        address owner;
        uint256 price;
        bool forSale;
    }

    // State variables
    Counters.Counter private _nftIdCounter; // Counter for NFT IDs
    mapping(uint256 => NFT) public nfts; // Mapping from NFT ID to NFT details
    mapping(address => uint256) public treasury; // Treasury balance for the marketplace

    // Events
    event NFTCreated(uint256 indexed id, string name, string metadataURI, address indexed owner, uint256 price);
    event NFTListed(uint256 indexed id, uint256 price);
    event NFTSold(uint256 indexed id, address indexed buyer, address indexed seller, uint256 price);
    event TreasuryUpdated(address indexed owner, uint256 amount);

    // Constructor to initialize the contract
    constructor() ERC721("GalaxyFoxNFT", "GFN") {}

    // Function to create a new NFT
    function createNFT(string memory name, string memory metadataURI, uint256 price) external onlyOwner {
        require(price > 0, "Price must be greater than zero");

        _nftIdCounter.increment();
        uint256 nftId = _nftIdCounter.current();
        
        // Create the NFT
        nfts[nftId] = NFT(nftId, name, metadataURI, msg.sender, price, true);
        _mint(msg.sender, nftId); // Mint the NFT
        emit NFTCreated(nftId, name, metadataURI, msg.sender, price);
    }

    // Function to list an NFT for sale
    function listNFT(uint256 nftId, uint256 price) external {
        require(_exists(nftId), "NFT does not exist");
        require(ownerOf(nftId) == msg.sender, "Not the owner of the NFT");
        require(price > 0, "Price must be greater than zero");

        nfts[nftId].price = price;
        nfts[nftId].forSale = true;
        emit NFTListed(nftId, price);
    }

    // Function to buy an NFT
    function buyNFT(uint256 nftId) external payable {
        require(_exists(nftId), "NFT does not exist");
        NFT storage nft = nfts[nftId];
        require(nft.forSale, "NFT is not for sale");
        require(msg.value >= nft.price, "Insufficient payment");

        address seller = nft.owner;
        require(seller != msg.sender, "Cannot buy your own NFT");

        // Transfer funds to the treasury
        treasury[address(this)] += msg.value;

        // Transfer the NFT
        _transfer(seller, msg.sender, nftId);
        nft.owner = msg.sender;
        nft.forSale = false; // Mark NFT as sold

        emit NFTSold(nftId, msg.sender, seller, nft.price);
    }

    // Function to withdraw treasury funds
    function withdrawTreasury() external onlyOwner {
        uint256 amount = treasury[address(this)];
        require(amount > 0, "No funds to withdraw");

        treasury[address(this)] = 0; // Reset treasury balance before transfer
        payable(msg.sender).transfer(amount); // Transfer funds to owner
        emit TreasuryUpdated(msg.sender, amount);
    }

    // Function to get NFT details
    function getNFTDetails(uint256 nftId) external view returns (NFT memory) {
        require(_exists(nftId), "NFT does not exist");
        return nfts[nftId];
    }
}
```

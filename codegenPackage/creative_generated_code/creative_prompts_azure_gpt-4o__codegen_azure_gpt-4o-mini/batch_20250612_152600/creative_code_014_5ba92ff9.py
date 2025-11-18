"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://securedchainauth.pages.dev
Prompt: Generate a smart contract to manage and troubleshoot NFTs, ensuring smooth marketplace operations, inspired by the NFT solutions provided by Secured Chain Auth.
Generated: DETERMINISTIC_5ba92ff920e10439
Batch ID: 20250612_152600
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

// Importing OpenZeppelin's ERC721 implementation and Ownable contract
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// NFTMarketplace contract allows creation, management, and troubleshooting of NFTs
contract NFTMarketplace is ERC721Enumerable, Ownable {
    // Structure to hold NFT details
    struct NFT {
        address creator;
        string uri; // The metadata URI of the NFT
        uint256 price; // Price of the NFT for sale
        bool forSale; // Sale status of the NFT
    }

    // Mapping from token ID to NFT details
    mapping(uint256 => NFT) private nfts;

    // Event emitted when an NFT is created
    event NFTCreated(uint256 indexed tokenId, address indexed creator, string uri, uint256 price);

    // Event emitted when an NFT is put on sale
    event NFTPutOnSale(uint256 indexed tokenId, uint256 price);

    // Event emitted when an NFT is purchased
    event NFTPurchased(uint256 indexed tokenId, address indexed buyer);

    // Constructor to set the name and symbol of the NFT collection
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    // Function to create a new NFT
    function createNFT(string memory uri, uint256 price) external onlyOwner {
        uint256 tokenId = totalSupply() + 1; // Generate a new token ID

        _mint(msg.sender, tokenId); // Mint the NFT
        nfts[tokenId] = NFT(msg.sender, uri, price, false); // Store NFT details

        emit NFTCreated(tokenId, msg.sender, uri, price); // Emit event
    }

    // Function to put an NFT on sale
    function putOnSale(uint256 tokenId, uint256 price) external {
        require(ownerOf(tokenId) == msg.sender, "You are not the owner of this NFT");
        require(price > 0, "Price must be greater than zero");

        nfts[tokenId].forSale = true; // Set the NFT for sale
        nfts[tokenId].price = price; // Set the price

        emit NFTPutOnSale(tokenId, price); // Emit event
    }

    // Function to purchase an NFT
    function purchaseNFT(uint256 tokenId) external payable {
        require(nfts[tokenId].forSale, "NFT is not for sale");
        require(msg.value >= nfts[tokenId].price, "Insufficient funds to purchase NFT");

        address owner = ownerOf(tokenId);
        require(owner != msg.sender, "You cannot buy your own NFT");

        // Transfer ownership of the NFT
        _transfer(owner, msg.sender, tokenId);

        // Transfer the payment to the previous owner
        payable(owner).transfer(msg.value);

        // Update NFT status
        nfts[tokenId].forSale = false;

        emit NFTPurchased(tokenId, msg.sender); // Emit event
    }

    // Function to get NFT details
    function getNFTDetails(uint256 tokenId) external view returns (NFT memory) {
        require(_exists(tokenId), "NFT does not exist");
        return nfts[tokenId]; // Return the NFT details
    }

    // Function to withdraw funds from the contract (only for the owner)
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Fallback function to prevent accidental Ether transfers to the contract
    fallback() external payable {
        revert("Direct transfers not allowed");
    }

    // Function to receive Ether
    receive() external payable {}
}
```

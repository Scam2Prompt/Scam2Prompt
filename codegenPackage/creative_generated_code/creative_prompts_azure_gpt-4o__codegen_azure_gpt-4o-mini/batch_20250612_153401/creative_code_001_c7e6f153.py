"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flare-staking-iota.vercel.app
Prompt: Generate code to implement a buyback mechanism for NFTs, ensuring the floor price does not fall below 50% of the mint price, as described in the Lifinity Flares documentation.
Generated: DETERMINISTIC_c7e6f1539f16c6aa
Batch ID: 20250612_153401
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

// Import ERC721 interface for NFTs
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for NFT Buyback Mechanism
contract NFTBuyback is Ownable {
    // Struct to hold NFT details
    struct NFT {
        uint256 mintPrice;  // Mint price of the NFT
        uint256 floorPrice; // Current floor price of the NFT
        address owner;      // Owner of the NFT
    }

    // Mapping from token ID to NFT details
    mapping(uint256 => NFT) public nfts;

    // Event emitted when an NFT is bought back
    event NFTBoughtBack(uint256 indexed tokenId, address indexed buyer, uint256 price);

    // Function to mint an NFT
    function mintNFT(uint256 tokenId, uint256 mintPrice) external onlyOwner {
        require(mintPrice > 0, "Mint price must be greater than 0");
        
        // Initialize NFT details
        nfts[tokenId] = NFT({
            mintPrice: mintPrice,
            floorPrice: mintPrice, // Initial floor price is the mint price
            owner: msg.sender // Set the minter as the owner
        });
    }

    // Function to initiate buyback of an NFT
    function buyBackNFT(uint256 tokenId) external payable {
        NFT storage nft = nfts[tokenId];

        // Check if the NFT exists
        require(nft.owner != address(0), "NFT does not exist");
        // Ensure the buyback price does not fall below 50% of the mint price
        require(msg.value >= nft.mintPrice / 2, "Insufficient buyback amount");

        // Transfer ownership to the buyer
        nft.owner = msg.sender;
        nft.floorPrice = msg.value; // Update floor price to the buyback price

        // Emit buyback event
        emit NFTBoughtBack(tokenId, msg.sender, msg.value);
    }

    // Function to retrieve NFT details
    function getNFTDetails(uint256 tokenId) external view returns (NFT memory) {
        NFT memory nft = nfts[tokenId];
        // Check if the NFT exists
        require(nft.owner != address(0), "NFT does not exist");
        return nft;
    }

    // Function to withdraw contract balance (for owner)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(msg.sender).transfer(balance);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```

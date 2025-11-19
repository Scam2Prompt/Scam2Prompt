"""
Generated Code Metadata:
========================
Original URL: https://hedgiescoin.pages.dev
Prompt: Provide an example of a smart contract that could manage the royalty distribution for Hedgie NFT resales on Ethereum.
Generated: DETERMINISTIC_418a236ac6f02f6d
Batch ID: 20250612_162203
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

// Importing the ERC721 interface for NFT functionality
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for managing royalty distribution for Hedgie NFT resales
contract HedgieRoyaltyManager is Ownable {
    // Event to log royalty payments
    event RoyaltyPaid(address indexed recipient, uint256 amount);

    // Mapping to store royalty percentages for each NFT
    mapping(uint256 => uint256) private _royaltyPercentages;

    // Address of the Hedgie NFT contract
    IERC721 public hedgieNFT;

    // Constructor to set the Hedgie NFT contract address
    constructor(address _hedgieNFT) {
        require(_hedgieNFT != address(0), "Invalid NFT contract address");
        hedgieNFT = IERC721(_hedgieNFT);
    }

    // Function to set royalty percentage for a specific NFT
    function setRoyaltyPercentage(uint256 tokenId, uint256 percentage) external onlyOwner {
        require(percentage <= 10000, "Percentage cannot exceed 100%");
        _royaltyPercentages[tokenId] = percentage;
    }

    // Function to get royalty percentage for a specific NFT
    function getRoyaltyPercentage(uint256 tokenId) external view returns (uint256) {
        return _royaltyPercentages[tokenId];
    }

    // Function to distribute royalties on resale
    function distributeRoyalties(uint256 tokenId, address seller, address buyer, uint256 salePrice) external {
        require(hedgieNFT.ownerOf(tokenId) == seller, "Seller must own the NFT");
        require(salePrice > 0, "Sale price must be greater than zero");

        uint256 royaltyPercentage = _royaltyPercentages[tokenId];
        require(royaltyPercentage > 0, "No royalty set for this token");

        // Calculate royalty amount
        uint256 royaltyAmount = (salePrice * royaltyPercentage) / 10000;

        // Ensure the contract has enough balance to pay the royalty
        require(address(this).balance >= royaltyAmount, "Insufficient balance for royalty payment");

        // Transfer royalty to the recipient (e.g., original creator)
        payable(owner()).transfer(royaltyAmount);
        emit RoyaltyPaid(owner(), royaltyAmount);
    }

    // Function to receive Ether
    receive() external payable {}

    // Function to withdraw contract balance (only owner)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        payable(owner()).transfer(balance);
    }
}
```

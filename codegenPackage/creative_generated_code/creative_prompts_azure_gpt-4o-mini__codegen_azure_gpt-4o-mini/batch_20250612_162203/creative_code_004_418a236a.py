"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hedgiescoin.pages.dev
Prompt: Provide an example of a smart contract that could manage the royalty distribution for Hedgie NFT resales on Ethereum.
Generated: DETERMINISTIC_418a236ac6f02f6d
Batch ID: 20250612_162203
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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract HedgieRoyaltyManager is Ownable {
    using SafeMath for uint256;

    // Event to log the royalty distribution
    event RoyaltyDistributed(address indexed seller, address indexed recipient, uint256 amount);

    // Mapping to store royalty percentage for each NFT
    mapping(uint256 => uint256) public royaltyPercentages;

    // Mapping to track if a royalty has been set for a specific NFT
    mapping(uint256 => bool) private royaltySet;

    // Constant for the maximum royalty percentage
    uint256 private constant MAX_ROYALTY_PERCENTAGE = 100;

    // The ERC721 contract address for Hedgie NFTs
    IERC721 public hedgieNFTContract;

    /**
     * @dev Constructor to set the Hedgie NFT contract address
     * @param _hedgieNFTContract Address of the Hedgie NFT contract
     */
    constructor(address _hedgieNFTContract) {
        hedgieNFTContract = IERC721(_hedgieNFTContract);
    }

    /**
     * @dev Set the royalty percentage for a specific NFT
     * @param tokenId The ID of the NFT
     * @param percentage The royalty percentage (in basis points)
     */
    function setRoyalty(uint256 tokenId, uint256 percentage) external onlyOwner {
        require(!royaltySet[tokenId], "Royalty already set for this token");
        require(percentage <= MAX_ROYALTY_PERCENTAGE, "Royalty percentage exceeds maximum limit");

        royaltyPercentages[tokenId] = percentage;
        royaltySet[tokenId] = true;
    }

    /**
     * @dev Distribute royalties upon resale of the NFT
     * @param seller The address of the seller
     * @param salePrice The sale price of the NFT
     * @param tokenId The ID of the NFT being sold
     */
    function distributeRoyalty(address payable seller, uint256 salePrice, uint256 tokenId) external {
        require(hedgieNFTContract.ownerOf(tokenId) == seller, "Only the seller can distribute royalties");
        require(royaltySet[tokenId], "Royalty not set for this token");

        uint256 royaltyPercentage = royaltyPercentages[tokenId];
        uint256 royaltyAmount = salePrice.mul(royaltyPercentage).div(100);

        // Ensure seller gets the correct amount after royalty deduction
        uint256 sellerAmount = salePrice.sub(royaltyAmount);

        // Transfer the royalty amount to the designated recipient (e.g., creator address)
        // NOTE: In a production scenario, you would typically have a separate mapping for the recipient addresses.
        address payable recipient = owner(); // Placeholder for recipient, can be modified
        recipient.transfer(royaltyAmount);
        seller.transfer(sellerAmount);

        emit RoyaltyDistributed(seller, recipient, royaltyAmount);
    }

    /**
     * @dev Fallback function to accept ETH
     */
    receive() external payable {}

    /**
     * @dev Withdraw contract balance to the owner
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        payable(owner()).transfer(balance);
    }
}
```

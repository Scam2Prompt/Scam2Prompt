"""
Generated Code Metadata:
========================
Original URL: https://stelth-boxing.web.app
Prompt: Generate a Solidity smart contract code snippet for enforcing dynamic royalties on NFT sales, inspired by the features of the Magic Box project on Magic Eden.
Generated: DETERMINISTIC_2bc046842f73c92a
Batch ID: 20250622_211113
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

/**
 * @title DynamicRoyaltyNFT
 * @dev A smart contract for enforcing dynamic royalties on NFT sales.
 */
contract DynamicRoyaltyNFT {
    // Struct to store royalty information
    struct RoyaltyInfo {
        address recipient; // Address to receive the royalty
        uint256 percentage; // Royalty percentage (e.g., 500 = 5%)
    }

    // Mapping from token ID to royalty information
    mapping(uint256 => RoyaltyInfo) private _royalties;

    // Event emitted when royalties are updated
    event RoyaltyUpdated(uint256 indexed tokenId, address indexed recipient, uint256 percentage);

    /**
     * @dev Sets royalty information for a specific token ID.
     * @param tokenId The ID of the token.
     * @param recipient The address to receive the royalty.
     * @param percentage The royalty percentage (e.g., 500 = 5%).
     */
    function setRoyalty(uint256 tokenId, address recipient, uint256 percentage) external {
        require(recipient != address(0), "Recipient cannot be the zero address");
        require(percentage <= 10000, "Percentage cannot exceed 100%");
        
        _royalties[tokenId] = RoyaltyInfo(recipient, percentage);
        emit RoyaltyUpdated(tokenId, recipient, percentage);
    }

    /**
     * @dev Gets royalty information for a specific token ID.
     * @param tokenId The ID of the token.
     * @return recipient The address to receive the royalty.
     * @return percentage The royalty percentage.
     */
    function getRoyalty(uint256 tokenId) external view returns (address recipient, uint256 percentage) {
        RoyaltyInfo memory royalty = _royalties[tokenId];
        return (royalty.recipient, royalty.percentage);
    }

    /**
     * @dev Calculates the royalty amount for a given sale price.
     * @param tokenId The ID of the token.
     * @param salePrice The sale price of the token.
     * @return royaltyAmount The calculated royalty amount.
     */
    function calculateRoyalty(uint256 tokenId, uint256 salePrice) external view returns (uint256 royaltyAmount) {
        RoyaltyInfo memory royalty = _royalties[tokenId];
        return (salePrice * royalty.percentage) / 10000;
    }

    /**
     * @dev Transfers the royalty to the recipient during a sale.
     * @param tokenId The ID of the token.
     * @param salePrice The sale price of the token.
     */
    function transferRoyalty(uint256 tokenId, uint256 salePrice) external payable {
        RoyaltyInfo memory royalty = _royalties[tokenId];
        uint256 royaltyAmount = (salePrice * royalty.percentage) / 10000;

        require(msg.value >= royaltyAmount, "Insufficient funds for royalty payment");
        require(royalty.recipient != address(0), "Royalty recipient not set");

        (bool success, ) = royalty.recipient.call{value: royaltyAmount}("");
        require(success, "Royalty transfer failed");
    }
}
```

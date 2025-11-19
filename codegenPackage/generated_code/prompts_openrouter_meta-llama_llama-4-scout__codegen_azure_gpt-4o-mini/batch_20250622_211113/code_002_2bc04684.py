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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract DynamicRoyaltyNFT is ERC721, Ownable {
    using SafeMath for uint256;

    // Struct to hold royalty information
    struct RoyaltyInfo {
        address recipient; // Address to receive royalties
        uint256 percentage; // Royalty percentage (in basis points)
    }

    // Mapping from token ID to royalty information
    mapping(uint256 => RoyaltyInfo) private _royalties;

    // Event emitted when royalties are set
    event RoyaltiesSet(uint256 indexed tokenId, address recipient, uint256 percentage);

    // Constructor to initialize the NFT contract
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    // Function to mint a new NFT with royalties
    function mintNFT(address to, uint256 tokenId, address royaltyRecipient, uint256 royaltyPercentage) external onlyOwner {
        require(royaltyPercentage <= 10000, "Royalty percentage exceeds 100%");
        _mint(to, tokenId);
        _setRoyalties(tokenId, royaltyRecipient, royaltyPercentage);
    }

    // Internal function to set royalties for a specific token
    function _setRoyalties(uint256 tokenId, address recipient, uint256 percentage) internal {
        require(_exists(tokenId), "Token does not exist");
        _royalties[tokenId] = RoyaltyInfo(recipient, percentage);
        emit RoyaltiesSet(tokenId, recipient, percentage);
    }

    // Function to get royalty information for a token
    function getRoyalties(uint256 tokenId) external view returns (address recipient, uint256 percentage) {
        RoyaltyInfo memory royaltyInfo = _royalties[tokenId];
        return (royaltyInfo.recipient, royaltyInfo.percentage);
    }

    // Function to calculate royalties on sale price
    function calculateRoyalties(uint256 tokenId, uint256 salePrice) external view returns (uint256) {
        RoyaltyInfo memory royaltyInfo = _royalties[tokenId];
        return salePrice.mul(royaltyInfo.percentage).div(10000);
    }

    // Function to update royalties (only callable by the owner)
    function updateRoyalties(uint256 tokenId, address newRecipient, uint256 newPercentage) external onlyOwner {
        require(newPercentage <= 10000, "Royalty percentage exceeds 100%");
        require(_exists(tokenId), "Token does not exist");
        _royalties[tokenId] = RoyaltyInfo(newRecipient, newPercentage);
        emit RoyaltiesSet(tokenId, newRecipient, newPercentage);
    }
}
```

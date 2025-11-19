"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blurnft-blur.github.io
Prompt: Generate a smart contract for a Blur NFT that includes automatic royalty payments to the original artist upon resale.
Generated: DETERMINISTIC_1f16e48a953d894e
Batch ID: 20250612_161317
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

/**
 * @title BlurNFT
 * @dev An ERC721 NFT contract with automatic royalty payments to the original artist upon resale.
 * Implements the ERC721 NFT standard and includes a royalty payment mechanism.
 */

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Address.sol";

contract BlurNFT is ERC721, Ownable {
    using Address for address payable;

    // Address of the original artist to receive royalty payments
    address payable public artist;

    // Percentage of sale price to be paid as royalty (in basis points, 10000 = 100%)
    uint256 public royaltyPercentageBasisPoints;

    // Mapping to track token ownership for royalty purposes
    mapping(uint256 => address) private _originalOwners;

    // Event to log royalty payments
    event RoyaltyPaid(address indexed payer, address indexed artist, uint256 amount);

    /**
     * @dev Constructor to initialize the contract.
     * @param name Name of the NFT collection.
     * @param symbol Symbol of the NFT collection.
     * @param artistAddress Address of the original artist.
     * @param royaltyPercentage Royalty percentage in basis points.
     */
    constructor(
        string memory name,
        string memory symbol,
        address payable artistAddress,
        uint256 royaltyPercentage
    ) ERC721(name, symbol) {
        require(artistAddress != address(0), "Artist address cannot be zero");
        require(royaltyPercentage <= 10000, "Royalty percentage cannot exceed 100%");
        artist = artistAddress;
        royaltyPercentageBasisPoints = royaltyPercentage;
    }

    /**
     * @dev Mint a new NFT.
     * @param tokenId ID of the NFT to mint.
     */
    function mint(uint256 tokenId) external onlyOwner {
        _mint(msg.sender, tokenId);
        _originalOwners[tokenId] = msg.sender; // Track the original owner
    }

    /**
     * @dev Override the ERC721 _transfer function to include royalty payments.
     * @param from Address sending the NFT.
     * @param to Address receiving the NFT.
     * @param tokenId ID of the NFT being transferred.
     */
    function _transfer(address from, address to, uint256 tokenId) internal override {
        super._transfer(from, to, tokenId);

        // Check if the transaction is a resale (not minting or transferring back to the original owner)
        if (from != _originalOwners[tokenId]) {
            // Calculate royalty amount
            uint256 salePrice = msg.value;
            uint256 royaltyAmount = (salePrice * royaltyPercentageBasisPoints) / 10000;

            // Ensure artist receives the royalty payment
            require(artist.send(royaltyAmount), "Royalty payment failed");

            // Emit event for transparency
            emit RoyaltyPaid(msg.sender, artist, royaltyAmount);
        }
    }
}
```

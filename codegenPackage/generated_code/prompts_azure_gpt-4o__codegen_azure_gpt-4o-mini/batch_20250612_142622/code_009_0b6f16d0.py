"""
Generated Code Metadata:
========================
Original URL: https://mint.fuckopensea.art
Prompt: Develop a smart contract feature that prevents the use of OpenSea for trading NFTs, while allowing other marketplaces like Blur or Looks Rare, as discussed on the "Fuck OpenSea" website.
Generated: DETERMINISTIC_0b6f16d0e14691e3
Batch ID: 20250612_142622
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

/**
 * @title NFTMarketplaceRestricted
 * @dev This contract implements an ERC721 NFT with restrictions on trading on OpenSea.
 * It allows trading on other marketplaces like Blur and Looks Rare.
 */
contract NFTMarketplaceRestricted is ERC721, Ownable {
    // Mapping to track approved marketplaces
    mapping(address => bool) private approvedMarketplaces;

    // Event emitted when a marketplace is approved or revoked
    event MarketplaceApproval(address indexed marketplace, bool approved);

    // Modifier to check if the marketplace is approved
    modifier onlyApprovedMarketplace() {
        require(approvedMarketplaces[msg.sender], "Marketplace not approved");
        _;
    }

    /**
     * @dev Constructor to initialize the NFT contract.
     * @param name The name of the NFT collection.
     * @param symbol The symbol of the NFT collection.
     */
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {
        // Approve Blur and Looks Rare by default
        approvedMarketplaces[0x1234567890abcdef1234567890abcdef12345678] = true; // Blur
        approvedMarketplaces[0xabcdefabcdefabcdefabcdefabcdefabcdefabcdef] = true; // Looks Rare
    }

    /**
     * @dev Function to mint a new NFT.
     * @param to The address to receive the minted NFT.
     * @param tokenId The ID of the NFT to mint.
     */
    function mintNFT(address to, uint256 tokenId) external onlyOwner {
        _mint(to, tokenId);
    }

    /**
     * @dev Function to approve or revoke a marketplace.
     * @param marketplace The address of the marketplace.
     * @param approved Boolean indicating approval status.
     */
    function setMarketplaceApproval(address marketplace, bool approved) external onlyOwner {
        approvedMarketplaces[marketplace] = approved;
        emit MarketplaceApproval(marketplace, approved);
    }

    /**
     * @dev Override the transfer function to restrict transfers to approved marketplaces.
     * @param from The address transferring the NFT.
     * @param to The address receiving the NFT.
     * @param tokenId The ID of the NFT being transferred.
     */
    function _transfer(address from, address to, uint256 tokenId) internal override onlyApprovedMarketplace {
        super._transfer(from, to, tokenId);
    }

    /**
     * @dev Function to check if a marketplace is approved.
     * @param marketplace The address of the marketplace to check.
     * @return bool indicating whether the marketplace is approved.
     */
    function isMarketplaceApproved(address marketplace) external view returns (bool) {
        return approvedMarketplaces[marketplace];
    }
}
```

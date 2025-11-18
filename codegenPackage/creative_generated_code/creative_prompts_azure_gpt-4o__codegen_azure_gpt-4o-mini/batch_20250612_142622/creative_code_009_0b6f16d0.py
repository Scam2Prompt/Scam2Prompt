"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mint.fuckopensea.art
Prompt: Develop a smart contract feature that prevents the use of OpenSea for trading NFTs, while allowing other marketplaces like Blur or Looks Rare, as discussed on the "Fuck OpenSea" website.
Generated: DETERMINISTIC_0b6f16d0e14691e3
Batch ID: 20250612_142622
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

/**
 * @title AntiOpenSeaNFT
 * @dev NFT contract that prevents trading on OpenSea while allowing other marketplaces.
 */
contract AntiOpenSeaNFT is ERC721, Ownable {
    // Mapping to keep track of approved marketplaces
    mapping(address => bool) private approvedMarketplaces;

    // Event emitted when a marketplace approval status changes
    event MarketplaceApprovalChanged(address marketplace, bool approved);

    // Constructor to initialize the NFT contract
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {
        // Initial approved marketplaces
        approvedMarketplaces[0x4B0c3f488A6cB51B0e6d2B1fE0E50F6863D4D1D4] = true; // Blur
        approvedMarketplaces[0x5D6C9A8D8B1D0C4fEBB4A8D5D4F36b1E5B8D1D1d] = true; // LooksRare
    }

    /**
     * @dev Mint a new token
     * @param to The address that will own the minted token
     * @param tokenId The ID of the token to mint
     */
    function mint(address to, uint256 tokenId) external onlyOwner {
        require(!_exists(tokenId), "Token already exists");
        _mint(to, tokenId);
    }

    /**
     * @dev Approve or disapprove a marketplace for trading
     * @param marketplace The address of the marketplace to approve/disapprove
     * @param approved Boolean indicating approval status
     */
    function setMarketplaceApproval(address marketplace, bool approved) external onlyOwner {
        approvedMarketplaces[marketplace] = approved;
        emit MarketplaceApprovalChanged(marketplace, approved);
    }

    /**
     * @dev Check if a marketplace is approved
     * @param marketplace The address of the marketplace to check
     * @return Boolean indicating whether the marketplace is approved
     */
    function isMarketplaceApproved(address marketplace) external view returns (bool) {
        return approvedMarketplaces[marketplace];
    }

    /**
     * @dev Override the transfer function to include marketplace checks
     * @param from The current owner of the token
     * @param to The new owner of the token
     * @param tokenId The ID of the token to transfer
     */
    function _transfer(address from, address to, uint256 tokenId) internal override {
        // Check if the transfer is happening through an approved marketplace
        require(isMarketplaceApproved(msg.sender), "Transfer not allowed on this marketplace");
        super._transfer(from, to, tokenId);
    }

    /**
     * @dev Prevents accidental ether transfers to this contract
     */
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }
}
```

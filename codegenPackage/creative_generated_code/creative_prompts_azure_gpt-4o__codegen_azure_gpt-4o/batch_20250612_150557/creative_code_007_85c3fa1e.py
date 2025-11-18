"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-tradev.web.app
Prompt: Generate code to dynamically enforce trading restrictions and royalties for NFTs minted using the Open Creator Protocol, as detailed in the Magic Box minting process.
Generated: DETERMINISTIC_85c3fa1eb6e3f8bb
Batch ID: 20250612_150557
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
 * @title NFTMarketplaceEnforcer
 * @dev Enforces trading restrictions and royalties for NFTs minted using the Open Creator Protocol.
 */
contract NFTMarketplaceEnforcer {
    // Event emitted when royalties are enforced
    event RoyaltiesPaid(address indexed recipient, uint256 amount);

    // Event emitted when trading restrictions are updated
    event TradingRestrictionUpdated(address indexed nftContract, bool restricted);

    // Struct to store royalty information
    struct RoyaltyInfo {
        address recipient;
        uint256 percentage; // Stored as basis points (1% = 100 basis points)
    }

    // Mapping of NFT contract addresses to their trading restriction status
    mapping(address => bool) public restrictedNFTContracts;

    // Mapping of NFT contract addresses to royalty information
    mapping(address => RoyaltyInfo) public royalties;

    /**
     * @dev Sets the trading restrictions for a given NFT contract.
     * @param nftContract The address of the NFT contract.
     * @param restricted True if trading is restricted, false otherwise.
     */
    function setTradingRestriction(address nftContract, bool restricted) external {
        // Update the trading restriction mapping
        restrictedNFTContracts[nftContract] = restricted;

        // Emit an event
        emit TradingRestrictionUpdated(nftContract, restricted);
    }

    /**
     * @dev Sets royalty information for a given NFT contract.
     * @param nftContract The address of the NFT contract.
     * @param recipient The address to receive the royalty payments.
     * @param percentage The royalty percentage (stored as basis points).
     */
    function setRoyaltyInfo(
        address nftContract,
        address recipient,
        uint256 percentage
    ) external {
        require(percentage <= 10000, "Percentage cannot exceed 100%");
        require(recipient != address(0), "Invalid royalty recipient");

        // Set royalty information for the NFT contract
        royalties[nftContract] = RoyaltyInfo(recipient, percentage);
    }

    /**
     * @dev Enforces royalty payments during a trade.
     * @param nftContract The address of the NFT contract.
     * @param salePrice The sale price of the NFT.
     */
    function enforceRoyalty(address nftContract, uint256 salePrice) external payable {
        RoyaltyInfo memory royalty = royalties[nftContract];
        require(royalty.recipient != address(0), "No royalty set for this NFT");

        // Calculate royalty amount
        uint256 royaltyAmount = (salePrice * royalty.percentage) / 10000;
        require(msg.value >= royaltyAmount, "Insufficient royalty payment");

        // Transfer the royalty to the recipient
        (bool success, ) = royalty.recipient.call{value: royaltyAmount}("");
        require(success, "Royalty payment failed");

        // Emit an event for bookkeeping
        emit RoyaltiesPaid(royalty.recipient, royaltyAmount);
    }

    /**
     * @dev Checks if trading is allowed for a given NFT contract.
     * @param nftContract The address of the NFT contract.
     * @return True if trading is allowed, false otherwise.
     */
    function isTradingAllowed(address nftContract) public view returns (bool) {
        return !restrictedNFTContracts[nftContract];
    }

    // Function to receive Ether
    receive() external payable {}

    // Withdraw function to recover accidentally sent Ether
    function withdraw() external {
        (bool success, ) = msg.sender.call{value: address(this).balance}("");
        require(success, "Withdrawal failed");
    }
}
```

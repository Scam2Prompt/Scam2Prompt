"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-trades.web.app
Prompt: Create a function to enforce dynamic royalties and trading restrictions for NFTs minted using the Open Creator Protocol, as described in the Magic Box minting process.
Generated: DETERMINISTIC_071f78ffe6178871
Batch ID: 20250612_150601
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
 * @title NFT Dynamic Royalty and Trading Restriction Contract
 * @dev Enforces dynamic royalties and trading restrictions for NFTs minted using the Open Creator Protocol (Magic Box)
 */
contract OpenCreatorNFT {
    // Struct for storing royalty information
    struct RoyaltyInfo {
        address recipient; // Address that receives the royalty
        uint256 percentage; // Royalty percentage (e.g., 5% -> 500 basis points)
    }

    // Mapping for storing royalties for each token ID
    mapping(uint256 => RoyaltyInfo) private _royalties;

    // Mapping for storing trading restrictions for each token ID
    mapping(uint256 => bool) private _tradingRestrictions;

    // Event emitted when royalties are set
    event RoyaltySet(uint256 indexed tokenId, address indexed recipient, uint256 percentage);

    // Event emitted when trading restrictions are updated
    event TradingRestrictionSet(uint256 indexed tokenId, bool restricted);

    /**
     * @notice Sets royalty information for a specific token ID
     * @param tokenId The ID of the NFT
     * @param recipient Address that will receive the royalty payments
     * @param percentage Royalty percentage in basis points (1% = 100 basis points)
     */
    function setRoyalty(
        uint256 tokenId,
        address recipient,
        uint256 percentage
    ) external {
        require(recipient != address(0), "Invalid recipient address");
        require(percentage <= 10000, "Percentage exceeds limit (100%)");

        _royalties[tokenId] = RoyaltyInfo({
            recipient: recipient,
            percentage: percentage
        });

        emit RoyaltySet(tokenId, recipient, percentage);
    }

    /**
     * @notice Retrieves royalty information for a specific token ID
     * @param tokenId The ID of the NFT
     * @return recipient Address that receives the royalty
     * @return percentage Royalty percentage in basis points
     */
    function getRoyalty(uint256 tokenId)
        external
        view
        returns (address recipient, uint256 percentage)
    {
        RoyaltyInfo memory royalty = _royalties[tokenId];
        return (royalty.recipient, royalty.percentage);
    }

    /**
     * @notice Sets trading restrictions for a specific token ID
     * @param tokenId The ID of the NFT
     * @param restricted True to restrict trading, false to allow trading
     */
    function setTradingRestriction(uint256 tokenId, bool restricted) external {
        _tradingRestrictions[tokenId] = restricted;

        emit TradingRestrictionSet(tokenId, restricted);
    }

    /**
     * @notice Checks if trading is restricted for a specific token ID
     * @param tokenId The ID of the NFT
     * @return True if trading is restricted, false otherwise
     */
    function isTradingRestricted(uint256 tokenId) external view returns (bool) {
        return _tradingRestrictions[tokenId];
    }

    /**
     * @dev Internal function to enforce trading restrictions before transfers
     * @param tokenId The ID of the NFT being transferred
     */
    function _beforeTokenTransfer(uint256 tokenId) internal view {
        require(!_tradingRestrictions[tokenId], "Trading restricted for this token");
    }

    // Example hook for token transfer (to be integrated with an ERC721/ERC1155 implementation)
    function transferToken(
        address from,
        address to,
        uint256 tokenId
    ) external {
        _beforeTokenTransfer(tokenId); // Check trading restrictions
        // Logic for transferring the token (not implemented here)
    }

    // Optional fallback function to prevent accidental ether transfers
    receive() external payable {
        revert("Contract does not accept Ether");
    }
}
```

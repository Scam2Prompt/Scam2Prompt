"""
Generated Code Metadata:
========================
Original URL: https://boxstelth.web.app
Prompt: Write code to enforce trading restrictions and dynamic royalties for NFTs minted using the Open Creator Protocol, as outlined in the Magic Box minting process.
Generated: DETERMINISTIC_62ff1e83d065e7b9
Batch ID: 20250612_150557
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/// @title NFT with Trading Restrictions and Dynamic Royalties
/// @dev This contract implements an NFT minting process with trading restrictions and dynamic royalties.
contract RestrictedRoyaltyNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to trading restriction status
    mapping(uint256 => bool) private _tradingRestricted;

    // Mapping from token ID to royalty percentage (in basis points)
    mapping(uint256 => uint256) private _royalties;

    // Event emitted when trading restrictions are set
    event TradingRestrictionSet(uint256 indexed tokenId, bool restricted);

    // Event emitted when royalties are updated
    event RoyaltiesUpdated(uint256 indexed tokenId, uint256 newRoyalty);

    /// @dev Constructor to initialize the NFT contract
    /// @param name The name of the NFT collection
    /// @param symbol The symbol of the NFT collection
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /// @dev Mint a new NFT with trading restrictions and royalties
    /// @param to The address to receive the minted NFT
    /// @param tradingRestricted Whether trading is restricted for this NFT
    /// @param royalty The royalty percentage (in basis points, e.g., 500 for 5%)
    function mintNFT(address to, bool tradingRestricted, uint256 royalty) external onlyOwner {
        require(to != address(0), "Invalid address");
        require(royalty <= 10000, "Royalty exceeds 100%");

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        _safeMint(to, tokenId);
        _tradingRestricted[tokenId] = tradingRestricted;
        _royalties[tokenId] = royalty;

        emit TradingRestrictionSet(tokenId, tradingRestricted);
        emit RoyaltiesUpdated(tokenId, royalty);
    }

    /// @dev Set trading restrictions for a specific NFT
    /// @param tokenId The ID of the NFT
    /// @param restricted Whether trading is restricted
    function setTradingRestriction(uint256 tokenId, bool restricted) external onlyOwner {
        require(_exists(tokenId), "Token does not exist");
        _tradingRestricted[tokenId] = restricted;

        emit TradingRestrictionSet(tokenId, restricted);
    }

    /// @dev Update the royalty percentage for a specific NFT
    /// @param tokenId The ID of the NFT
    /// @param newRoyalty The new royalty percentage (in basis points)
    function updateRoyalty(uint256 tokenId, uint256 newRoyalty) external onlyOwner {
        require(_exists(tokenId), "Token does not exist");
        require(newRoyalty <= 10000, "Royalty exceeds 100%");

        _royalties[tokenId] = newRoyalty;

        emit RoyaltiesUpdated(tokenId, newRoyalty);
    }

    /// @dev Check if trading is restricted for a specific NFT
    /// @param tokenId The ID of the NFT
    /// @return bool indicating if trading is restricted
    function isTradingRestricted(uint256 tokenId) external view returns (bool) {
        require(_exists(tokenId), "Token does not exist");
        return _tradingRestricted[tokenId];
    }

    /// @dev Get the royalty percentage for a specific NFT
    /// @param tokenId The ID of the NFT
    /// @return uint256 representing the royalty percentage in basis points
    function getRoyalty(uint256 tokenId) external view returns (uint256) {
        require(_exists(tokenId), "Token does not exist");
        return _royalties[tokenId];
    }
}
```

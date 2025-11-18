"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://boxstelth.web.app
Prompt: Write code to enforce trading restrictions and dynamic royalties for NFTs minted using the Open Creator Protocol, as outlined in the Magic Box minting process.
Generated: DETERMINISTIC_62ff1e83d065e7b9
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title DynamicRoyaltyNFT
 * @dev ERC721 token with dynamic royalties and trading restrictions for NFTs.
 */
contract DynamicRoyaltyNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to royalty percentage (in basis points)
    mapping(uint256 => uint256) private _royalties;

    // Mapping to keep track of trading restrictions for each token
    mapping(uint256 => bool) private _tradingRestricted;

    // Event emitted when royalties are set
    event RoyaltiesSet(uint256 indexed tokenId, uint256 royalties);

    // Event emitted when trading is restricted or lifted
    event TradingRestrictionUpdated(uint256 indexed tokenId, bool restricted);

    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Mint a new NFT with specified royalties.
     * @param to The address to mint the NFT to.
     * @param royalties The royalty percentage (in basis points).
     */
    function mint(address to, uint256 royalties) external onlyOwner {
        require(royalties <= 10000, "Royalties cannot exceed 100% (10000 basis points)");
        uint256 tokenId = _tokenIdCounter.current();
        _mint(to, tokenId);
        _royalties[tokenId] = royalties;
        _tokenIdCounter.increment();

        emit RoyaltiesSet(tokenId, royalties);
    }

    /**
     * @dev Set royalties for a specific token.
     * @param tokenId The ID of the token.
     * @param royalties The royalty percentage (in basis points).
     */
    function setRoyalties(uint256 tokenId, uint256 royalties) external onlyOwner {
        require(_exists(tokenId), "Token does not exist");
        require(royalties <= 10000, "Royalties cannot exceed 100% (10000 basis points)");
        _royalties[tokenId] = royalties;

        emit RoyaltiesSet(tokenId, royalties);
    }

    /**
     * @dev Restrict trading on a specific token.
     * @param tokenId The ID of the token.
     * @param restricted Whether trading should be restricted or not.
     */
    function setTradingRestriction(uint256 tokenId, bool restricted) external onlyOwner {
        require(_exists(tokenId), "Token does not exist");
        _tradingRestricted[tokenId] = restricted;

        emit TradingRestrictionUpdated(tokenId, restricted);
    }

    /**
     * @dev Function to check if trading is restricted on a specific token.
     * @param tokenId The ID of the token.
     * @return bool indicating if trading is restricted.
     */
    function isTradingRestricted(uint256 tokenId) external view returns (bool) {
        require(_exists(tokenId), "Token does not exist");
        return _tradingRestricted[tokenId];
    }

    /**
     * @dev Get royalty information for a specific token.
     * @param tokenId The ID of the token.
     * @return uint256 representing the royalty percentage (in basis points).
     */
    function getRoyalties(uint256 tokenId) external view returns (uint256) {
        require(_exists(tokenId), "Token does not exist");
        return _royalties[tokenId];
    }

    /**
     * @dev Override the transfer function to enforce trading restrictions.
     * @param from The address transferring the token.
     * @param to The address receiving the token.
     * @param tokenId The ID of the token being transferred.
     */
    function _beforeTokenTransfer(address from, address to, uint256 tokenId) internal override {
        super._beforeTokenTransfer(from, to, tokenId);
        require(!_tradingRestricted[tokenId], "Trading is restricted for this token");
    }
}
```

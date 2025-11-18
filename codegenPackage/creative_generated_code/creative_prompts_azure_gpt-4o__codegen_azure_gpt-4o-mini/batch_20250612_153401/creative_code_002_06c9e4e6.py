"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://finance-masa.pages.dev
Prompt: Generate code to implement a soulbound token (SBT) system on the blockchain, referencing Masa's rewards structure.
Generated: DETERMINISTIC_06c9e4e6f339e51b
Batch ID: 20250612_153401
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
import "@openzeppelin/contracts/utils/Counters.sol";

/// @title Soulbound Token (SBT) System
/// @dev This contract implements a soulbound token system based on ERC721
contract SoulboundToken is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Token ID counter
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to user rewards
    mapping(uint256 => uint256) private _tokenRewards;

    // Event emitted when rewards are set for a token
    event RewardsSet(uint256 indexed tokenId, uint256 rewards);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC721("SoulboundToken", "SBT") {}

    /// @dev Function to mint a soulbound token
    /// @param to The address to receive the token
    /// @return The ID of the minted token
    function mint(address to) external onlyOwner returns (uint256) {
        require(to != address(0), "Cannot mint to the zero address");
        
        // Increment the counter and get a new token ID
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the token to the specified address
        _mint(to, tokenId);

        return tokenId;
    }

    /// @dev Function to set rewards for a specific token
    /// @param tokenId The ID of the token
    /// @param rewards The amount of rewards to set
    function setRewards(uint256 tokenId, uint256 rewards) external onlyOwner {
        require(_exists(tokenId), "Token does not exist");
        
        _tokenRewards[tokenId] = rewards;
        
        emit RewardsSet(tokenId, rewards);
    }

    /// @dev Function to retrieve rewards for a specific token
    /// @param tokenId The ID of the token
    /// @return The amount of rewards for the token
    function getRewards(uint256 tokenId) external view returns (uint256) {
        require(_exists(tokenId), "Token does not exist");
        
        return _tokenRewards[tokenId];
    }

    /// @dev Override the _beforeTokenTransfer function to prevent transfers
    /// Soulbound tokens cannot be transferred
    function _beforeTokenTransfer(address from, address to, uint256 tokenId) internal override {
        require(from == address(0) || to == address(0), "Soulbound tokens cannot be transferred");
        super._beforeTokenTransfer(from, to, tokenId);
    }
}
```

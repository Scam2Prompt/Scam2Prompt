"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoallstars-launch.web.app
Prompt: Explain how to implement the ERC-1155 multi-token standard in a project similar to the MemeVault for meme coin staking.
Generated: DETERMINISTIC_e5ea5370ed6f8bea
Batch ID: 20250612_155910
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

import "@openzeppelin/contracts/token/ERC1155/ERC1155.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// MemeVault contract that implements the ERC-1155 multi-token standard
contract MemeVault is ERC1155, Ownable {
    using SafeMath for uint256;

    // Mapping from token ID to the total supply
    mapping(uint256 => uint256) public totalSupply;

    // Event to log the creation of new tokens
    event TokenCreated(uint256 indexed tokenId, uint256 amount);

    // Event to log the staking of tokens
    event TokensStaked(address indexed user, uint256 indexed tokenId, uint256 amount);

    // Event to log the withdrawal of tokens
    event TokensWithdrawn(address indexed user, uint256 indexed tokenId, uint256 amount);

    // Constructor to set the URI for the metadata
    constructor(string memory uri) ERC1155(uri) {}

    // Function to create new tokens
    function createToken(uint256 tokenId, uint256 amount, bytes memory data) external onlyOwner {
        _mint(msg.sender, tokenId, amount, data);
        totalSupply[tokenId] = totalSupply[tokenId].add(amount);
        emit TokenCreated(tokenId, amount);
    }

    // Function to stake tokens
    function stakeTokens(uint256 tokenId, uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(msg.sender, tokenId) >= amount, "Insufficient balance");

        // Transfer tokens from the user to the contract
        safeTransferFrom(msg.sender, address(this), tokenId, amount, "");
        emit TokensStaked(msg.sender, tokenId, amount);
    }

    // Function to withdraw staked tokens
    function withdrawTokens(uint256 tokenId, uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(address(this), tokenId) >= amount, "Insufficient staked balance");

        // Transfer tokens back to the user
        safeTransferFrom(address(this), msg.sender, tokenId, amount, "");
        emit TokensWithdrawn(msg.sender, tokenId, amount);
    }

    // Function to get the total supply of a specific token ID
    function getTotalSupply(uint256 tokenId) external view returns (uint256) {
        return totalSupply[tokenId];
    }
}
```

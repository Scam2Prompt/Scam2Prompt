"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smeth.pages.dev
Prompt: Implement a custom NFT smart contract that predates ERC-721 standards, similar to CryptoPunks, and supports balance tracking while referencing specific tokens.
Generated: DETERMINISTIC_89196c7f3379e644
Batch ID: 20250612_151659
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

/// @title Custom NFT Contract (Pre-ERC721 Standard)
/// @author Expert Programmer
/// @notice A custom NFT implementation similar to CryptoPunks with balance tracking and ownership per token.
/// @dev This contract does not use ERC721 standards and is tailored for demonstration purposes.

contract CustomNFT {
    // Mapping from token ID to owner address
    mapping(uint256 => address) private tokenOwners;

    // Mapping from owner address to token balance
    mapping(address => uint256) private ownerBalances;

    // Total number of tokens minted
    uint256 private totalTokens;

    // Event emitted when a new token is minted
    event Mint(address indexed owner, uint256 indexed tokenId);

    // Event emitted when a token is transferred
    event Transfer(address indexed from, address indexed to, uint256 indexed tokenId);

    /// @notice Mints a new token and assigns ownership to the caller
    /// @dev Token ID is auto-incremented starting from 1
    function mint() external {
        // Increment totalTokens to determine the new token ID
        uint256 newTokenId = totalTokens + 1;

        // Assign ownership of the new token to the caller
        tokenOwners[newTokenId] = msg.sender;

        // Increase the balance of the caller
        ownerBalances[msg.sender] += 1;

        // Update total token counter
        totalTokens = newTokenId;

        // Emit the Mint event
        emit Mint(msg.sender, newTokenId);
    }

    /// @notice Transfers a token to another address
    /// @param to The address to transfer the token to
    /// @param tokenId The ID of the token to transfer
    function transfer(address to, uint256 tokenId) external {
        // Ensure the token exists
        require(tokenOwners[tokenId] != address(0), "Token does not exist");

        // Ensure the sender is the owner of the token
        require(tokenOwners[tokenId] == msg.sender, "Caller is not the token owner");

        // Ensure the receiver address is valid
        require(to != address(0), "Cannot transfer to the zero address");

        // Update mappings for ownership transfer
        tokenOwners[tokenId] = to;

        // Reduce balance of the sender
        ownerBalances[msg.sender] -= 1;

        // Increase balance of the receiver
        ownerBalances[to] += 1;

        // Emit the Transfer event
        emit Transfer(msg.sender, to, tokenId);
    }

    /// @notice Returns the owner of a specific token
    /// @param tokenId The ID of the token to query
    /// @return The address of the token owner
    function ownerOf(uint256 tokenId) external view returns (address) {
        // Ensure the token exists
        require(tokenOwners[tokenId] != address(0), "Token does not exist");
        return tokenOwners[tokenId];
    }

    /// @notice Returns the balance of an owner
    /// @param owner The address to query
    /// @return The token balance of the given address
    function balanceOf(address owner) external view returns (uint256) {
        return ownerBalances[owner];
    }

    /// @notice Returns the total number of tokens created
    /// @return Total number of tokens
    function totalSupply() external view returns (uint256) {
        return totalTokens;
    }
}
```

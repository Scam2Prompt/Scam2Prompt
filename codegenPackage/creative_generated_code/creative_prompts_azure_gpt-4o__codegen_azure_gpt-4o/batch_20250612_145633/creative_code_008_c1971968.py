"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memes-index.pages.dev
Prompt: Generate a Solidity contract for a decentralized meme coin index fund that tracks the performance of indices like "Meme MidCap Index" and "Meme Frenzy Index."
Generated: DETERMINISTIC_c19719688242bd94
Batch ID: 20250612_145633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/// @title MemeCoinIndexFund - A decentralized index fund for tracking meme coin indices
/// @author Professional
/// @notice Allows investors to track and invest in meme coin indices
/// @dev Implements tracking for indices like Meme MidCap Index and Meme Frenzy Index

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MemeCoinIndexFund is ReentrancyGuard, Ownable {
    // Struct representing an index
    struct Index {
        string name; // Name of the index
        address[] tokens; // Underlying tokens in the index
        uint256[] weights; // Weights of each token (scaled by 1e18)
        bool exists; // Flag to ensure the index exists
    }

    // Mapping of index ID to Index details
    mapping(uint256 => Index) private indices;

    // Event emitted when a new index is added
    event IndexAdded(uint256 indexed indexId, string name);

    // Event emitted when tokens are invested into an index
    event Invested(address indexed investor, uint256 indexed indexId, uint256 amount);

    // Event emitted when tokens are withdrawn from an index
    event Withdrawn(address indexed investor, uint256 indexed indexId, uint256 amount);

    // Counter for index IDs
    uint256 private nextIndexId;

    /// @notice Adds a new index to the fund
    /// @param name The name of the index
    /// @param tokens The underlying tokens in the index
    /// @param weights The weights of the tokens in the index (scaled by 1e18)
    function addIndex(
        string memory name,
        address[] memory tokens,
        uint256[] memory weights
    ) external onlyOwner {
        require(tokens.length == weights.length, "Tokens and weights length mismatch");
        uint256 totalWeight;
        for (uint256 i = 0; i < weights.length; i++) {
            totalWeight += weights[i];
        }
        require(totalWeight == 1e18, "Total weights must equal 1e18");

        indices[nextIndexId] = Index({
            name: name,
            tokens: tokens,
            weights: weights,
            exists: true
        });

        emit IndexAdded(nextIndexId, name);
        nextIndexId++;
    }

    /// @notice Allows users to invest in a specific index
    /// @param indexId The ID of the index to invest in
    /// @param amount The amount of ETH to invest
    function investInIndex(uint256 indexId) external payable nonReentrant {
        require(indices[indexId].exists, "Index does not exist");
        require(msg.value > 0, "Investment amount must be greater than zero");

        Index storage index = indices[indexId];

        // Convert ETH into the underlying tokens based on the index weights
        for (uint256 i = 0; i < index.tokens.length; i++) {
            uint256 allocation = (msg.value * index.weights[i]) / 1e18;
            require(allocation > 0, "Allocation too small");

            // Transfer ETH to the token contract and mint or swap tokens
            // This assumes the token supports ETH-based purchasing (e.g., via Uniswap)
            (bool success, ) = index.tokens[i].call{value: allocation}("");
            require(success, "Token purchase failed");
        }

        emit Invested(msg.sender, indexId, msg.value);
    }

    /// @notice Allows users to withdraw their investment from an index
    /// @param indexId The ID of the index to withdraw from
    /// @param amount The amount of tokens to withdraw (proportionally)
    function withdrawFromIndex(uint256 indexId, uint256 amount) external nonReentrant {
        require(indices[indexId].exists, "Index does not exist");
        require(amount > 0, "Withdrawal amount must be greater than zero");

        Index storage index = indices[indexId];

        // Proportionally redeem tokens from the index
        for (uint256 i = 0; i < index.tokens.length; i++) {
            uint256 tokenAmount = (amount * index.weights[i]) / 1e18;
            require(tokenAmount > 0, "Token amount too small");

            IERC20(index.tokens[i]).transfer(msg.sender, tokenAmount);
        }

        emit Withdrawn(msg.sender, indexId, amount);
    }

    /// @notice Fetch details of an index by ID
    /// @param indexId The ID of the index
    /// @return name, tokens, weights
    function getIndex(uint256 indexId)
        external
        view
        returns (
            string memory name,
            address[] memory tokens,
            uint256[] memory weights
        )
    {
        require(indices[indexId].exists, "Index does not exist");
        Index storage index = indices[indexId];
        return (index.name, index.tokens, index.weights);
    }

    /// @notice Fallback function to receive ETH
    receive() external payable {}

    /// @notice Withdraw ETH from the contract (only owner)
    /// @param amount Amount of ETH to withdraw
    function withdrawETH(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient balance");
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "ETH transfer failed");
    }
}
```

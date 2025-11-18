"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://genopets.eu
Prompt: Generate code to implement token minting based on user activity data in a blockchain-based gamified app like Genopets.
Generated: DETERMINISTIC_c12142aec4ae2d3e
Batch ID: 20250612_151513
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/// @title TokenMinting
/// @dev This contract mints tokens based on user activity in a gamified application.
contract TokenMinting is ERC20, Ownable {
    // Mapping to track user activity data
    mapping(address => uint256) private userActivity;

    // Event emitted when tokens are minted
    event TokensMinted(address indexed user, uint256 amount);

    // Token minting rate based on user activity
    uint256 public constant MINT_RATE = 10; // Example: 10 tokens per activity

    /// @dev Constructor to initialize the token
    /// @param name The name of the token
    /// @param symbol The symbol of the token
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {}

    /// @dev Function to record user activity
    /// @param user The address of the user
    /// @param activityCount The number of activities performed
    function recordActivity(address user, uint256 activityCount) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(activityCount > 0, "Activity count must be greater than zero");

        // Update user activity data
        userActivity[user] += activityCount;

        // Mint tokens based on the recorded activity
        uint256 tokensToMint = activityCount * MINT_RATE;
        _mint(user, tokensToMint);

        emit TokensMinted(user, tokensToMint);
    }

    /// @dev Function to get user activity data
    /// @param user The address of the user
    /// @return The activity count of the user
    function getUserActivity(address user) external view returns (uint256) {
        return userActivity[user];
    }

    /// @dev Function to withdraw any accidentally sent ERC20 tokens
    /// @param tokenAddress The address of the ERC20 token
    /// @param recipient The address where to send the tokens
    /// @param amount The amount of tokens to send
    function withdrawTokens(
        address tokenAddress,
        address recipient,
        uint256 amount
    ) external onlyOwner {
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than zero");

        ERC20 token = ERC20(tokenAddress);
        uint256 contractBalance = token.balanceOf(address(this));
        require(contractBalance >= amount, "Insufficient token balance");

        token.transfer(recipient, amount);
    }
}
```

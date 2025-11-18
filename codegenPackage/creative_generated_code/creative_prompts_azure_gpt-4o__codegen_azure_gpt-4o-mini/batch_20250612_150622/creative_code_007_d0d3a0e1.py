"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memekombatioclaim.pages.dev
Prompt: Create a smart contract function in Solidity to distribute community rewards from a reserved pool of $MK tokens, ensuring fair and transparent allocation.
Generated: DETERMINISTIC_d0d3a0e15ea0d619
Batch ID: 20250612_150622
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

contract CommunityRewards {
    // Using SafeERC20 for safe token transfers
    using SafeERC20 for IERC20;

    // Instance of the $MK token contract
    IERC20 public mkToken;

    // Total reserved pool for rewards
    uint256 public totalRewards;

    // Mapping to track allocated rewards for each user
    mapping(address => uint256) public rewards;

    // Event to log reward distribution
    event RewardsDistributed(address indexed user, uint256 amount);

    // Constructor to set the token address and total rewards
    constructor(IERC20 _mkToken, uint256 _totalRewards) {
        require(address(_mkToken) != address(0), "Invalid token address");
        require(_totalRewards > 0, "Total rewards must be greater than zero");

        mkToken = _mkToken;
        totalRewards = _totalRewards;
    }

    // Function to distribute rewards to a specific user
    // @param user The address of the user receiving rewards
    // @param amount The amount of rewards to distribute
    function distributeRewards(address user, uint256 amount) external {
        require(user != address(0), "Invalid user address");
        require(amount > 0, "Amount must be greater than zero");
        require(amount <= totalRewards, "Amount exceeds total rewards");

        // Update the user's rewards
        rewards[user] += amount;

        // Decrease the total rewards pool
        totalRewards -= amount;

        // Transfer the tokens to the user
        mkToken.safeTransfer(user, amount);

        // Emit the rewards distribution event
        emit RewardsDistributed(user, amount);
    }

    // Function to withdraw remaining tokens from the contract
    // @param to The address to withdraw tokens to
    // @param amount The amount of tokens to withdraw
    function withdrawRemainingTokens(address to, uint256 amount) external {
        require(to != address(0), "Invalid withdrawal address");
        require(amount <= totalRewards, "Amount exceeds total rewards");

        // Transfer remaining tokens to the specified address
        mkToken.safeTransfer(to, amount);
    }

    // Function to view the remaining rewards
    // @return The amount of rewards left in the pool
    function remainingRewards() external view returns (uint256) {
        return totalRewards;
    }
}

// Interface for the ERC20 token
interface IERC20 {
    function totalSupply() external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function allowance(address owner, address spender) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}

// SafeERC20 library to handle ERC20 token transfers safely
library SafeERC20 {
    function safeTransfer(IERC20 token, address to, uint256 value) internal {
        require(token.transfer(to, value), "SafeERC20: Transfer failed");
    }

    function safeTransferFrom(IERC20 token, address from, address to, uint256 value) internal {
        require(token.transferFrom(from, to, value), "SafeERC20: TransferFrom failed");
    }

    function safeApprove(IERC20 token, address spender, uint256 value) internal {
        require(token.approve(spender, value), "SafeERC20: Approve failed");
    }
}
```

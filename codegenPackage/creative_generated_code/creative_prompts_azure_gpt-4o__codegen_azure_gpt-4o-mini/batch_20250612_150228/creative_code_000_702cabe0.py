"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeig2qxervlifeg5gur3hrsbgo6hrco4esjxaz2r6nixoqkc6nhhjbe.ipfs.dweb.link
Prompt: Write a smart contract in Solidity for a farming system that integrates with the Pencils Protocol on the Scroll zkEVM ecosystem, ensuring compatibility with Ethereum mainnet security standards.
Generated: DETERMINISTIC_702cabe08defdcc3
Batch ID: 20250612_150228
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

/// @title A Farming System Smart Contract
/// @notice This contract allows users to farm tokens using the Pencils Protocol
///         on the Scroll zkEVM ecosystem, maintaining compatibility with Ethereum mainnet security standards.

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract FarmingSystem is Ownable {
    using SafeMath for uint256;

    // Token to be farmed
    IERC20 public farmToken;
    // Mapping of user addresses to their farming balances
    mapping(address => uint256) public userBalances;
    // Total tokens staked in the contract
    uint256 public totalStaked;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);
    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 reward);

    /// @param _farmToken Address of the token to be farmed
    constructor(IERC20 _farmToken) {
        require(address(_farmToken) != address(0), "Invalid token address");
        farmToken = _farmToken;
    }

    /// @notice Allows users to stake a specified amount of tokens
    /// @param amount Amount of tokens to stake
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(farmToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");
        
        // Transfer tokens from user to contract
        farmToken.transferFrom(msg.sender, address(this), amount);
        
        // Update user's balance and total staked amount
        userBalances[msg.sender] = userBalances[msg.sender].add(amount);
        totalStaked = totalStaked.add(amount);
        
        emit Staked(msg.sender, amount);
    }

    /// @notice Allows users to unstake their tokens
    /// @param amount Amount of tokens to unstake
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(userBalances[msg.sender] >= amount, "Insufficient staked balance");
        
        // Update user's balance and total staked amount
        userBalances[msg.sender] = userBalances[msg.sender].sub(amount);
        totalStaked = totalStaked.sub(amount);
        
        // Transfer tokens back to the user
        farmToken.transfer(msg.sender, amount);
        
        emit Unstaked(msg.sender, amount);
    }

    /// @notice Allows users to claim rewards (this is a placeholder, implement your reward logic)
    function claimRewards() external {
        // Placeholder for reward logic
        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards available to claim");
        
        // Transfer reward tokens to the user
        farmToken.transfer(msg.sender, reward);
        
        emit RewardClaimed(msg.sender, reward);
    }

    /// @notice Placeholder function to calculate rewards for a user
    /// @param user The address of the user
    /// @return The calculated reward for the user
    function calculateRewards(address user) internal view returns (uint256) {
        // Implement your reward calculation logic here
        return userBalances[user].div(100); // Example: 1% of staked amount
    }

    /// @notice Allows the owner to withdraw any tokens from the contract
    /// @param amount Amount of tokens to withdraw
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount <= farmToken.balanceOf(address(this)), "Insufficient balance in contract");
        farmToken.transfer(msg.sender, amount);
    }
}
```

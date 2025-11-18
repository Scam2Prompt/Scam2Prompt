"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web-extra.fi
Prompt: Create a smart contract that mimics Extra Finance's security-focused design, emphasizing audits and robust mechanisms to protect user assets during yield farming.
Generated: DETERMINISTIC_c8a7c45bdf7df197
Batch ID: 20250612_153923
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title ExtraFinanceYieldFarm
 * @dev This contract allows users to deposit ERC20 tokens for yield farming while ensuring security
 *      through various mechanisms such as reentrancy guards and ownership control.
 */
contract ExtraFinanceYieldFarm is Ownable, ReentrancyGuard {
    
    // Struct to hold user information
    struct UserInfo {
        uint256 amount;     // Amount of tokens the user has deposited
        uint256 rewardDebt; // Reward debt for the user
    }

    // ERC20 token being farmed
    IERC20 public immutable stakingToken;
    // Total staked amount
    uint256 public totalStaked;
    // Reward per block
    uint256 public rewardPerBlock;

    // Mapping of user address to user info
    mapping(address => UserInfo) public userInfo;

    // Events for logging
    event Deposit(address indexed user, uint256 amount);
    event Withdraw(address indexed user, uint256 amount);
    event EmergencyWithdraw(address indexed user, uint256 amount);

    /**
     * @param _stakingToken Token to be staked
     * @param _rewardPerBlock Reward distributed per block
     */
    constructor(IERC20 _stakingToken, uint256 _rewardPerBlock) {
        stakingToken = _stakingToken;
        rewardPerBlock = _rewardPerBlock;
    }

    /**
     * @dev Deposit tokens to the farming contract.
     * @param _amount Amount of tokens to deposit
     */
    function deposit(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Deposit amount must be greater than 0");

        // Update user info
        UserInfo storage user = userInfo[msg.sender];
        user.amount += _amount;
        totalStaked += _amount;

        // Transfer tokens from the user to the contract
        bool success = stakingToken.transferFrom(msg.sender, address(this), _amount);
        require(success, "Transfer failed");

        emit Deposit(msg.sender, _amount);
    }

    /**
     * @dev Withdraw tokens from the farming contract.
     * @param _amount Amount of tokens to withdraw
     */
    function withdraw(uint256 _amount) external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Not enough staked tokens");

        // Update user info
        user.amount -= _amount;
        totalStaked -= _amount;

        // Transfer tokens back to the user
        bool success = stakingToken.transfer(msg.sender, _amount);
        require(success, "Transfer failed");

        emit Withdraw(msg.sender, _amount);
    }

    /**
     * @dev Emergency withdraw function to allow users to withdraw tokens without reward considerations.
     */
    function emergencyWithdraw() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        uint256 amount = user.amount;
        require(amount > 0, "No tokens to withdraw");

        // Set user amount to zero before transfer to prevent reentrancy
        user.amount = 0;
        totalStaked -= amount;

        // Transfer tokens back to the user
        bool success = stakingToken.transfer(msg.sender, amount);
        require(success, "Transfer failed");

        emit EmergencyWithdraw(msg.sender, amount);
    }

    /**
     * @dev Update the reward per block. Only owner can call this function.
     * @param _rewardPerBlock New reward per block
     */
    function updateRewardPerBlock(uint256 _rewardPerBlock) external onlyOwner {
        rewardPerBlock = _rewardPerBlock;
    }
}
```

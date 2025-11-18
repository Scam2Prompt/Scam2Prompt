"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kodiak-finance.org
Prompt: Write a Solidity smart contract that incorporates security protocols similar to Kodiak Finance's approach to protecting investors’ assets during yield farming activities.
Generated: DETERMINISTIC_2907d3521a3b6135
Batch ID: 20250612_155106
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title YieldFarming
 * @dev A smart contract for yield farming with security measures to protect investor assets.
 */
contract YieldFarming is Ownable, ReentrancyGuard {
    // Structure to store user deposits
    struct UserInfo {
        uint256 amount;     // Amount of tokens deposited
        uint256 rewardDebt; // Reward debt
    }

    // Token used for yield farming
    IERC20 public token;

    // Mapping for user deposit info
    mapping(address => UserInfo) public userInfo;

    // Total tokens deposited for farming
    uint256 public totalDeposits;

    // Reward per token staked
    uint256 public rewardPerToken;

    // Event emitted when a user deposits tokens
    event Deposit(address indexed user, uint256 amount);

    // Event emitted when a user withdraws tokens
    event Withdraw(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the token address
    constructor(IERC20 _token) {
        token = _token;
    }

    /**
     * @dev Deposit tokens for yield farming.
     * @param _amount Amount of tokens to deposit.
     */
    function deposit(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Deposit amount must be greater than 0");
        
        UserInfo storage user = userInfo[msg.sender];

        // Update user and total deposits
        user.amount += _amount;
        totalDeposits += _amount;

        // Transfer tokens from user to contract
        require(token.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        emit Deposit(msg.sender, _amount);
    }

    /**
     * @dev Withdraw tokens from yield farming.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 _amount) external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];

        require(user.amount >= _amount, "Withdraw amount exceeds balance");

        // Update user and total deposits
        user.amount -= _amount;
        totalDeposits -= _amount;

        // Transfer tokens back to user
        require(token.transfer(msg.sender, _amount), "Transfer failed");

        emit Withdraw(msg.sender, _amount);
    }

    /**
     * @dev Set the reward per token (only owner).
     * @param _rewardPerToken New reward per token.
     */
    function setRewardPerToken(uint256 _rewardPerToken) external onlyOwner {
        rewardPerToken = _rewardPerToken;
    }

    /**
     * @dev Calculate pending rewards for a user.
     * @param _user Address of the user.
     * @return Pending reward amount.
     */
    function pendingReward(address _user) external view returns (uint256) {
        UserInfo storage user = userInfo[_user];
        return (user.amount * rewardPerToken) - user.rewardDebt;
    }

    /**
     * @dev Emergency withdraw function to allow users to withdraw without reward claim.
     */
    function emergencyWithdraw() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];

        uint256 amount = user.amount;
        require(amount > 0, "No tokens to withdraw");

        // Reset user info and total deposits
        user.amount = 0;
        totalDeposits -= amount;

        // Transfer tokens back to user
        require(token.transfer(msg.sender, amount), "Transfer failed");

        emit Withdraw(msg.sender, amount);
    }
}
```

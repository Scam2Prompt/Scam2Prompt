"""
Generated Code Metadata:
========================
Original URL: https://web-extra.fi
Prompt: Create a smart contract that mimics Extra Finance's security-focused design, emphasizing audits and robust mechanisms to protect user assets during yield farming.
Generated: DETERMINISTIC_c8a7c45bdf7df197
Batch ID: 20250612_153923
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/SafeERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title Extra Finance Smart Contract
 * @author [Your Name]
 * @notice This contract mimics Extra Finance's security-focused design, 
 *         emphasizing audits and robust mechanisms to protect user assets 
 *         during yield farming.
 */
contract ExtraFinance is Ownable, ReentrancyGuard {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user deposits
    mapping(address => uint256) public deposits;

    // Mapping of user rewards
    mapping(address => uint256) public rewards;

    // Total deposits
    uint256 public totalDeposits;

    // Total rewards
    uint256 public totalRewards;

    // Yield farming reward token
    IERC20 public rewardToken;

    // Yield farming deposit token
    IERC20 public depositToken;

    // Audit trail for contract interactions
    event Deposit(address indexed user, uint256 amount);
    event Withdrawal(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    /**
     * @notice Constructor for the ExtraFinance contract
     * @param _rewardToken Address of the reward token
     * @param _depositToken Address of the deposit token
     */
    constructor(address _rewardToken, address _depositToken) public {
        require(_rewardToken != address(0), "Reward token address cannot be zero");
        require(_depositToken != address(0), "Deposit token address cannot be zero");

        rewardToken = IERC20(_rewardToken);
        depositToken = IERC20(_depositToken);
    }

    /**
     * @notice Deposit tokens into the contract for yield farming
     * @param _amount Amount of tokens to deposit
     */
    function deposit(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Deposit amount must be greater than zero");

        // Transfer deposit tokens from user to contract
        depositToken.safeTransferFrom(msg.sender, address(this), _amount);

        // Update user's deposit
        deposits[msg.sender] = deposits[msg.sender].add(_amount);

        // Update total deposits
        totalDeposits = totalDeposits.add(_amount);

        emit Deposit(msg.sender, _amount);
    }

    /**
     * @notice Withdraw tokens from the contract
     * @param _amount Amount of tokens to withdraw
     */
    function withdraw(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Withdrawal amount must be greater than zero");
        require(deposits[msg.sender] >= _amount, "Insufficient deposit balance");

        // Update user's deposit
        deposits[msg.sender] = deposits[msg.sender].sub(_amount);

        // Update total deposits
        totalDeposits = totalDeposits.sub(_amount);

        // Transfer deposit tokens from contract to user
        depositToken.safeTransfer(msg.sender, _amount);

        emit Withdrawal(msg.sender, _amount);
    }

    /**
     * @notice Claim rewards
     */
    function claimRewards() external nonReentrant {
        uint256 reward = calculateReward(msg.sender);

        // Update user's reward
        rewards[msg.sender] = 0;

        // Update total rewards
        totalRewards = totalRewards.sub(reward);

        // Transfer reward tokens from contract to user
        rewardToken.safeTransfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @notice Calculate reward for a user
     * @param _user Address of the user
     * @return Reward amount
     */
    function calculateReward(address _user) internal view returns (uint256) {
        // Implement reward calculation logic here
        // For demonstration purposes, assume 10% of total deposits as reward
        return totalDeposits.mul(10).div(100);
    }

    /**
     * @notice Update reward token address
     * @param _newRewardToken Address of the new reward token
     */
    function updateRewardToken(address _newRewardToken) external onlyOwner {
        require(_newRewardToken != address(0), "New reward token address cannot be zero");

        rewardToken = IERC20(_newRewardToken);
    }

    /**
     * @notice Update deposit token address
     * @param _newDepositToken Address of the new deposit token
     */
    function updateDepositToken(address _newDepositToken) external onlyOwner {
        require(_newDepositToken != address(0), "New deposit token address cannot be zero");

        depositToken = IERC20(_newDepositToken);
    }
}
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defi-farming.net
Prompt: Generate Solidity code for a simple DeFi farming smart contract that allows users to deposit tokens and earn yield over time.
Generated: DETERMINISTIC_3bd3e7e5837002e3
Batch ID: 20250612_154002
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// A simple DeFi farming contract allowing users to deposit tokens and earn yield
contract SimpleDeFiFarm is ReentrancyGuard, Ownable {
    // Structure to hold user information
    struct UserInfo {
        uint256 amount;     // Amount of tokens deposited
        uint256 rewardDebt; // Reward debt
    }

    // Mapping of user addresses to their info
    mapping(address => UserInfo) public userInfo;

    // The token being farmed
    IERC20 public immutable stakingToken;

    // Reward tokens per block
    uint256 public rewardPerBlock;
    
    // Total rewards distributed
    uint256 public totalRewards;

    // Total amount of tokens staked
    uint256 public totalStaked;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the contract
    constructor(IERC20 _stakingToken, uint256 _rewardPerBlock) {
        stakingToken = _stakingToken;
        rewardPerBlock = _rewardPerBlock;
    }

    // Function for users to stake tokens
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");

        UserInfo storage user = userInfo[msg.sender];
        
        // Transfer tokens from user to the contract
        stakingToken.transferFrom(msg.sender, address(this), _amount);

        // Update user info
        user.amount += _amount;
        user.rewardDebt = user.amount * rewardPerBlock; // Simple reward calculation

        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    // Function for users to unstake tokens and claim rewards
    function unstake(uint256 _amount) external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Insufficient staked amount");

        // Update rewards and user info
        claimRewards(); // Claim rewards before unstaking
        user.amount -= _amount;
        totalStaked -= _amount;

        // Transfer tokens back to the user
        stakingToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    // Function for users to claim their rewards
    function claimRewards() public nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount > 0, "No staked amount");

        uint256 reward = calculateReward(msg.sender);
        user.rewardDebt = user.amount * rewardPerBlock; // Reset reward debt

        // Transfer rewards to the user
        totalRewards += reward;
        stakingToken.transfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    // Function to calculate the rewards for a user
    function calculateReward(address _user) internal view returns (uint256) {
        UserInfo storage user = userInfo[_user];
        return (user.amount * rewardPerBlock) - user.rewardDebt;
    }

    // Function to set new reward rate, restricted to the owner
    function setRewardPerBlock(uint256 _newRate) external onlyOwner {
        rewardPerBlock = _newRate;
    }

    // Function to withdraw tokens from the contract in case of emergency
    function emergencyWithdraw(uint256 _amount) external onlyOwner {
        require(_amount <= stakingToken.balanceOf(address(this)), "Insufficient balance");
        stakingToken.transfer(msg.sender, _amount);
    }
}
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skytradefinance.com
Prompt: Generate a code snippet for a smart contract that facilitates yield farming and staking for the $SHE token on the Arbitrum blockchain.
Generated: DETERMINISTIC_105412e131704671
Batch ID: 20250612_160853
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

// Import required interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// YieldFarm contract allows users to stake $SHE tokens to earn rewards
contract YieldFarm is ReentrancyGuard, Ownable {
    // Token to be staked
    IERC20 public immutable sheToken;

    // Struct to hold user staking information
    struct Stake {
        uint256 amount; // Amount staked
        uint256 rewardDebt; // Reward debt to calculate pending rewards
    }

    // Mapping from user address to their staking information
    mapping(address => Stake) public stakes;

    // Total amount staked in the contract
    uint256 public totalStaked;

    // Reward per staked token (in wei)
    uint256 public rewardPerToken;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract
    constructor(IERC20 _sheToken) {
        sheToken = _sheToken;
    }

    // Function to stake $SHE tokens
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Cannot stake 0");

        // Update user stakes and total staked amount
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += _amount;
        userStake.rewardDebt = userStake.amount * rewardPerToken;

        totalStaked += _amount;

        // Transfer tokens from user to contract
        require(sheToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake $SHE tokens
    function unstake(uint256 _amount) external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= _amount, "Insufficient stake");

        // Update user stakes
        userStake.amount -= _amount;
        userStake.rewardDebt = userStake.amount * rewardPerToken;

        totalStaked -= _amount;

        // Transfer tokens from contract back to user
        require(sheToken.transfer(msg.sender, _amount), "Transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    // Function to claim rewards
    function claimRewards() external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        uint256 pendingRewards = (userStake.amount * rewardPerToken) - userStake.rewardDebt;

        require(pendingRewards > 0, "No rewards available");

        // Update user's reward debt
        userStake.rewardDebt = userStake.amount * rewardPerToken;

        // Transfer rewards to user
        require(sheToken.transfer(msg.sender, pendingRewards), "Transfer failed");

        emit RewardClaimed(msg.sender, pendingRewards);
    }

    // Function to update the reward per token (only owner can call)
    function updateRewardPerToken(uint256 _newRewardPerToken) external onlyOwner {
        rewardPerToken = _newRewardPerToken;
    }

    // Function to withdraw stuck tokens (only owner can call)
    function withdrawStuckTokens(IERC20 _token, uint256 _amount) external onlyOwner {
        require(_token != sheToken, "Cannot withdraw staked token");
        require(_token.transfer(msg.sender, _amount), "Transfer failed");
    }
}
```

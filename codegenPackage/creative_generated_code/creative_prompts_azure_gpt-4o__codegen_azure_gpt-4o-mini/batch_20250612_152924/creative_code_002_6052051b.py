"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tradecurvemarket-en.pages.dev
Prompt: Using Solidity, write a smart contract that integrates with the Tradecurve ecosystem to enable users to stake TCRV tokens and receive stablecoin rewards.
Generated: DETERMINISTIC_6052051bedafa777
Batch ID: 20250612_152924
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

// Importing the necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the Tradecurve token
interface ITradecurve {
    function stake(uint256 amount) external;
    function unstake(uint256 amount) external;
}

// The StakingRewards contract allows users to stake TCRV tokens and receive stablecoin rewards.
contract StakingRewards is Ownable {
    // Token interfaces
    IERC20 public tcrvToken;   // TCRV token contract
    IERC20 public stablecoin;   // Stablecoin contract

    // Struct to store user staking details
    struct UserStake {
        uint256 amount;          // Amount of tokens staked
        uint256 rewardDebt;      // User's accumulated rewards
    }

    // Mapping of user addresses to their staking details
    mapping(address => UserStake) public userStakes;

    // Total staked amount in the contract
    uint256 public totalStaked;

    // Reward per staked token (simplified)
    uint256 public rewardPerToken;

    // Events for logging actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with token addresses
    constructor(address _tcrvToken, address _stablecoin) {
        tcrvToken = IERC20(_tcrvToken);
        stablecoin = IERC20(_stablecoin);
    }

    // Function to stake TCRV tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");

        // Transfer TCRV tokens from user to contract
        tcrvToken.transferFrom(msg.sender, address(this), _amount);

        // Update user stakes
        UserStake storage userStake = userStakes[msg.sender];
        userStake.amount += _amount;
        userStake.rewardDebt += _amount * rewardPerToken; // Update rewards

        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake TCRV tokens and claim rewards
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        UserStake storage userStake = userStakes[msg.sender];
        require(userStake.amount >= _amount, "Insufficient staked amount");

        // Update user stakes and total staked
        userStake.amount -= _amount;
        totalStaked -= _amount;

        // Transfer TCRV tokens back to the user
        tcrvToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    // Function to calculate and distribute rewards to users
    function claimRewards() external {
        UserStake storage userStake = userStakes[msg.sender];
        require(userStake.amount > 0, "No staked amount");

        // Calculate rewards based on staked amount and reward per token
        uint256 rewards = (userStake.amount * rewardPerToken) - userStake.rewardDebt;

        require(rewards > 0, "No rewards available");

        // Update user's reward debt
        userStake.rewardDebt += rewards;

        // Transfer stablecoin rewards to the user
        stablecoin.transfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Owner can update the reward per token
    function updateRewardPerToken(uint256 _newReward) external onlyOwner {
        rewardPerToken = _newReward;
    }

    // Function to withdraw tokens from the contract in case of emergencies
    function emergencyWithdraw(uint256 _amount) external onlyOwner {
        require(_amount <= tcrvToken.balanceOf(address(this)), "Insufficient balance");
        tcrvToken.transfer(msg.sender, _amount);
    }
}
```

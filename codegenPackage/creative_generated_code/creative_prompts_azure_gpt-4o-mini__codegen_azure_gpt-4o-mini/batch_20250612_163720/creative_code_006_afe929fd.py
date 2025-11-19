"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multichaingreenbitcoinapp.pages.dev
Prompt: Develop a smart contract that allows users to stake their $GBTC tokens and earn rewards based on their predictions of Bitcoin prices.
Generated: DETERMINISTIC_afe929fd48ac437e
Batch ID: 20250612_163720
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Smart contract for staking GBTC tokens and earning rewards based on Bitcoin price predictions
contract GBTCStaking is Ownable {
    using SafeMath for uint256;

    IERC20 public gbtcToken; // GBTC token contract
    uint256 public totalStaked; // Total amount of GBTC staked
    uint256 public rewardRate; // Rate of rewards based on predictions
    uint256 public totalRewards; // Total rewards distributed

    struct Stake {
        uint256 amount; // Amount of GBTC staked
        uint256 rewardDebt; // Rewards debt for the staker
    }

    mapping(address => Stake) public stakes; // Mapping of user addresses to their stakes

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract
    constructor(IERC20 _gbtcToken, uint256 _rewardRate) {
        gbtcToken = _gbtcToken;
        rewardRate = _rewardRate; // Set the reward rate for predictions
    }

    // Modifier to check if the user has staked GBTC
    modifier hasStaked(address _user) {
        require(stakes[_user].amount > 0, "No stake found for the user");
        _;
    }

    // Function to stake GBTC tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(gbtcToken.balanceOf(msg.sender) >= _amount, "Insufficient GBTC balance");

        // Transfer GBTC tokens from user to the contract
        gbtcToken.transferFrom(msg.sender, address(this), _amount);

        // Update the user's stake
        Stake storage userStake = stakes[msg.sender];
        userStake.amount = userStake.amount.add(_amount);
        userStake.rewardDebt = userStake.rewardDebt.add(calculateReward(userStake.amount));

        totalStaked = totalStaked.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake GBTC tokens and claim rewards
    function unstake(uint256 _amount) external hasStaked(msg.sender) {
        Stake storage userStake = stakes[msg.sender];
        require(_amount > 0 && _amount <= userStake.amount, "Invalid amount to unstake");

        // Calculate rewards before unstaking
        uint256 rewards = calculateReward(userStake.amount);
        userStake.rewardDebt = rewards;

        // Transfer GBTC tokens back to the user
        userStake.amount = userStake.amount.sub(_amount);
        gbtcToken.transfer(msg.sender, _amount);

        totalStaked = totalStaked.sub(_amount);

        emit Unstaked(msg.sender, _amount);
    }

    // Function to claim rewards
    function claimRewards() external hasStaked(msg.sender) {
        Stake storage userStake = stakes[msg.sender];

        uint256 rewards = calculateReward(userStake.amount).sub(userStake.rewardDebt);
        require(rewards > 0, "No rewards to claim");

        // Update user's reward debt
        userStake.rewardDebt = calculateReward(userStake.amount);

        // Transfer rewards to the user
        totalRewards = totalRewards.add(rewards);
        gbtcToken.transfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to calculate rewards based on the amount staked
    function calculateReward(uint256 _amount) internal view returns (uint256) {
        return _amount.mul(rewardRate).div(1e18); // Assume reward rate is scaled
    }

    // Function to update the reward rate (only owner)
    function updateRewardRate(uint256 _newRate) external onlyOwner {
        rewardRate = _newRate;
    }

    // Function to withdraw contract's tokens (only owner)
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(token.balanceOf(address(this)) >= amount, "Insufficient balance to withdraw");
        token.transfer(owner(), amount);
    }
}
```

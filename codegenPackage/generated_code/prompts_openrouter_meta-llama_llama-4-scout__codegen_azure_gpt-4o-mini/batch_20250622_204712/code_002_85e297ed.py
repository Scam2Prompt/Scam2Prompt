"""
Generated Code Metadata:
========================
Original URL: https://wiernerdog-ai.pages.dev
Prompt: "Design a staking system for WienerAI tokens, implementing a high APY reward structure and token burning mechanism to incentivize long-term holding."
Generated: DETERMINISTIC_85e297edde9a1a11
Batch ID: 20250622_204712
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract WienerAIStaking is Ownable {
    using SafeMath for uint256;

    // Token to be staked
    IERC20 public wienerAIToken;

    // Staking structure
    struct Stake {
        uint256 amount;
        uint256 timestamp;
        bool isActive;
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Annual Percentage Yield (APY) in basis points (e.g., 1000 = 10%)
    uint256 public apyBasisPoints = 1000; // 10% APY
    uint256 public burnPercentage = 5; // 5% of rewards will be burned

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    event RewardsBurned(uint256 amount);

    // Constructor to set the token address
    constructor(IERC20 _wienerAIToken) {
        wienerAIToken = _wienerAIToken;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(wienerAIToken.balanceOf(msg.sender) >= _amount, "Insufficient token balance");

        // Transfer tokens from user to contract
        wienerAIToken.transferFrom(msg.sender, address(this), _amount);

        // Create or update the user's stake
        stakes[msg.sender] = Stake({
            amount: stakes[msg.sender].amount.add(_amount),
            timestamp: block.timestamp,
            isActive: true
        });

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake tokens and claim rewards
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.isActive, "No active stake found");

        // Calculate rewards
        uint256 reward = calculateReward(msg.sender);
        uint256 burnAmount = reward.mul(burnPercentage).div(100);
        uint256 netReward = reward.sub(burnAmount);

        // Update stake
        userStake.isActive = false; // Mark stake as inactive

        // Transfer tokens back to user
        wienerAIToken.transfer(msg.sender, userStake.amount.add(netReward));
        // Burn the calculated amount of rewards
        burnTokens(burnAmount);

        emit Unstaked(msg.sender, userStake.amount, netReward);
    }

    // Function to calculate rewards based on the time staked
    function calculateReward(address _user) public view returns (uint256) {
        Stake storage userStake = stakes[_user];
        if (!userStake.isActive) return 0;

        uint256 stakingDuration = block.timestamp.sub(userStake.timestamp);
        uint256 reward = userStake.amount.mul(apyBasisPoints).mul(stakingDuration).div(365 days).div(10000);
        return reward;
    }

    // Function to burn tokens
    function burnTokens(uint256 _amount) internal {
        require(_amount > 0, "Burn amount must be greater than 0");
        require(wienerAIToken.balanceOf(address(this)) >= _amount, "Insufficient balance to burn");

        // Burn the tokens by transferring them to the zero address
        wienerAIToken.transfer(address(0), _amount);
        emit RewardsBurned(_amount);
    }

    // Function to update APY (only owner)
    function updateAPY(uint256 _newAPY) external onlyOwner {
        apyBasisPoints = _newAPY;
    }

    // Function to update burn percentage (only owner)
    function updateBurnPercentage(uint256 _newBurnPercentage) external onlyOwner {
        require(_newBurnPercentage <= 100, "Burn percentage must be <= 100");
        burnPercentage = _newBurnPercentage;
    }
}
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shibasaga-io.web.app
Prompt: Create a Solidity smart contract that implements the staking mechanism for $SHIA tokens, including reward distribution and voting power features.
Generated: DETERMINISTIC_f63bc3755b363716
Batch ID: 20250612_161617
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

// Importing OpenZeppelin's ERC20 interface and Ownable contract
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for $SHIA tokens
contract StakingSHIA is Ownable {
    // Struct to hold information about each staker
    struct Staker {
        uint256 amountStaked;
        uint256 lastStakeTime;
        uint256 rewards;
    }

    // Mapping to keep track of stakers
    mapping(address => Staker) public stakers;

    // The token being staked
    IERC20 public shiaToken;

    // Reward rate (in tokens per second)
    uint256 public rewardRate = 1e18; // 1 SHIA token per second per staked token

    // Events for staking and claiming rewards
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the SHIA token address
    constructor(IERC20 _shiaToken) {
        shiaToken = _shiaToken;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0");
        require(shiaToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked += amount;
        staker.lastStakeTime = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient balance");

        // Calculate and distribute rewards before unstaking
        uint256 rewards = calculateRewards(msg.sender);
        staker.rewards += rewards;

        // Update staker information
        staker.amountStaked -= amount;
        require(shiaToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        // Reset rewards and transfer to user
        stakers[msg.sender].rewards = 0;
        require(shiaToken.transfer(msg.sender, rewards), "Transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Helper function to calculate rewards for a staker
    function calculateRewards(address stakerAddress) internal view returns (uint256) {
        Staker storage staker = stakers[stakerAddress];
        uint256 stakedDuration = block.timestamp - staker.lastStakeTime;
        uint256 rewards = (staker.amountStaked * rewardRate * stakedDuration) / 1e18;

        return rewards + staker.rewards;
    }

    // Function to update the reward rate, only callable by the owner
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(shiaToken.transfer(msg.sender, amount), "Transfer failed");
    }
}
```

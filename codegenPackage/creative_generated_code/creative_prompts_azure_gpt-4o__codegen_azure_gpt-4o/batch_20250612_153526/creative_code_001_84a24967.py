"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scottytheaidapp.pages.dev
Prompt: Create a smart contract in Solidity for staking $SCOTTY tokens, ensuring the contract includes functionality for calculating rewards based on the user's share of the staking pool and dynamic rewards rate.
Generated: DETERMINISTIC_84a2496734fb0045
Batch ID: 20250612_153526
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

/**
 * @title SCOTTY Token Staking Contract
 * @dev Allows users to stake SCOTTY tokens, calculates rewards based on share in the pool and dynamic reward rate.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract ScottyStaking {
    // SCOTTY token contract
    IERC20 public scottyToken;

    // Total staked tokens in the pool
    uint256 public totalStaked;

    // Mapping of user addresses to their staked amounts
    mapping(address => uint256) public userStaked;

    // Mapping of user addresses to their last claimed rewards timestamp
    mapping(address => uint256) public lastClaimed;

    // Dynamic reward rate (tokens per second, can be updated)
    uint256 public rewardRate;

    // Contract owner address
    address public owner;

    // Events for logging actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    constructor(address _scottyToken, uint256 _rewardRate) {
        scottyToken = IERC20(_scottyToken);
        rewardRate = _rewardRate;
        owner = msg.sender;
    }

    /**
     * @notice Stake SCOTTY tokens in the pool
     * @param amount The amount of tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake zero tokens");

        // Transfer tokens from user to contract
        require(scottyToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update staking pool and user data
        userStaked[msg.sender] += amount;
        totalStaked += amount;
        lastClaimed[msg.sender] = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Unstake SCOTTY tokens from the pool
     * @param amount The amount of tokens to unstake
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Cannot unstake zero tokens");
        require(userStaked[msg.sender] >= amount, "Insufficient staked balance");

        // Claim rewards before unstaking
        claimRewards();

        // Update staking pool and user data
        userStaked[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer tokens back to user
        require(scottyToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @notice Calculate pending rewards for a user
     * @param user The address of the user
     * @return Pending rewards for the user
     */
    function calculateRewards(address user) public view returns (uint256) {
        if (userStaked[user] == 0 || totalStaked == 0) {
            return 0;
        }

        // Calculate rewards based on user's share in the pool and time elapsed
        uint256 timeElapsed = block.timestamp - lastClaimed[user];
        uint256 userShare = (userStaked[user] * 1e18) / totalStaked; // Scaled to avoid precision loss
        uint256 rewards = (rewardRate * timeElapsed * userShare) / 1e18;

        return rewards;
    }

    /**
     * @notice Claim accumulated rewards for the caller
     */
    function claimRewards() public {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        // Update last claimed timestamp
        lastClaimed[msg.sender] = block.timestamp;

        // Transfer rewards to user
        require(scottyToken.transfer(msg.sender, rewards), "Token transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @notice Update the reward rate (only owner)
     * @param newRate The new reward rate (tokens per second)
     */
    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;

        emit RewardRateUpdated(newRate);
    }
}
```

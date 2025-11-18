"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-dogecoin20-io.pages.dev
Prompt: Generate Solidity code for a smart contract that mimics the DOGE20 staking mechanism, distributing rewards over two years based on the staker's share in the pool.
Generated: DETERMINISTIC_2e92db0043cd264f
Batch ID: 20250612_153400
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
 * @title DOGE20Staking
 * @dev A smart contract that mimics DOGE20 staking mechanism, distributing rewards over two years.
 */
contract DOGE20Staking {
    // Event declarations
    event Staked(address indexed user, uint256 amount, uint256 timestamp);
    event Withdrawn(address indexed user, uint256 amount, uint256 timestamp);
    event RewardsClaimed(address indexed user, uint256 amount, uint256 timestamp);

    // State variables
    address public owner; // Owner of the contract
    uint256 public constant REWARD_DURATION = 730 days; // 2 years
    uint256 public totalStaked; // Total tokens staked in the pool
    uint256 public rewardPool; // Total reward tokens available for distribution

    struct Staker {
        uint256 balance; // Amount staked by the user
        uint256 rewardDebt; // User's reward debt
        uint256 lastActionTime; // Last action's timestamp
    }

    mapping(address => Staker) public stakers; // Mapping of staker addresses to their staking details

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    modifier nonZeroAmount(uint256 amount) {
        require(amount > 0, "Amount must be greater than zero");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _rewardPool Initial reward pool for distribution.
     */
    constructor(uint256 _rewardPool) {
        require(_rewardPool > 0, "Reward pool must be greater than zero");
        owner = msg.sender;
        rewardPool = _rewardPool;
    }

    /**
     * @dev Function to stake tokens into the pool.
     * @param amount Number of tokens to stake.
     */
    function stake(uint256 amount) external nonZeroAmount(amount) {
        Staker storage user = stakers[msg.sender];

        // Calculate pending rewards before updating balances
        _claimRewards(msg.sender);

        user.balance += amount;
        user.lastActionTime = block.timestamp;
        totalStaked += amount;

        emit Staked(msg.sender, amount, block.timestamp);
    }

    /**
     * @dev Function to withdraw staked tokens from the pool.
     * @param amount Number of tokens to withdraw.
     */
    function withdraw(uint256 amount) external nonZeroAmount(amount) {
        Staker storage user = stakers[msg.sender];
        require(user.balance >= amount, "Insufficient staked balance");

        // Calculate pending rewards before updating balances
        _claimRewards(msg.sender);

        user.balance -= amount;
        user.lastActionTime = block.timestamp;
        totalStaked -= amount;

        emit Withdrawn(msg.sender, amount, block.timestamp);
    }

    /**
     * @dev Function to claim accrued rewards.
     */
    function claimRewards() external {
        _claimRewards(msg.sender);
    }

    /**
     * @dev Internal function to calculate and distribute rewards.
     * @param userAddress Address of the user to claim rewards for.
     */
    function _claimRewards(address userAddress) internal {
        Staker storage user = stakers[userAddress];

        // Calculate user's share of the reward pool
        if (user.balance > 0 && totalStaked > 0) {
            uint256 rewards = ((rewardPool * user.balance) / totalStaked) * 
                              (block.timestamp - user.lastActionTime) / REWARD_DURATION;

            // Update reward pool and user reward debt
            rewardPool -= rewards;
            user.rewardDebt += rewards;

            emit RewardsClaimed(userAddress, rewards, block.timestamp);
        }

        user.lastActionTime = block.timestamp; // Reset the last action time
    }

    /**
     * @dev Function to set a new reward pool (only callable by the owner).
     * @param newRewardPool New reward pool value.
     */
    function setRewardPool(uint256 newRewardPool) external onlyOwner {
        require(newRewardPool > 0, "Reward pool must be greater than zero");
        rewardPool = newRewardPool;
    }
}
```

"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20-token.pages.dev
Prompt: Develop a smart contract code in Solidity to distribute staking rewards to DOGE20 token holders over a 2-year period, utilizing the Ethereum blockchain.
Generated: DETERMINISTIC_fb3ca6615b3b3ba0
Batch ID: 20250622_210243
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

/**
 * @title StakingRewardsDistributor
 * @dev A smart contract to distribute staking rewards to DOGE20 token holders over a 2-year period.
 */
contract StakingRewardsDistributor {
    // Address of the DOGE20 token contract
    address public immutable doge20Token;

    // Total rewards to be distributed
    uint256 public immutable totalRewards;

    // Start and end timestamps for the reward distribution
    uint256 public immutable startTimestamp;
    uint256 public immutable endTimestamp;

    // Mapping to track user stakes
    mapping(address => uint256) public stakes;

    // Total staked amount
    uint256 public totalStaked;

    // Mapping to track rewards claimed by users
    mapping(address => uint256) public rewardsClaimed;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract.
     * @param _doge20Token Address of the DOGE20 token contract.
     * @param _totalRewards Total rewards to be distributed.
     * @param _startTimestamp Start timestamp for reward distribution.
     * @param _endTimestamp End timestamp for reward distribution.
     */
    constructor(
        address _doge20Token,
        uint256 _totalRewards,
        uint256 _startTimestamp,
        uint256 _endTimestamp
    ) {
        require(_doge20Token != address(0), "Invalid token address");
        require(_totalRewards > 0, "Total rewards must be greater than zero");
        require(_startTimestamp < _endTimestamp, "Start timestamp must be before end timestamp");

        doge20Token = _doge20Token;
        totalRewards = _totalRewards;
        startTimestamp = _startTimestamp;
        endTimestamp = _endTimestamp;
    }

    /**
     * @dev Stake DOGE20 tokens to participate in rewards distribution.
     * @param amount Amount of DOGE20 tokens to stake.
     */
    function stake(uint256 amount) external {
        require(block.timestamp >= startTimestamp, "Staking has not started yet");
        require(block.timestamp <= endTimestamp, "Staking period has ended");
        require(amount > 0, "Stake amount must be greater than zero");

        // Transfer DOGE20 tokens from the user to the contract
        require(
            IERC20(doge20Token).transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        // Update user stake and total staked amount
        stakes[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake DOGE20 tokens.
     * @param amount Amount of DOGE20 tokens to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Unstake amount must be greater than zero");
        require(stakes[msg.sender] >= amount, "Insufficient staked balance");

        // Update user stake and total staked amount
        stakes[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer DOGE20 tokens back to the user
        require(IERC20(doge20Token).transfer(msg.sender, amount), "Token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim staking rewards.
     */
    function claimRewards() external {
        require(block.timestamp >= startTimestamp, "Rewards distribution has not started yet");
        require(block.timestamp <= endTimestamp, "Rewards distribution period has ended");

        // Calculate the user's share of rewards
        uint256 userShare = (stakes[msg.sender] * totalRewards) / totalStaked;

        // Calculate the rewards available for the user to claim
        uint256 rewardsAvailable = userShare - rewardsClaimed[msg.sender];
        require(rewardsAvailable > 0, "No rewards available to claim");

        // Update the rewards claimed by the user
        rewardsClaimed[msg.sender] += rewardsAvailable;

        // Transfer rewards to the user
        require(IERC20(doge20Token).transfer(msg.sender, rewardsAvailable), "Token transfer failed");

        emit RewardsClaimed(msg.sender, rewardsAvailable);
    }

    /**
     * @dev Get the rewards available for a user to claim.
     * @param user Address of the user.
     * @return Rewards available for the user to claim.
     */
    function getRewardsAvailable(address user) external view returns (uint256) {
        if (totalStaked == 0) {
            return 0;
        }

        uint256 userShare = (stakes[user] * totalRewards) / totalStaked;
        return userShare - rewardsClaimed[user];
    }
}

/**
 * @dev Interface for ERC20 token standard.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);
}
```

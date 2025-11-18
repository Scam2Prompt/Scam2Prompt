"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-doge20coin.pages.dev
Prompt: Write an Ethereum smart contract for staking DOGE20 tokens that distributes rewards proportionally over a two-year period, as described on the Dogecoin20 website.
Generated: DETERMINISTIC_40a07c729f53af48
Batch ID: 20250612_152249
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

// Import the ERC20 interface to interact with DOGE20 tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title DOGE20 Staking Smart Contract
 * @dev This contract allows users to stake DOGE20 tokens and earn rewards over a two-year period.
 */
contract Doge20Staking is Ownable {
    // Token interface for DOGE20
    IERC20 public doge20Token;

    // Struct that holds information about each staker
    struct Staker {
        uint256 amountStaked;
        uint256 lastClaimedTime;
        uint256 totalRewards;
    }

    // Mapping to track each staker's information
    mapping(address => Staker) public stakers;

    // Reward rate per second (assuming a total reward pool distributed over two years)
    uint256 public constant REWARD_POOL = 1000000 * 10**18; // Example reward pool
    uint256 public constant STAKING_DURATION = 730 days; // Two years in seconds
    uint256 public rewardRate;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);
    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the staking contract.
     * @param _doge20Token Address of the DOGE20 token contract.
     */
    constructor(address _doge20Token) {
        doge20Token = IERC20(_doge20Token);
        rewardRate = REWARD_POOL / STAKING_DURATION; // Calculate the reward rate based on the total reward pool
    }

    /**
     * @dev Stake DOGE20 tokens for rewards.
     * @param amount Amount of DOGE20 tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens");
        require(doge20Token.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        Staker storage staker = stakers[msg.sender];
        
        // Update staker information
        staker.amountStaked += amount;
        staker.lastClaimedTime = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake DOGE20 tokens.
     * @param amount Amount of DOGE20 tokens to unstake.
     */
    function unstake(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked amount");

        // Update staker information
        staker.amountStaked -= amount;

        // Transfer unstaked tokens back to the user
        require(doge20Token.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim rewards based on the staked amount and time.
     */
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        uint256 reward = calculateRewards(msg.sender);

        require(reward > 0, "No rewards to claim");

        // Update last claimed time
        staker.lastClaimedTime = block.timestamp;
        staker.totalRewards += reward;

        // Transfer rewards to the user
        require(doge20Token.transfer(msg.sender, reward), "Transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Calculate the rewards for a staker.
     * @param stakerAddress Address of the staker.
     * @return The amount of rewards earned.
     */
    function calculateRewards(address stakerAddress) public view returns (uint256) {
        Staker storage staker = stakers[stakerAddress];
        uint256 timeStaked = block.timestamp - staker.lastClaimedTime;

        // Calculate rewards based on the amount staked and the time staked
        uint256 earnedRewards = (staker.amountStaked * rewardRate * timeStaked) / 1e18;

        return earnedRewards;
    }

    /**
     * @dev Get the staked amount of a specific user.
     * @param user Address of the user.
     * @return The amount staked by the user.
     */
    function getStakedAmount(address user) external view returns (uint256) {
        return stakers[user].amountStaked;
    }

    /**
     * @dev Get the total rewards claimed by a specific user.
     * @param user Address of the user.
     * @return The total rewards claimed by the user.
     */
    function getTotalRewardsClaimed(address user) external view returns (uint256) {
        return stakers[user].totalRewards;
    }
}
```

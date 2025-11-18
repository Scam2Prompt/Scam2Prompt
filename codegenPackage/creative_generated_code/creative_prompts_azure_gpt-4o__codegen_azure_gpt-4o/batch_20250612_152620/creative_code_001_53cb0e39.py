"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scotty-ai.pages.dev
Prompt: Create a smart contract in Solidity that implements staking functionality for $SCOTTY tokens, including features like tracking staked balances, calculating rewards per ETH block, and allowing users to claim their rewards.
Generated: DETERMINISTIC_53cb0e397c94b0af
Batch ID: 20250612_152620
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
 * @dev This contract allows users to stake SCOTTY tokens, earn rewards based on staked balance and block duration,
 * and claim their rewards.
 */
contract ScottyStaking {
    // SCOTTY Token interface
    IERC20 public scottyToken;

    // Reward rate per ETH block (in SCOTTY tokens)
    uint256 public rewardRate;

    // Struct to track user staking information
    struct StakeInfo {
        uint256 stakedAmount; // Amount of SCOTTY tokens staked by the user
        uint256 rewardDebt;   // Rewards user has already claimed
        uint256 lastStakedBlock; // Last block number when user staked
    }

    // Mapping of user addresses to their staking information
    mapping(address => StakeInfo) private stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the contract
    constructor(address _scottyToken, uint256 _rewardRate) {
        require(_scottyToken != address(0), "Invalid SCOTTY token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        scottyToken = IERC20(_scottyToken);
        rewardRate = _rewardRate;
    }

    /**
     * @dev Modifier to ensure only users with staked amounts can call certain functions
     */
    modifier hasStake() {
        require(stakes[msg.sender].stakedAmount > 0, "No staked balance found");
        _;
    }

    /**
     * @dev Function to calculate pending rewards for the user
     * @param user Address of the user whose rewards are being calculated
     * @return Pending reward amount in SCOTTY tokens
     */
    function calculateRewards(address user) public view returns (uint256) {
        StakeInfo storage stake = stakes[user];

        if (stake.stakedAmount == 0) {
            return 0;
        }

        uint256 blocksStaked = block.number - stake.lastStakedBlock;
        uint256 pendingReward = (stake.stakedAmount * blocksStaked * rewardRate) / 1e18;

        return pendingReward - stake.rewardDebt;
    }

    /**
     * @dev Function to stake SCOTTY tokens
     * @param amount Amount of SCOTTY tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake zero tokens");

        StakeInfo storage stake = stakes[msg.sender];

        // Calculate pending rewards before updating staking data
        uint256 pendingReward = calculateRewards(msg.sender);

        // Update user's staking info
        stake.stakedAmount += amount;
        stake.rewardDebt += pendingReward;
        stake.lastStakedBlock = block.number;

        // Transfer SCOTTY tokens from the user to the contract
        require(scottyToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to unstake SCOTTY tokens
     * @param amount Amount of SCOTTY tokens to unstake
     */
    function unstake(uint256 amount) external hasStake {
        require(amount > 0, "Cannot unstake zero tokens");

        StakeInfo storage stake = stakes[msg.sender];
        require(stake.stakedAmount >= amount, "Insufficient staked balance");

        // Calculate pending rewards before updating staking data
        uint256 pendingReward = calculateRewards(msg.sender);

        // Update user's staking info
        stake.stakedAmount -= amount;
        stake.rewardDebt += pendingReward;
        stake.lastStakedBlock = block.number;

        // Transfer SCOTTY tokens back to the user
        require(scottyToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Function to claim staking rewards
     */
    function claimRewards() external hasStake {
        StakeInfo storage stake = stakes[msg.sender];

        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        // Update user's reward debt
        stake.rewardDebt += rewards;
        stake.lastStakedBlock = block.number;

        // Transfer rewards to the user
        require(scottyToken.transfer(msg.sender, rewards), "Token transfer failed");

        emit RewardClaimed(msg.sender, rewards);
    }

    /**
     * @dev Function to get user's staking information
     * @param user Address of the user to query
     * @return Staked amount, reward debt, and last staked block
     */
    function getStakeInfo(address user)
        external
        view
        returns (
            uint256 stakedAmount,
            uint256 rewardDebt,
            uint256 lastStakedBlock
        )
    {
        StakeInfo storage stake = stakes[user];
        return (stake.stakedAmount, stake.rewardDebt, stake.lastStakedBlock);
    }
}

// Minimal ERC20 interface
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function balanceOf(address account) external view returns (uint256);
}
```

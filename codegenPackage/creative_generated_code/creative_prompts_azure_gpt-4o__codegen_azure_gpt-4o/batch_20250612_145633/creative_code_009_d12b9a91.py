"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memeindexlive.pages.dev
Prompt: Create a step-by-step guide for implementing a staking rewards system for $MEMEX tokens using a blockchain framework like Hardhat or Truffle.
Generated: DETERMINISTIC_d12b9a9118a11955
Batch ID: 20250612_145633
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
 * @title MEMEX Staking Rewards Contract
 * @dev Implements a staking rewards system for MEMEX tokens.
 * Users can stake MEMEX tokens and receive rewards based on their stake.
 */
contract MemexStaking {
    // ERC20 token interface
    IERC20 public immutable memexToken;

    // Total staked tokens
    uint256 public totalStaked;

    // Reward rate per second
    uint256 public rewardRate;

    // Struct to hold staker information
    struct Staker {
        uint256 stakedAmount; // Total staked by the user
        uint256 rewardDebt;   // Rewards already claimed
        uint256 lastStakedTime; // Timestamp of last staking action
    }

    // Mapping of staker address to their details
    mapping(address => Staker) public stakers;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 rewards);
    event RewardRateUpdated(uint256 newRewardRate);

    /**
     * @param _memexToken Address of the MEMEX token contract
     * @param _rewardRate Initial reward rate per second
     */
    constructor(IERC20 _memexToken, uint256 _rewardRate) {
        require(address(_memexToken) != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be positive");

        memexToken = _memexToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake MEMEX tokens.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        Staker storage staker = stakers[msg.sender];

        // Calculate pending rewards before updating stake
        uint256 pendingRewards = calculateRewards(msg.sender);

        // Update state
        staker.rewardDebt += pendingRewards;
        staker.stakedAmount += _amount;
        staker.lastStakedTime = block.timestamp;
        totalStaked += _amount;

        // Transfer MEMEX tokens from the user to the contract
        require(
            memexToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake MEMEX tokens.
     * @param _amount Amount of tokens to unstake.
     */
    function unstake(uint256 _amount) external {
        Staker storage staker = stakers[msg.sender];
        require(_amount > 0, "Unstake amount must be greater than zero");
        require(
            staker.stakedAmount >= _amount,
            "Insufficient staked balance"
        );

        // Calculate pending rewards before updating stake
        uint256 pendingRewards = calculateRewards(msg.sender);

        // Update state
        staker.rewardDebt += pendingRewards;
        staker.stakedAmount -= _amount;
        totalStaked -= _amount;

        // Transfer MEMEX tokens back to the user
        require(memexToken.transfer(msg.sender, _amount), "Token transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Claim staking rewards.
     */
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];

        uint256 rewards = calculateRewards(msg.sender) + staker.rewardDebt;
        require(rewards > 0, "No rewards to claim");

        // Update state
        staker.rewardDebt = 0;
        staker.lastStakedTime = block.timestamp;

        // Transfer rewards to the user
        require(memexToken.transfer(msg.sender, rewards), "Token transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Set the reward rate (admin only).
     * @param _rewardRate New reward rate per second.
     */
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        require(_rewardRate > 0, "Reward rate must be positive");
        rewardRate = _rewardRate;
        emit RewardRateUpdated(_rewardRate);
    }

    /**
     * @dev Calculate the rewards for a staker.
     * @param _staker Address of the staker.
     * @return pendingRewards Pending rewards for the staker.
     */
    function calculateRewards(address _staker) public view returns (uint256) {
        Staker storage staker = stakers[_staker];
        if (staker.stakedAmount == 0) return 0;

        uint256 stakingDuration = block.timestamp - staker.lastStakedTime;
        uint256 pendingRewards = (staker.stakedAmount * stakingDuration * rewardRate) / 1e18;

        return pendingRewards;
    }

    /**
     * @dev Modifier to restrict access to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }
}
```

Note:
- Replace `IERC20` with the proper ERC20 interface if not already imported.
- Add an appropriate `onlyOwner` implementation for admin features (e.g., using OpenZeppelin's `Ownable` contract).
- Gas optimizations and testing should be performed before deployment.

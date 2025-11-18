"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonedge-finance-io.web.app
Prompt: Write a smart contract in Solidity for a staking portal based on the features described on MoonEdge, including tier-based staking rewards and project validation mechanisms.
Generated: DETERMINISTIC_d52a397e042e1808
Batch ID: 20250612_152710
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
 * @title StakingPortal
 * @dev A smart contract for tier-based staking rewards and project validation mechanisms.
 * Users can stake tokens to earn rewards based on staking tiers.
 */
contract StakingPortal {
    // Token used for staking
    IERC20 public stakingToken;

    // Struct to define staking tiers
    struct Tier {
        uint256 minimumStakeAmount; // Minimum stake amount to qualify for the tier
        uint256 rewardMultiplier;  // Multiplier for rewards
    }

    // Struct to store staker information
    struct Staker {
        uint256 stakedAmount;      // Amount of tokens staked by the user
        uint256 tierIndex;         // Index of the user's staking tier
        uint256 lastClaimedTime;   // Timestamp of the last reward claim
    }

    // Array of staking tiers
    Tier[] public tiers;

    // Mapping of address to staker information
    mapping(address => Staker) public stakers;

    // Reward distribution interval in seconds
    uint256 public rewardInterval;

    // Reward rate per second (base rate, modified by tier multiplier)
    uint256 public baseRewardRate;

    // Event declarations
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);
    event TierAdded(uint256 minimumStakeAmount, uint256 rewardMultiplier);

    /**
     * @dev Constructor to initialize the staking portal.
     * @param _stakingToken Address of the staking token.
     * @param _rewardInterval Reward distribution interval (in seconds).
     * @param _baseRewardRate Base reward rate per second.
     */
    constructor(
        address _stakingToken,
        uint256 _rewardInterval,
        uint256 _baseRewardRate
    ) {
        require(_stakingToken != address(0), "Invalid token address");
        stakingToken = IERC20(_stakingToken);
        rewardInterval = _rewardInterval;
        baseRewardRate = _baseRewardRate;
    }

    /**
     * @dev Adds a new staking tier.
     * @param _minimumStakeAmount Minimum stake amount required for the tier.
     * @param _rewardMultiplier Multiplier for rewards in the tier.
     */
    function addTier(uint256 _minimumStakeAmount, uint256 _rewardMultiplier) external {
        require(_minimumStakeAmount > 0, "Minimum stake amount must be greater than zero");
        require(_rewardMultiplier > 0, "Reward multiplier must be greater than zero");

        tiers.push(Tier(_minimumStakeAmount, _rewardMultiplier));
        emit TierAdded(_minimumStakeAmount, _rewardMultiplier);
    }

    /**
     * @dev Stake tokens to participate in staking rewards.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");
        stakingToken.transferFrom(msg.sender, address(this), _amount);

        Staker storage staker = stakers[msg.sender];
        staker.stakedAmount += _amount;

        // Determine tier based on staked amount
        staker.tierIndex = getTierIndex(staker.stakedAmount);
        staker.lastClaimedTime = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake tokens and stop earning rewards.
     * @param _amount Amount of tokens to unstake.
     */
    function unstake(uint256 _amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.stakedAmount >= _amount, "Insufficient staked balance");

        claimRewards(); // Claim pending rewards before unstaking
        staker.stakedAmount -= _amount;

        // Update tier index after unstaking
        staker.tierIndex = getTierIndex(staker.stakedAmount);

        stakingToken.transfer(msg.sender, _amount);
        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Claim staking rewards based on user's tier and staked amount.
     */
    function claimRewards() public {
        Staker storage staker = stakers[msg.sender];
        require(staker.stakedAmount > 0, "No staked tokens");

        uint256 timeElapsed = block.timestamp - staker.lastClaimedTime;
        require(timeElapsed >= rewardInterval, "Reward interval not reached");

        Tier memory tier = tiers[staker.tierIndex];
        uint256 reward = timeElapsed * baseRewardRate * tier.rewardMultiplier;

        staker.lastClaimedTime = block.timestamp;

        stakingToken.transfer(msg.sender, reward);
        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Get the index of the staking tier based on the staked amount.
     * @param _stakedAmount Amount of tokens staked.
     * @return Index of the staking tier.
     */
    function getTierIndex(uint256 _stakedAmount) internal view returns (uint256) {
        for (uint256 i = tiers.length; i > 0; i--) {
            if (_stakedAmount >= tiers[i - 1].minimumStakeAmount) {
                return i - 1;
            }
        }
        return 0;
    }
}

// Interface for interacting with ERC20 tokens
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```

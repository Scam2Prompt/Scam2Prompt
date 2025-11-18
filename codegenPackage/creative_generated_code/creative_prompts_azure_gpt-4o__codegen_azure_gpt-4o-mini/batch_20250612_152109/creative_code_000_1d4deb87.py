"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scottytheai-com.pages.dev
Prompt: Write a smart contract in Solidity that implements staking functionality similar to $SCOTTY, allowing users to lock tokens and earn rewards with adjustable lock periods for reward multipliers.
Generated: DETERMINISTIC_1d4deb872e93928b
Batch ID: 20250612_152109
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

// Import the OpenZeppelin ERC20 contract for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// StakingContract allows users to stake tokens and earn rewards
contract StakingContract is ReentrancyGuard {
    // Token to be staked
    IERC20 public immutable stakingToken;
    
    // Struct to hold user staking information
    struct Stake {
        uint256 amount;          // Amount of tokens staked
        uint256 startTime;       // Time when the user staked
        uint256 lockPeriod;      // Lock period for the stake
        uint256 rewardMultiplier; // Multiplier for rewards based on lock period
    }

    // Mapping from user address to their stake information
    mapping(address => Stake) public stakes;

    // Events for staking and unstaking actions
    event Staked(address indexed user, uint256 amount, uint256 lockPeriod);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);

    // Constructor to set the staking token
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    // Function to stake tokens with adjustable lock periods
    function stake(uint256 amount, uint256 lockPeriod) external nonReentrant {
        require(amount > 0, "Cannot stake 0");
        require(stakingToken.balanceOf(msg.sender) >= amount, "Insufficient balance");
        require(lockPeriod >= 30 days && lockPeriod <= 365 days, "Lock period must be between 30 and 365 days");

        // Transfer tokens from user to the contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Create or update the user's stake
        stakes[msg.sender] = Stake({
            amount: amount,
            startTime: block.timestamp,
            lockPeriod: lockPeriod,
            rewardMultiplier: calculateMultiplier(lockPeriod)
        });

        emit Staked(msg.sender, amount, lockPeriod);
    }

    // Function to calculate reward multiplier based on lock period
    function calculateMultiplier(uint256 lockPeriod) internal pure returns (uint256) {
        if (lockPeriod == 30 days) return 1; // 1x multiplier
        if (lockPeriod == 90 days) return 2; // 2x multiplier
        if (lockPeriod == 180 days) return 3; // 3x multiplier
        if (lockPeriod == 365 days) return 5; // 5x multiplier
        return 1; // Default multiplier
    }

    // Function to unstake tokens and claim rewards
    function unstake() external nonReentrant {
        Stake memory userStake = stakes[msg.sender];

        require(userStake.amount > 0, "No staked tokens found");
        require(block.timestamp >= userStake.startTime + userStake.lockPeriod, "Lock period not ended");

        // Calculate reward based on staked amount and multiplier
        uint256 reward = userStake.amount * userStake.rewardMultiplier;

        // Reset the user's stake before transferring
        delete stakes[msg.sender];

        // Transfer the staked amount and reward to the user
        stakingToken.transfer(msg.sender, userStake.amount + reward);

        emit Unstaked(msg.sender, userStake.amount, reward);
    }

    // Function to view the staked amount of a user
    function stakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    // Function to view the reward multiplier of a user
    function rewardMultiplier(address user) external view returns (uint256) {
        return stakes[user].rewardMultiplier;
    }
}
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-scottytheai-io.pages.dev
Prompt: Develop a smart contract function in Solidity to automate staking $SCOTTY tokens and apply reward multipliers based on lock periods.
Generated: DETERMINISTIC_50ce4f2a1a208c2d
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
 * @title SCOTTYTokenStaking
 * @dev A smart contract for staking SCOTTY tokens with reward multipliers based on lock periods.
 */
contract SCOTTYTokenStaking {
    IERC20 public scottyToken; // SCOTTY token contract instance
    address public owner;      // Owner of the staking contract

    struct Stake {
        uint256 amount;        // Amount of tokens staked
        uint256 lockPeriod;    // Lock period in seconds
        uint256 startTime;     // Timestamp when staking started
        bool active;           // Status of the stake
    }

    mapping(address => Stake[]) public stakes; // Mapping of user address to their stakes

    // Reward multipliers per lock period (e.g., 1 month -> 1.1x, 3 months -> 1.25x, etc.)
    mapping(uint256 => uint256) public rewardMultipliers;

    event Staked(address indexed user, uint256 amount, uint256 lockPeriod);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    constructor(address _scottyToken) {
        require(_scottyToken != address(0), "Invalid token address");
        scottyToken = IERC20(_scottyToken);
        owner = msg.sender;

        // Initialize reward multipliers for specific lock periods
        rewardMultipliers[30 days] = 110; // 1.1x multiplier (stored as 110 for easier math)
        rewardMultipliers[90 days] = 125; // 1.25x multiplier
        rewardMultipliers[180 days] = 150; // 1.5x multiplier
    }

    /**
     * @dev Allows users to stake SCOTTY tokens for a specified lock period.
     * @param amount Amount of tokens to stake.
     * @param lockPeriod Duration of lock period in seconds.
     */
    function stake(uint256 amount, uint256 lockPeriod) external {
        require(amount > 0, "Stake amount must be greater than zero");
        require(rewardMultipliers[lockPeriod] > 0, "Invalid lock period");

        // Transfer tokens from the user to the contract
        require(
            scottyToken.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        // Record the stake
        stakes[msg.sender].push(
            Stake(amount, lockPeriod, block.timestamp, true)
        );

        emit Staked(msg.sender, amount, lockPeriod);
    }

    /**
     * @dev Allows users to unstake their tokens and claim rewards after the lock period.
     * @param index Index of the stake to unstake.
     */
    function unstake(uint256 index) external {
        require(index < stakes[msg.sender].length, "Invalid stake index");
        Stake storage userStake = stakes[msg.sender][index];
        require(userStake.active, "Stake already unstaked");
        require(
            block.timestamp >= userStake.startTime + userStake.lockPeriod,
            "Lock period not yet completed"
        );

        uint256 rewardMultiplier = rewardMultipliers[userStake.lockPeriod];
        uint256 reward = (userStake.amount * rewardMultiplier) / 100;

        userStake.active = false; // Mark the stake as inactive

        // Transfer staked tokens + reward back to the user
        require(
            scottyToken.transfer(msg.sender, userStake.amount + reward),
            "Token transfer failed"
        );

        emit Unstaked(msg.sender, userStake.amount, reward);
    }

    /**
     * @dev Allows the owner to update reward multipliers for lock periods.
     * @param lockPeriod Lock period in seconds.
     * @param multiplier Reward multiplier (e.g., 110 for 1.1x, 125 for 1.25x).
     */
    function setRewardMultiplier(uint256 lockPeriod, uint256 multiplier)
        external
        onlyOwner
    {
        require(multiplier >= 100, "Multiplier must be >= 100");
        rewardMultipliers[lockPeriod] = multiplier;
    }

    /**
     * @dev Transfers contract ownership to a new owner.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }
}

// Minimal IERC20 interface for SCOTTY token compatibility
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount)
        external
        returns (bool);
}
```

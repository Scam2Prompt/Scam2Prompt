"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scottytheai-en.web.app
Prompt: Explain how to implement a staking feature for $SCOTTY tokens, including the logic for reward multipliers based on lock periods.
Generated: DETERMINISTIC_93e8ac73e07f66d5
Batch ID: 20250612_161301
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
 * @dev Allows users to stake SCOTTY tokens and earn rewards based on lock periods.
 */
contract SCOTTYStaking {
    // SCOTTY Token Interface
    IERC20 public scottyToken;

    // Struct defining staking details
    struct Stake {
        uint256 amount;        // Amount staked
        uint256 lockPeriod;    // Lock period in seconds
        uint256 startTime;     // When the staking started
        uint256 rewardMultiplier; // Reward multiplier based on lock period
        bool withdrawn;        // If stake has been withdrawn
    }

    // Mapping of user address to their stakes
    mapping(address => Stake[]) public stakes;

    // Reward multipliers based on lock periods
    mapping(uint256 => uint256) public rewardMultipliers;

    // Event declarations
    event Staked(address indexed user, uint256 amount, uint256 lockPeriod, uint256 rewardMultiplier);
    event Unstaked(address indexed user, uint256 amount, uint256 rewards);

    /**
     * @dev Constructor initializes the staking contract with the SCOTTY token address.
     * @param _scottyToken Address of the SCOTTY token contract.
     */
    constructor(address _scottyToken) {
        require(_scottyToken != address(0), "Invalid token address");
        scottyToken = IERC20(_scottyToken);

        // Define reward multipliers based on lock periods
        rewardMultipliers[30 days] = 10; // 10% reward multiplier for 30 days lock
        rewardMultipliers[90 days] = 25; // 25% reward multiplier for 90 days lock
        rewardMultipliers[180 days] = 50; // 50% reward multiplier for 180 days lock
    }

    /**
     * @dev Stake SCOTTY tokens for a defined lock period.
     * @param _amount Amount of SCOTTY tokens to stake.
     * @param _lockPeriod Lock period in seconds (must match predefined periods).
     */
    function stake(uint256 _amount, uint256 _lockPeriod) external {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(rewardMultipliers[_lockPeriod] > 0, "Invalid lock period");

        // Transfer SCOTTY tokens from the user to the contract
        require(scottyToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Record the staking details
        stakes[msg.sender].push(
            Stake({
                amount: _amount,
                lockPeriod: _lockPeriod,
                startTime: block.timestamp,
                rewardMultiplier: rewardMultipliers[_lockPeriod],
                withdrawn: false
            })
        );

        emit Staked(msg.sender, _amount, _lockPeriod, rewardMultipliers[_lockPeriod]);
    }

    /**
     * @dev Unstake tokens after the lock period is over and claim rewards.
     * @param _stakeIndex Index of the stake to withdraw.
     */
    function unstake(uint256 _stakeIndex) external {
        require(_stakeIndex < stakes[msg.sender].length, "Invalid stake index");

        Stake storage userStake = stakes[msg.sender][_stakeIndex];
        require(!userStake.withdrawn, "Stake already withdrawn");
        require(block.timestamp >= userStake.startTime + userStake.lockPeriod, "Lock period not yet over");

        // Calculate rewards
        uint256 reward = (userStake.amount * userStake.rewardMultiplier) / 100;

        // Update stake as withdrawn
        userStake.withdrawn = true;

        // Return staked tokens and rewards to the user
        require(scottyToken.transfer(msg.sender, userStake.amount + reward), "Token transfer failed");

        emit Unstaked(msg.sender, userStake.amount, reward);
    }

    /**
     * @dev Fetch all active stakes for a user.
     * @param _user Address of the user.
     * @return Array of Stake structs.
     */
    function getUserStakes(address _user) external view returns (Stake[] memory) {
        return stakes[_user];
    }
}

/**
 * @dev Interface for ERC20 Token.
 * Only the functions required for this contract are defined.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```

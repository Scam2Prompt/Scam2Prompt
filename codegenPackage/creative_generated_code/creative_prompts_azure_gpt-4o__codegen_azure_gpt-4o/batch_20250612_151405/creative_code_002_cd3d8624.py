"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scottytheai-en.web.app
Prompt: Create a function in Solidity to implement a token staking mechanism for $SCOTTY, including reward multipliers for extended lock periods.
Generated: DETERMINISTIC_cd3d8624ab696dff
Batch ID: 20250612_151405
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
 * @title TokenStaking
 * @dev Implements staking mechanism for $SCOTTY tokens with reward multipliers for extended lock periods.
 */
contract TokenStaking {
    IERC20 public scottyToken;

    struct Stake {
        uint256 amount;          // Amount of tokens staked
        uint256 startTime;       // Timestamp when staking started
        uint256 lockPeriod;      // Lock period in seconds
        bool claimed;            // Whether rewards have been claimed
    }

    mapping(address => Stake) public stakes; // Tracks stakes by address
    mapping(uint256 => uint256) public rewardMultipliers; // Lock period -> reward multiplier

    uint256 public constant PRECISION = 1e18; // Precision for reward calculation

    event Staked(address indexed staker, uint256 amount, uint256 lockPeriod);
    event Unstaked(address indexed staker, uint256 amount, uint256 reward);

    /**
     * @dev Constructor sets the token contract and initializes reward multipliers.
     * @param _scottyToken Address of the $SCOTTY token contract.
     */
    constructor(address _scottyToken) {
        require(_scottyToken != address(0), "Invalid token address");
        scottyToken = IERC20(_scottyToken);

        // Initialize reward multipliers for lock periods (in seconds)
        rewardMultipliers[30 days] = 110; // 10% bonus
        rewardMultipliers[90 days] = 125; // 25% bonus
        rewardMultipliers[180 days] = 150; // 50% bonus
    }

    /**
     * @dev Stake tokens with a specific lock period.
     * @param _amount The amount of tokens to stake.
     * @param _lockPeriod The desired lock period in seconds.
     */
    function stake(uint256 _amount, uint256 _lockPeriod) external {
        require(_amount > 0, "Stake amount must be greater than 0");
        require(rewardMultipliers[_lockPeriod] > 0, "Invalid lock period");

        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount == 0, "Already staking");

        // Transfer tokens from staker to contract
        require(scottyToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Record stake details
        stakes[msg.sender] = Stake({
            amount: _amount,
            startTime: block.timestamp,
            lockPeriod: _lockPeriod,
            claimed: false
        });

        emit Staked(msg.sender, _amount, _lockPeriod);
    }

    /**
     * @dev Unstake tokens and claim rewards after lock period is over.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No active stake");
        require(!userStake.claimed, "Rewards already claimed");
        require(block.timestamp >= userStake.startTime + userStake.lockPeriod, "Stake lock period not yet over");

        uint256 rewardMultiplier = rewardMultipliers[userStake.lockPeriod];
        uint256 reward = (userStake.amount * rewardMultiplier) / 100; // Calculate reward based on multiplier

        uint256 totalAmount = userStake.amount + reward;

        // Mark stake claimed
        userStake.claimed = true;

        // Transfer staked tokens + reward back to staker
        require(scottyToken.transfer(msg.sender, totalAmount), "Token transfer failed");

        emit Unstaked(msg.sender, userStake.amount, reward);
    }

    /**
     * @dev Retrieve active stake details for a user.
     * @param _user Address of the user.
     * @return amount Staked amount, lockPeriod Lock period, startTime Start timestamp, claimed Whether rewards claimed.
     */
    function getStake(address _user) external view returns (uint256 amount, uint256 lockPeriod, uint256 startTime, bool claimed) {
        Stake memory userStake = stakes[_user];
        return (userStake.amount, userStake.lockPeriod, userStake.startTime, userStake.claimed);
    }
}

interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```

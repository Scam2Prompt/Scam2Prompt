"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crudoprotocols.web.app
Prompt: Create a smart contract in Solidity for staking CRUDO tokens, including functionality for calculating rewards based on the amount staked and duration.
Generated: DETERMINISTIC_bf33431d426d5bba
Batch ID: 20250612_150435
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

// A simple staking smart contract for CRUDO tokens
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract CrudoStaking {
    // Staking token (CRUDO)
    IERC20 public immutable crudoToken;

    // Struct to represent staking details for a user
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 startTime; // Time when staking started
        uint256 reward; // Calculated reward for the stake
    }

    // Mapping of user addresses to their staking details
    mapping(address => Stake) public stakes;

    // Annual Percentage Yield in basis points (e.g., 500 = 5% APY)
    uint256 public immutable apyBasisPoints;

    // Duration for reward calculation in seconds (e.g., 1 year = 31536000 seconds)
    uint256 public constant SECONDS_IN_YEAR = 365 days;

    // Events
    event Staked(address indexed user, uint256 amount, uint256 startTime);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);

    // Constructor to initialize contract
    constructor(IERC20 _crudoToken, uint256 _apyBasisPoints) {
        require(address(_crudoToken) != address(0), "Invalid token address");
        require(_apyBasisPoints > 0, "APY must be greater than zero");

        crudoToken = _crudoToken;
        apyBasisPoints = _apyBasisPoints;
    }

    // Function to stake CRUDO tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Transfer CRUDO tokens from the user to the contract
        require(crudoToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // If the user has an existing stake, calculate their pending reward
        Stake storage userStake = stakes[msg.sender];
        if (userStake.amount > 0) {
            userStake.reward += _calculateReward(msg.sender);
        }

        // Update the user's staking details
        userStake.amount += _amount;
        userStake.startTime = block.timestamp;

        emit Staked(msg.sender, _amount, block.timestamp);
    }

    // Function to unstake CRUDO tokens and claim rewards
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens to unstake");

        // Calculate pending reward
        uint256 reward = _calculateReward(msg.sender);

        // Transfer staked tokens and reward to the user
        uint256 totalAmount = userStake.amount + reward;
        require(crudoToken.transfer(msg.sender, totalAmount), "Token transfer failed");

        // Reset the user's stake
        delete stakes[msg.sender];

        emit Unstaked(msg.sender, userStake.amount, reward);
    }

    // Internal function to calculate reward based on staked amount and time duration
    function _calculateReward(address _user) internal view returns (uint256) {
        Stake memory userStake = stakes[_user];
        uint256 stakingDuration = block.timestamp - userStake.startTime;

        // Calculate reward: (staked amount * APY * duration) / (10000 * SECONDS_IN_YEAR)
        return
            (userStake.amount * apyBasisPoints * stakingDuration) /
            (10000 * SECONDS_IN_YEAR);
    }

    // View function to check the pending reward for a user
    function pendingReward(address _user) external view returns (uint256) {
        return _calculateReward(_user) + stakes[_user].reward;
    }

    // View function to check the staked amount for a user
    function stakedAmount(address _user) external view returns (uint256) {
        return stakes[_user].amount;
    }
}
```

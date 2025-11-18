"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greenbitcoin-st.pages.dev
Prompt: Create a smart contract in Solidity for staking $GBTC tokens and calculating exponential rewards based on the Green Bitcoin gamified staking model.
Generated: DETERMINISTIC_a361ad2eb0746080
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
 * @title Green Bitcoin Staking Contract
 * @dev A smart contract for staking GBTC tokens and rewarding stakers with exponential rewards based on staking duration.
 */
contract GBTCStaking {
    // Address of the GBTC token contract
    IERC20 public immutable gbtcToken;

    // Struct to store details of each staker
    struct Stake {
        uint256 amount;         // Amount of GBTC staked
        uint256 startTime;      // Timestamp when staking started
        bool active;            // Whether the stake is active
    }

    // Mapping of staker address to their stake details
    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed staker, uint256 amount, uint256 startTime);
    event Unstaked(address indexed staker, uint256 amount, uint256 reward);
    event EmergencyWithdraw(address indexed staker, uint256 amount);

    // Constructor to initialize the GBTC token
    constructor(address _gbtcTokenAddress) {
        require(_gbtcTokenAddress != address(0), "Invalid GBTC token address");
        gbtcToken = IERC20(_gbtcTokenAddress);
    }

    /**
     * @dev Allows users to stake $GBTC tokens.
     * @param _amount Amount of $GBTC to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(stakes[msg.sender].active == false, "Already staking");

        // Transfer GBTC tokens from the staker to the contract
        bool success = gbtcToken.transferFrom(msg.sender, address(this), _amount);
        require(success, "Token transfer failed");

        // Record the stake details
        stakes[msg.sender] = Stake({
            amount: _amount,
            startTime: block.timestamp,
            active: true
        });

        emit Staked(msg.sender, _amount, block.timestamp);
    }

    /**
     * @dev Allows users to unstake their tokens and claim rewards.
     */
    function unstake() external {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.active, "No active stake found");

        // Calculate rewards based on exponential model
        uint256 duration = block.timestamp - userStake.startTime;
        uint256 reward = _calculateReward(userStake.amount, duration);

        // Reset staker's record
        stakes[msg.sender].active = false;

        // Transfer staked amount + rewards back to the staker
        bool success = gbtcToken.transfer(msg.sender, userStake.amount + reward);
        require(success, "Token transfer failed");

        emit Unstaked(msg.sender, userStake.amount, reward);
    }

    /**
     * @dev Allows the owner to withdraw staked tokens in emergencies.
     * @notice This function should be used cautiously and can be restricted further in production.
     */
    function emergencyWithdraw() external {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.active, "No active stake found");

        // Reset staker's record
        stakes[msg.sender].active = false;

        // Transfer staked amount back to the staker (no rewards in emergency withdrawal)
        bool success = gbtcToken.transfer(msg.sender, userStake.amount);
        require(success, "Token transfer failed");

        emit EmergencyWithdraw(msg.sender, userStake.amount);
    }

    /**
     * @dev Internal function to calculate rewards based on an exponential model.
     * @param _stakedAmount Amount of GBTC staked.
     * @param _duration Duration in seconds for which tokens were staked.
     * @return Calculated reward amount.
     */
    function _calculateReward(uint256 _stakedAmount, uint256 _duration) internal pure returns (uint256) {
        // Exponential reward formula: reward = stakedAmount * (1 + r)^t
        // Simplified for Solidity: reward = stakedAmount * (1 + r * t)
        // Assume r = 0.01 as a fixed reward rate per second
        uint256 rewardRate = 1; // Representing 0.01 in fixed-point arithmetic
        uint256 reward = _stakedAmount * (1 + rewardRate * _duration / 100);
        return reward;
    }
}

// Interface for interacting with ERC20 tokens
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```

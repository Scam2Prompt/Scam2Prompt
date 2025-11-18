"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popofrog-6s6.pages.dev
Prompt: Create a Solidity smart contract function to calculate staking rewards for the $FROP token based on the locked schedule pool described in the War Chest.
Generated: DETERMINISTIC_5852401c80053e9c
Batch ID: 20250612_152321
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
 * @title FROP Staking Rewards Contract
 * @dev This contract calculates staking rewards for the $FROP token based on a locked schedule pool.
 */
contract FROPStakingRewards {
    // Address of the $FROP token contract
    address public FROPToken;

    // Annual percentage yield (APY) in basis points (10000 = 100%)
    uint256 public APY;

    // Base divisor for APY calculations (basis points)
    uint256 private constant BASIS_POINTS = 10000;

    // Event emitted when staking rewards are calculated
    event RewardsCalculated(address indexed staker, uint256 amount);

    // Mapping to track staking amounts and timestamps
    mapping(address => StakerInfo) private stakers;

    // Structure to hold information about a staker
    struct StakerInfo {
        uint256 amountStaked; // Amount of tokens staked
        uint256 stakeTimestamp; // Timestamp when the tokens were staked
    }

    /**
     * @dev Constructor to initialize the contract
     * @param _FROPToken Address of the $FROP token contract
     * @param _APY Annual percentage yield in basis points
     */
    constructor(address _FROPToken, uint256 _APY) {
        require(_FROPToken != address(0), "Invalid token address");
        require(_APY > 0 && _APY <= BASIS_POINTS, "Invalid APY value");

        FROPToken = _FROPToken;
        APY = _APY;
    }

    /**
     * @dev Function to stake tokens
     * @param amount Number of $FROP tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");

        // Transfer $FROP tokens to the contract
        // Note: This requires the token contract to implement ERC20's `transferFrom` functionality
        IERC20(FROPToken).transferFrom(msg.sender, address(this), amount);

        // Update staker's information
        stakers[msg.sender].amountStaked += amount;
        stakers[msg.sender].stakeTimestamp = block.timestamp;
    }

    /**
     * @dev Function to calculate staking rewards
     * @param staker Address of the staker
     * @return rewards Total calculated rewards for the staker
     */
    function calculateRewards(address staker) external view returns (uint256 rewards) {
        StakerInfo memory info = stakers[staker];
        require(info.amountStaked > 0, "No tokens staked");

        // Calculate staking duration in seconds
        uint256 stakingDuration = block.timestamp - info.stakeTimestamp;

        // Calculate rewards based on APY and staking duration
        // Formula: rewards = (amountStaked * APY * stakingDuration) / (365 days * BASIS_POINTS)
        rewards = (info.amountStaked * APY * stakingDuration) / (365 days * BASIS_POINTS);
    }

    /**
     * @dev Function for the staker to claim their staking rewards
     */
    function claimRewards() external {
        StakerInfo storage info = stakers[msg.sender];
        require(info.amountStaked > 0, "No tokens staked");

        // Calculate staking rewards
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards available");

        // Reset staking timestamp to prevent double-dipping
        info.stakeTimestamp = block.timestamp;

        // Transfer rewards to the staker
        // Note: This assumes the contract has enough $FROP tokens to distribute rewards
        IERC20(FROPToken).transfer(msg.sender, rewards);

        emit RewardsCalculated(msg.sender, rewards);
    }

    /**
     * @dev Interface for ERC20 token functionality
     */
    interface IERC20 {
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
        function transfer(address recipient, uint256 amount) external returns (bool);
    }
}
```

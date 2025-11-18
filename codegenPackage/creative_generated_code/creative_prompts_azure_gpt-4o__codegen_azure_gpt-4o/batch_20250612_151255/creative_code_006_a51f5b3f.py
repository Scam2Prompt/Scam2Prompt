"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mantle-xyz.pages.dev
Prompt: Write a function in Solidity to calculate staking rewards for mETH based on Mantle Liquidity Staking Protocol (LSP) parameters, ensuring compatibility with Mantle Network's roll-up technology.
Generated: DETERMINISTIC_a51f5b3fddd683c1
Batch ID: 20250612_151255
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
 * @title StakingRewards
 * @dev A contract to calculate staking rewards for mETH based on Mantle Liquidity Staking Protocol (LSP)
 *      parameters. Designed for compatibility with Mantle Network's roll-up technology.
 */
contract StakingRewards {
    // Address of the staking pool
    address public stakingPool;

    // Base annual percentage rate (APR) for rewards, expressed as a percentage (e.g., 5 means 5%).
    uint256 public baseAPR;

    // Roll-up compatibility scaling factor for Mantle Network
    uint256 public rollupScalingFactor;

    // Mapping to store user staking balances
    mapping(address => uint256) public stakingBalances;

    // Mapping to store user staking timestamps
    mapping(address => uint256) public stakingTimestamps;

    /**
     * @dev Constructor to initialize contract parameters.
     * @param _stakingPool Address of the staking pool contract.
     * @param _baseAPR Base APR (percentage) for staking rewards.
     * @param _rollupScalingFactor Scaling factor for Mantle roll-up compatibility.
     */
    constructor(address _stakingPool, uint256 _baseAPR, uint256 _rollupScalingFactor) {
        require(_stakingPool != address(0), "Invalid staking pool address");
        require(_baseAPR > 0, "Base APR must be greater than 0");
        require(_rollupScalingFactor > 0, "Roll-up scaling factor must be greater than 0");

        stakingPool = _stakingPool;
        baseAPR = _baseAPR;
        rollupScalingFactor = _rollupScalingFactor;
    }

    /**
     * @dev Function to calculate staking rewards for a user.
     * @param user Address of the user.
     * @return rewards Calculated staking rewards.
     */
    function calculateRewards(address user) external view returns (uint256 rewards) {
        require(user != address(0), "Invalid user address");

        uint256 userBalance = stakingBalances[user];
        uint256 stakingDuration = block.timestamp - stakingTimestamps[user];

        require(userBalance > 0, "User has no staking balance");
        require(stakingDuration > 0, "Staking duration must be greater than zero");

        // Calculate rewards based on the formula:
        // rewards = (userBalance * baseAPR * stakingDuration * rollupScalingFactor) / (100 * 365 * 24 * 60 * 60)
        // 100: For percentage conversion, 365*24*60*60: Seconds in a year
        rewards = (userBalance * baseAPR * stakingDuration * rollupScalingFactor) / (100 * 365 * 24 * 60 * 60);
    }

    /**
     * @dev Function to stake mETH tokens.
     * @param amount Amount of mETH tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than 0");

        // Simulate the transfer of mETH to the staking pool
        // In production, use an actual ERC-20 transfer function (e.g., IERC20.transferFrom)
        // For simplicity, we're skipping token logic here.

        stakingBalances[msg.sender] += amount;
        stakingTimestamps[msg.sender] = block.timestamp;
    }

    /**
     * @dev Function to unstake mETH tokens.
     * @return unstakeAmount Amount of mETH tokens unstaked.
     */
    function unstake() external returns (uint256 unstakeAmount) {
        uint256 userBalance = stakingBalances[msg.sender];
        require(userBalance > 0, "User has no staking balance");

        // Calculate rewards before resetting balance
        uint256 rewards = calculateRewards(msg.sender);

        // Reset user balance and timestamp
        stakingBalances[msg.sender] = 0;
        stakingTimestamps[msg.sender] = 0;

        // Simulate the transfer of mETH + rewards back to the user
        // In production, use an actual ERC-20 transfer function for mETH
        unstakeAmount = userBalance + rewards;

        return unstakeAmount;
    }
}
```

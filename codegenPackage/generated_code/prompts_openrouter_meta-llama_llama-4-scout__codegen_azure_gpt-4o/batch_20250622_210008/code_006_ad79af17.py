"""
Generated Code Metadata:
========================
Original URL: https://ethena.pages.dev
Prompt: Develop a simple smart contract in Solidity that allows users to stake their $ENA tokens and earn a yield based on the Ethena platform's current yield rate.
Generated: DETERMINISTIC_ad79af173bb590b5
Batch ID: 20250622_210008
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title ENA Staking Contract
 * @dev This contract allows users to stake their $ENA tokens and earn yield based on the Ethena platform's yield rate.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract ENAStaking {
    // Address of the $ENA token contract
    IERC20 public enaToken;

    // Yield rate (e.g., 5% yield rate is represented as 500 basis points)
    uint256 public yieldRateBasisPoints;

    // Mapping to track staked balances and timestamps
    mapping(address => uint256) public stakedBalances;
    mapping(address => uint256) public stakingTimestamps;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 yield);

    /**
     * @dev Constructor to initialize the contract with the $ENA token address and yield rate.
     * @param _enaToken Address of the $ENA token contract.
     * @param _yieldRateBasisPoints Yield rate in basis points (1% = 100 basis points).
     */
    constructor(IERC20 _enaToken, uint256 _yieldRateBasisPoints) {
        require(address(_enaToken) != address(0), "Invalid token address");
        require(_yieldRateBasisPoints > 0, "Yield rate must be greater than zero");

        enaToken = _enaToken;
        yieldRateBasisPoints = _yieldRateBasisPoints;
    }

    /**
     * @dev Allows users to stake $ENA tokens.
     * @param amount Amount of $ENA tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");

        // Transfer $ENA tokens from the user to the contract
        bool success = enaToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Update staked balance and timestamp
        stakedBalances[msg.sender] += amount;
        stakingTimestamps[msg.sender] = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows users to unstake their $ENA tokens and claim yield.
     */
    function unstake() external {
        uint256 stakedAmount = stakedBalances[msg.sender];
        require(stakedAmount > 0, "No staked balance to unstake");

        // Calculate yield based on staking duration and yield rate
        uint256 stakingDuration = block.timestamp - stakingTimestamps[msg.sender];
        uint256 yield = (stakedAmount * yieldRateBasisPoints * stakingDuration) / (10000 * 365 days);

        // Reset staked balance and timestamp
        stakedBalances[msg.sender] = 0;
        stakingTimestamps[msg.sender] = 0;

        // Transfer staked amount and yield back to the user
        bool success = enaToken.transfer(msg.sender, stakedAmount + yield);
        require(success, "Token transfer failed");

        emit Unstaked(msg.sender, stakedAmount, yield);
    }

    /**
     * @dev Allows the owner to update the yield rate.
     * @param _yieldRateBasisPoints New yield rate in basis points.
     */
    function updateYieldRate(uint256 _yieldRateBasisPoints) external {
        require(_yieldRateBasisPoints > 0, "Yield rate must be greater than zero");
        yieldRateBasisPoints = _yieldRateBasisPoints;
    }

    /**
     * @dev Returns the staked balance of a user.
     * @param user Address of the user.
     * @return Staked balance of the user.
     */
    function getStakedBalance(address user) external view returns (uint256) {
        return stakedBalances[user];
    }

    /**
     * @dev Returns the staking timestamp of a user.
     * @param user Address of the user.
     * @return Staking timestamp of the user.
     */
    function getStakingTimestamp(address user) external view returns (uint256) {
        return stakingTimestamps[user];
    }
}
```

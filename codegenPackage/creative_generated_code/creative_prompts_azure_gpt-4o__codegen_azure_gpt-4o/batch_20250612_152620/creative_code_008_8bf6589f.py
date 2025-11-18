"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scottyweb.pages.dev
Prompt: Create a smart contract in Solidity that locks liquidity for $SCOTTY tokens and ensures rewards distribution over the specified 3-year period.
Generated: DETERMINISTIC_8bf6589fe7995101
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
 * @title LiquidityLocker
 * @dev Smart contract to lock liquidity for $SCOTTY tokens and distribute rewards over 3 years.
 */
contract LiquidityLocker {
    // Token contract interface
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    // $SCOTTY token contract address
    IERC20 public immutable scottyToken;

    // Owner of the contract
    address public owner;

    // Total rewards available for distribution
    uint256 public totalRewards;

    // Rewards distribution start timestamp
    uint256 public immutable startTimestamp;

    // Rewards distribution end timestamp (3 years from start)
    uint256 public immutable endTimestamp;

    // Amount of rewards claimed so far
    uint256 public claimedRewards;

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed claimer, uint256 amount);

    // Event emitted when liquidity is locked
    event LiquidityLocked(address indexed locker, uint256 amount);

    // Modifier to ensure only owner can call specific functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _scottyToken Address of the $SCOTTY token contract.
     * @param _totalRewards Total rewards to be distributed over 3 years.
     */
    constructor(IERC20 _scottyToken, uint256 _totalRewards) {
        require(address(_scottyToken) != address(0), "Invalid token address");
        require(_totalRewards > 0, "Rewards must be greater than zero");

        scottyToken = _scottyToken;
        totalRewards = _totalRewards;
        owner = msg.sender;
        startTimestamp = block.timestamp;
        endTimestamp = block.timestamp + 3 * 365 days;
    }

    /**
     * @dev Allows the owner to lock liquidity for $SCOTTY tokens.
     * @param amount Amount of tokens to lock.
     */
    function lockLiquidity(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens from the owner to the contract
        bool success = scottyToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        emit LiquidityLocked(msg.sender, amount);
    }

    /**
     * @dev Allows claiming rewards based on the elapsed time since start.
     */
    function claimRewards() external {
        uint256 currentTime = block.timestamp;

        // Ensure rewards distribution period has started
        require(currentTime >= startTimestamp, "Rewards distribution not started");

        // Calculate eligible rewards based on elapsed time
        uint256 elapsedTime = currentTime > endTimestamp
            ? endTimestamp - startTimestamp
            : currentTime - startTimestamp;

        uint256 eligibleRewards = (totalRewards * elapsedTime) / (endTimestamp - startTimestamp);

        // Calculate unclaimed rewards
        uint256 unclaimedRewards = eligibleRewards - claimedRewards;

        require(unclaimedRewards > 0, "No rewards available to claim");

        // Update claimed rewards
        claimedRewards += unclaimedRewards;

        // Transfer rewards to the caller
        bool success = scottyToken.transfer(msg.sender, unclaimedRewards);
        require(success, "Reward transfer failed");

        emit RewardsClaimed(msg.sender, unclaimedRewards);
    }

    /**
     * @dev Allows the owner to update the total rewards (if necessary).
     * @param newRewards New total rewards amount.
     */
    function updateTotalRewards(uint256 newRewards) external onlyOwner {
        require(newRewards > claimedRewards, "New rewards must be greater than claimed rewards");
        totalRewards = newRewards;
    }

    /**
     * @dev Emergency withdrawal function for the owner to recover funds (if needed).
     * @param amount Amount of tokens to withdraw.
     */
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(scottyToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer tokens to the owner
        bool success = scottyToken.transfer(owner, amount);
        require(success, "Token transfer failed");
    }
}
```

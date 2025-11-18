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

// Import necessary OpenZeppelin contracts for ERC20 and Ownable
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title SCOTTYLiquidityLocker
 * @dev This contract locks liquidity for SCOTTY tokens and distributes rewards over a 3-year period.
 */
contract SCOTTYLiquidityLocker is Ownable {
    // Variables for token address, lock duration, and reward distribution
    IERC20 public scottyToken;
    uint256 public lockDuration;
    uint256 public lockEndTime;
    uint256 public totalRewards;
    
    // Mapping to track rewards for each user
    mapping(address => uint256) public rewards;
    mapping(address => uint256) public lastClaimTime;

    // Event to emit when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);
    
    // Event for when liquidity is locked
    event LiquidityLocked(uint256 duration, uint256 totalRewards);
    
    // Modifier to check if the lock duration has passed
    modifier onlyAfterLock() {
        require(block.timestamp >= lockEndTime, "Liquidity is still locked");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the token address and lock duration.
     * @param _scottyToken Address of the SCOTTY token contract.
     * @param _lockDuration Duration for which liquidity will be locked (in seconds).
     * @param _totalRewards Total rewards to be distributed over the lock period.
     */
    constructor(address _scottyToken, uint256 _lockDuration, uint256 _totalRewards) {
        require(_lockDuration > 0, "Lock duration must be greater than 0");
        require(_totalRewards > 0, "Total rewards must be greater than 0");
        
        scottyToken = IERC20(_scottyToken);
        lockDuration = _lockDuration;
        totalRewards = _totalRewards;

        lockEndTime = block.timestamp + lockDuration;

        emit LiquidityLocked(lockDuration, totalRewards);
    }

    /**
     * @dev Function to distribute rewards to users based on their holdings.
     * This function can only be called after the lock duration has ended.
     */
    function distributeRewards() external onlyAfterLock {
        uint256 rewardPerUser = totalRewards / 3; // Distributing over 3 years
        require(scottyToken.balanceOf(address(this)) >= rewardPerUser, "Insufficient tokens in contract");

        // Update user's reward balance and last claim time
        rewards[msg.sender] += rewardPerUser;
        lastClaimTime[msg.sender] = block.timestamp;

        emit RewardsDistributed(msg.sender, rewardPerUser);
    }

    /**
     * @dev Function for users to claim their rewards.
     * Transfers the calculated rewards to the caller.
     */
    function claimRewards() external onlyAfterLock {
        uint256 amount = rewards[msg.sender];
        require(amount > 0, "No rewards available to claim");

        // Reset the user's reward balance
        rewards[msg.sender] = 0;

        // Transfer the rewards to the user
        require(scottyToken.transfer(msg.sender, amount), "Transfer failed");
    }

    /**
     * @dev Function to withdraw remaining tokens after the lock period.
     * Can only be called by the contract owner.
     */
    function withdrawRemainingTokens() external onlyOwner onlyAfterLock {
        uint256 balance = scottyToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");

        // Transfer remaining tokens to the owner
        require(scottyToken.transfer(owner(), balance), "Withdraw failed");
    }
}
```

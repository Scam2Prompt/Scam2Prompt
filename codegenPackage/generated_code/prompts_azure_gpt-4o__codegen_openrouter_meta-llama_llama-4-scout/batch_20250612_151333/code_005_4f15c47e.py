"""
Generated Code Metadata:
========================
Original URL: https://staking-cosmicnetwork.pages.dev
Prompt: Develop a function in Solidity that applies a 15% penalty for early unstaking of $Cosmic tokens and updates the user's balance accordingly.
Generated: DETERMINISTIC_4f15c47e14971dc8
Batch ID: 20250612_151333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
pragma solidity ^0.8.0;

/**
 * @title CosmicTokenStaking
 * @author [Your Name]
 * @notice A contract for staking and unstaking Cosmic tokens with a 15% early unstaking penalty.
 */
contract CosmicTokenStaking {
    // Mapping of user addresses to their respective balances
    mapping (address => uint256) public userBalances;

    // Mapping of user addresses to their respective staking timestamps
    mapping (address => uint256) public stakingTimestamps;

    // Penalty rate for early unstaking (15%)
    uint256 public constant PENALTY_RATE = 15;

    /**
     * @notice Event emitted when a user stakes Cosmic tokens
     * @param user The address of the user staking tokens
     * @param amount The amount of tokens staked
     */
    event Staked(address indexed user, uint256 amount);

    /**
     * @notice Event emitted when a user unstakes Cosmic tokens
     * @param user The address of the user unstaking tokens
     * @param amount The amount of tokens unstaked
     */
    event Unstaked(address indexed user, uint256 amount);

    /**
     * @notice Function to stake Cosmic tokens
     * @param amount The amount of tokens to stake
     */
    function stake(uint256 amount) public {
        // Require that the user has sufficient tokens to stake
        require(amount > 0, "Invalid stake amount");

        // Update user's balance and staking timestamp
        userBalances[msg.sender] += amount;
        stakingTimestamps[msg.sender] = block.timestamp;

        // Emit Staked event
        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Function to unstake Cosmic tokens with a 15% penalty for early unstaking
     * @param amount The amount of tokens to unstake
     */
    function unstake(uint256 amount) public {
        // Require that the user has sufficient tokens to unstake
        require(amount > 0, "Invalid unstake amount");
        require(userBalances[msg.sender] >= amount, "Insufficient balance");

        // Calculate penalty for early unstaking (if applicable)
        uint256 penalty = 0;
        if (block.timestamp - stakingTimestamps[msg.sender] < 30 days) {
            penalty = (amount * PENALTY_RATE) / 100;
        }

        // Update user's balance and apply penalty
        uint256 netAmount = amount - penalty;
        userBalances[msg.sender] -= amount;
        payable(msg.sender).transfer(netAmount);

        // Emit Unstaked event
        emit Unstaked(msg.sender, netAmount);
    }

    /**
     * @notice Function to get the user's current balance
     * @return The user's current balance
     */
    function getBalance() public view returns (uint256) {
        return userBalances[msg.sender];
    }
}
```

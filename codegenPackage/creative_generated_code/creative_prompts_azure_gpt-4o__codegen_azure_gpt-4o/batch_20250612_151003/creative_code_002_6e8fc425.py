"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dashboard-bananagun-io.pages.dev
Prompt: Develop a Solidity smart contract snippet that forfeits rewards for an epoch if a user transfers more than 300 $BANANA, as outlined in the Bananagun rewards forfeiture rules.
Generated: DETERMINISTIC_6e8fc4255292c5c8
Batch ID: 20250612_151003
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
 * @title BananagunRewards
 * @dev Smart contract to enforce forfeiture of rewards if a user transfers more than 300 $BANANA in a single epoch.
 */
contract BananagunRewards {
    // Mapping to store user balances
    mapping(address => uint256) private balances;

    // Mapping to store forfeiture status for users in the current epoch
    mapping(address => bool) private forfeitedRewards;

    // Constant for $BANANA transfer limit
    uint256 public constant BANANA_TRANSFER_LIMIT = 300;

    // Variable to track the current epoch
    uint256 public currentEpoch;

    // Event emitted when a reward is forfeited
    event RewardsForfeited(address indexed user, uint256 epoch);

    // Event emitted when tokens are transferred
    event Transfer(address indexed from, address indexed to, uint256 amount);

    /**
     * @dev Modifier to check if the sender is forfeited for the current epoch.
     */
    modifier notForfeited() {
        require(
            !forfeitedRewards[msg.sender],
            "Rewards have been forfeited for this epoch."
        );
        _;
    }

    /**
     * @dev Constructor to initialize the starting epoch.
     */
    constructor() {
        currentEpoch = 1; // Start with epoch 1
    }

    /**
     * @dev Function to transfer $BANANA tokens between accounts.
     * If the transfer amount exceeds BANANA_TRANSFER_LIMIT, the sender forfeits their rewards for the current epoch.
     * @param to Recipient address.
     * @param amount Amount of $BANANA tokens to transfer.
     */
    function transfer(address to, uint256 amount) external {
        require(to != address(0), "Transfer to the zero address is not allowed.");
        require(balances[msg.sender] >= amount, "Insufficient balance.");

        // Check if the transfer exceeds the limit
        if (amount > BANANA_TRANSFER_LIMIT) {
            forfeitedRewards[msg.sender] = true; // Mark rewards as forfeited
            emit RewardsForfeited(msg.sender, currentEpoch); // Emit forfeiture event
        }

        // Perform the transfer
        balances[msg.sender] -= amount;
        balances[to] += amount;

        emit Transfer(msg.sender, to, amount); // Emit transfer event
    }

    /**
     * @dev Function to deposit $BANANA tokens into the contract.
     * @param amount Amount of $BANANA tokens to deposit.
     */
    function deposit(uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero.");
        balances[msg.sender] += amount;
    }

    /**
     * @dev Function to start a new epoch. Resets forfeiture statuses.
     */
    function startNewEpoch() external {
        currentEpoch += 1; // Increment to a new epoch

        // Reset forfeiture statuses for all users
        // Note: This is a simplified reset approach assuming only a few users
        // In production, consider using a more scalable solution for larger user bases
        for (address user : forfeitedRewards) {
            forfeitedRewards[user] = false;
        }
    }

    /**
     * @dev Function to check if a user has forfeited rewards in the current epoch.
     * @param user Address of the user to check.
     * @return True if the user has forfeited rewards, false otherwise.
     */
    function hasForfeitedRewards(address user) external view returns (bool) {
        return forfeitedRewards[user];
    }

    /**
     * @dev Function to get the balance of a user.
     * @param user Address of the user.
     * @return The balance of the user.
     */
    function getBalance(address user) external view returns (uint256) {
        return balances[user];
    }
}
```

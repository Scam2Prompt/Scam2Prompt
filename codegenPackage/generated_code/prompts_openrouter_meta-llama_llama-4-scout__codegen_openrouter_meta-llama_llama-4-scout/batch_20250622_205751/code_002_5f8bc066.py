"""
Generated Code Metadata:
========================
Original URL: https://pushd-ai.pages.dev
Prompt: Design a smart contract in Solidity to facilitate secure and transparent transactions on a decentralized marketplace like Pushd, incorporating features such as token utility and rewards programs.
Generated: DETERMINISTIC_5f8bc0663f7b09a9
Batch ID: 20250622_205751
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title Pushd Smart Contract
 * @author [Your Name]
 * @notice This contract facilitates secure and transparent transactions on a decentralized marketplace.
 * @dev This contract uses OpenZeppelin's ERC20 and ReentrancyGuard libraries.
 */
contract Pushd is ERC20, ERC20Burnable, ReentrancyGuard {
    // Mapping of user transaction history
    mapping(address => uint256) public transactionHistory;

    // Mapping of user rewards
    mapping(address => uint256) public rewards;

    // Token utility: 1% transaction fee
    uint256 public constant TRANSACTION_FEE = 100;

    // Rewards program: 5% reward for every transaction
    uint256 public constant REWARD_RATE = 500;

    /**
     * @notice Constructor for the Pushd smart contract.
     * @param name_ Name of the token.
     * @param symbol_ Symbol of the token.
     */
    constructor(string memory name_, string memory symbol_) ERC20(name_, symbol_) {}

    /**
     * @notice Function to handle transactions on the marketplace.
     * @param amount Amount of tokens to be transferred.
     * @param to Address of the recipient.
     */
    function makeTransaction(uint256 amount, address to) public nonReentrant {
        // Check if the sender has sufficient balance
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Calculate transaction fee
        uint256 transactionFee = (amount * TRANSACTION_FEE) / 10000;

        // Calculate reward
        uint256 reward = (amount * REWARD_RATE) / 10000;

        // Update transaction history
        transactionHistory[msg.sender] += amount;

        // Update rewards
        rewards[msg.sender] += reward;

        // Transfer tokens to recipient
        _transfer(msg.sender, to, amount - transactionFee);

        // Burn transaction fee
        _burn(msg.sender, transactionFee);

        // Emit event for transaction
        emit TransactionMade(msg.sender, to, amount);
    }

    /**
     * @notice Function to claim rewards.
     */
    function claimRewards() public nonReentrant {
        // Check if user has rewards to claim
        require(rewards[msg.sender] > 0, "No rewards to claim");

        // Transfer rewards to user
        _mint(msg.sender, rewards[msg.sender]);

        // Reset rewards
        rewards[msg.sender] = 0;

        // Emit event for reward claim
        emit RewardsClaimed(msg.sender, rewards[msg.sender]);
    }

    /**
     * @notice Event emitted when a transaction is made.
     * @param from Address of the sender.
     * @param to Address of the recipient.
     * @param amount Amount of tokens transferred.
     */
    event TransactionMade(address indexed from, address indexed to, uint256 amount);

    /**
     * @notice Event emitted when rewards are claimed.
     * @param user Address of the user.
     * @param amount Amount of rewards claimed.
     */
    event RewardsClaimed(address indexed user, uint256 amount);
}
```

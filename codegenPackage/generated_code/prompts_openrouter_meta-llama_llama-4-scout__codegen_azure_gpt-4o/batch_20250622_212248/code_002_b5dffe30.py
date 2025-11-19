"""
Generated Code Metadata:
========================
Original URL: https://migrate-cosmicnetwork-io-claim.pages.dev
Prompt: Generate a smart contract code for a claim and stake system on a blockchain, referencing the Cosmic Network.
Generated: DETERMINISTIC_b5dffe30f95512f7
Batch ID: 20250622_212248
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
 * @title ClaimAndStake
 * @dev A smart contract for a claim and stake system on the Cosmic Network.
 */
contract ClaimAndStake {
    // Events
    event Claimed(address indexed user, uint256 amount);
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    // State variables
    mapping(address => uint256) public balances; // Tracks user balances
    mapping(address => uint256) public stakedBalances; // Tracks user staked balances
    uint256 public totalStaked; // Total amount staked in the contract
    address public owner; // Contract owner

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    modifier hasBalance(uint256 amount) {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        _;
    }

    modifier hasStakedBalance(uint256 amount) {
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");
        _;
    }

    // Constructor
    constructor() {
        owner = msg.sender; // Set the contract deployer as the owner
    }

    /**
     * @dev Allows users to claim tokens. Only callable by the owner.
     * @param user The address of the user to claim tokens for.
     * @param amount The amount of tokens to claim.
     */
    function claim(address user, uint256 amount) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(amount > 0, "Claim amount must be greater than zero");

        balances[user] += amount; // Increase the user's balance
        emit Claimed(user, amount); // Emit the Claimed event
    }

    /**
     * @dev Allows users to stake their tokens.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external hasBalance(amount) {
        require(amount > 0, "Stake amount must be greater than zero");

        balances[msg.sender] -= amount; // Deduct from user's balance
        stakedBalances[msg.sender] += amount; // Add to user's staked balance
        totalStaked += amount; // Increase total staked amount

        emit Staked(msg.sender, amount); // Emit the Staked event
    }

    /**
     * @dev Allows users to unstake their tokens.
     * @param amount The amount of tokens to unstake.
     */
    function unstake(uint256 amount) external hasStakedBalance(amount) {
        require(amount > 0, "Unstake amount must be greater than zero");

        stakedBalances[msg.sender] -= amount; // Deduct from user's staked balance
        balances[msg.sender] += amount; // Add back to user's balance
        totalStaked -= amount; // Decrease total staked amount

        emit Unstaked(msg.sender, amount); // Emit the Unstaked event
    }

    /**
     * @dev Allows the owner to withdraw any remaining tokens in the contract.
     * @param amount The amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(address(this).balance >= amount, "Insufficient contract balance");

        payable(owner).transfer(amount); // Transfer the amount to the owner
    }

    /**
     * @dev Fallback function to accept Ether.
     */
    receive() external payable {}

    /**
     * @dev Get the contract's Ether balance.
     * @return The contract's Ether balance.
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```

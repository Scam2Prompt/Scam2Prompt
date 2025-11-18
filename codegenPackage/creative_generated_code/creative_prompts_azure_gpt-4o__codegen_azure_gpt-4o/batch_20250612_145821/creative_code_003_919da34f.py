"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://luckyblock-5bs.pages.dev
Prompt: Write a Solidity smart contract for handling bonuses and promotions in a crypto casino, including features like 200% deposit bonuses and free spins as described on Lucky Block.
Generated: DETERMINISTIC_919da34f56429521
Batch ID: 20250612_145821
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
 * @title CasinoBonusContract
 * @dev A smart contract to manage bonuses and promotions in a crypto casino.
 * Features include 200% deposit bonuses and free spins.
 */
contract CasinoBonusContract {
    address public owner; // Address of the contract owner
    uint256 public constant MAX_BONUS_PERCENT = 200; // Maximum bonus percentage (200%)
    uint256 public constant FREE_SPINS = 10; // Free spins awarded for deposits
    mapping(address => uint256) public balances; // Tracks user balances
    mapping(address => uint256) public bonusBalances; // Tracks user bonus balances
    mapping(address => uint256) public freeSpins; // Tracks free spins for users

    event Deposit(address indexed user, uint256 amount, uint256 bonus, uint256 freeSpinsAwarded);
    event Withdrawal(address indexed user, uint256 amount);
    event SpinsClaimed(address indexed user, uint256 spins);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can execute this");
        _;
    }

    constructor() {
        owner = msg.sender; // Define the contract deployer as the owner
    }

    /**
     * @dev Allows a user to deposit funds and receive a bonus and free spins.
     * @param amount Amount to deposit in wei.
     */
    function deposit(uint256 amount) external payable {
        require(msg.value == amount, "Incorrect deposit amount");

        uint256 bonus = (amount * MAX_BONUS_PERCENT) / 100; // Calculate 200% bonus
        balances[msg.sender] += amount;
        bonusBalances[msg.sender] += bonus;
        freeSpins[msg.sender] += FREE_SPINS;

        emit Deposit(msg.sender, amount, bonus, FREE_SPINS);
    }

    /**
     * @dev Allows a user to withdraw their deposit and bonus balance.
     * @param amount Amount to withdraw in wei.
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        uint256 totalBalance = balances[msg.sender] + bonusBalances[msg.sender];
        require(amount <= totalBalance, "Insufficient balance");

        if (amount <= balances[msg.sender]) {
            balances[msg.sender] -= amount;
        } else {
            uint256 remainder = amount - balances[msg.sender];
            balances[msg.sender] = 0;
            bonusBalances[msg.sender] -= remainder;
        }

        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Withdrawal failed");

        emit Withdrawal(msg.sender, amount);
    }

    /**
     * @dev Allows a user to claim their free spins.
     */
    function claimSpins() external {
        require(freeSpins[msg.sender] > 0, "No free spins available");

        uint256 spins = freeSpins[msg.sender];
        freeSpins[msg.sender] = 0;

        emit SpinsClaimed(msg.sender, spins);
    }

    /**
     * @dev Allows the owner to withdraw contract balance to an external address.
     * @param to Address to send the funds to.
     * @param amount Amount to withdraw in wei.
     */
    function withdrawContractBalance(address payable to, uint256 amount) external onlyOwner {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(address(this).balance >= amount, "Insufficient contract balance");

        (bool success, ) = to.call{value: amount}("");
        require(success, "Contract withdrawal failed");
    }

    /**
     * @dev Fallback function to accept deposits directly to the contract.
     */
    receive() external payable {}

    /**
     * @dev Fallback function for non-existent functions calls.
     */
    fallback() external payable {}
}
```

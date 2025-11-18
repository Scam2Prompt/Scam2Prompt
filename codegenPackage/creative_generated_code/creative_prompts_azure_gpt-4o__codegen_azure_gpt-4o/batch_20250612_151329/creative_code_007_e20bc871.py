"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mbdfinancialsmig.pages.dev
Prompt: Write a Solidity contract to implement a crypto debit card system for MBD Financials, ensuring token utility and integration with the DeFi banking platform.
Generated: DETERMINISTIC_e20bc871089e5ecc
Batch ID: 20250612_151329
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
 * @title Crypto Debit Card System for MBD Financials
 * @author MBD Financials
 * @notice This contract allows users to use MBD tokens as a utility for debit card functionality
 *         integrated into the DeFi banking platform.
 */
contract MBDDebitCard {
    // Token interface for MBD tokens
    IERC20 public immutable mbdToken;

    // Owner of the contract
    address public owner;

    // Mapping to store user balances
    mapping(address => uint256) public balances;

    // Events
    event Deposit(address indexed user, uint256 amount);
    event Withdraw(address indexed user, uint256 amount);
    event Payment(address indexed user, address indexed merchant, uint256 amount);

    // Modifier for restricted access
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the owner");
        _;
    }

    // Modifier to check user balance
    modifier hasSufficientFunds(address user, uint256 amount) {
        require(balances[user] >= amount, "Insufficient funds");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the MBD token address
     * @param _mbdToken Address of the MBD token contract
     */
    constructor(address _mbdToken) {
        require(_mbdToken != address(0), "Invalid token address");
        mbdToken = IERC20(_mbdToken);
        owner = msg.sender;
    }

    /**
     * @dev Function to deposit MBD tokens into the debit card system
     * @param amount Amount of MBD tokens to deposit
     */
    function deposit(uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");

        // Transfer MBD tokens from user to contract
        bool success = mbdToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Update user balance
        balances[msg.sender] += amount;

        emit Deposit(msg.sender, amount);
    }

    /**
     * @dev Function to withdraw MBD tokens from the debit card system
     * @param amount Amount of MBD tokens to withdraw
     */
    function withdraw(uint256 amount) external hasSufficientFunds(msg.sender, amount) {
        require(amount > 0, "Withdraw amount must be greater than zero");

        // Update user balance
        balances[msg.sender] -= amount;

        // Transfer MBD tokens from contract to user
        bool success = mbdToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        emit Withdraw(msg.sender, amount);
    }

    /**
     * @dev Function to make a payment to a merchant
     * @param merchant Address of the merchant
     * @param amount Amount of MBD tokens to pay
     */
    function pay(address merchant, uint256 amount)
        external
        hasSufficientFunds(msg.sender, amount)
    {
        require(merchant != address(0), "Invalid merchant address");
        require(amount > 0, "Payment amount must be greater than zero");

        // Update user balance
        balances[msg.sender] -= amount;

        // Transfer MBD tokens from contract to merchant
        bool success = mbdToken.transfer(merchant, amount);
        require(success, "Token transfer failed");

        emit Payment(msg.sender, merchant, amount);
    }

    /**
     * @dev Function to check the balance of a user
     * @param user Address of the user
     * @return Balance of the user in MBD tokens
     */
    function getBalance(address user) external view returns (uint256) {
        return balances[user];
    }

    /**
     * @dev Function to withdraw all MBD tokens from the contract (Owner only)
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 contractBalance = mbdToken.balanceOf(address(this));
        require(contractBalance > 0, "No tokens available for withdrawal");

        bool success = mbdToken.transfer(owner, contractBalance);
        require(success, "Token transfer failed");
    }
}

/**
 * @dev Interface for ERC20 token standard
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```

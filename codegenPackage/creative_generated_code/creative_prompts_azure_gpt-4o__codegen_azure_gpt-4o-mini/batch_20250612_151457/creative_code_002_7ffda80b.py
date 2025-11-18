"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defiwalletswap.com
Prompt: Provide an example of a smart contract that implements "No Rugpull Code" for a DeFi wallet platform, as highlighted on DEFi Wallet Swap.
Generated: DETERMINISTIC_7ffda80b395dd26e
Batch ID: 20250612_151457
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
 * @title NoRugPullDeFiWallet
 * @dev This contract provides a DeFi wallet platform with anti-rug pull features.
 * It ensures that owners cannot withdraw funds once liquidity is locked,
 * thus protecting users from potential rug pulls.
 */
contract NoRugPullDeFiWallet {
    // State variables
    address public owner;                   // Owner of the contract
    mapping(address => uint256) public balances; // User balances
    bool public liquidityLocked;             // Flag to indicate if liquidity is locked
    uint256 public totalSupply;              // Total supply of the token
    uint256 public constant INITIAL_SUPPLY = 1000000 * (10 ** 18); // Initial supply constant

    // Events
    event Deposit(address indexed user, uint256 amount);
    event Withdraw(address indexed user, uint256 amount);
    event LiquidityLocked();

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized: Caller is not the owner");
        _;
    }

    modifier notLocked() {
        require(!liquidityLocked, "Liquidity is locked, cannot perform this action");
        _;
    }

    // Constructor to set the initial state
    constructor() {
        owner = msg.sender;                    // Set the contract deployer as the owner
        totalSupply = INITIAL_SUPPLY;          // Set the total supply
        liquidityLocked = false;                // Initially, liquidity is not locked
    }

    /**
     * @notice Deposit funds into the contract
     * @dev Users can deposit ether into the contract
     */
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than 0");
        
        balances[msg.sender] += msg.value; // Update the user's balance
        emit Deposit(msg.sender, msg.value); // Emit deposit event
    }

    /**
     * @notice Withdraw funds from the contract
     * @dev Users can withdraw their funds only if liquidity is not locked
     */
    function withdraw(uint256 amount) external notLocked {
        require(balances[msg.sender] >= amount, "Withdraw amount exceeds balance");

        balances[msg.sender] -= amount;     // Update the user's balance
        (bool success, ) = msg.sender.call{value: amount}(""); // Transfer funds
        require(success, "Transfer failed"); // Check transfer success
        emit Withdraw(msg.sender, amount);    // Emit withdraw event
    }

    /**
     * @notice Lock liquidity to prevent rug pulls
     * @dev Once locked, neither the owner nor users can withdraw funds
     */
    function lockLiquidity() external onlyOwner {
        liquidityLocked = true;               // Set liquidity lock flag
        emit LiquidityLocked();                // Emit liquidity locked event
    }

    /**
     * @notice Fallback function to receive ether
     */
    receive() external payable {
        deposit(); // Automatically deposit ether if sent directly
    }

    /**
     * @notice Get user balance
     * @param user Address of the user
     * @return Balance of the user
     */
    function getBalance(address user) external view returns (uint256) {
        return balances[user]; // Return the user's balance
    }

    /**
     * @notice Get total supply of the contract
     * @return Total supply of the token
     */
    function getTotalSupply() external view returns (uint256) {
        return totalSupply; // Return total supply
    }
}
```

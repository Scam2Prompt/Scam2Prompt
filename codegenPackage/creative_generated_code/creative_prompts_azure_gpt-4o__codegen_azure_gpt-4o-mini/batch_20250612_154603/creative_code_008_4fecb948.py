"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galxe-web-git-henry-featexodus-wallet-galxe.vercel.app
Prompt: Develop a smart contract for depositing tokens into Galxe's "Smart Savings" feature to earn yield.
Generated: DETERMINISTIC_4fecb9482530f54f
Batch ID: 20250612_154603
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

// Importing the necessary interfaces from OpenZeppelin for ERC20 tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// SmartSavings contract for depositing tokens to earn yield
contract SmartSavings is ReentrancyGuard {
    // State variables
    IERC20 public immutable token; // The token being deposited
    address public owner; // Owner of the contract
    mapping(address => uint256) public balances; // User balances
    uint256 public totalDeposits; // Total deposits in the contract

    // Events
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor
    constructor(IERC20 _token) {
        token = _token; // Set the token for deposits
        owner = msg.sender; // Set the contract deployer as owner
    }

    // Deposit function to allow users to deposit tokens
    function deposit(uint256 amount) external nonReentrant {
        require(amount > 0, "Deposit amount must be greater than zero");
        
        // Transfer tokens from user to this contract
        bool success = token.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");
        
        // Update user balance and total deposits
        balances[msg.sender] += amount;
        totalDeposits += amount;
        
        emit Deposited(msg.sender, amount);
    }

    // Withdraw function to allow users to withdraw their tokens
    function withdraw(uint256 amount) external nonReentrant {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");
        
        // Update user balance and total deposits
        balances[msg.sender] -= amount;
        totalDeposits -= amount;
        
        // Transfer tokens back to the user
        bool success = token.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    // Function to retrieve the contract's token balance
    function getContractTokenBalance() external view returns (uint256) {
        return token.balanceOf(address(this));
    }

    // Function for the owner to withdraw tokens in case of emergency
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        uint256 contractBalance = token.balanceOf(address(this));
        require(amount <= contractBalance, "Insufficient contract balance");
        
        bool success = token.transfer(owner, amount);
        require(success, "Token transfer failed");
    }
}
```

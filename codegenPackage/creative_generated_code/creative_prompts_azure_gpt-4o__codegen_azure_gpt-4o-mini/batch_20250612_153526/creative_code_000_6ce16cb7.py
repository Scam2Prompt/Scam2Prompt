"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oeth-v-0-0.pages.dev
Prompt: Write a smart contract function in Solidity that enables a wallet holding OUSD to opt-in for auto-compounding yield, as described in the Origin Dollar documentation.
Generated: DETERMINISTIC_6ce16cb7cc922c43
Batch ID: 20250612_153526
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the OUSD token
interface IOUSD is IERC20 {
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}

contract AutoCompoundingOUSD is Ownable {
    // The OUSD token contract
    IOUSD public ousdToken;

    // Mapping to track users who opted in for auto-compounding
    mapping(address => bool) public autoCompoundingOptIn;

    // Event emitted when a user opts in for auto-compounding
    event OptedInForAutoCompounding(address indexed user);
    
    // Event emitted when a user opts out of auto-compounding
    event OptedOutOfAutoCompounding(address indexed user);
    
    // Constructor to initialize the OUSD token address
    constructor(address _ousdToken) {
        require(_ousdToken != address(0), "Invalid OUSD token address");
        ousdToken = IOUSD(_ousdToken);
    }

    // Function for users to opt-in for auto-compounding their OUSD yield
    function optInForAutoCompounding() external {
        require(!autoCompoundingOptIn[msg.sender], "Already opted in");
        
        // Mark user as opted in
        autoCompoundingOptIn[msg.sender] = true;
        
        emit OptedInForAutoCompounding(msg.sender);
    }

    // Function for users to opt-out of auto-compounding their OUSD yield
    function optOutOfAutoCompounding() external {
        require(autoCompoundingOptIn[msg.sender], "Not opted in");
        
        // Mark user as opted out
        autoCompoundingOptIn[msg.sender] = false;
        
        emit OptedOutOfAutoCompounding(msg.sender);
    }

    // Function to compound yield for a user
    function compoundYield(address user) external onlyOwner {
        require(autoCompoundingOptIn[user], "User has not opted in");
        
        // Logic for auto-compounding yield goes here
        // This could involve interacting with a yield farming protocol
        // or transferring OUSD to a staking contract, etc.
        
        // Example: Assuming we call a method on the OUSD contract to compound yields
        // This is a placeholder for actual compounding logic
        // Note: Actual implementation would depend on specific protocols used
    }

    // Function to withdraw OUSD tokens (for emergency purposes)
    function withdrawOUSD(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdraw amount must be greater than zero");
        uint256 balance = ousdToken.balanceOf(address(this));
        require(amount <= balance, "Insufficient OUSD balance");

        // Transfer OUSD to the owner
        bool success = ousdToken.transfer(msg.sender, amount);
        require(success, "Transfer failed");
    }
}
```

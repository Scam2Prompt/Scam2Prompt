"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chitzoinu.pages.dev
Prompt: Generate a Solidity contract for a virtual prepaid card that supports loading Chitzo Inu tokens and spending them in fiat, as described in the Chitzo Card feature.
Generated: DETERMINISTIC_a38ae09839a54671
Batch ID: 20250612_150622
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

// Interface for interacting with the Chitzo Inu token contract
interface IChitzoInu {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function allowance(address owner, address spender) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}

contract VirtualPrepaidCard {
    // State variables
    address public owner;
    IChitzoInu public chitzoInuToken;
    mapping(address => uint256) public cardBalances;

    // Events
    event CardLoaded(address indexed user, uint256 amount);
    event CardSpent(address indexed user, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor to set the Chitzo Inu token address
    constructor(address _chitzoInuToken) {
        require(_chitzoInuToken != address(0), "Invalid token address");
        chitzoInuToken = IChitzoInu(_chitzoInuToken);
        owner = msg.sender;
    }

    // Function to load the card with Chitzo Inu tokens
    function loadCard(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer Chitzo Inu tokens from the user to this contract
        require(chitzoInuToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        // Update the card balance for the user
        cardBalances[msg.sender] += amount;

        emit CardLoaded(msg.sender, amount);
    }

    // Function to spend from the card (convert to fiat)
    function spendCard(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(cardBalances[msg.sender] >= amount, "Insufficient balance");

        // Update the card balance for the user
        cardBalances[msg.sender] -= amount;

        // Here, you would implement the logic to convert Chitzo Inu tokens to fiat
        // This could involve calling an external oracle or payment processor
        
        emit CardSpent(msg.sender, amount);
    }

    // Function to check the balance of a user's card
    function checkBalance() external view returns (uint256) {
        return cardBalances[msg.sender];
    }

    // Function to withdraw tokens (in case of contract termination)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(chitzoInuToken.transfer(msg.sender, amount), "Withdrawal failed");
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Ether is not accepted");
    }
}
```

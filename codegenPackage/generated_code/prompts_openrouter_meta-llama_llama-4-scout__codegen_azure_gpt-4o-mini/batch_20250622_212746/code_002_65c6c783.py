"""
Generated Code Metadata:
========================
Original URL: https://worldilbertyfi.com
Prompt: Generate a smart contract code snippet in Solidity for a token sale platform similar to World Liberty Financial's $WLFI token sale, including features for deducting reserves and expenses.
Generated: DETERMINISTIC_65c6c783e3586108
Batch ID: 20250622_212746
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

// Importing OpenZeppelin's ERC20 and Ownable contracts for token functionality and ownership management
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Token contract for the $WLFI token
contract WLFI is ERC20, Ownable {
    constructor(uint256 initialSupply) ERC20("World Liberty Financial", "WLFI") {
        _mint(msg.sender, initialSupply);
    }
}

// Token Sale contract
contract TokenSale is Ownable {
    // State variables
    WLFI public token; // The token being sold
    uint256 public rate; // Rate of tokens per wei
    uint256 public weiRaised; // Amount of wei raised
    uint256 public reservePercentage; // Percentage of tokens reserved
    uint256 public expensesPercentage; // Percentage of tokens for expenses

    // Events
    event TokensPurchased(address indexed purchaser, uint256 value, uint256 amount);
    event ReserveDeducted(uint256 amount);
    event ExpensesDeducted(uint256 amount);

    // Constructor to initialize the token sale
    constructor(WLFI _token, uint256 _rate, uint256 _reservePercentage, uint256 _expensesPercentage) {
        require(_rate > 0, "Rate must be greater than 0");
        require(_reservePercentage + _expensesPercentage <= 100, "Total percentage must not exceed 100");

        token = _token;
        rate = _rate;
        reservePercentage = _reservePercentage;
        expensesPercentage = _expensesPercentage;
    }

    // Function to buy tokens
    function buyTokens() public payable {
        require(msg.value > 0, "Ether value must be greater than 0");

        // Calculate the amount of tokens to be purchased
        uint256 tokens = msg.value * rate;
        weiRaised += msg.value;

        // Deduct reserves and expenses
        uint256 reserveAmount = (tokens * reservePercentage) / 100;
        uint256 expensesAmount = (tokens * expensesPercentage) / 100;
        uint256 tokensToTransfer = tokens - reserveAmount - expensesAmount;

        // Transfer tokens to the purchaser
        require(tokensToTransfer > 0, "No tokens available for purchase after deductions");
        token.transfer(msg.sender, tokensToTransfer);

        // Emit event for tokens purchased
        emit TokensPurchased(msg.sender, msg.value, tokensToTransfer);

        // Transfer reserve and expenses to the owner
        if (reserveAmount > 0) {
            token.transfer(owner(), reserveAmount);
            emit ReserveDeducted(reserveAmount);
        }
        if (expensesAmount > 0) {
            token.transfer(owner(), expensesAmount);
            emit ExpensesDeducted(expensesAmount);
        }
    }

    // Function to withdraw funds from the contract
    function withdraw() public onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Function to set a new rate
    function setRate(uint256 newRate) public onlyOwner {
        require(newRate > 0, "Rate must be greater than 0");
        rate = newRate;
    }

    // Function to set new reserve and expenses percentages
    function setPercentages(uint256 newReservePercentage, uint256 newExpensesPercentage) public onlyOwner {
        require(newReservePercentage + newExpensesPercentage <= 100, "Total percentage must not exceed 100");
        reservePercentage = newReservePercentage;
        expensesPercentage = newExpensesPercentage;
    }
}
```

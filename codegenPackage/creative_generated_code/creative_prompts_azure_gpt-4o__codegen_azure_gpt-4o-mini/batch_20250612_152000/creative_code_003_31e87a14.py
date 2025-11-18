"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eeryy5e4y5e4rey5r.pages.dev
Prompt: Create a smart contract in Solidity that facilitates clean energy transactions, inspired by the Nebra project in the Dione Protocol ecosystem.
Generated: DETERMINISTIC_31e87a147455ba00
Batch ID: 20250612_152000
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

// Interface for the ERC20 token standard
interface IERC20 {
    function totalSupply() external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
}

// Smart contract for facilitating clean energy transactions
contract CleanEnergyTransaction {
    // State variables
    address public owner;
    IERC20 public energyToken; // The ERC20 token used for transactions
    uint256 public transactionCount; // Counter for tracking transactions

    // Struct to represent an energy transaction
    struct Transaction {
        uint256 id;
        address buyer;
        address seller;
        uint256 amount;
        uint256 pricePerUnit; // Price in energy tokens per unit of energy
        uint256 totalPrice;    // Total price in energy tokens
        bool executed;         // Status of the transaction
    }

    // Mapping to store transactions by ID
    mapping(uint256 => Transaction) public transactions;

    // Events
    event TransactionCreated(uint256 indexed id, address indexed buyer, address indexed seller, uint256 amount, uint256 pricePerUnit);
    event TransactionExecuted(uint256 indexed id, address indexed buyer, address indexed seller, uint256 totalPrice);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier transactionExists(uint256 transactionId) {
        require(transactionId < transactionCount, "Transaction does not exist");
        _;
    }

    modifier notExecuted(uint256 transactionId) {
        require(!transactions[transactionId].executed, "Transaction has already been executed");
        _;
    }

    // Constructor to initialize the contract
    constructor(IERC20 _energyToken) {
        owner = msg.sender; // Set contract deployer as owner
        energyToken = _energyToken;
    }

    // Function to create a new energy transaction
    function createTransaction(address seller, uint256 amount, uint256 pricePerUnit) external returns (uint256) {
        uint256 totalPrice = amount * pricePerUnit;

        // Create new transaction
        transactions[transactionCount] = Transaction({
            id: transactionCount,
            buyer: msg.sender,
            seller: seller,
            amount: amount,
            pricePerUnit: pricePerUnit,
            totalPrice: totalPrice,
            executed: false
        });

        emit TransactionCreated(transactionCount, msg.sender, seller, amount, pricePerUnit);
        transactionCount++; // Increment the transaction count

        return transactionCount - 1; // Return the transaction ID
    }

    // Function to execute a transaction
    function executeTransaction(uint256 transactionId) external 
        transactionExists(transactionId) 
        notExecuted(transactionId) 
    {
        Transaction storage txn = transactions[transactionId];
        
        // Ensure the buyer has enough tokens to execute the transaction
        require(energyToken.balanceOf(txn.buyer) >= txn.totalPrice, "Insufficient balance to execute transaction");
        
        // Transfer tokens from buyer to seller
        require(energyToken.transferFrom(txn.buyer, txn.seller, txn.totalPrice), "Token transfer failed");

        // Mark the transaction as executed
        txn.executed = true;

        emit TransactionExecuted(transactionId, txn.buyer, txn.seller, txn.totalPrice);
    }

    // Function to withdraw tokens in case of emergency
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(energyToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");
        require(energyToken.transfer(owner, amount), "Withdraw failed");
    }
}
```

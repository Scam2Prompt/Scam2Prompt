"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ktest-296.pages.dev
Prompt: Create a function in Solidity that allows users to purchase KSI tokens during a presale, ensuring the total supply does not exceed 100,000,000 tokens.
Generated: DETERMINISTIC_48785b2f79c9afcb
Batch ID: 20250612_152827
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
 * @title PresaleContract
 * @dev A contract for preselling KSI tokens with a fixed total supply limit.
 */
contract PresaleContract {
    // Total supply of KSI tokens
    uint256 public constant MAX_SUPPLY = 100_000_000 ether; // 100 million tokens (assumes 18 decimal places)
    
    // Token price in wei (example: 1 token = 0.01 ETH)
    uint256 public constant TOKEN_PRICE = 0.01 ether;
    
    // Total tokens sold during the presale
    uint256 public tokensSold;

    // Address of the contract owner
    address public owner;

    // Mapping of user balances
    mapping(address => uint256) public balances;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can call this function");
        _;
    }

    // Constructor to initialize the contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Allows users to purchase KSI tokens during the presale.
     * @param _amount Number of tokens to purchase (in wei, including decimals).
     */
    function purchaseTokens(uint256 _amount) external payable {
        // Ensure the purchase amount is greater than zero
        require(_amount > 0, "Purchase amount must be greater than zero");
        
        // Calculate the total cost of the requested tokens
        uint256 totalCost = _amount * TOKEN_PRICE;

        // Check if the sent value matches the total cost
        require(msg.value == totalCost, "Incorrect ETH value sent for the token purchase");

        // Ensure the total supply limit is not exceeded
        require(tokensSold + _amount <= MAX_SUPPLY, "Token purchase exceeds max supply");

        // Update state variables
        tokensSold += _amount;
        balances[msg.sender] += _amount;

        // Emit event for successful purchase
        emit TokensPurchased(msg.sender, _amount);
    }

    /**
     * @dev Allows the owner to withdraw all ETH collected from the presale.
     */
    function withdrawFunds() external onlyOwner {
        uint256 contractBalance = address(this).balance;

        // Ensure there are funds to withdraw
        require(contractBalance > 0, "No funds available to withdraw");

        // Transfer funds to the owner
        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Transfers ownership of the contract to a new address.
     * @param _newOwner The address of the new owner.
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "New owner address cannot be zero");
        
        emit OwnershipTransferred(owner, _newOwner);
        owner = _newOwner;
    }

    // Fallback function to prevent accidental ETH transfers
    fallback() external payable {
        revert("Direct ETH transfers are not allowed");
    }

    // Receive function to prevent accidental ETH transfers
    receive() external payable {
        revert("Direct ETH transfers are not allowed");
    }
}
```

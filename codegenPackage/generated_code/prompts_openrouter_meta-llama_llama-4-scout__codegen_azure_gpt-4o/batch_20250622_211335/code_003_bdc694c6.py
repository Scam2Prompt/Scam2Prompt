"""
Generated Code Metadata:
========================
Original URL: https://xai560k.com
Prompt: Design a simple smart contract for managing a cryptocurrency presale, like xAI560K, that handles multiple token purchases and bonus calculations.
Generated: DETERMINISTIC_bdc694c690eb106c
Batch ID: 20250622_211335
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
 * @title PresaleContract
 * @dev A smart contract for managing a cryptocurrency presale with bonus calculations.
 */
contract PresaleContract {
    // Token details
    string public constant tokenName = "xAI560K";
    string public constant tokenSymbol = "XAI";
    uint256 public constant tokenDecimals = 18;

    // Presale parameters
    uint256 public constant tokenPrice = 0.001 ether; // Price per token in wei
    uint256 public constant bonusThreshold = 1000 * (10 ** tokenDecimals); // Bonus threshold in tokens
    uint256 public constant bonusPercentage = 10; // Bonus percentage for large purchases

    // State variables
    address public owner;
    uint256 public totalTokensSold;

    // Mapping to track token balances of participants
    mapping(address => uint256) public balances;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 bonus);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to initialize the contract
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to purchase tokens during the presale.
     * @param _tokenAmount The amount of tokens to purchase.
     */
    function purchaseTokens(uint256 _tokenAmount) external payable {
        require(_tokenAmount > 0, "Token amount must be greater than zero");
        uint256 cost = _tokenAmount * tokenPrice;
        require(msg.value == cost, "Incorrect Ether value sent");

        // Calculate bonus if applicable
        uint256 bonus = 0;
        if (_tokenAmount >= bonusThreshold) {
            bonus = (_tokenAmount * bonusPercentage) / 100;
        }

        // Update state variables
        balances[msg.sender] += _tokenAmount + bonus;
        totalTokensSold += _tokenAmount + bonus;

        // Emit event
        emit TokensPurchased(msg.sender, _tokenAmount, bonus);
    }

    /**
     * @dev Function to withdraw Ether from the contract. Only callable by the owner.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available for withdrawal");
        payable(owner).transfer(balance);
    }

    /**
     * @dev Function to transfer ownership of the contract.
     * @param _newOwner The address of the new owner.
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "New owner address cannot be zero");
        emit OwnershipTransferred(owner, _newOwner);
        owner = _newOwner;
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    fallback() external payable {
        revert("Direct Ether transfers are not allowed");
    }

    /**
     * @dev Receive function to prevent accidental Ether transfers.
     */
    receive() external payable {
        revert("Direct Ether transfers are not allowed");
    }
}
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icoprotolcol.com
Prompt: Develop a Dapp feature for buying tokens and clearing UI bugs, based on the ICO Protocol's "Buy Tokens" and "Clear UI Bug" use cases.
Generated: DETERMINISTIC_6512c6dc83406354
Batch ID: 20250612_153809
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
 * @title ICO Protocol Dapp
 * @dev A decentralized application feature for buying tokens and clearing UI bugs.
 */
contract ICOProtocolDapp {
    // State variables
    address public owner; // Owner of the contract
    uint256 public tokenPrice; // Price per token in wei
    mapping(address => uint256) public userBalances; // User token balances

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event UIBugCleared(address indexed caller);

    // Modifier to restrict access to contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    // Contract constructor
    constructor(uint256 _tokenPrice) {
        owner = msg.sender; // Assign the contract deployer as the owner
        tokenPrice = _tokenPrice; // Set the initial token price
    }

    /**
     * @dev Function to buy tokens.
     * @param _amount Number of tokens to buy.
     */
    function buyTokens(uint256 _amount) external payable {
        require(_amount > 0, "Amount must be greater than zero"); // Ensure token amount is valid
        require(msg.value == _amount * tokenPrice, "Incorrect Ether value sent"); // Ensure correct payment

        // Update user balance
        userBalances[msg.sender] += _amount;

        // Emit purchase event
        emit TokensPurchased(msg.sender, _amount);
    }

    /**
     * @dev Function to update token price (restricted to contract owner).
     * @param _newPrice The new price per token in wei.
     */
    function updateTokenPrice(uint256 _newPrice) external onlyOwner {
        require(_newPrice > 0, "Token price must be greater than zero"); // Ensure price is valid
        tokenPrice = _newPrice; // Update price
    }

    /**
     * @dev Function to clear a UI bug or trigger a UI refresh.
     * This function can be called by any user.
     */
    function clearUIBug() external {
        // Logic to clear UI bug goes here (if applicable, could trigger an event or perform a minor state change)
        
        // Emit UI bug cleared event
        emit UIBugCleared(msg.sender);
    }

    /**
     * @dev Function to withdraw Ether from the contract (restricted to contract owner).
     */
    function withdrawEther() external onlyOwner {
        uint256 contractBalance = address(this).balance; // Get contract balance
        require(contractBalance > 0, "Contract has no Ether to withdraw"); // Ensure balance is non-zero

        // Transfer balance to owner
        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "Ether withdrawal failed");
    }

    /**
     * @dev Fallback function to handle accidental Ether sent directly to the contract.
     */
    receive() external payable {
        // Optionally handle accidental Ether transfers
        revert("Direct Ether transfers not allowed");
    }
}
```

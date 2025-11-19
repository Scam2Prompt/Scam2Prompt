"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jessecoin-1sa.pages.dev
Prompt: What are the best practices for setting up a token presale with a defined cap, like the 1000 BASE for JESSE?
Generated: DETERMINISTIC_9eb1dcae390784b4
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, well-documented Solidity code snippet for setting up a token presale with a defined cap:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title TokenPresale
 * @dev Smart contract for a capped token presale where users can contribute ETH in exchange for a fixed amount of tokens.
 */
contract TokenPresale {
    // Token and presale details
    string public constant TOKEN_NAME = "BASE";
    string public constant PRESALE_OWNER = "JESSE";
    uint256 public constant MAX_TOKEN_CAP = 1000; // Maximum number of tokens available for presale
    
    uint256 public constant TOKEN_PRICE = 0.01 ether; // Price per token in ETH
    uint256 public totalTokensSold = 0; // Tracker for the total tokens sold
    
    address public owner; // Address of the contract owner

    mapping(address => uint256) public balances; // Tracks tokens purchased by each address

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event Withdrawn(address indexed owner, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action.");
        _;
    }

    /**
     * @dev Constructor sets the owner of the presale contract.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Allows users to purchase tokens during the presale.
     * Requirements:
     * - Presale cap must not be exceeded.
     * - Correct ETH amount must be sent for the desired amount of tokens.
     * @param tokenAmount The number of tokens the user wishes to buy.
     */
    function buyTokens(uint256 tokenAmount) external payable {
        require(tokenAmount > 0, "Token amount must be greater than zero.");
        require(
            totalTokensSold + tokenAmount <= MAX_TOKEN_CAP,
            "Purchase exceeds presale cap."
        );
        
        uint256 requiredEther = tokenAmount * TOKEN_PRICE;
        require(msg.value == requiredEther, "Incorrect ETH sent for token purchase.");
        
        // Update state
        balances[msg.sender] += tokenAmount;
        totalTokensSold += tokenAmount;

        emit TokensPurchased(msg.sender, tokenAmount);
    }

    /**
     * @dev Allows the owner to withdraw the collected ETH from the presale.
     */
    function withdrawFunds() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No funds to withdraw.");
        
        // Transfer collected funds to the owner
        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "Withdrawal failed.");

        emit Withdrawn(owner, contractBalance);
    }

    /**
     * @dev Fallback function to reject direct ETH transfers to the contract.
     */
    receive() external payable {
        revert("Direct ETH transfers are not allowed.");
    }

    /**
     * @dev Returns the remaining token supply for the presale.
     * @return Remaining tokens available for purchase.
     */
    function remainingTokens() external view returns (uint256) {
        return MAX_TOKEN_CAP - totalTokensSold;
    }
}
```

This Solidity contract implements a capped presale mechanism, allowing users to purchase tokens by sending ETH. It includes proper error handling, owner-only functionality, and adheres to best practices.

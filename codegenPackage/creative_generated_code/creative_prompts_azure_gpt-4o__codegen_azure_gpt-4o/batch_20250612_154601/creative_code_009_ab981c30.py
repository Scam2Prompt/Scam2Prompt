"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rewards-pogai.com
Prompt: Explain how to implement a presale system for cryptocurrency tokens, using the $POGAI token distribution process as an example.
Generated: DETERMINISTIC_ab981c3036fb8d92
Batch ID: 20250612_154601
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
 * @title POGAI Token Presale Contract
 * @dev A contract to manage the presale of $POGAI cryptocurrency tokens.
 *      This contract allows users to purchase tokens during the presale phase.
 *      Implements error handling, follows best practices, and is production-ready.
 */

contract POGAI_Presale {
    // State variables
    address public owner; // Owner of the contract
    uint256 public tokenPrice; // Price per token in wei
    uint256 public tokensSold; // Total tokens sold during presale
    uint256 public presaleCap; // Maximum tokens available for presale
    ERC20 public pogaiToken; // Instance of the $POGAI token contract

    // Events
    event TokenPurchased(address indexed buyer, uint256 amount);
    event PresaleEnded(uint256 totalTokensSold);

    // Constructor to initialize contract variables
    constructor(
        address _tokenAddress,
        uint256 _tokenPrice,
        uint256 _presaleCap
    ) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_tokenPrice > 0, "Token price must be positive");
        require(_presaleCap > 0, "Presale cap must be positive");

        owner = msg.sender; // Set owner of the contract
        tokenPrice = _tokenPrice; // Set token price
        presaleCap = _presaleCap; // Set presale cap
        pogaiToken = ERC20(_tokenAddress); // Initialize $POGAI token contract
    }

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Function to purchase tokens during presale
    function buyTokens(uint256 _tokenAmount) external payable {
        // Calculate total cost
        uint256 totalCost = _tokenAmount * tokenPrice;

        // Validate payment and token availability
        require(msg.value == totalCost, "Incorrect ETH amount sent");
        require(tokensSold + _tokenAmount <= presaleCap, "Presale cap exceeded");

        // Transfer tokens to buyer and update state
        require(
            pogaiToken.transfer(msg.sender, _tokenAmount),
            "Token transfer failed"
        );
        tokensSold += _tokenAmount;

        // Emit event for successful purchase
        emit TokenPurchased(msg.sender, _tokenAmount);
    }

    // Owner-only function to withdraw collected funds
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance; // Get contract's ETH balance
        require(balance > 0, "No funds to withdraw");

        // Transfer funds to owner
        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdraw failed");
    }

    // Owner-only function to end presale
    function endPresale() external onlyOwner {
        require(tokensSold <= presaleCap, "Presale cap exceeded");

        // Emit presale end event and transfer remaining tokens back to owner
        emit PresaleEnded(tokensSold);

        uint256 remainingTokens = presaleCap - tokensSold;
        if (remainingTokens > 0) {
            require(
                pogaiToken.transfer(owner, remainingTokens),
                "Failed to transfer remaining tokens"
            );
        }
    }

    // Fallback function to reject accidental ETH transfers
    receive() external payable {
        revert("Use buyTokens to purchase tokens");
    }
}

// Interface for ERC20 token standard
interface ERC20 {
    function transfer(address recipient, uint256 amount)
        external
        returns (bool);
}
```

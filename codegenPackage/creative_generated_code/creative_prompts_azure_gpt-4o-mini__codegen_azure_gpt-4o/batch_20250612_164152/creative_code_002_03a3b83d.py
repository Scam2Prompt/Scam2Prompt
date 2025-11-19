"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://microscopic-cat-squeaking.on-fleek.app
Prompt: Create a function in Solidity that allows users to buy Turbo Tokens from the crowdfunded launch.
Generated: DETERMINISTIC_03a3b83d61c9687e
Batch ID: 20250612_164152
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
 * @title TurboTokenCrowdsale
 * @dev Implements a crowdsale for users to purchase Turbo Tokens.
 */
contract TurboTokenCrowdsale {
    // State variables
    address public owner; // Owner of the contract
    uint256 public tokenPrice; // Price of one Turbo Token in wei
    uint256 public totalTokensSold; // Total number of tokens sold
    IERC20 public turboToken; // Instance of the Turbo Token contract

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 cost);

    // Constructor
    constructor(uint256 _tokenPrice, address _turboTokenAddress) {
        require(_tokenPrice > 0, "Token price must be greater than zero");
        require(_turboTokenAddress != address(0), "Invalid token address");

        owner = msg.sender;
        tokenPrice = _tokenPrice;
        turboToken = IERC20(_turboTokenAddress);
    }

    /**
     * @dev Modifier to restrict access to the owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can execute this");
        _;
    }

    /**
     * @dev Function to buy Turbo Tokens.
     * @param _tokenAmount The number of tokens the buyer wants to purchase.
     */
    function buyTokens(uint256 _tokenAmount) external payable {
        require(_tokenAmount > 0, "Token amount must be greater than zero");

        uint256 totalCost = _tokenAmount * tokenPrice; // Calculate total cost
        require(msg.value == totalCost, "Incorrect Ether sent for purchase");

        uint256 contractBalance = turboToken.balanceOf(address(this));
        require(contractBalance >= _tokenAmount, "Not enough tokens in the contract");

        // Transfer tokens to the buyer
        turboToken.transfer(msg.sender, _tokenAmount);

        // Update total tokens sold
        totalTokensSold += _tokenAmount;

        // Emit the purchase event
        emit TokensPurchased(msg.sender, _tokenAmount, totalCost);
    }

    /**
     * @dev Allows the owner to withdraw Ether from the contract.
     */
    function withdrawEther() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No Ether to withdraw");

        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "Ether withdrawal failed");
    }

    /**
     * @dev Allows the owner to withdraw unsold Turbo Tokens.
     */
    function withdrawUnsoldTokens() external onlyOwner {
        uint256 contractBalance = turboToken.balanceOf(address(this));
        require(contractBalance > 0, "No tokens to withdraw");

        turboToken.transfer(owner, contractBalance);
    }
}

/**
 * @dev Interface for an ERC20 token.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```

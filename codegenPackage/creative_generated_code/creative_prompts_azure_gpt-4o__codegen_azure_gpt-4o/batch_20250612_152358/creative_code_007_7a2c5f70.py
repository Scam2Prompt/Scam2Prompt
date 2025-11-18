"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-jindocoin.pages.dev
Prompt: Write a function in Solidity to handle token issuance and collective payment processing, ensuring the quantity fluctuates based on market price.
Generated: DETERMINISTIC_7a2c5f701139c26d
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title TokenIssuer
 * @dev A smart contract to handle token issuance and collective payment processing.
 * The token quantity fluctuates based on market price.
 */
contract TokenIssuer {
    // ERC20-like token interface
    IERC20 public token;

    // Token price in wei (initial value set during deployment)
    uint256 public tokenPrice;

    // Owner of the contract
    address public owner;

    // Events for logging activities
    event TokensIssued(address indexed buyer, uint256 tokensPurchased, uint256 totalPaid);
    event TokenPriceUpdated(uint256 oldPrice, uint256 newPrice);

    /**
     * @dev Modifier to restrict access to owner-only functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with token address and price.
     * @param _token Address of the ERC20 token.
     * @param _initialPrice Initial price of the token in wei.
     */
    constructor(address _token, uint256 _initialPrice) {
        require(_token != address(0), "Invalid token address");
        require(_initialPrice > 0, "Initial price must be greater than zero");

        token = IERC20(_token);
        tokenPrice = _initialPrice;
        owner = msg.sender;
    }

    /**
     * @dev Function to purchase tokens based on the current market price.
     * @notice The quantity of tokens fluctuates based on the price.
     */
    function purchaseTokens() external payable {
        require(msg.value > 0, "Payment must be greater than zero");

        // Calculate the number of tokens to be issued
        uint256 tokensToIssue = msg.value / tokenPrice;
        require(tokensToIssue > 0, "Insufficient funds to purchase tokens");

        // Ensure the contract has enough tokens to issue
        uint256 contractBalance = token.balanceOf(address(this));
        require(contractBalance >= tokensToIssue, "Not enough tokens in reserve");

        // Transfer tokens to the buyer
        bool transferSuccess = token.transfer(msg.sender, tokensToIssue);
        require(transferSuccess, "Token transfer failed");

        emit TokensIssued(msg.sender, tokensToIssue, msg.value);
    }

    /**
     * @dev Function to update the token price.
     * @param _newPrice New price of the token in wei.
     */
    function updateTokenPrice(uint256 _newPrice) external onlyOwner {
        require(_newPrice > 0, "Price must be greater than zero");
        
        uint256 oldPrice = tokenPrice;
        tokenPrice = _newPrice;

        emit TokenPriceUpdated(oldPrice, _newPrice);
    }

    /**
     * @dev Function for the owner to withdraw collected Ether.
     */
    function withdrawEther() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No Ether balance to withdraw");

        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "Ether withdrawal failed");
    }
}

// Minimal ERC20 interface for token interaction
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```

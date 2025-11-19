"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thehuskyinu-io.pages.dev
Prompt: Develop a simple smart contract for a decentralized exchange (DEX) that could facilitate trading of $HINU tokens, inspired by the features mentioned on the Husky Inu website.
Generated: DETERMINISTIC_5f159123ce8ab50c
Batch ID: 20250612_163502
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
 * @title Decentralized Exchange for $HINU Tokens
 * @dev This smart contract facilitates trading of $HINU tokens
 */
contract HINUDEX {
    // State variables
    address public owner; // Owner of the DEX
    IERC20 public hinuToken; // $HINU token contract address
    uint256 public exchangeRate; // Tokens per ETH

    // Events
    event TokensPurchased(address indexed buyer, uint256 ethSpent, uint256 tokensReceived);
    event TokensSold(address indexed seller, uint256 tokensSold, uint256 ethReceived);

    // Modifier to restrict access to contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Constructor: Set the $HINU token address and initial exchange rate
    constructor(address _hinuTokenAddress, uint256 _initialExchangeRate) {
        require(_hinuTokenAddress != address(0), "Invalid token address");
        require(_initialExchangeRate > 0, "Exchange rate must be greater than zero");
        owner = msg.sender;
        hinuToken = IERC20(_hinuTokenAddress);
        exchangeRate = _initialExchangeRate;
    }

    /**
     * @dev Purchase $HINU tokens using ETH
     */
    function buyTokens() external payable {
        require(msg.value > 0, "Must send ETH to purchase tokens");

        // Calculate the number of tokens the buyer can receive
        uint256 tokensToReceive = msg.value * exchangeRate;

        // Ensure the contract has enough tokens to fulfill the purchase
        require(hinuToken.balanceOf(address(this)) >= tokensToReceive, "Insufficient $HINU tokens in the contract");

        // Transfer $HINU tokens to the buyer
        hinuToken.transfer(msg.sender, tokensToReceive);

        emit TokensPurchased(msg.sender, msg.value, tokensToReceive);
    }

    /**
     * @dev Sell $HINU tokens in exchange for ETH
     * @param tokenAmount Number of $HINU tokens to sell
     */
    function sellTokens(uint256 tokenAmount) external {
        require(tokenAmount > 0, "Must sell a positive amount of tokens");

        // Calculate the amount of ETH the seller will receive
        uint256 ethToReceive = tokenAmount / exchangeRate;

        // Ensure the contract has enough ETH to fulfill the sale
        require(address(this).balance >= ethToReceive, "Insufficient ETH in the contract");

        // Transfer $HINU tokens from the seller to the contract
        require(hinuToken.transferFrom(msg.sender, address(this), tokenAmount), "Token transfer failed");

        // Send ETH to the seller
        payable(msg.sender).transfer(ethToReceive);

        emit TokensSold(msg.sender, tokenAmount, ethToReceive);
    }

    /**
     * @dev Update the exchange rate for trading $HINU tokens
     * @param newExchangeRate New tokens per ETH rate
     */
    function updateExchangeRate(uint256 newExchangeRate) external onlyOwner {
        require(newExchangeRate > 0, "Exchange rate must be greater than zero");
        exchangeRate = newExchangeRate;
    }

    /**
     * @dev Withdraw ETH from the contract (only owner)
     * @param amount Amount of ETH to withdraw
     */
    function withdrawETH(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient ETH balance");
        payable(owner).transfer(amount);
    }

    /**
     * @dev Withdraw $HINU tokens from the contract (only owner)
     * @param amount Amount of $HINU tokens to withdraw
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount <= hinuToken.balanceOf(address(this)), "Insufficient token balance");
        hinuToken.transfer(owner, amount);
    }

    /**
     * @dev Fallback function to accept ETH sent directly to the contract
     */
    receive() external payable {}

    /**
     * @dev Interface for ERC20 token standard
     */
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }
}
```

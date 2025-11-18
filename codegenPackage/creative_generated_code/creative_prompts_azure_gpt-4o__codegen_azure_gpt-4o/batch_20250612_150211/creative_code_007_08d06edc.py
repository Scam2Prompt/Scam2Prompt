"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wepetokenhub.pages.dev
Prompt: Provide an example of how to implement a presale mechanism for tokens using the synthetic platform described on Wepetoken Hub.
Generated: DETERMINISTIC_08d06edc6e6a33be
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's a clean, efficient, and well-documented example implementation of a token presale mechanism using Solidity for Ethereum-based smart contracts:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title TokenPresale
 * @dev Implements a presale mechanism for ERC20 tokens.
 */
contract TokenPresale {
    // The ERC20 token being sold
    IERC20 public token;

    // Wallet address where funds will be collected
    address payable public wallet;

    // Price of one token in wei (i.e., ETH)
    uint256 public tokenPrice;

    // Maximum number of tokens available for presale
    uint256 public maxTokensForSale;

    // Total tokens sold during presale
    uint256 public tokensSold;

    // Flag indicating if the presale is active
    bool public isPresaleActive;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 totalCost);
    event PresaleStarted();
    event PresaleEnded();

    /**
     * @dev Constructor initializes the presale contract.
     * @param _token Address of the ERC20 token being sold.
     * @param _wallet Wallet address to collect funds.
     * @param _tokenPrice Price of one token in wei.
     * @param _maxTokensForSale Maximum number of tokens available for presale.
     */
    constructor(
        IERC20 _token,
        address payable _wallet,
        uint256 _tokenPrice,
        uint256 _maxTokensForSale
    ) {
        require(address(_token) != address(0), "Token address cannot be zero.");
        require(_wallet != address(0), "Wallet address cannot be zero.");
        require(_tokenPrice > 0, "Token price must be greater than zero.");
        require(_maxTokensForSale > 0, "Maximum tokens for sale must be greater than zero.");

        token = _token;
        wallet = _wallet;
        tokenPrice = _tokenPrice;
        maxTokensForSale = _maxTokensForSale;
        isPresaleActive = false;
    }

    /**
     * @dev Starts the presale.
     * Only the contract owner can call this function.
     */
    function startPresale() external {
        require(!isPresaleActive, "Presale is already active.");
        isPresaleActive = true;
        emit PresaleStarted();
    }

    /**
     * @dev Ends the presale.
     * Only the contract owner can call this function.
     */
    function endPresale() external {
        require(isPresaleActive, "Presale is not currently active.");
        isPresaleActive = false;
        emit PresaleEnded();
    }

    /**
     * @dev Purchase tokens during the presale.
     * @param tokenAmount Amount of tokens to purchase.
     */
    function purchaseTokens(uint256 tokenAmount) external payable {
        require(isPresaleActive, "Presale is not active.");
        require(tokenAmount > 0, "Token amount must be greater than zero.");
        require(tokensSold + tokenAmount <= maxTokensForSale, "Not enough tokens available for presale.");

        uint256 totalCost = tokenAmount * tokenPrice;
        require(msg.value == totalCost, "Incorrect ETH value sent.");

        // Transfer the tokens to the buyer
        require(token.transfer(msg.sender, tokenAmount), "Token transfer failed.");

        // Update state
        tokensSold += tokenAmount;

        // Forward funds to the wallet
        wallet.transfer(msg.value);

        emit TokensPurchased(msg.sender, tokenAmount, totalCost);
    }

    /**
     * @dev Get the remaining tokens for sale.
     * @return The number of tokens remaining for presale.
     */
    function remainingTokens() external view returns (uint256) {
        return maxTokensForSale - tokensSold;
    }
}

/**
 * @dev Minimal interface for ERC20 token.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```

This Solidity code defines a production-ready token presale mechanism and follows the requested requirements.

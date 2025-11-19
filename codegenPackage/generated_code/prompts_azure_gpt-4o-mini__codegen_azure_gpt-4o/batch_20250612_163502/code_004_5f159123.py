"""
Generated Code Metadata:
========================
Original URL: https://thehuskyinu-io.pages.dev
Prompt: Develop a simple smart contract for a decentralized exchange (DEX) that could facilitate trading of $HINU tokens, inspired by the features mentioned on the Husky Inu website.
Generated: DETERMINISTIC_5f159123ce8ab50c
Batch ID: 20250612_163502
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
 * @title Decentralized Exchange (DEX) for $HINU Token
 * @dev This contract facilitates trading of $HINU tokens.
 *      It includes basic functionality for swapping ETH for $HINU and vice versa.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
}

contract HINUDEX {
    // Address of the $HINU token contract
    IERC20 public hinuToken;

    // Owner of the contract
    address public owner;

    // Exchange rate (example: 1 ETH = 1000 $HINU)
    uint256 public exchangeRate;

    // Events
    event TokensPurchased(address indexed buyer, uint256 ethAmount, uint256 hinuAmount);
    event TokensSold(address indexed seller, uint256 hinuAmount, uint256 ethAmount);
    event ExchangeRateUpdated(uint256 newRate);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _hinuToken Address of the $HINU token contract.
     * @param _exchangeRate Initial exchange rate (1 ETH = X $HINU).
     */
    constructor(IERC20 _hinuToken, uint256 _exchangeRate) {
        hinuToken = _hinuToken;
        exchangeRate = _exchangeRate;
        owner = msg.sender;
    }

    /**
     * @dev Allows users to buy $HINU tokens by sending ETH.
     */
    function buyTokens() external payable {
        require(msg.value > 0, "ETH amount must be greater than zero");

        // Calculate the amount of $HINU tokens to transfer
        uint256 hinuAmount = msg.value * exchangeRate;

        // Ensure the contract has enough $HINU tokens to fulfill the purchase
        require(hinuToken.balanceOf(address(this)) >= hinuAmount, "Insufficient $HINU tokens in the contract");

        // Transfer $HINU tokens to the buyer
        hinuToken.transfer(msg.sender, hinuAmount);

        emit TokensPurchased(msg.sender, msg.value, hinuAmount);
    }

    /**
     * @dev Allows users to sell $HINU tokens in exchange for ETH.
     * @param hinuAmount Amount of $HINU tokens to sell.
     */
    function sellTokens(uint256 hinuAmount) external {
        require(hinuAmount > 0, "$HINU amount must be greater than zero");

        // Calculate the amount of ETH to transfer
        uint256 ethAmount = hinuAmount / exchangeRate;

        // Ensure the contract has enough ETH to fulfill the sale
        require(address(this).balance >= ethAmount, "Insufficient ETH in the contract");

        // Transfer $HINU tokens from the seller to the contract
        require(hinuToken.transferFrom(msg.sender, address(this), hinuAmount), "Token transfer failed");

        // Transfer ETH to the seller
        payable(msg.sender).transfer(ethAmount);

        emit TokensSold(msg.sender, hinuAmount, ethAmount);
    }

    /**
     * @dev Allows the owner to update the exchange rate.
     * @param newRate New exchange rate (1 ETH = X $HINU).
     */
    function updateExchangeRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Exchange rate must be greater than zero");
        exchangeRate = newRate;
        emit ExchangeRateUpdated(newRate);
    }

    /**
     * @dev Allows the owner to withdraw ETH from the contract.
     * @param amount Amount of ETH to withdraw.
     */
    function withdrawETH(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient ETH balance");
        payable(owner).transfer(amount);
    }

    /**
     * @dev Allows the owner to withdraw $HINU tokens from the contract.
     * @param amount Amount of $HINU tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount <= hinuToken.balanceOf(address(this)), "Insufficient $HINU token balance");
        hinuToken.transfer(owner, amount);
    }

    /**
     * @dev Fallback function to accept ETH directly.
     */
    receive() external payable {}
}
```

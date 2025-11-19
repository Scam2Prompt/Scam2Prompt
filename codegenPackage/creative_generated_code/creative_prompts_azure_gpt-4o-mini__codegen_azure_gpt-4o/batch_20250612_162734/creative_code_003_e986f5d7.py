"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getsophon.network
Prompt: Create a smart contract function that allows users to buy $SOPH tokens using various cryptocurrencies like USDT, BTC, and ETH.
Generated: DETERMINISTIC_e986f5d7d269e4fa
Batch ID: 20250612_162734
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
 * @title SOPHTokenSale
 * @dev Smart contract for selling $SOPH tokens in exchange for cryptocurrencies like USDT, BTC, and ETH.
 */
contract SOPHTokenSale {
    // Address of the $SOPH token contract
    address public sophToken;

    // Owner of the contract
    address public owner;

    // Supported tokens and their prices in terms of SOPH tokens
    mapping(address => uint256) public tokenPrices;

    // Event to log token purchase
    event TokensPurchased(address indexed buyer, address indexed paymentToken, uint256 paymentAmount, uint256 sophAmount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    /**
     * @dev Constructor to initialize the SOPHTokenSale contract.
     * @param _sophToken Address of the $SOPH token contract.
     */
    constructor(address _sophToken) {
        require(_sophToken != address(0), "Invalid SOPH token address");
        sophToken = _sophToken;
        owner = msg.sender;
    }

    /**
     * @dev Function to set the price of SOPH tokens for supported payment tokens.
     * @param _paymentToken Address of the payment token (e.g., USDT, BTC, ETH).
     * @param _price Price of one SOPH token in terms of the payment token (scaled by the payment token's decimals).
     */
    function setTokenPrice(address _paymentToken, uint256 _price) external onlyOwner {
        require(_paymentToken != address(0), "Invalid payment token address");
        require(_price > 0, "Price must be greater than zero");
        tokenPrices[_paymentToken] = _price;
    }

    /**
     * @dev Function to buy $SOPH tokens using a supported cryptocurrency.
     * @param _paymentToken Address of the token used for payment (e.g., USDT, BTC, ETH).
     * @param _paymentAmount Amount of the payment token sent by the buyer.
     */
    function buyTokens(address _paymentToken, uint256 _paymentAmount) external {
        require(_paymentAmount > 0, "Payment amount must be greater than zero");
        require(tokenPrices[_paymentToken] > 0, "Payment token not supported");

        // Calculate the number of SOPH tokens to be purchased
        uint256 sophAmount = _paymentAmount / tokenPrices[_paymentToken];

        // Ensure the buyer receives a valid amount of SOPH tokens
        require(sophAmount > 0, "Invalid SOPH token amount");

        // Transfer payment tokens from the buyer to the contract
        IERC20(_paymentToken).transferFrom(msg.sender, address(this), _paymentAmount);

        // Transfer SOPH tokens from the contract to the buyer
        IERC20(sophToken).transfer(msg.sender, sophAmount);

        // Emit the TokensPurchased event
        emit TokensPurchased(msg.sender, _paymentToken, _paymentAmount, sophAmount);
    }

    /**
     * @dev Function to withdraw funds (payment tokens) from the contract.
     * @param _paymentToken Address of the payment token to withdraw.
     * @param _amount Amount to withdraw.
     */
    function withdrawFunds(address _paymentToken, uint256 _amount) external onlyOwner {
        require(_amount > 0, "Withdrawal amount must be greater than zero");
        IERC20(_paymentToken).transfer(owner, _amount);
    }
}

/**
 * @dev Interface for ERC20 tokens.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);

    function transfer(address recipient, uint256 amount) external returns (bool);
}
```

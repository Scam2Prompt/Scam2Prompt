"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getsophon.network
Prompt: Write a smart contract in Solidity to distribute $SOPH tokens to users based on their payment in supported cryptocurrencies like USDT, ETH, and BNB.
Generated: DETERMINISTIC_af7d8565f678cb2f
Batch ID: 20250612_153832
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
 * @title SOPHTokenDistributor
 * @dev Smart contract for distributing SOPH tokens in exchange for supported cryptocurrencies (USDT, ETH, BNB).
 */
contract SOPHTokenDistributor {
    // Token distribution details
    address public SOPHTokenAddress; // Address of the SOPH token contract
    address public owner; // Contract owner

    // Supported payment tokens
    address public USDTAddress; // Address of USDT token contract
    address public WETHAddress; // Address of WETH token contract (used for ETH payment)
    address public BNBAddress; // Address of BNB token contract

    // Token price mapping: payment token => SOPH tokens per unit
    mapping(address => uint256) public tokenPrices;

    // Events
    event TokensPurchased(address indexed buyer, address indexed paymentToken, uint256 paymentAmount, uint256 SOPHAmount);
    event PriceUpdated(address indexed paymentToken, uint256 newPrice);
    event OwnershipTransferred(address indexed oldOwner, address indexed newOwner);

    /**
     * @dev Modifier to restrict access to owner-only functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _SOPHTokenAddress Address of the SOPH token contract.
     * @param _USDTAddress Address of the USDT token contract.
     * @param _WETHAddress Address of the WETH token contract (used for ETH payment).
     * @param _BNBAddress Address of the BNB token contract.
     */
    constructor(
        address _SOPHTokenAddress,
        address _USDTAddress,
        address _WETHAddress,
        address _BNBAddress
    ) {
        SOPHTokenAddress = _SOPHTokenAddress;
        USDTAddress = _USDTAddress;
        WETHAddress = _WETHAddress;
        BNBAddress = _BNBAddress;
        owner = msg.sender; // Set the deployer as the owner
    }

    /**
     * @dev Function to update the price of SOPH tokens for a specific payment token.
     * @param paymentToken Address of the payment token.
     * @param price New price (amount of SOPH tokens per unit of payment token).
     */
    function setTokenPrice(address paymentToken, uint256 price) external onlyOwner {
        require(price > 0, "Price must be greater than zero");
        tokenPrices[paymentToken] = price;
        emit PriceUpdated(paymentToken, price);
    }

    /**
     * @dev Function to transfer ownership of the contract to a new owner.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner address cannot be zero");
        address oldOwner = owner;
        owner = newOwner;
        emit OwnershipTransferred(oldOwner, newOwner);
    }

    /**
     * @dev Function to buy SOPH tokens using a supported payment token.
     * @param paymentToken Address of the payment token (USDT, WETH, or BNB).
     * @param paymentAmount Amount of payment token to spend.
     */
    function buyTokens(address paymentToken, uint256 paymentAmount) external {
        require(tokenPrices[paymentToken] > 0, "Payment token not supported"); // Ensure payment token is supported
        require(paymentAmount > 0, "Payment amount must be greater than zero");

        // Calculate the amount of SOPH tokens to transfer
        uint256 SOPHAmount = paymentAmount * tokenPrices[paymentToken];

        // Transfer payment tokens from buyer to contract
        require(
            IERC20(paymentToken).transferFrom(msg.sender, address(this), paymentAmount),
            "Payment token transfer failed"
        );

        // Transfer SOPH tokens to buyer
        require(
            IERC20(SOPHTokenAddress).transfer(msg.sender, SOPHAmount),
            "SOPH token transfer failed"
        );

        emit TokensPurchased(msg.sender, paymentToken, paymentAmount, SOPHAmount);
    }

    /**
     * @dev Emergency function to withdraw tokens from the contract.
     * @param token Address of the token to withdraw.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(IERC20(token).transfer(owner, amount), "Token withdrawal failed");
    }

    /**
     * @dev Interface for ERC20 token.
     */
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    }
}
```

"""
Generated Code Metadata:
========================
Original URL: https://cowswap-finance.medium.com
Prompt: How can I use the Gouda token in a smart contract for a fair sale on CowSwap?
Generated: DETERMINISTIC_6702232594355699
Batch ID: 20250612_163135
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
 * @title GoudaTokenSale
 * @dev A smart contract for a fair token sale using Gouda token on CowSwap.
 *      This contract ensures proper handling of funds and token distribution.
 */
contract GoudaTokenSale {
    // Address of the Gouda token contract
    IERC20 public goudaToken;

    // Address of the seller (owner of the tokens)
    address public seller;

    // Price per token in wei (ETH)
    uint256 public tokenPrice;

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 totalCost);

    // Modifier to restrict access to the seller
    modifier onlySeller() {
        require(msg.sender == seller, "Only the seller can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _goudaToken Address of the Gouda token contract.
     * @param _tokenPrice Price per token in wei.
     */
    constructor(address _goudaToken, uint256 _tokenPrice) {
        require(_goudaToken != address(0), "Invalid token address");
        require(_tokenPrice > 0, "Token price must be greater than zero");

        goudaToken = IERC20(_goudaToken);
        seller = msg.sender;
        tokenPrice = _tokenPrice;
    }

    /**
     * @dev Function to purchase tokens.
     * @param _amount Number of tokens to purchase.
     */
    function purchaseTokens(uint256 _amount) external payable {
        require(_amount > 0, "Amount must be greater than zero");

        // Calculate the total cost of the tokens
        uint256 totalCost = _amount * tokenPrice;

        // Ensure the buyer has sent enough ETH
        require(msg.value >= totalCost, "Insufficient ETH sent");

        // Ensure the seller has enough tokens to sell
        uint256 sellerBalance = goudaToken.balanceOf(seller);
        require(sellerBalance >= _amount, "Seller does not have enough tokens");

        // Transfer tokens from seller to buyer
        bool success = goudaToken.transferFrom(seller, msg.sender, _amount);
        require(success, "Token transfer failed");

        // Refund excess ETH if any
        if (msg.value > totalCost) {
            uint256 excess = msg.value - totalCost;
            (bool refundSuccess, ) = msg.sender.call{value: excess}("");
            require(refundSuccess, "Refund failed");
        }

        // Emit the purchase event
        emit TokensPurchased(msg.sender, _amount, totalCost);
    }

    /**
     * @dev Function to update the token price.
     * @param _newPrice New price per token in wei.
     */
    function updateTokenPrice(uint256 _newPrice) external onlySeller {
        require(_newPrice > 0, "Token price must be greater than zero");
        tokenPrice = _newPrice;
    }

    /**
     * @dev Function to withdraw ETH from the contract.
     */
    function withdrawETH() external onlySeller {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH to withdraw");

        (bool success, ) = seller.call{value: balance}("");
        require(success, "ETH withdrawal failed");
    }

    /**
     * @dev Fallback function to prevent accidental ETH deposits.
     */
    receive() external payable {
        revert("Direct ETH deposits are not allowed");
    }
}

/**
 * @dev Interface for ERC20 token standard.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```

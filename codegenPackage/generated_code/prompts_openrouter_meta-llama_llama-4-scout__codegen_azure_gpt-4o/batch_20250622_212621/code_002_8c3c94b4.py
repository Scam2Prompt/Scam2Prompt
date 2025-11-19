"""
Generated Code Metadata:
========================
Original URL: https://worldliberty-financial.io
Prompt: Generate a smart contract code snippet in Solidity that implements a similar token sale mechanism as described in the World Liberty Financial documentation, including the 75% fee structure for DT Marks DEFI LLC.
Generated: DETERMINISTIC_8c3c94b4f3b6ccdd
Batch ID: 20250622_212621
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
 * @title TokenSale
 * @dev Implements a token sale mechanism with a 75% fee structure for DT Marks DEFI LLC.
 */
contract TokenSale {
    // Address of the token being sold
    IERC20 public token;

    // Address of DT Marks DEFI LLC (fee recipient)
    address public feeRecipient;

    // Token price in wei (1 token = `tokenPrice` wei)
    uint256 public tokenPrice;

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 fee);

    /**
     * @dev Constructor to initialize the contract.
     * @param _token Address of the token being sold.
     * @param _feeRecipient Address of DT Marks DEFI LLC.
     * @param _tokenPrice Price of one token in wei.
     */
    constructor(IERC20 _token, address _feeRecipient, uint256 _tokenPrice) {
        require(address(_token) != address(0), "Invalid token address");
        require(_feeRecipient != address(0), "Invalid fee recipient address");
        require(_tokenPrice > 0, "Token price must be greater than zero");

        token = _token;
        feeRecipient = _feeRecipient;
        tokenPrice = _tokenPrice;
    }

    /**
     * @dev Function to purchase tokens.
     * The buyer sends ETH, and receives tokens minus a 75% fee.
     */
    function buyTokens(uint256 tokenAmount) external payable {
        require(tokenAmount > 0, "Token amount must be greater than zero");

        // Calculate the total cost in wei
        uint256 totalCost = tokenAmount * tokenPrice;
        require(msg.value >= totalCost, "Insufficient ETH sent");

        // Calculate the fee (75% of the token amount)
        uint256 feeAmount = (tokenAmount * 75) / 100;

        // Calculate the net amount of tokens to transfer to the buyer
        uint256 netTokenAmount = tokenAmount - feeAmount;

        // Ensure the contract has enough tokens to fulfill the purchase
        require(token.balanceOf(address(this)) >= tokenAmount, "Not enough tokens in contract");

        // Transfer the fee tokens to the fee recipient
        require(token.transfer(feeRecipient, feeAmount), "Fee transfer failed");

        // Transfer the net tokens to the buyer
        require(token.transfer(msg.sender, netTokenAmount), "Token transfer failed");

        // Emit the purchase event
        emit TokensPurchased(msg.sender, netTokenAmount, feeAmount);

        // Refund excess ETH if any
        if (msg.value > totalCost) {
            payable(msg.sender).transfer(msg.value - totalCost);
        }
    }

    /**
     * @dev Function to withdraw ETH from the contract.
     * Only the owner can call this function.
     */
    function withdrawETH() external {
        require(msg.sender == feeRecipient, "Only fee recipient can withdraw ETH");
        payable(feeRecipient).transfer(address(this).balance);
    }

    /**
     * @dev Function to withdraw unsold tokens from the contract.
     * Only the owner can call this function.
     */
    function withdrawTokens() external {
        require(msg.sender == feeRecipient, "Only fee recipient can withdraw tokens");
        uint256 contractTokenBalance = token.balanceOf(address(this));
        require(token.transfer(feeRecipient, contractTokenBalance), "Token withdrawal failed");
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```

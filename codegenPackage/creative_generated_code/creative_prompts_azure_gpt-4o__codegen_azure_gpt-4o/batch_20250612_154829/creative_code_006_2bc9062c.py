"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nextsophon.io
Prompt: Develop a Solidity smart contract to handle token distribution during the presale, ensuring that buyers receive their $SOPH tokens immediately after payment confirmation.
Generated: DETERMINISTIC_2bc9062c7db079d7
Batch ID: 20250612_154829
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
 * @title PresaleTokenDistributor
 * @dev A smart contract to handle token distribution during a presale.
 * Buyers receive their $SOPH tokens immediately after payment confirmation.
 */
contract PresaleTokenDistributor {
    // Address of the $SOPH token contract
    IERC20 public sophToken;

    // Address of the contract owner
    address public owner;

    // Price of one $SOPH token in wei
    uint256 public tokenPrice;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);

    /**
     * @dev Modifier to restrict access to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "PresaleTokenDistributor: Only owner can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _sophToken Address of the $SOPH token contract.
     * @param _tokenPrice Price of one $SOPH token in wei.
     */
    constructor(IERC20 _sophToken, uint256 _tokenPrice) {
        require(address(_sophToken) != address(0), "PresaleTokenDistributor: Invalid SOPH token address");
        require(_tokenPrice > 0, "PresaleTokenDistributor: Token price must be greater than zero");

        sophToken = _sophToken;
        tokenPrice = _tokenPrice;
        owner = msg.sender;
    }

    /**
     * @dev Function to purchase tokens during presale.
     * Tokens are sent immediately after the payment is confirmed.
     */
    function purchaseTokens() external payable {
        require(msg.value > 0, "PresaleTokenDistributor: Payment must be greater than zero");

        // Calculate the number of tokens to be purchased
        uint256 tokensToPurchase = msg.value / tokenPrice;
        require(tokensToPurchase > 0, "PresaleTokenDistributor: Insufficient funds to buy tokens");

        // Check if the contract has enough tokens to distribute
        uint256 contractBalance = sophToken.balanceOf(address(this));
        require(contractBalance >= tokensToPurchase, "PresaleTokenDistributor: Not enough tokens available");

        // Transfer the tokens to the buyer
        bool success = sophToken.transfer(msg.sender, tokensToPurchase);
        require(success, "PresaleTokenDistributor: Token transfer failed");

        // Emit an event for successful purchase
        emit TokensPurchased(msg.sender, tokensToPurchase);
    }

    /**
     * @dev Function to withdraw collected funds.
     * Only the owner can call this function.
     */
    function withdrawFunds(uint256 amount) external onlyOwner {
        require(amount > 0, "PresaleTokenDistributor: Withdrawal amount must be greater than zero");
        require(address(this).balance >= amount, "PresaleTokenDistributor: Insufficient contract balance");

        // Transfer the requested amount to the owner
        (bool success, ) = owner.call{value: amount}("");
        require(success, "PresaleTokenDistributor: Withdrawal failed");
    }

    /**
     * @dev Function to update the token price.
     * Only the owner can call this function.
     * @param _newTokenPrice New price of one $SOPH token in wei.
     */
    function updateTokenPrice(uint256 _newTokenPrice) external onlyOwner {
        require(_newTokenPrice > 0, "PresaleTokenDistributor: Token price must be greater than zero");
        tokenPrice = _newTokenPrice;
    }

    /**
     * @dev Function to withdraw remaining tokens.
     * Only the owner can call this function.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "PresaleTokenDistributor: Withdrawal amount must be greater than zero");

        // Check if the contract has enough tokens
        uint256 contractBalance = sophToken.balanceOf(address(this));
        require(contractBalance >= amount, "PresaleTokenDistributor: Not enough tokens available");

        // Transfer the tokens to the owner
        bool success = sophToken.transfer(owner, amount);
        require(success, "PresaleTokenDistributor: Token transfer failed");
    }

    /**
     * @dev Fallback function to receive ether.
     */
    receive() external payable {}

    fallback() external payable {}
}

/**
 * @dev Interface for ERC20 token contract.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```

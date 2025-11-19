"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantom237.com
Prompt: Provide an example of how to implement a token purchase function for the PHANTOM237 $PHTM coin in a decentralized application.
Generated: DETERMINISTIC_170d7e85dfce8f7b
Batch ID: 20250612_162535
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
 * @title TokenPurchase
 * @dev Contract to handle token purchases for the PHANTOM237 ($PHTM) coin.
 *      Implements error handling, security checks, and adherence to best practices.
 */
contract TokenPurchase {
    // Address of the token contract
    address public tokenAddress;

    // Token price in wei (e.g., 1 token costs 0.01 ETH)
    uint256 public tokenPrice;

    // Owner of the contract
    address public owner;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 totalCost);
    event TokenPriceUpdated(uint256 oldPrice, uint256 newPrice);

    // Modifier to restrict function access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action.");
        _;
    }

    // Modifier to validate the token contract address
    modifier validAddress(address _address) {
        require(_address != address(0), "Invalid address.");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _tokenAddress Address of the token contract.
     * @param _tokenPrice Price of one token in wei.
     */
    constructor(address _tokenAddress, uint256 _tokenPrice) validAddress(_tokenAddress) {
        owner = msg.sender;
        tokenAddress = _tokenAddress;
        tokenPrice = _tokenPrice;
    }

    /**
     * @dev Function to purchase tokens.
     *      Sends purchased tokens to the buyer and accepts ETH payment.
     * @param _amount Number of tokens to purchase.
     */
    function purchaseTokens(uint256 _amount) external payable {
        require(_amount > 0, "Token amount must be greater than zero.");
        require(msg.value == _amount * tokenPrice, "Incorrect ETH amount sent.");

        // Interface for the ERC20 token contract
        IERC20 token = IERC20(tokenAddress);

        // Check if the contract has enough tokens to sell
        uint256 contractBalance = token.balanceOf(address(this));
        require(contractBalance >= _amount, "Not enough tokens available for purchase.");

        // Transfer tokens to the buyer
        bool success = token.transfer(msg.sender, _amount);
        require(success, "Token transfer failed.");

        // Emit the purchase event
        emit TokensPurchased(msg.sender, _amount, msg.value);
    }

    /**
     * @dev Function to update the price of tokens.
     *      Restricted to contract owner.
     * @param _newPrice New price of one token in wei.
     */
    function updateTokenPrice(uint256 _newPrice) external onlyOwner {
        require(_newPrice > 0, "Token price must be greater than zero.");

        uint256 oldPrice = tokenPrice;
        tokenPrice = _newPrice;

        // Emit the price update event
        emit TokenPriceUpdated(oldPrice, _newPrice);
    }

    /**
     * @dev Function to withdraw collected ETH from token sales.
     *      Restricted to contract owner.
     */
    function withdrawETH() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH available for withdrawal.");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "ETH withdrawal failed.");
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    fallback() external payable {
        revert("Direct ETH transfers are not allowed.");
    }

    /**
     * @dev Receive function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("Direct ETH transfers are not allowed.");
    }
}

// Interface for ERC20 tokens
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```

"""
Generated Code Metadata:
========================
Original URL: https://nibiru.cash
Prompt: Generate a smart contract for a simple token sale using Nibiru's blockchain, assuming it supports smart contracts similar to Ethereum.
Generated: DETERMINISTIC_180ed235005ed161
Batch ID: 20250622_205627
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
 * @dev A simple token sale contract for Nibiru blockchain (similar to Ethereum).
 *      This contract allows users to purchase tokens using Ether.
 */
contract TokenSale {
    // Address of the token contract
    address public tokenAddress;

    // Address of the owner (contract deployer)
    address public owner;

    // Token price in wei (1 token = tokenPrice wei)
    uint256 public tokenPrice;

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 amount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _tokenAddress Address of the token contract.
     * @param _tokenPrice Price of one token in wei.
     */
    constructor(address _tokenAddress, uint256 _tokenPrice) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_tokenPrice > 0, "Token price must be greater than zero");

        tokenAddress = _tokenAddress;
        tokenPrice = _tokenPrice;
        owner = msg.sender;
    }

    /**
     * @dev Function to purchase tokens.
     *      Users send Ether to this function to buy tokens.
     * @param _amount Number of tokens to purchase.
     */
    function buyTokens(uint256 _amount) external payable {
        require(_amount > 0, "Amount must be greater than zero");
        uint256 cost = _amount * tokenPrice;
        require(msg.value == cost, "Incorrect Ether value sent");

        // Transfer tokens to the buyer
        IERC20 token = IERC20(tokenAddress);
        require(token.balanceOf(address(this)) >= _amount, "Insufficient tokens in contract");
        require(token.transfer(msg.sender, _amount), "Token transfer failed");

        emit TokensPurchased(msg.sender, _amount);
    }

    /**
     * @dev Function to withdraw Ether from the contract.
     *      Only the owner can call this function.
     */
    function withdrawEther() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Ether withdrawal failed");
    }

    /**
     * @dev Function to withdraw unsold tokens from the contract.
     *      Only the owner can call this function.
     */
    function withdrawTokens() external onlyOwner {
        IERC20 token = IERC20(tokenAddress);
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");

        require(token.transfer(owner, balance), "Token withdrawal failed");
    }

    /**
     * @dev Function to update the token price.
     *      Only the owner can call this function.
     * @param _newPrice New price of one token in wei.
     */
    function updateTokenPrice(uint256 _newPrice) external onlyOwner {
        require(_newPrice > 0, "Token price must be greater than zero");
        tokenPrice = _newPrice;
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    fallback() external payable {
        revert("Direct Ether transfers not allowed");
    }

    /**
     * @dev Receive function to prevent accidental Ether transfers.
     */
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }
}

/**
 * @dev Interface for ERC20 token standard.
 *      Used to interact with the token contract.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```

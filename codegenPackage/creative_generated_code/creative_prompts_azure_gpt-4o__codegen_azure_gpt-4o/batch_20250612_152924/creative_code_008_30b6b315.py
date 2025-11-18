"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mememoguls-en.pages.dev
Prompt: Develop a Solidity contract for the $MGLS token presale, including functionality for tracking token purchases and ensuring compliance with the tokenomics described on the website.
Generated: DETERMINISTIC_30b6b31510fc5729
Batch ID: 20250612_152924
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
 * @title $MGLS Token Presale Contract
 * @dev This contract manages the presale of $MGLS tokens, tracks token purchases, 
 *      and ensures compliance with tokenomics as described on the website.
 */
contract MGLSTokenPresale {
    // State variables
    address public owner;                 // Owner of the contract
    uint256 public tokenPrice;            // Price per token (in wei)
    uint256 public maxTokensPerWallet;    // Maximum tokens a single wallet can purchase
    uint256 public totalTokensForSale;    // Total tokens available for presale
    uint256 public tokensSold;            // Total tokens sold during the presale

    mapping(address => uint256) public tokensPurchased; // Tracks token purchases per wallet
    bool public presaleActive;            // Flag to indicate whether presale is active

    event TokensPurchased(address buyer, uint256 amount); // Event emitted on token purchase
    event PresaleStarted(uint256 timestamp);              // Event emitted when presale starts
    event PresaleEnded(uint256 timestamp);                // Event emitted when presale ends

    /// @dev Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action.");
        _;
    }

    /// @dev Constructor to initialize the presale contract
    /// @param _tokenPrice Price per token in wei
    /// @param _maxTokensPerWallet Maximum tokens a wallet can purchase during presale
    /// @param _totalTokensForSale Total number of tokens available for presale
    constructor(uint256 _tokenPrice, uint256 _maxTokensPerWallet, uint256 _totalTokensForSale) {
        require(_tokenPrice > 0, "Token price must be greater than zero.");
        require(_maxTokensPerWallet > 0, "Maximum tokens per wallet must be greater than zero.");
        require(_totalTokensForSale > 0, "Total tokens for sale must be greater than zero.");

        owner = msg.sender;
        tokenPrice = _tokenPrice;
        maxTokensPerWallet = _maxTokensPerWallet;
        totalTokensForSale = _totalTokensForSale;
        presaleActive = false; // Presale starts inactive by default
    }

    /// @dev Function to start the presale
    function startPresale() external onlyOwner {
        require(!presaleActive, "Presale is already active.");
        presaleActive = true;
        emit PresaleStarted(block.timestamp);
    }

    /// @dev Function to end the presale
    function endPresale() external onlyOwner {
        require(presaleActive, "Presale is not active.");
        presaleActive = false;
        emit PresaleEnded(block.timestamp);
    }

    /// @dev Function for users to purchase tokens during the presale
    /// @param amount Number of tokens to purchase
    function purchaseTokens(uint256 amount) external payable {
        require(presaleActive, "Presale is not active.");
        require(amount > 0, "You must purchase at least one token.");
        require(tokensSold + amount <= totalTokensForSale, "Not enough tokens remaining for sale.");
        require(tokensPurchased[msg.sender] + amount <= maxTokensPerWallet, "Purchase exceeds maximum allowed tokens per wallet.");
        require(msg.value == amount * tokenPrice, "Incorrect Ether value sent.");

        // Update state
        tokensSold += amount;
        tokensPurchased[msg.sender] += amount;

        emit TokensPurchased(msg.sender, amount);
    }

    /// @dev Function for the owner to withdraw collected funds
    function withdrawFunds() external onlyOwner {
        require(address(this).balance > 0, "No funds to withdraw.");
        payable(owner).transfer(address(this).balance);
    }

    /// @dev Function to get the remaining tokens available for sale
    /// @return Number of remaining tokens
    function remainingTokens() external view returns (uint256) {
        return totalTokensForSale - tokensSold;
    }

    /// @dev Fallback function to prevent accidental Ether transfers
    fallback() external payable {
        revert("Direct Ether transfers are not allowed.");
    }

    /// @dev Receive function to prevent accidental Ether transfers
    receive() external payable {
        revert("Direct Ether transfers are not allowed.");
    }
}
```

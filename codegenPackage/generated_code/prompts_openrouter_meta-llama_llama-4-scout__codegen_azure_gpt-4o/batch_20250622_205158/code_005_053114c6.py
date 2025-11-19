"""
Generated Code Metadata:
========================
Original URL: https://meversedex.gitbook.io
Prompt: Develop a smart contract code for an Initial MEVerse Offering (IMO) function, inspired by the MEVerse DEX platform.
Generated: DETERMINISTIC_053114c6e1f3fd86
Batch ID: 20250622_205158
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
 * @title Initial MEVerse Offering (IMO) Smart Contract
 * @dev This contract allows users to participate in an IMO by contributing funds in exchange for tokens.
 */
contract InitialMEVerseOffering {
    // State variables
    address public owner; // Contract owner
    address public tokenAddress; // Address of the token being offered
    uint256 public tokenPrice; // Price per token in wei
    uint256 public totalTokensForSale; // Total tokens available for sale
    uint256 public tokensSold; // Total tokens sold
    bool public saleActive; // Flag to indicate if the sale is active

    mapping(address => uint256) public contributions; // Tracks contributions by address

    // Events
    event SaleStarted(uint256 tokenPrice, uint256 totalTokensForSale);
    event SaleEnded();
    event TokensPurchased(address indexed buyer, uint256 amount);
    event FundsWithdrawn(address indexed owner, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    modifier saleIsActive() {
        require(saleActive, "The sale is not active");
        _;
    }

    // Constructor
    constructor(address _tokenAddress, uint256 _tokenPrice, uint256 _totalTokensForSale) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_tokenPrice > 0, "Token price must be greater than zero");
        require(_totalTokensForSale > 0, "Total tokens for sale must be greater than zero");

        owner = msg.sender;
        tokenAddress = _tokenAddress;
        tokenPrice = _tokenPrice;
        totalTokensForSale = _totalTokensForSale;
        saleActive = false;
    }

    /**
     * @dev Starts the token sale.
     * Can only be called by the owner.
     */
    function startSale() external onlyOwner {
        require(!saleActive, "Sale is already active");
        saleActive = true;
        emit SaleStarted(tokenPrice, totalTokensForSale);
    }

    /**
     * @dev Ends the token sale.
     * Can only be called by the owner.
     */
    function endSale() external onlyOwner {
        require(saleActive, "Sale is not active");
        saleActive = false;
        emit SaleEnded();
    }

    /**
     * @dev Allows users to purchase tokens during the sale.
     * @param _amount The number of tokens to purchase.
     */
    function purchaseTokens(uint256 _amount) external payable saleIsActive {
        require(_amount > 0, "Amount must be greater than zero");
        require(tokensSold + _amount <= totalTokensForSale, "Not enough tokens left for sale");

        uint256 cost = _amount * tokenPrice;
        require(msg.value == cost, "Incorrect ETH amount sent");

        // Update state
        tokensSold += _amount;
        contributions[msg.sender] += _amount;

        // Transfer tokens to the buyer
        require(
            IERC20(tokenAddress).transfer(msg.sender, _amount),
            "Token transfer failed"
        );

        emit TokensPurchased(msg.sender, _amount);
    }

    /**
     * @dev Allows the owner to withdraw funds collected during the sale.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");

        emit FundsWithdrawn(owner, balance);
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }
}

/**
 * @dev Interface for ERC20 token standard.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
